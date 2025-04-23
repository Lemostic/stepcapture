import os
from datetime import datetime

class Exporter:
    """将 steps 列表导出为 Markdown 文档"""
    def __init__(self, base_dir, steps):
        self.base_dir = base_dir
        self.steps = steps
        self.md_path = os.path.join(base_dir, 'steps.md')

    def export(self):
        with open(self.md_path, 'w', encoding='utf-8') as f:
            f.write(f'# 操作记录  {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
            for seq, ts, desc, img in self.steps:
                rel = os.path.join('screenshots', os.path.basename(img))
                f.write(f'## 步骤 {seq}\n')
                f.write(f'- 时间：{ts}\n')
                f.write(f'- 操作：{desc}\n\n')
                f.write(f'![step{seq}]({rel})\n\n')
        print(f'导出完成：{self.md_path}')
