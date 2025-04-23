import os
from datetime import datetime
from mss import mss
from .annotator import annotate_image
from .exporter import Exporter

class Recorder:
    """负责截图、调用注释、收集日志并最终导出"""
    def __init__(self, config):
        self.config = config
        self.steps = []  # 存 (seq, ts, desc, filepath)
        self.seq = 0
        # 创建输出目录
        base = os.getcwd()
        stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.output_dir = os.path.join(base, f'record_{stamp}')
        self.screenshot_dir = os.path.join(self.output_dir, 'screenshots')
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def _screenshot(self):
        """截取全屏并返回临时路径"""
        raw = mss().grab(mss().monitors[0])
        path = os.path.join(self.screenshot_dir, f'raw_{self.seq:04d}.png')
        from PIL import Image
        img = Image.frombytes('RGB', raw.size, raw.rgb)
        img.save(path)
        return path

    def record_mouse(self, x, y, button):
        self.seq += 1
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        raw = self._screenshot()
        out = os.path.join(self.screenshot_dir, f'{self.seq:04d}.png')
        desc = f'{button.name} 点击 at ({x},{y})'
        annotate_image(raw, out, (x, y), desc, self.config.annotation)
        self.steps.append((self.seq, ts, desc, out))
        print(f'[{ts}] {desc}')

    def record_keyboard(self, key):
        self.seq += 1
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        raw = self._screenshot()
        out = os.path.join(self.screenshot_dir, f'{self.seq:04d}.png')
        try:
            k = key.char
        except AttributeError:
            k = key.name
        desc = f'键盘按下 "{k}"'
        # 键盘操作不圈注，仅保存截图
        annotate_image(raw, out, None, desc, self.config.annotation)
        self.steps.append((self.seq, ts, desc, out))
        print(f'[{ts}] {desc}')

    def finish(self):
        """导出文档"""
        exporter = Exporter(self.output_dir, self.steps)
        exporter.export()
