import os

def get_files_with_prefix(directory, prefix):
    files_with_prefix = []
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            files_with_prefix.append(filename)
    return files_with_prefix

# Specify your directory path and prefix
directory_path = "C:\\Coding\\RIMES\\sample_data\\12122023"
file_prefix = "gfs_900hpa_temp_12122023"

# Get files with the specified prefix
files = get_files_with_prefix(directory_path, file_prefix)

# Print the list of files
print("Files with prefix {}: {}".format(file_prefix, files))