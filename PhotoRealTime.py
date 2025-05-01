import os
import subprocess
from datetime import datetime

def get_exif_datetime(file_path):
    """使用 exiftool 提取拍摄时间（DateTimeOriginal）"""
    try:
        result = subprocess.run(
            ['exiftool', '-DateTimeOriginal', '-s3', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.strip()
        if output:
            return datetime.strptime(output, "%Y:%m:%d %H:%M:%S")
        else:
            return None
    except Exception as e:
        print(f"[ERROR] 读取 EXIF 失败: {file_path} -> {e}")
        return None

def set_file_mtime(file_path, dt):
    """设置文件的修改时间"""
    timestamp = dt.timestamp()
    os.utime(file_path, (timestamp, timestamp))

def process_photos(folder_path):
    supported_exts = {'.heic', '.jpg', '.jpeg'}
    for file in os.listdir(folder_path):
        ext = os.path.splitext(file)[1].lower()
        if ext in supported_exts:
            full_path = os.path.join(folder_path, file)
            exif_dt = get_exif_datetime(full_path)
            if exif_dt:
                set_file_mtime(full_path, exif_dt)
                print(f"[OK] {file} 修改时间已更新为 {exif_dt}")
            else:
                print(f"[SKIP] 未找到 EXIF 拍摄时间: {file}")

if __name__ == "__main__":
    process_photos("./")
