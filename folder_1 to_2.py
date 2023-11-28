import os
import shutil

source_folder = "f2"
destination_folder = "f1"

if os.path.exists(source_folder) and os.path.isdir(source_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        if os.path.isfile(item_path):
            shutil.move(item_path, destination_folder)
        elif os.path.isdir(item_path):
            shutil.move(item_path, os.path.join(destination_folder, item))
else:
    print("Source folder does not exist or is not a directory")
