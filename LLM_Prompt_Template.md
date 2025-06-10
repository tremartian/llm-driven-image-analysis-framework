LLM Prompt Template for New Image Processing Modules:
Copy the prompt below and make necessary modifications!

Prompt Introduction:
Purpose: "Create a new image analysis module named '<MODULE_NAME>' within the existing framework to perform '<DESCRIPTION_OF_PROCESSING_TASK>'. This module will allow users to dynamically adjust parameters through a dynamically created user interface based on JSON, affecting the image processing results in real-time."
Static Details for Integration:
JSON Structure Requirements for methods.json:
•	Generate parameters based on the module purpose (the example below shows some as an example)
•	"The LLM should generate parameters typical for the specified processing task. For example, for a 'Contrast Adjustment' module, parameters might include 'contrast_level' with a default range and step size. Each parameter should be accompanied by metadata such as type, default, min, max, step, and a UI element type."
•	Make sure that the parameters are in correct type. 
•	There are 4 types of controls in UI named as: slider, dropdown, tickbox, and button.
•	<MODULE_NAME> is also the name of the function you will provide.

Example structure for JSON:
{
  "name": "<MODULE_NAME>",
  "parameters": {
    "<PARAMETER_NAME>": {
      "type": "<DATA_TYPE>",
      "default": <DEFAULT_VALUE>,
      "min": <MIN_VALUE>,
      "max": <MAX_VALUE>,
      "step": <STEP_VALUE>,
      "ui": "<UI_TYPE>",
      "adjustment": "<CONTROL_NAME_IN_PY>"
    }
  "example_dropdown": {
      "type": "string",
      "default": "option1",
      "options": ["option1", "option2", "option3"],
      "ui": "dropdown",
      "adjustment": "<CONTROL_NAME_IN_PY>"

    },
    "example_tickbox": {
      "type": "boolean",
      "default": true,
      "ui": "tickbox",
      "adjustment": "<CONTROL_NAME_IN_PY>"
    },
    "example_button": {
      "default": 0,
      "ui": "button",
      "adjustment": "<CONTROL_NAME_IN_PY>"
    }
    ... (additional parameters as needed)
  }
}

Python Function Template for methods.py:
def <FUNCTION_NAME_IN_PY>(image, method_parameters, original_image):
    """
    Description: Implement the functionality for <MODULE_NAME>, which involves <DESCRIPTION_OF_PROCESSING_TASK>.
    This function adjusts the processing based on dynamically provided parameters.

    Parameters that are used as inputs in the function call:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task. (parameters are in a list not dict! For example, brightness_level = method_parameters[0]

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.

Note: Ensure that method_parameters are validated and handled according to their roles in the processing task. This may include type checking and converting parameters to expected formats.
In case a single parameter, use method_parameters[0] 
In case of multiple parameters, the parameters in the list are in the same order as presented in the JSON.
"""
    # Check the format of method_parameters variable.
    # Check if the required parameter(s) are available and valid
    # Convert the type of the parameter(s) if needed. (for example, if int is needed (slider returns float))
    # Is Greyscale or colored image used. Convert if needed.
    # Default action or raise an error if parameters are not as expected
    # Process image by using the parameters and the image fed to the function

    return processed_image  # Return the processed image in Pillow format

********************************************************************
*** USER INPUT SECTION FOR SPECIFIC MODULE DETAILS: ***
•	MODULE NAME AND DESCRIPTION: Contour detection, and count contoured objects
•	ADDITIONAL INFORMATION: I want have selectors for all possible options
********************************************************************

Integration and Testing Instructions:
•	The code must integrate seamlessly with the existing system, ensuring full functionality from the UI to data processing.
•	All parameters should be dynamically adjustable through the UI, allowing real-time updates to the processing output as user inputs change.
•	Needed conversions should be taken care for methods. For example, if grayscale image is needed.

Reminder for Quality Assurance:
•	Strictly adhere to the defined JSON structure and Python coding standards to ensure compatibility with the existing framework.
•	Ensure easy updates and modifications to support future enhancements without extensive redevelopment.
•	If additional libraries are used, call them and use them correctly.

•	Use the templates provide to give contents for methods.json and methods.py for requested processing
•	Give full code for the function.
•	Provide only one function to process image.
