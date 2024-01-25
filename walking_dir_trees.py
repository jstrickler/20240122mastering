import os 

start_folder = "."

SKIP = ".git"

for curr_dir, dirs, files in os.walk(start_folder):
    if SKIP in dirs:
        dirs.remove(SKIP)
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.csv'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"     {file_size:8d} {file_name}")
