import tkinter as tk
from tkinter import ttk
import json
from AA_FileSelection import create_file_selection_tab
from AD_ResultsTab import create_results_tab
from B_templateForTabs import create_tab
from SharedState import SharedState  # Import the SharedState class

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Image Analysis Tool")
        self.geometry("800x600")

        self.shared_state = SharedState()  # Instantiate SharedState

        # Create the tab control
        self.tab_control = ttk.Notebook(self)

        # Add special tab for file selection
        self.tab_control.add(create_file_selection_tab(self.tab_control, self.shared_state), text="File Selection")

        # Dynamically load other tabs
        self.load_tabs()

        # Add results tab as the last tab
        self.tab_control.add(create_results_tab(self.tab_control, self.shared_state), text="Results")

        self.tab_control.pack(expand=1, fill="both")

    def load_tabs(self):
        with open('config/methods.json', 'r') as file:
            methods = json.load(file)
            for method in methods['methods']:
                if method['name'] not in ["File Selection", "Results"]:  # These are handled separately
                    tab = create_tab(self.tab_control, method, self.shared_state)
                    self.tab_control.add(tab, text=method['name'])

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
