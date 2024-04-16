import os
import shutil

# 다운로드 폴더 경로
download_folder = "C:\\Users\\student\\Downloads"

# 대상 확장자 및 대상 폴더 지정
file_types = {
    ".jpg": "\\images",
    ".jpeg": "\\images",
    ".csv": "\\data",
    ".xlsx": "\\data",
    ".txt": "\\docs",
    ".doc": "\\docs",
    ".pdf": "\\docs",
    ".zip": "\\archive"
}

# 폴더 생성 함수
def create_folders():
    for folder in file_types.values():
        folder_path = download_folder + folder
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# 파일 이동 함수
def move_files():
    for file in os.listdir(download_folder):
        if os.path.isfile(os.path.join(download_folder, file)):
            file_extension = os.path.splitext(file)[1]
            if file_extension in file_types:
                src = os.path.join(download_folder, file)
                dest_folder = download_folder + file_types[file_extension]
                dest = os.path.join(dest_folder, file)
                shutil.move(src, dest)
                print(f"Moved {file} to {dest_folder}")

# 메인 함수
def main():
    create_folders()
    move_files()

if __name__ == "__main__":
    main()
