from pathlib import Path
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css"],
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"

def organize_downloads(folder=Path.home() / "Downloads"):
    folder = Path(folder)
    print(f"Looking in: {folder}")

    files = list(folder.iterdir())
    print(f"Found {len(files)} item(s)")

    folder = Path(folder)
    for file in folder.iterdir():
        if not file.is_file():
            continue

        target_dir = folder / get_category(file.suffix)
        target_dir.mkdir(exist_ok=True)

        target_path = target_dir / file.name
        if target_path.exists():
            target_path = target_dir / f"{file.stem}_copy{file.suffix}"

        shutil.move(str(file), str(target_path))
        print(f"Moved {file.name} to {target_dir.name}/")

if __name__ == "__main__":
    organize_downloads()
