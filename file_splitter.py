import os

def split_file(file_path, output_dir, chunk_size=500 * 1024 * 1024):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    
    with open(file_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            output_file_path = os.path.join(output_dir, f"{file_name}_part_{part_num}.txt")
            with open(output_file_path, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Created {output_file_path}")
            part_num += 1

def split_files_in_folder(folder_path, output_dir, chunk_size=500 * 1024 * 1024):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            split_file(file_path, output_dir, chunk_size)

# Path ke folder "Data"
folder_path = "Data"

# Path ke folder output
output_dir = "Output"

# Ukuran chunk dalam byte (500MB)
chunk_size = 500 * 1024 * 1024

# Memanggil fungsi untuk memecah file
split_files_in_folder(folder_path, output_dir, chunk_size)
