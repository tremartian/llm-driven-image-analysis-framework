import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from config import methods

def create_tab(parent, method_config, shared_state):
    tab = ttk.Frame(parent)
    ttk.Label(tab, text=f"Method: {method_config['name']}", font=('Arial', 16)).pack()

    shared_state.add_to_allMethods(method_config['name'])
    all_methods = shared_state.get_allMethods()
    current_method_index = all_methods.index(method_config['name'])

    if current_method_index > 0:
        previous_method_name = all_methods[current_method_index - 1]
        sourceImage = previous_method_name
    else:
        sourceImage = "original image"

    ttk.Label(tab, text=f"Source image from method: {sourceImage}", font=('Arial', 10)).pack()

    def update_menu_options():
        method_options = shared_state.get_allMethods()
        menu["menu"].delete(0, "end")
        for method in method_options:
            menu["menu"].add_command(label=method, command=tk._setit(selected_method, method))

    selected_method = tk.StringVar()
    method_options = shared_state.get_allMethods()
    menu = ttk.OptionMenu(tab, selected_method, sourceImage, *method_options)
    menu.pack()

    def on_method_select(*args):
        selected_method_name = selected_method.get()
        shared_state.update_selectedMethod(method_config["name"], selected_method_name)
        if shared_state.get_image2(selected_method_name) is not None:
            sharedState_image = shared_state.get_image2(selected_method_name)
        else:
            sharedState_image = shared_state.get_image2("original image")

    selected_method.trace('w', on_method_select)
    menu.bind("<Button-1>", lambda event: update_menu_options())

    images_frame = ttk.LabelFrame(tab, text="Image Previews")
    images_frame.pack(fill='both', expand=True, padx=10, pady=10)

    left_frame = ttk.LabelFrame(images_frame, text="Image from Previous Tab")
    left_frame.pack(side='left', padx=5, pady=5, expand=True, fill='both')
    left_img_label = ttk.Label(left_frame, text="")
    left_img_label.pack(expand=True, fill='both')

    right_frame = ttk.LabelFrame(images_frame, text="Image after Processing")
    right_frame.pack(side='right', padx=5, pady=5, expand=True, fill='both')
    right_img_label = ttk.Label(right_frame, text="")
    right_img_label.pack(expand=True, fill='both')

    # Scrollable Settings Frame
    settings_container = ttk.LabelFrame(tab, text="Settings")
    settings_container.pack(fill='both', expand=True, padx=10, pady=10)

    canvas = tk.Canvas(settings_container)
    scrollbar = ttk.Scrollbar(settings_container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    controls = {}
    for param, config in method_config['parameters'].items():
        ttk.Label(scrollable_frame, text=param.capitalize()).pack()
        control_frame = ttk.Frame(scrollable_frame)
        control_frame.pack()
        uiType = method_config['parameters'][param]['ui']

        if uiType == "slider":
            control = ttk.Scale(scrollable_frame, from_=config['min'], to=config['max'], orient='horizontal')
            control.set(config['default'])
            control.pack()
            value_label = ttk.Label(scrollable_frame, text=str(control.get()))
            value_label.pack(side='left')

            control.bind("<ButtonRelease-1>",
                         lambda event, c=control, p=param, l=value_label: slider_update(event, c, p, shared_state,
                                                                                           method_config,
                                                                                           left_img_label,
                                                                                           right_img_label,
                                                                                           sourceImage, l))

            default_button = ttk.Button(scrollable_frame, text="Default",
                                        command=lambda c=control, d=config['default'], s=shared_state: set_to_default(
                                            value_label, c, d, s, param, method_config))
            default_button.pack()

        elif uiType == "dropdown":
            create_dropdown(scrollable_frame, shared_state, method_config, param, config)

        elif uiType == "tickbox":
            create_tickbox(scrollable_frame, shared_state, method_config, param, config)

        elif uiType == "button":
            create_button(scrollable_frame, shared_state, method_config, param, config)

    return tab

def create_tickbox(settings_frame, shared_state, method_config, param, config):
    tick_state = tk.BooleanVar(value=bool(config['default']))
    control = ttk.Checkbutton(settings_frame, text=param.capitalize(), variable=tick_state)
    control.pack()

    # Bind the Checkbutton state to a function that processes changes
    tick_state.trace('w', lambda *args: tickbox_update(tick_state, shared_state, method_config['name'], param))

    return control

def tickbox_update(tick_state, shared_state, method_name, parameter_name):
    checked = tick_state.get()
    shared_state.update_selected_value(method_name, parameter_name, checked)
    print(f"Tickbox Updated - Method: {method_name}, Parameter: {parameter_name}, State: {'Enabled' if checked else 'Disabled'}")


def create_dropdown(settings_frame, shared_state, method_config, param, config):
    selected_option = tk.StringVar(value=config['default'])
    dropdown = ttk.OptionMenu(settings_frame, selected_option, config['default'], *config['options'])
    dropdown.pack()
    # Bind the OptionMenu selection to a function that processes changes
    selected_option.trace('w', lambda *args: dropdown_update(selected_option, shared_state, method_config['name'], param))
    return dropdown

def tickbox_update(tick_state, shared_state, method_name, parameter_name):
    checked = tick_state.get()
    shared_state.update_selected_value(method_name, parameter_name, checked)
    print(f"Tickbox Updated - Method: {method_name}, Parameter: {parameter_name}, State: {'Enabled' if checked else 'Disabled'}")


def set_to_default(label, control, default_value, shared_state, param, method_config):
    print("Method Name:", method_config["name"])  # when button is pressed the name of the method is printed
    # Set the value in SharedState to the default value
    control.set(default_value)
    shared_state.update_selected_value(method_name=method_config["name"], parameter_name=param, value=default_value)
    print(f"Default Button - Parameter: {param}, Value: {control.get()}, Shared State Path: {method_config['name']} -> {param}")
    print("Current Slider Value:", control.get())
    label.config(text="{:.2f}".format(control.get()))  # Format the slider's value to two decimal places

def slider_update(event, control, param, shared_state, method_config, left_img_label, right_img_label, sourceImage, label):
    print("sourceImage: " + sourceImage)
    print("label: " + str(label))
    print("Current Slider Value:", control.get())
    # Update the selected value in SharedState
    shared_state.update_selected_value(method_name=method_config["name"], parameter_name=param, value=control.get())

    # Update the label text to display the current slider value
    label.config(text="{:.2f}".format(control.get())) # Format the slider's value to two decimal places

    # Print the name, value, and shared state path
    print(f"Parameter: {param}, Value: {control.get()}, Shared State Path: {method_config['name']} -> {param}")

    # Update the right image preview
    update_processed_image(shared_state, left_img_label, right_img_label, method_config, sourceImage)


def create_button(settings_frame, shared_state, method_config, param, config):
    button_text = param.capitalize()  # Usually, the button text is the parameter name capitalized
    command_action = lambda: button_action(shared_state, method_config['name'], param, config)
    button = ttk.Button(settings_frame, text=button_text, command=command_action)
    button.pack()
    return button

def button_action(shared_state, method_name, param, config):
    # Execute some action. For example, reset parameters or trigger a process
    print(f"Button Pressed - Method: {method_name}, Parameter: {param}")
    # Here you might want to trigger an image processing function or update some part of the UI
    # This is just a placeholder for whatever action you need to perform


def update_processed_image(shared_state, left_img_label, right_img_label, method_config, sourceImage):
    print("===============================================")
    print("sourceImage: " + sourceImage)
     # Retrieve the image from the shared state
    sharedState_image = shared_state.get_image2(sourceImage)[0]  # Update the shared state
    print("sharedState_image: " + str(sharedState_image))

    sharedState_image_orig = shared_state.get_image2('original image')[0]  # Update the shared state
    print("sharedState_image_orig: " + str(sharedState_image_orig))

    if sharedState_image:
        print("sharedState_image exists")
        # Display the image from the shared state on the left image label
        previous_img = ImageTk.PhotoImage(sharedState_image.resize((500, 500)))
        left_img_label.configure(image=previous_img)
        left_img_label.image = previous_img

        # Get the settings from the shared state based on the method name
        method_name = method_config["name"]
        print("method_name: " + str(method_name))
        method_parameter_names = method_config["parameters"].keys()  # get existing method parameters from json
        print("method_parameter_names: " + str(method_parameter_names))

        # Retrieve the function name dynamically from the config
        first_param_key = list(method_config["parameters"].keys())[0]  # Assume the first parameter key will have the function name
        function_name = method_config["name"]
        print("Function Name: " + str(function_name))

        # Dynamically import the function using the `methods` module
        try:
            function = getattr(methods, function_name)
        except AttributeError:
            raise ValueError(f"Function {function_name} is not found in the methods module.")

        method_parameters = []  # Initialize an empty list to store parameter names
        for parameter_name in method_parameter_names:
            print("Parameter Name:", parameter_name)
            method_parameter = shared_state.get_selected_value(method_name, parameter_name)

            if method_config["parameters"][parameter_name]["ui"] == "slider": # other ui types do not need default parameter
                print("slider")
            if method_parameter is None:
             method_parameter = method_config["parameters"][parameter_name]["default"]  # Fetch default value from JSON
             print("method_parameter: " + str(method_parameter))
            print("method_parameter: " + str(method_parameter))
            method_parameters.append(method_parameter)  # Add parameter name to the list
            print("Method Parameters: ", method_parameters)


        # Process the image
        processed_image = function(sharedState_image, method_parameters, sharedState_image_orig)  # Process the image with the dynamically imported function
        shared_state.update_image2(method_name, sharedState_image, processed_image)  # Update the shared state

        # Display the processed image on the right image label
        processed_img = ImageTk.PhotoImage(processed_image.resize((500, 500)))
        right_img_label.configure(image=processed_img)
        right_img_label.image = processed_img
    else:
        print("shared path image does not exist")
        exit()



def apply_processing(image, settings, method_config):
    # Dynamically call the function defined in methods.json
    for param, config in method_config['parameters'].items():
        func = getattr(methods, config['function'])
        image = func(image, settings[param])
    return image







