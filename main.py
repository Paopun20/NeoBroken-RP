import zipfile
import os
import sys

def make_zip():
    # Define the output directory and filename
    output_dir = 'build'
    zip_filename = 'my_files.zip'
    output_path = os.path.join(output_dir, zip_filename)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True) # exist_ok=True prevents error if dir already exists

    # Create the zip file in the specified output directory
    with zipfile.ZipFile(output_path, 'w') as myzip:
        # Define the source directory to zip
        source_dir = 'auto-zip'

        # Check if the source directory exists before walking
        if not os.path.isdir(source_dir):
            print(f"Error: Source directory '{source_dir}' not found.")
            return 1  # Exit the function with an error status code

        # Add all files in the source directory to the zip file
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip file, using a relative path inside the zip
                # based on the source directory
                archive_path = os.path.relpath(file_path, source_dir)
                myzip.write(file_path, archive_path)

        print(f"Successfully created zip file at: {output_path}")
        return 0  # Exit the function with a success status code

# Run the function
sys.exit(make_zip())  # Exit the script with a success status code
# This script creates a zip file containing all files from the 'auto-zip' directory