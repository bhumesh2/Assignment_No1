"""Q4. In DevOps, performing regular backups of important files is crucial:
●  Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
●  The script should copy all files from the source directory to the destination directory.
●  Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the
   file name to ensure uniqueness.
●  Handle errors gracefully, such as when the source directory or destination directory does not exist.
 
Sample Command:
python backup.py /path/to/source /path/to/destination
By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, 
ensuring unique file names in the destination directory. """

import os
import shutil
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get list of files in the source directory
    files_to_backup = os.listdir(source_dir)

    # Copy files to the destination directory
    for file_name in files_to_backup:
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)

        if os.path.exists(destination_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            base_name, extension = os.path.splitext(file_name)
            file_name = f"{base_name}_{timestamp}{extension}"
            destination_path = os.path.join(destination_dir, file_name)

        try:
            shutil.copy2(source_path, destination_path)
            print(f"File copied: {file_name}")
        except Exception as e:
            print(f"Error copying file '{file_name}': {str(e)}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)

"""OUTPUT
PS D:\personal data\Cloud\Assignments> python backup.py 'D:\personal data\Cloud\Assignments\source_folder' 'D:\dest_folder'
File copied: bhumesh.txt
PS D:\personal data\Cloud\Assignments> python backup.py 'D:\personal data\Cloud\Assignments\source_folder' 'D:\dest_folder'
File copied: bhumesh_20240125114532.txt
PS D:\personal data\Cloud\Assignments>"""