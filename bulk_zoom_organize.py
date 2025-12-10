bulimport os
import csv
from datetime import datetime
import shutil  # Import the shutil module for file/folder operations

# Create a dictionary to store date-to-meeting-name mapping
date_to_name = {}

# Specify the encoding when opening the CSV file as 'utf-8-sig' to handle BOM
with open("meeting_names.csv", mode='r', encoding='utf-8-sig') as csv_file:
    # Use the expected header as fieldnames and skip the first row
    csv_reader = csv.DictReader(csv_file, fieldnames=['Date', 'MeetingName'])
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Make sure the CSV column names match the case in the CSV file
        date = row['Date']  # Ensure 'Date' matches exactly, including case
        meeting_name = row['MeetingName']  # Ensure 'MeetingName' matches exactly, including case
        date_to_name[date] = meeting_name

# Specify the directory where your Zoom files are located
zoom_directory = "/Users/katefisher/Desktop/Zoom/Zoom Downloads"

# Define the list of allowed file extensions
allowed_extensions = [".mp4", ".m4a", ".vtt", ".txt"]

# Create a directory for storing the renamed folders
renamed_folders_directory = "/Users/katefisher/Desktop/Zoom/Renamed Folders"

# Iterate through the files in the directory
for filename in os.listdir(zoom_directory):
    # Extract the file extension
    file_extension = os.path.splitext(filename)[-1].lower()

    # Check if the file extension is allowed
    if file_extension in allowed_extensions:
        # Extract the date code from the filename (assuming it's in 'GMTYYYYMMDD' format)
        date_code_gmt = filename[3:11]

        # Extract the 6-digit meeting identifier from the filename
        meeting_identifier = filename[12:18]

        # Convert 'GMTYYYYMMDD' to 'YYYY-MM-DD' format
        date_code = datetime.strptime(date_code_gmt, '%Y%m%d').strftime('%Y-%m-%d')

        # Check if the date code is in the CSV
        if date_code in date_to_name:
            meeting_name = date_to_name[date_code]

            # Create a directory based on the meeting name, date, and meeting identifier if it doesn't exist
            folder_name = f"{date_code}_{meeting_name}_{meeting_identifier}"
            meeting_directory = os.path.join(zoom_directory, folder_name)
            if not os.path.exists(meeting_directory):
                os.makedirs(meeting_directory)

            # Move the file to the meeting directory and rename it
            file_path = os.path.join(zoom_directory, filename)
            new_file_path = os.path.join(meeting_directory, filename)
            os.rename(file_path, new_file_path)

            print(f"Moved file '{filename}' to '{meeting_directory}'")
        else:
            print(f"Date code not found in CSV for file '{filename}': '{date_code}'")

# Prompt the user to move the renamed folders to another directory
user_input = input("Do you want to move the renamed folders to another directory? (yes/no): ")
if user_input.lower() == "yes":
    # Specify the destination directory (Dropbox)
    destination_directory = "/Users/katefisher/Dropbox"

    # Create the renamed folders directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Move the renamed folders to the specified directory (Dropbox)
    for folder_name in os.listdir(zoom_directory):
        folder_path = os.path.join(zoom_directory, folder_name)
        if os.path.isdir(folder_path):
            shutil.move(folder_path, os.path.join(destination_directory, folder_name))
    
    print(f"Renamed folders moved to '{destination_directory}'.")
else:
    print("Renamed folders were not moved.")

print("Files organized successfully.")
