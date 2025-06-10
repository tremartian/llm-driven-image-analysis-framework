import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from SharedState import SharedState  # Import the shared state class

def create_file_selection_tab(parent, shared_state):
    tab = ttk.Frame(parent)
    listbox = tk.Listbox(tab, height=6, width=50)
    listbox.pack(pady=20)

    label_image = ttk.Label(tab)
    label_image.pack(pady=20)

    shared_state.add_to_allMethods("original image")  # when a tab is created the name of the method is saved in list

    def open_files(listbox):
        file_paths = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.tif")]
        )
        listbox.delete(0, tk.END)
        for file_path in file_paths:
            listbox.insert(tk.END, file_path)

    def update_preview(selected_file):
        original_img = Image.open(selected_file) # Open with Pillow

        img = original_img.copy()

        img.thumbnail((800, 800)) # Adjust preview size
        tk_img = ImageTk.PhotoImage(img)
        label_image.configure(image=tk_img)
        label_image.image = tk_img  # Keep a reference!
        shared_state.update_image(selected_file, original_img)  # Update the shared state => old code, can be removed
        shared_state.update_imageOriginal("original image", selected_file, original_img)  # Update the shared state

        shared_state.update_imageLoaded() #set the image loaded flag true


        print("selected_file: "+selected_file)
        image_path = shared_state.get_image_path() # Get the image path from the shared state
        print("shared image path: "+image_path)
        image = shared_state.get_image() # Get the image from the shared state # Should be a Pillow image
        print("shared image: "+str(image))
        print("-------------- image selected -------------------------------- ")

    listbox.bind("<<ListboxSelect>>", lambda event: update_preview(listbox.get(listbox.curselection())))

    ttk.Button(tab, text="Select Images", command=lambda: open_files(listbox)).pack(pady=10)
    return tab
