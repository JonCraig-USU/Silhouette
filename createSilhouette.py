import os
from PIL import Image, ImageFilter

# =os.path.join(os.path.dirname(os.path.dirname(path)),"_reverse_silhouettes")
def iterate_over_folders(path, output_path, threshold_value=[125]):
    # Get the current working directory
    # cwd = os.getcwd()
    if os.path.exists(path) and os.path.isabs(path):
        if os.path.isfile(path) and (path.lower().endswith(".jpg") or path.lower().endswith(".jpeg")):
            if not os.path.exists(output_path):
                try:
                    os.mkdir(output_path)
                    create_silhouette(path, output_path, threshold_value)
                except Exception as e:
                     print(f"Error {e}.\n Could not create output directory")
            else:
                create_silhouette(path, output_path, threshold_value)
            return

        elif os.path.isdir(path):
            # Iterate over all files in the directory
            for name in os.listdir(path):
                iterate_over_folders(os.path.join(path, name), os.path.join(os.path.dirname(path), f"{os.path.basename(path)}_reverse_silhouette"), threshold_value)

def create_silhouette(filepath, output_path, threshold_value):
        try:
            # Open the image file
            image = Image.open(filepath)

            # Convert the image to grayscale
            gray_image = image.convert("L")
            
            # Blur the image
            blurred_image = gray_image.filter(ImageFilter.BLUR)
            
            for threshold in threshold_value:
                threshold = int(threshold)
                # Apply the reverse threshold
                reverse_silhouette = blurred_image.point(lambda p: p <= threshold and 255)
                
                # Save the reverse thresholded image with a new name
                filename = os.path.basename(filepath)
                reverse_silhouette_path = os.path.join(output_path, f"reverse_silhouette_T{threshold}_{filename}")
                reverse_silhouette.save(reverse_silhouette_path)

        except Exception as e:
            print(f"Could not process {filename}: {e}")


# def create_silhouettes(filename, image_input, image_output, threshold_value):
#         try:
#             # Open the image file
#             image_path = os.path.join(image_input, filename)
#             image = Image.open(image_path)

#             # Convert the image to grayscale
#             gray_image = image.convert("L")
            
#             # Blur the image
#             blurred_image = gray_image.filter(ImageFilter.BLUR)
            
#             for threshold in threshold_value:
#                 # Apply the reverse threshold
#                 reverse_silhouette = blurred_image.point(lambda p: p <= threshold and 255)
                
#                 # Save the reverse thresholded image with a new name
#                 reverse_silhouette_path = os.path.join(image_output, f"reverse_silhouette_T{threshold}_{filename}")
#                 reverse_silhouette.save(reverse_silhouette_path)

#         except Exception as e:
#             print(f"Could not process {filename}: {e}")
