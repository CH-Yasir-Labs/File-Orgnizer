#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     14/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import shutil

# Define categories for file types
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".exe", ".msi", ".bat"],
}

# Function to organize files
def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: '{folder_path}' does not exist!")
        return

    # Scan all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()

        # Find the right category for the file
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                category_path = os.path.join(folder_path, category)
                os.makedirs(category_path, exist_ok=True)  # Create category folder if missing
                shutil.move(file_path, os.path.join(category_path, file))
                print(f"Moved: {file} → {category}/")
                break
        else:
            # Move unknown file types to 'Others' folder
            other_path = os.path.join(folder_path, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, file))
            print(f"Moved: {file} → Others/")

# Run the organizer
if __name__ == "__main__":
    folder_to_organize = input("Enter folder path to organize: ")
    organize_files(folder_to_organize)
    print("✅ File organization complete!")
