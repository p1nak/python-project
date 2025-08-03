import os
import shutil
from datetime import datetime

# Mapping extensions to folder names with more comprehensive categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv", ".rtf"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".php", ".json", ".xml"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Databases": [".sql", ".db", ".sqlite", ".mdb"]
}

def organize_folder(folder_path):
    """Organize files into categorized folders with duplicate handling"""
    stats = {"moved": 0, "skipped": 0, "errors": 0}
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.'):
            stats["skipped"] += 1
            continue

        try:
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    
                    # Handle duplicates by adding timestamp
                    dest_path = os.path.join(target_folder, filename)
                    if os.path.exists(dest_path):
                        base, ext = os.path.splitext(filename)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        new_filename = f"{base}_{timestamp}{ext}"
                        dest_path = os.path.join(target_folder, new_filename)
                    
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {filename} → {folder_name}/")
                    stats["moved"] += 1
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved: {filename} → Others/")
                stats["moved"] += 1

        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")
            stats["errors"] += 1
    
    return stats

def main():
    print("📂 File Organizer 2.0")
    print("---------------------")
    
    while True:
        path = input("\nEnter folder path (or 'q' to quit): ").strip()
        
        if path.lower() == 'q':
            break
            
        if not os.path.exists(path):
            print("❌ Error: Folder does not exist. Please try again.")
            continue
            
        print("\nOrganizing files...")
        stats = organize_folder(path)
        
        print("\n📊 Organization Summary:")
        print(f"- Files moved: {stats['moved']}")
        print(f"- Files skipped: {stats['skipped']}")
        print(f"- Errors encountered: {stats['errors']}")
        print("\n✅ Operation completed successfully!")

if __name__ == "__main__":
    main()
