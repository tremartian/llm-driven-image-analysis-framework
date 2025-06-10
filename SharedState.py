
import tkinter as tk


# shared_state.update_image(selected_file, img)  # Update the shared state
# shared_state.update_image2(self, method_name, image_path, image)  # Update the shared state

# shared_state.get_image2(self, method_name)  # Update the shared state

class SharedState:
    def __init__(self):
        self.imageLoaded = False
        self.current_image = None
        self.image_path = None
        self.selected_values = {}  # Dictionary to store selected values for each tab
        self.allMethods = []  # List to store all added methods
        self.selectedMethod = {}
        self.real_time_updates = tk.BooleanVar(value=True)  # BooleanVar to track real-time updates, default is True


    # FOR IMAGES
    def update_imageOriginal(self, method_name, image_path, image):
        """
        Update the selected value for a specific parameter in a method.
        Args:
            method_name (str): The name or identifier of the method.
            parameter_name (str): The name of the parameter.
            value: The selected value for the parameter.
        """
        if method_name not in self.selected_values:
            self.selected_values["original image"] = {}
        self.selected_values['original image']['image'] = image
        self.selected_values['original image']['image_path'] = image_path

    def update_image2(self, method_name, image_path, image):
        """
        Update the selected value for a specific parameter in a method.
        Args:
            method_name (str): The name or identifier of the method.
            parameter_name (str): The name of the parameter.
            value: The selected value for the parameter.
        """
        if method_name not in self.selected_values:
            self.selected_values[method_name] = {}
        self.selected_values[method_name]['image'] = image
        self.selected_values[method_name]['image_path'] = image_path

    def get_image2(self, method_name):
        print("get_image2 - method_name: " + method_name)
        """
        Retrieve the image and image path for a given method name.
        Args:
            method_name (str): The name or identifier of the method.
        Returns:
            list: [PIL.Image, str] The image and image path.
        """
        if method_name in self.selected_values:
            print("self.selected_values[method_name]:", self.selected_values[method_name])
            print("Method name exists in selected_values.")
            print("self.selected_values[method_name]['image_path']: " + str(self.selected_values[method_name]['image_path']))
            return [self.selected_values[method_name]['image'], self.selected_values[method_name]['image_path']]
        elif "original image" in self.selected_values:
            print("Fallback to original image.")
            return [
                self.selected_values["original image"]['image'],
                self.selected_values["original image"]['image_path']
            ]
        else:
            print("Warning: No image found for method_name or 'original image'. Returning None.")
            return [None, None]



    def get_imageLoaded(self):
        return self.imageLoaded

    def update_imageLoaded(self): # if image is
        self.imageLoaded = True




    def update_image(self, image_path, image):
        self.image_path = image_path
        self.current_image = image

    def get_image(self):
        return self.current_image

    def get_image_path(self):
        return self.image_path






    # FOR METHODS

    def add_to_allMethods(self, method):  # shared_state.add_to_allMethods(self, method) # Update the shared state
        #self.allMethods = method
        self.allMethods.append(method)

    def get_allMethods(self):  # shared_state.get_allMethods() # Update the shared state
        return self.allMethods


    def update_selectedMethod(self, method, selected_method_name ):  # shared_state.update_selectedMethod(method, selected_method_name ) # Update the shared state
        self.selectedMethod[method] = selected_method_name


    def get_selectedMethod(self, method):  # shared_state.get_selectedMethod(method) # Update the shared state
        return self.selectedMethod[method]




    def set_real_time_updates(self, value):
        self.real_time_updates.set(value)

    def get_real_time_updates(self):
        return self.real_time_updates.get()

    def update_selected_value(self, method_name, parameter_name, value):
        """
        Update the selected value for a specific parameter in a method.
        Args:
            method_name (str): The name or identifier of the method.
            parameter_name (str): The name of the parameter.
            value: The selected value for the parameter.
        """
        if method_name not in self.selected_values:
            self.selected_values[method_name] = {}
        self.selected_values[method_name][parameter_name] = value

    def get_selected_value(self, method_name, parameter_name):
        """
        Get the selected value for a specific parameter in a method.
        Args:
            method_name (str): The name or identifier of the method.
            parameter_name (str): The name of the parameter.
        Returns:
            value: The selected value for the parameter.
                   Returns None if the parameter is not found.
        """
        if method_name in self.selected_values and parameter_name in self.selected_values[method_name]:
            return self.selected_values[method_name][parameter_name]
        else:
            return None

    # Additional methods for clearing or accessing selected values as needed...


