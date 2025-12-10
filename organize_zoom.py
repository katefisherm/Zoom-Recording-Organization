import os
from datetime import datetime
import shutil  # Import the shutil module for file/folder operations

# Specify the directory where your Zoom files are located
zoom_directory = "/Users/katefisher/Desktop/Zoom/Zoom Downloads"

# Define the list of allowed file extensions
allowed_extensions = [".mp4", ".m4a", ".vtt", ".txt"]

# Create a directory for storing the renamed folders
renamed_folders_directory = "/Users/katefisher/Desktop/Zoom/Renamed Folders"

# Prompt the user to enter the meeting name
meeting_name = input("Enter the meeting name: ")

# Iterate through the files in the directory
for filename in os.listdir(zoom_directory):
    # Extract the file extension
    file_extension = os.path.splitext(filename)[-1].lower()

    # Check if the file extension is allowed
    if file_extension in allowed_extensions:
        # Extract the date code from the filename (assuming it's in 'GMTYYYYMMDD' format)
        date_code_gmt = filename[3:11]

        # Convert 'GMTYYYYMMDD' to 'YYYY-MM-DD' format
        date_code = datetime.strptime(date_code_gmt, '%Y%m%d').strftime('%Y-%m-%d')

        # Create a directory based on the manually entered meeting name and date if it doesn't exist
        folder_name = f"{meeting_name}_{date_code}"
        meeting_directory = os.path.join(zoom_directory, folder_name)
        if not os.path.exists(meeting_directory):
            os.makedirs(meeting_directory)

        # Move the file to the meeting directory and rename it
        file_path = os.path.join(zoom_directory, filename)
        new_file_path = os.path.join(meeting_directory, filename)
        os.rename(file_path, new_file_path)

        print(f"Moved file '{filename}' to '{meeting_directory}'")

print("Files organized successfully.")
