from PIL import ImageEnhance
import cv2
import numpy as np
from PIL import Image  # Importing the Image class from the Pillow library
import csv
from random import randint

from PIL import ImageEnhance
from PIL import ImageFilter



from PIL import Image, ImageEnhance

def Brightness_Adjustment(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Brightness Adjustment, which involves adjusting the brightness of the image.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task.

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    # Check if method_parameters variable is in the correct format
   # if not isinstance(method_parameters, list) or len(method_parameters) != 1:
    #    raise ValueError("method_parameters must be a list with one element")

    # Extract brightness level from method_parameters
    brightness_level = method_parameters[0]

    # Validate brightness_level
    if not isinstance(brightness_level, (int, float)):
        raise TypeError("Brightness level must be a number")

    # Adjust brightness of the image
    processed_image = image.point(lambda p: p * brightness_level)

    return processed_image  # Return the processed image in Pillow format


def Contrast_Adjustment(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Contrast Adjustment, which involves enhancing image contrast.
    This function adjusts the processing based on dynamically provided parameters.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task.

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    # Extracting parameters
    contrast_level = method_parameters[0]

    # Adjusting contrast
    processed_image = ImageEnhance.Contrast(image).enhance(contrast_level)

    return processed_image  # Return the processed image in Pillow format


def Segmentation(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Segmentation, which involves partitioning the image into distinct segments based on defined criteria and the selected method. This function adjusts the processing based on dynamically provided parameters.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task. The parameters are in the same order as presented in the JSON:
         [segmentation_threshold, segmentation_method, enable_preprocessing, reset_segmentation]
    - original_image (PIL.Image): The original image before any processing is applied.

    Returns:
    - PIL.Image: Processed image reflecting the applied segmentation.

    Note: Ensure that method_parameters are validated and handled according to their roles in the processing task. This may include type checking and converting parameters to expected formats.
    In the case of a single parameter, use method_parameters[0]. For multiple parameters, the parameters in the list are in the same order as presented in the JSON.
    """
    # Validate the method_parameters list length.
    if len(method_parameters) < 4:
        raise ValueError("Insufficient parameters provided for segmentation.")

    # Extract and convert parameters as needed.
    try:
        threshold = float(method_parameters[0])
    except Exception as e:
        raise ValueError("Conversion of segmentation_threshold parameter failed: " + str(e))

    segmentation_method = method_parameters[1]
    enable_preprocessing = bool(method_parameters[2])
    reset_button = method_parameters[3]  # This can be used to trigger reset functionality if applicable.

    # **Optional: If preprocessing is enabled, convert the image to grayscale.**
    if enable_preprocessing:
        image = image.convert("L")

    # **Implement segmentation based on the chosen method. The following dummy logic is provided as a placeholder:**
    import numpy as np
    import PIL.Image as Image

    image_np = np.array(image)

    if segmentation_method == "otsu":
        # Dummy implementation: Apply simple thresholding.
        processed_np = (image_np > (threshold * 255)).astype(np.uint8) * 255
        processed_image = Image.fromarray(processed_np)
    elif segmentation_method == "k-means":
        # **Placeholder for k-means segmentation implementation. Replace with actual algorithm if available.**
        processed_image = image  # Replace with actual k-means segmentation process.
    elif segmentation_method == "watershed":
        # **Placeholder for watershed segmentation implementation. Replace with actual algorithm if available.**
        processed_image = image  # Replace with actual watershed segmentation process.
    else:
        processed_image = image  # Default to returning the original image if no valid method is selected.

    return processed_image  # Return the processed image in Pillow format.



def MorphologicalClosing(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Morphological Closing, which involves applying
    a morphological closing operation (dilation followed by erosion) on the image. This operation
    helps close small holes and gaps between nearby objects, improving contour detection.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task.
        [kernel_size, iterations]

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    import numpy as np
    import cv2
    from PIL import Image

    # Unpack parameters
    try:
        kernel_size = int(method_parameters[0])
        iterations = int(method_parameters[1])
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid method_parameters provided: {e}")

    # Convert the PIL image to a grayscale numpy array
    img_cv = np.array(image.convert('L'))

    # Create kernel
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Apply morphological closing
    closed = cv2.morphologyEx(img_cv, cv2.MORPH_CLOSE, kernel, iterations=iterations)

    # Convert back to Pillow Image (grayscale)
    processed_image = Image.fromarray(closed)

    return processed_image




def GaussianBlur(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Gaussian Blur, which involves applying a Gaussian
    filter to the image to reduce noise and smooth details. This operation is commonly used to
    pre-process images before edge detection or segmentation.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task.
        [kernel_size]

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    import numpy as np
    import cv2
    from PIL import Image

    # Unpack parameters
    try:
        kernel_size = int(method_parameters[0])
        if kernel_size % 2 == 0:
            kernel_size += 1  # Ensure kernel size is odd
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid method_parameters provided: {e}")

    # Convert the PIL image to a grayscale numpy array
    img_cv = np.array(image.convert('L'))

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(img_cv, (kernel_size, kernel_size), 0)

    # Convert back to Pillow Image (grayscale)
    processed_image = Image.fromarray(blurred)

    return processed_image



def Dilation(image, method_parameters, original_image):
    """
    Description: Implement the functionality for Dilation, which involves applying a morphological
    dilation operation on the image. This operation can be used to connect nearby objects and
    enhance structure for subsequent analysis.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task.
        [kernel_size, iterations]

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    import numpy as np
    import cv2
    from PIL import Image

    # Unpack parameters
    try:
        kernel_size = int(method_parameters[0])
        iterations = int(method_parameters[1])
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid method_parameters provided: {e}")

    # Convert the PIL image to a grayscale numpy array
    img_cv = np.array(image.convert('L'))

    # Create kernel
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(img_cv, kernel, iterations=iterations)

    # Convert back to Pillow Image (grayscale)
    processed_image = Image.fromarray(dilated)

    return processed_image


def ContourDetection(image, method_parameters, original_image):
    """
    Description: Implement the functionality for ContourDetection, which involves detecting contours in an image,
    filtering them by minimum object size, and optionally drawing them and overlaying a count of detected contours.
    Each contour is displayed with a unique color, and labeled with a number for identification.

    Parameters:
    - image (PIL.Image): Input image for processing. The image is always in Pillow format.
    - method_parameters (list): List of parameters needed for the processing task. (parameters are in a list, not dict).

    Returns:
    - PIL.Image: Processed image reflecting the applied changes.
    """
    import numpy as np
    import cv2
    from PIL import Image
    import csv
    import random

    # Unpack method_parameters
    try:
        threshold1 = float(method_parameters[0])
        threshold2 = float(method_parameters[1])
        retrieval_mode = method_parameters[2]
        approximation_method = method_parameters[3]
        show_contours = bool(method_parameters[4])
        show_count = bool(method_parameters[5])
        min_object_size = float(method_parameters[6])
        export_results = bool(method_parameters[7])  # New parameter
    except (IndexError, ValueError) as e:
        raise ValueError("Invalid method_parameters provided: {}".format(e))

    # Convert the PIL image to grayscale numpy array
    img_cv = np.array(image.convert('L'))

    # Map retrieval_mode
    retrieval_modes = {
        "external": cv2.RETR_EXTERNAL,
        "list": cv2.RETR_LIST,
        "ccomp": cv2.RETR_CCOMP,
        "tree": cv2.RETR_TREE
    }
    retrieval_mode_cv = retrieval_modes.get(retrieval_mode, cv2.RETR_EXTERNAL)

    # Map approximation_method
    approx_methods = {
        "simple": cv2.CHAIN_APPROX_SIMPLE,
        "none": cv2.CHAIN_APPROX_NONE,
        "tc89_l1": cv2.CHAIN_APPROX_TC89_L1,
        "tc89_kcos": cv2.CHAIN_APPROX_TC89_KCOS
    }
    approx_method_cv = approx_methods.get(approximation_method, cv2.CHAIN_APPROX_SIMPLE)

    # Apply Canny edge detection
    edges = cv2.Canny(img_cv, threshold1, threshold2)

    # Find contours
    contours, _ = cv2.findContours(edges, retrieval_mode_cv, approx_method_cv)

    # Filter contours by minimum area
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) >= min_object_size]

    # Export contour data if requested
    if export_results:
        with open('contour_areas.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Contour Index', 'Area'])
            for idx, cnt in enumerate(filtered_contours):
                area = cv2.contourArea(cnt)
                writer.writerow([idx, area])

    # Draw contours with different colors and label each contour
    img_color = np.array(image.convert('RGB'))
    if show_contours or show_count:
        for idx, cnt in enumerate(filtered_contours):
            # Generate a random color
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            # Draw the contour
            cv2.drawContours(img_color, [cnt], -1, color, 2)
            # Compute the contour's centroid for placing the number
            M = cv2.moments(cnt)
            if M['m00'] != 0:
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                # Put the contour index at the centroid
                cv2.putText(
                    img_color, str(idx),
                    (cX, cY),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    color,
                    2,
                    cv2.LINE_AA
                )

        # Draw count label if requested
        if show_count:
            text = f"Objects: {len(filtered_contours)}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 2.0
            color = (255, 0, 0)  # Blue text
            thickness = 3
            position = (10, 80)  # Top-left corner
            cv2.putText(img_color, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    processed_image = Image.fromarray(img_color)
    return processed_image
