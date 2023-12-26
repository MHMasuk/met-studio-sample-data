import os
import shutil

def duplicate_files_with_prefix(src_folder, src_prefix, dest_prefix):
    for filename in os.listdir(src_folder):
        if filename.startswith(src_prefix):
            new_filename = filename.replace(src_prefix, dest_prefix)
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(src_folder, new_filename)
            shutil.copy(src_path, dest_path)

# Specify your directory path and prefixes
directory_path = "C:\\Coding\\RIMES\\sample_data\\12122023"
src_prefix = "ecmwf_900hpa_rain_12122023"
dest_prefix = "gfs_900hpa_visibility_12122023"

# Duplicate files
duplicate_files_with_prefix(directory_path, src_prefix, dest_prefix)