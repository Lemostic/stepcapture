# StepCapture

轻量级的 Windows 屏幕交互记录工具，使用 Python 和 PySimpleGUI 构建。

## 🧰 功能特性

- 🖱️ 记录鼠标点击位置，并添加高亮圈注
- ⌨️ 记录键盘按键
- 🎨 可定制圈注样式（颜色、线条粗细）
- 💬 鼠标点击处显示注释气泡（Tooltip）
- 📝 支持设置日志级别
- 📁 图形界面用于配置首选项
- 📦 一键打包为独立的 Windows 可执行文件（.exe）

## 💻 安装与运行

### 环境要求

- Windows 10 或更高版本
- Python 3.7 及以上

### 安装步骤

1. 克隆本仓库：

```bash
 git clone https://github.com/your_username/StepCapture.git
cd StepCapture
```

2. 创建虚拟环境并激活：

```bash
python -m venv venv
venv\Scripts\activate
```
3. 安装依赖：

```bash
复制
编辑
pip install -r requirements.txt
```
4. 运行主程序：

```bash
python main.py
```

# 打包为可执行文件
使用 PyInstaller 打包：

```bash
pyinstaller --onefile --windowed main.py
```
打包后的可执行文件位于 dist/ 目录下。

# ⚙️ 配置说明
配置文件位于 config.json，用于设置日志级别、圈注样式等参数。您也可以通过图形界面进行配置，配置界面类似于 Snipaste 的首选项设置。

# 📸 截图展示

# 🤝 贡献指南
欢迎贡献代码、提出建议或报告问题！
1. Fork 本仓库

2. 创建新分支：git checkout -b feature/YourFeature

3. 提交更改：git commit -m 'Add YourFeature'

4. 推送到分支：git push origin feature/YourFeature

5. 提交 Pull Request

# 📄 许可证
本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。