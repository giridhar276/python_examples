"""
Program 21:
More shutil methods:
- move()
- make_archive()
- unpack_archive()
"""

import shutil
from pathlib import Path

demo_folder = Path("../output/shutil_advanced")
demo_folder.mkdir(exist_ok=True)

file1 = demo_folder / "file1.txt"
file1.write_text("This file will be moved.", encoding="utf-8")

moved_folder = Path("../output/moved_files")
moved_folder.mkdir(exist_ok=True)

# Move file
new_location = moved_folder / "file1.txt"

if new_location.exists():
    new_location.unlink()

shutil.move(str(file1), str(new_location))
print("File moved to:", new_location)

# Make archive
archive_path = shutil.make_archive("../output/moved_files_backup", "zip", moved_folder)
print("Archive created:", archive_path)

# Unpack archive
unpack_folder = Path("../output/unpacked_backup")
if unpack_folder.exists():
    shutil.rmtree(unpack_folder)

shutil.unpack_archive(archive_path, unpack_folder)
print("Archive unpacked to:", unpack_folder)
