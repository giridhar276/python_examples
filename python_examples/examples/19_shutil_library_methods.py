"""
Program 19:
Built-in library: shutil module methods.
"""

import shutil
from pathlib import Path

source_file = Path("../data/source_file.txt")
destination_folder = Path("../output/shutil_demo")
destination_folder.mkdir(exist_ok=True)

destination_file = destination_folder / "copied_file.txt"

# Copy file
shutil.copy(source_file, destination_file)
print("File copied to:", destination_file)

# Copy file with metadata
metadata_file = destination_folder / "copied_with_metadata.txt"
shutil.copy2(source_file, metadata_file)
print("File copied with metadata to:", metadata_file)

# Copy complete folder
backup_folder = Path("../output/shutil_backup")

if backup_folder.exists():
    shutil.rmtree(backup_folder)

shutil.copytree(destination_folder, backup_folder)
print("Folder copied to:", backup_folder)

# Remove copied backup folder
shutil.rmtree(backup_folder)
print("Backup folder removed.")
