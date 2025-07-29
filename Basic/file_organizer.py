import os
import shutil


FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder_name, extensions in FILE_TYPES.items(): 
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename)) 
                print(f"Moved: {filename} → {folder_name}/")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(folder_path, "Others") 
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} → Others/")

def main():
    path = input("Enter the folder path you want to organize: ").strip()

    if os.path.exists(path):
        organize_folder(path)
        print("\n✅ Organizing complete!")
    else:
        print("❌ Folder not found. Please check the path.")

if __name__ == "__main__":
    main()
