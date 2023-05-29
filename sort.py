import argparse
from pathlib import Path
import shutil
import threading


def copy_file(folder_path: Path, destination_folder):
    for file in folder_path.iterdir():
        if file.is_file():
            extension = file.suffix
            extension_folder = destination_folder / extension[1:]
            extension_folder.mkdir(parents=True, exist_ok=True)
            shutil.copy(str(file), str(extension_folder))



def grabs_folder(path: Path) -> None:
    folders = []
    for folder in path.iterdir():
        if folder.is_dir():
            folders.append(folder)
            folder_thread = threading.Thread(target=grabs_folder, args=(folder,))
            folder_thread.start()
    return folders


def main():
    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")

    args = vars(parser.parse_args())
    
    source = Path(args.get("source"))
    output = Path(args.get("output"))

    output.mkdir(parents=True, exist_ok=True)
    folders = grabs_folder(source)

    for el in folders:
        copy_file(el, output)


if __name__ == "__main__":
    main()