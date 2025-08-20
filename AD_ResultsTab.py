import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pandas as pd
import json, datetime, os

def create_results_tab(parent, shared_state):
    tab = ttk.Frame(parent)
    ttk.Label(tab, text="Results and Analysis", font=('Arial', 16)).pack(pady=10)

    def refresh_results():
        """
        Rebuild the Results tab to ensure it displays the latest image and data.
        """
        for widget in tab.winfo_children():
            widget.destroy()
        updated_tab = create_results_tab(parent, shared_state)
        parent.forget(tab)  # Remove the current tab
        parent.add(updated_tab, text="Results")

    ttk.Button(tab, text="Refresh Results", command=refresh_results).pack(pady=5)

    all_methods = shared_state.get_allMethods()
    if all_methods:
        latest_method = all_methods[-1]
        ttk.Label(tab, text=f"Displaying results from: {latest_method}", font=('Arial', 10)).pack()
    else:
        ttk.Label(tab, text="No processed image available.", font=('Arial', 10)).pack()
        return tab

    # Try to get the latest image
    try:
        image_info = shared_state.get_image2(latest_method)
        image_pil = image_info[0]
    except Exception as e:
        image_pil = None
        print(f"Error loading image: {e}")

    if image_pil is None:
        ttk.Label(tab, text="No image loaded.", font=('Arial', 10)).pack()
        return tab

    # Create a canvas with scrollbars to hold the image
    canvas_frame = ttk.Frame(tab)
    canvas_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(canvas_frame, width=400, height=400, scrollregion=(0, 0, image_pil.width, image_pil.height))
    hbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=canvas.xview)
    vbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
    canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    hbar.pack(side=tk.BOTTOM, fill=tk.X)
    vbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    img_tk = ImageTk.PhotoImage(image_pil)
    image_on_canvas = canvas.create_image(0, 0, anchor='nw', image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection

    # Zoom functionality: adjust scrollregion and scale the canvas
    current_zoom = [1.0]

    def zoom_in():
        current_zoom[0] *= 1.2
        apply_zoom()

    def zoom_out():
        current_zoom[0] /= 1.2
        apply_zoom()

    def apply_zoom():
        # Clear the canvas and redraw the image at the new zoom level
        canvas.delete(image_on_canvas)
        new_size = (int(image_pil.width * current_zoom[0]), int(image_pil.height * current_zoom[0]))
        resized_image = image_pil.resize(new_size)
        new_img_tk = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor='nw', image=new_img_tk)
        canvas.image = new_img_tk  # Update reference
        canvas.config(scrollregion=(0, 0, *new_size))

    zoom_controls = ttk.Frame(tab)
    zoom_controls.pack(pady=5)
    ttk.Button(zoom_controls, text="Zoom In", command=zoom_in).pack(side=tk.LEFT, padx=5)
    ttk.Button(zoom_controls, text="Zoom Out", command=zoom_out).pack(side=tk.LEFT, padx=5)

    ttk.Separator(tab, orient='horizontal').pack(fill='x', pady=10)

    ttk.Label(tab, text="Analyze CSV Data", font=('Arial', 12)).pack(pady=5)

    def analyze_csv():
        try:
            csv_file = filedialog.askopenfilename(
                filetypes=[("CSV Files", "*.csv")],
                title="Select CSV File"
            )
            if csv_file:
                data = pd.read_csv(csv_file)
                print(f"CSV data loaded:\n{data.head()}")
                if 'Area' in data.columns:
                    plt.figure(figsize=(8, 5))
                    plt.hist(data['Area'], bins=20, color='skyblue', edgecolor='black')
                    plt.title('Histogram of Contour Areas')
                    plt.xlabel('Area')
                    plt.ylabel('Frequency')
                    plt.show()
                else:
                    messagebox.showinfo("CSV Analysis", "No 'Area' column found in the CSV.")
            else:
                messagebox.showinfo("CSV Analysis", "No file selected.")
        except Exception as e:
            messagebox.showerror("CSV Analysis Error", f"Error processing CSV: {e}")

    ttk.Button(tab, text="Select and Analyze CSV File", command=analyze_csv).pack(pady=5)

    def export_pipeline_json():
        payload = {
            "version": "0.1",
            "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
            "pipeline_order": getattr(shared_state, "pipeline_order", []),
            "params": getattr(shared_state, "params", {}),
            "io": getattr(shared_state, "io_spec", {})
        }
        fpath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile="pipeline_params.json",
            title="Save pipeline as JSON"
        )
        if not fpath:
            return
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        messagebox.showinfo("Export", f"Saved: {os.path.basename(fpath)}")

    ttk.Button(tab, text="Export pipeline (JSON)", command=export_pipeline_json).pack(pady=5)


    return tab




