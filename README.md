📌 脚本功能：
本脚本自动扫描当前文件夹下的照片文件（HEIC、JPG、JPEG），
从照片的 EXIF 信息中提取拍摄时间（DateTimeOriginal），
并将该时间设置为文件的“修改时间”（mtime），用于同步照片实际拍摄时间。

📁 支持格式：
- .HEIC / .heic
- .JPG / .jpg
- .JPEG / .jpeg

✅ 环境要求：
- Python 3.x（已安装）
- 不需要安装额外 Python 库
- 需要安装 `exiftool`（用于读取 EXIF 拍摄时间）

━━━━━━━━━━━━━━━━━━━━━━
📥 安装 exiftool 方法
━━━━━━━━━━━━━━━━━━━━━━

🔹 macOS 安装步骤：
1. 安装 Homebrew（如果尚未安装）：
   打开“终端”，粘贴并运行以下命令：
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   安装完成后，按照屏幕提示，可能需要把 Homebrew 加入到你的 shell 路径里，通常是运行：
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"


2. 安装 exiftool：
   brew install exiftool

3. 验证安装是否成功：
   exiftool -ver
   如果能看到版本号，例如 12.76，则说明成功。

🔹 Windows 安装步骤：
1. 访问官网下载安装包：
   https://exiftool.org/

2. 下载“Windows Executable”（可执行文件）版本：
   - 解压后，将 `exiftool(-k).exe` 改名为 `exiftool.exe`
   - 将它放到你运行脚本的同一目录，或添加到系统 PATH

3. 验证安装是否成功：
   打开命令提示符，输入：
   exiftool -ver

━━━━━━━━━━━━━━━━━━━━━━
▶️ 运行脚本
━━━━━━━━━━━━━━━━━━━━━━

1. 将 `fix_photo_mtime.py` 脚本放在包含照片的文件夹内。
2. 打开终端（macOS）或命令提示符（Windows）。
3. 进入该文件夹路径。
4. 执行脚本：

   python fix_photo_mtime.py

脚本会自动处理当前文件夹中的所有 HEIC 和 JPEG 照片，
并将每个文件的“修改时间”更新为拍摄时间。

━━━━━━━━━━━━━━━━━━━━━━
📌 注意事项：
━━━━━━━━━━━━━━━━━━━━━━

- 脚本不会修改照片内容，只修改文件的“修改日期”（mtime）。
- 如果某张照片缺少拍摄时间，将跳过处理并给出提示。
- 脚本默认处理当前文件夹（可修改代码支持子目录）。
- 若你使用的是中文系统，确保照片是由支持 EXIF 拍摄时间的设备拍摄（例如 iPhone、相机）。

━━━━━━━━━━━━━━━━━━━━━━
