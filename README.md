# PhotoRealTime

这个脚本用于读取照片文件中的 EXIF 拍摄时间（`DateTimeOriginal`），并将照片文件的系统时间同步为真实拍摄时间。

适用于相机照片导入电脑后，文件的创建时间或修改时间与实际拍摄时间不一致的情况。

---

## 功能说明

- 自动读取当前目录下的照片文件
- 支持 `.heic`、`.jpg`、`.jpeg` 格式
- 使用 `exiftool` 提取照片的 EXIF 拍摄时间
- 根据不同操作系统自动选择更新时间方式：
  - **Windows**：同时更新文件的“创建时间”和“修改时间”
  - **macOS**：只更新文件的“修改时间”
  - **其他系统**：只更新文件的“修改时间”
- 自动跳过没有 EXIF 拍摄时间的照片
- 处理完成后输出成功、失败、跳过数量统计

---

## 使用前准备

### 1. 安装 Python

请先确保电脑已经安装 Python 3.x。

可以随便安装，任意版本皆可；若已安装，则无需重复安装，可直接跳过此步骤。

### 2. 安装 ExifTool

本脚本依赖 ExifTool 读取照片 EXIF 信息，因此运行前必须先安装 ExifTool。

#### Windows

1. 打开 ExifTool 官网：

   https://exiftool.org/

2. 下载 Windows 版本：

   ```text
   exiftool-13.xx_64.zip.zip
   ```

3. 解压后，将：

   ```text
   exiftool(-k).exe
   ```

   去掉后面的(-k)，重命名为：

   ```text
   exiftool.exe
   ```

4. 将 `exiftool.exe` 所在目录加入系统 `PATH`。

5. 打开命令行验证：

   ```bash
   exiftool -ver
   ```

6. 正常情况下会显示版本号，则为安装成功，例如：

   ```text
   13.31
   ```

#### macOS

##### 1. 安装 Homebrew（如果尚未安装）

打开“终端”，粘贴并运行以下命令：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装完成后，按照屏幕提示，可能需要把 Homebrew 加入到 Shell 路径中，通常执行：

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

##### 2. 安装 ExifTool

```bash
brew install exiftool
```

##### 3. 验证安装是否成功

```bash
exiftool -ver
```

如果能看到版本号（例如 `12.76`），则说明安装成功。

---

## 使用方法

1. 将 `PhotoRealTime_v2.0.py` 放到需要处理的照片文件夹中。
2. 将所有需要修正时间的照片也放在同一个文件夹中。
3. 双击或右键运行脚本。

脚本会自动处理当前文件夹下支持格式的照片。

---

## 处理逻辑

脚本会按以下流程工作：

1. 判断当前操作系统。
2. 扫描当前文件夹下的 `.heic`、`.jpg`、`.jpeg` 文件。
3. 使用 `exiftool` 读取每张照片的 `DateTimeOriginal`。
4. 如果读取成功：
   - Windows 下同步创建时间和修改时间；
   - macOS 下同步修改时间。
5. 如果照片没有 EXIF 拍摄时间，则跳过该文件。
6. 最后输出处理统计结果。

---

## 输出示例

```text
[SYSTEM] 当前系统判定为: Windows
[MODE] Windows：同时修改文件的“创建时间”和“修改时间”
[OK] IMG_0001.JPG 创建时间 + 修改时间 已更新为 2024-01-01 12:30:00
[SKIP] 未找到 EXIF 拍摄时间: IMG_0002.JPG

===== 处理完成 =====
成功: 1 张
失败: 0 张
跳过(无EXIF): 1 张
```
