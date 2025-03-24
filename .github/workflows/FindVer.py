import os
import re

def extract_version(folder_name):
    """Extracts version numbers as a tuple of integers for proper comparison."""
    match = re.match(r'v(\d+)(?:\.(\d+))?(?:\.(\d+))?$', folder_name)  
    if match:
        return tuple(int(x) if x else 0 for x in match.groups())
    return None

def get_highest_version(folder_list):
    """Finds the highest versioned folder, ignoring 'archive'."""
    versions = [(extract_version(folder), folder) for folder in folder_list if extract_version(folder) and folder.lower() != 'archive']
    return max(versions)[1] if versions else None

def find_highest_subfolder(base_dir):
    """Finds the highest versioned subfolder inside base_dir, ignoring 'archive'."""
    subfolders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f.lower() != 'archive']
    return get_highest_version(subfolders)

if __name__ == "__main__":
    root_folders = [f for f in os.listdir('.') if os.path.isdir(f) and f.lower() != 'archive']
    highest_root = get_highest_version(root_folders)

    if highest_root:
        highest_sub = find_highest_subfolder(highest_root)
        if highest_sub:
            print(f"./{highest_root}/{highest_sub}/")
