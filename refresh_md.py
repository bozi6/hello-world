"""Module for refreshing the readme.md file with project information."""
import os
from datetime import datetime
from pathlib import Path

DATE_FORMAT = '%Y-%m-%d %H:%m:%S'

README_INTRO = """
# Python Home Projects
## Projects list:
| File Name | Creation Date | Last Modificated Date | Description |
| --------- | ------------- | --------------------- | ----------- |
"""

README_FOOTER = f"""
---
## License  
MIT  
---  
Created by kontab@gmail.com  
Latest version generated: {datetime.today().strftime(DATE_FORMAT)}
"""

GITHUB_BASE_URL = "https://github.com/bozi6/hello-world/tree/master/"


def get_directory_info(directory_path):
    """
    Create a dictionary containing file information from the given directory.
    
    Args:
        directory_path: Path to the directory to analyze
        
    Returns:
        Dictionary containing file number, name, creation and modification dates
    """
    file_paths = [fd for fd in os.listdir(directory_path)]
    data_dict = {}

    for index, file_path in enumerate(file_paths):
        full_path = Path(directory_path) / file_path
        stat_info = os.stat(full_path)
        creation_date = datetime.fromtimestamp(stat_info.st_ctime)
        modification_date = datetime.fromtimestamp(stat_info.st_mtime)

        data_dict[index] = {
            'index'      : index,
            'filename'   : file_path,
            'create_date': creation_date.strftime(DATE_FORMAT),
            'mod_date'   : modification_date.strftime(DATE_FORMAT),
            'is_dir'     : full_path.is_dir()
        }

    return data_dict


def get_description(directory):
    """
    Read description from description.txt file if directory exists.
    
    Args:
        directory: Path to the directory containing description.txt
        
    Returns:
        Description text or '-' if file not found or path is not a directory
    """
    if not directory.is_dir():
        return '-'

    filepath = directory / "description.txt"
    try:
        with filepath.open("r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return '-'


def main():
    """Refresh the README.md file in current working directory."""
    path = Path.cwd()
    directory_data = get_directory_info(path)

    with Path(path / "README.md").open("w", encoding="utf-8") as f:
        f.write(README_INTRO)
        for _, file_data in directory_data.items():
            if not file_data['filename'].startswith('.'):
                description = get_description(path / file_data['filename'])
                file_entry = (
                    f"| [{file_data['filename']}]({GITHUB_BASE_URL + file_data['filename']}) | "
                    f"{file_data['create_date']} | {file_data['mod_date']} | {description}\n"
                )
                f.write(file_entry)
        f.write(README_FOOTER)


if __name__ == '__main__':
    main()
