import os

def rename_files(start_directory):
    # track & inc folder number only when isdir finds a folder
    fold_num = 1 

    # Loop through all folders in the start directory
    for season_num, folder in enumerate(sorted(os.listdir(start_directory)), 1):
        folder_path = os.path.join(start_directory, folder)
        print(f'folder_path: {folder_path}')
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Loop through all files in the folder
            for episode_num, filename in enumerate(sorted(os.listdir(folder_path)), 1):
                old_path = os.path.join(folder_path, filename)
                
                # Check if it's a file
                if os.path.isfile(old_path):
                    # Split the filename and extension
                    name, ext = os.path.splitext(filename)
                    
                    # Create new filename with season and episode (sXXeXX format)
                    new_name = f"{name}_s{fold_num:02d}e{episode_num:02d}{ext}"
                    new_path = os.path.join(folder_path, new_name)
                    
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_name}")

            # track & inc folder number only when isdir finds a folder
            fold_num += 1

# Specify your starting directory here
start_dir = "/start/dir"  # Replace with your actual path

# Run the renaming function
try:
    rename_files(start_dir)
    print("Renaming complete!")
except Exception as e:
    print(f"An error occurred: {e}")