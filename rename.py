import os
import datetime
from pymediainfo import MediaInfo

# Folder containing files
folder_path = r"C:\path\to\your\files"  # Change to your folder

# Naming convention menu
options = {
    "1": "examplefilename-01.02.2023 (MM.DD.YYYY)",
    "2": "examplefilename-2023.02.01 (YYYY.MM.DD)",
    "3": "examplefilename_01-02-2023 (MM-DD-YYYY)",
    "4": "examplefilename (2023-02-01) (YYYY-MM-DD in parentheses)",
    "5": "01.02.2023-examplefilename (MM.DD.YYYY at the start)",
    "6": "20230201-examplefilename (YYYYMMDD without separators at the start)",
    "7": "examplefilename_20230201 (YYYYMMDD without separators at the end)",
    "8": "2023-02-01 examplefilename (YYYY-MM-DD at the start with a space)"
}

# Print options
print("Select a naming convention:")
for key, value in options.items():
    print(f"{key}) {value}")

# Get selection
choice = input("Enter a number (1-8): ")

# Define formatting options
format_options = {
    "1": "-%m.%d.%Y",
    "2": "-%Y.%m.%d",
    "3": "_%m-%d-%Y",
    "4": " (%Y-%m-%d)",
    "5": "%m.%d.%Y-",
    "6": "%Y%m%d-",
    "7": "_%Y%m%d",
    "8": "%Y-%m-%d "
}

# Validate choice
if choice not in format_options:
    print("Invalid choice. Exiting.")
    exit()

# Selected date format
date_format = format_options[choice]

# Process files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        media_info = MediaInfo.parse(file_path)
        created_date = None

        for track in media_info.tracks:
            if track.track_type == "General":
                created_date = getattr(track, "encoded_date", None)  # Extract encoded_date
                if created_date:
                    created_date = created_date.split(" ")[0]  # Keep only YYYY-MM-DD
                break

        if created_date:
            formatted_date = datetime.datetime.strptime(created_date, "%Y-%m-%d").strftime(date_format)
            name, ext = os.path.splitext(filename)

            # Determine position of the date
            if choice in ["1", "2", "3", "4", "7"]:  # Append date at the end
                new_filename = f"{name}{formatted_date}{ext}"
            else:  # Prepend date at the start
                new_filename = f"{formatted_date}{name}{ext}"

            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipping {filename}: No valid date found")
