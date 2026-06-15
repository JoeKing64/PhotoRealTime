import os
import platform
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
        return None
    except Exception as e:
        print(f"[ERROR] 读取 EXIF 失败: {file_path} -> {e}")
        return None


def set_file_mtime(file_path, dt):
    """只设置文件的修改时间"""
    timestamp = dt.timestamp()
    os.utime(file_path, (timestamp, timestamp))


def set_file_times_windows(file_path, dt):
    """Windows 下同时设置创建时间和修改时间"""
    formatted_time = dt.strftime("%Y:%m:%d %H:%M:%S")

    result = subprocess.run(
        [
            'exiftool',
            f'-FileModifyDate={formatted_time}',
            f'-FileCreateDate={formatted_time}',
            '-overwrite_original',
            file_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())


def process_photos(folder_path):
    system_name = platform.system()

    print(f"[SYSTEM] 当前系统判定为: {system_name}")

    if system_name == "Darwin":
        print("[MODE] macOS：只修改文件的“修改时间”")
    elif system_name == "Windows":
        print("[MODE] Windows：同时修改文件的“创建时间”和“修改时间”")
    else:
        print("[MODE] 其他系统：只修改文件的“修改时间”")

    supported_exts = {'.heic', '.jpg', '.jpeg'}

    success_count = 0
    fail_count = 0
    skip_count = 0

    for file in os.listdir(folder_path):
        ext = os.path.splitext(file)[1].lower()

        if ext not in supported_exts:
            continue

        full_path = os.path.join(folder_path, file)
        exif_dt = get_exif_datetime(full_path)

        if not exif_dt:
            print(f"[SKIP] 未找到 EXIF 拍摄时间: {file}")
            skip_count += 1
            continue

        try:
            if system_name == "Windows":
                set_file_times_windows(full_path, exif_dt)
                print(f"[OK] {file} 创建时间 + 修改时间 已更新为 {exif_dt}")
            else:
                set_file_mtime(full_path, exif_dt)
                print(f"[OK] {file} 修改时间 已更新为 {exif_dt}")

            success_count += 1

        except Exception as e:
            print(f"[ERROR] 更新时间失败: {file} -> {e}")
            fail_count += 1

    print("\n===== 处理完成 =====")
    print(f"成功: {success_count} 张")
    print(f"失败: {fail_count} 张")
    print(f"跳过(无EXIF): {skip_count} 张")


if __name__ == "__main__":
    process_photos("./")