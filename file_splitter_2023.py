import os
from calendar import monthrange

def create_directory_structure(base_dir):
    year_dir = os.path.join(base_dir, "2023")
    os.makedirs(year_dir, exist_ok=True)

    for month in range(1, 13):
        month_dir = os.path.join(year_dir, f"{month:02}")
        os.makedirs(month_dir, exist_ok=True)

        # Tentukan jumlah hari dalam bulan berdasarkan kalender
        days_in_month = monthrange(2023, month)[1]

        for day in range(1, days_in_month + 1):
            day_dir = os.path.join(month_dir, f"{day:02}")
            os.makedirs(day_dir, exist_ok=True)

def split_file(input_file, output_dir):
    create_directory_structure(output_dir)

    year_dir = os.path.join(output_dir, "2023")
    month, day = 1, 1
    file_count, size_per_file = 1, 0
    max_size = 1 * 1024 * 1024 * 1024  # 1 GB in bytes

    with open(input_file, 'r', encoding='latin-1') as file:
        current_day_dir = os.path.join(year_dir, f"{month:02}", f"{day:02}")
        output_file = open(os.path.join(current_day_dir, f"part_{file_count}.txt"), 'w', encoding='utf-8')

        for line in file:
            output_file.write(line)
            size_per_file += len(line.encode('utf-8'))

            # Jika ukuran file mencapai atau melebihi 1 GB
            if size_per_file >= max_size:
                output_file.close()
                file_count += 1
                size_per_file = 0

                # Update tanggal dan bulan
                day += 1
                days_in_month = monthrange(2023, month)[1]

                if day > days_in_month:
                    day = 1
                    month += 1
                    if month > 12:
                        break

                current_day_dir = os.path.join(year_dir, f"{month:02}", f"{day:02}")
                output_file = open(os.path.join(current_day_dir, f"part_{file_count}.txt"), 'w', encoding='utf-8')

        output_file.close()

if __name__ == "__main__":
    input_file = "file_.txt"  # Ganti dengan path ke file besar Anda
    output_dir = "path_directory"      # Ganti dengan path ke direktori output
    split_file(input_file, output_dir)
