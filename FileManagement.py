import os
import shutil

# Path to the downloads directory
downloads_path = '/path/to/your/downloads'

# Dictionary mapping file extensions to folder names
file_categories = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.gif'],
    'Audio': ['.mp3', '.wav', '.ogg'],
    # Add more categories and file extensions as needed
}

# Create category folders if they don't exist
for category in file_categories.keys():
    folder_path = os.path.join(downloads_path, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize the files
for filename in os.listdir(downloads_path):
    # Skip directories
    if os.path.isdir(os.path.join(downloads_path, filename)):
        continue
    
    # Get the file extension
    file_extension = os.path.splitext(filename)[1].lower()
    
    # Find the category for the file extension
    for category, extensions in file_categories.items():
        if file_extension in extensions:
            # Move the file to the category folder
            shutil.move(os.path.join(downloads_path, filename),
                        os.path.join(downloads_path, category, filename))
            break
