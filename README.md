# Media File Renamer

A Python script to rename media files by appending or prepending the media creation date extracted from the file metadata. The script allows for customizable naming conventions based on the user's preferences.

This tool was originally created for personal use to help organize and back up media files by renaming them in a consistent and easily searchable format.

## Features

- Extracts the media creation date from video files
- Supports multiple customizable naming formats
- Renames files by appending or prepending the date in various formats
- Works with common video formats (MP4, MOV, AVI, etc.)
- Easy-to-use menu interface to choose from multiple date formats

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tylermong/media-file-renamer.git
   ```

2. Install the required dependencies:
   ```bash
   pip install pymediainfo
   ```

3. Run the script:
   ```bash
   python rename.py
   ```

## Usage

When running the script, you will be prompted to select a naming convention. Options include:

- **filename-MM.DD.YYYY**: `examplefilename-01.02.2023`
- **filename-YYYY.MM.DD**: `examplefilename-2023.02.01`
- **filename_MM-DD-YYYY**: `examplefilename_01-02-2023`
- **filename (YYYY-MM-DD)**: `examplefilename (2023-02-01)`
- **MM.DD.YYYY-filename**: `01.20.2023-examplefilename`
- **YYYYMMDD-filename**: `20230201-examplefilename`
- **filename_YYYYMMDD**: `examplefilename_20230201`
- **YYYY-MM-DD filename**: `2023-02-01 examplefilename`

You can adjust the script to fit your own file structure and renaming preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
