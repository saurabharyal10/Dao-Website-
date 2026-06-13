import os

def rename_images(folder_path):
    # Check if the directory exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(folder_path)
    
    # Filter for image files (you can add more extensions if needed)
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    image_files = [f for f in files if f.lower().endswith(valid_extensions)]
    
    # Sort files to ensure a consistent renaming order
    image_files.sort()

    # Rename the files
    for index, filename in enumerate(image_files, start=1):
        # Get the file extension
        extension = os.path.splitext(filename)[1]
        
        # Define the new name
        new_name = f"image_{index}{extension}"
        
        # Define full paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} to {new_name}")

# Run the function
rename_images("images")