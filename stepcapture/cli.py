import os
import PySimpleGUI as sg
from .config import Config
from .listener import start_listening

def main():
    # 界面布局
    # sg.theme('SystemDefault')
    config = Config()
    # 左侧参数表单
    layout = [
        [sg.Text('日志级别：'), sg.Combo(['all','mouse','keyboard'], default_value=config.log_level, key='log_level')],
        [sg.Frame('圈注样式', [
            [sg.Text('半径：'), sg.InputText(str(config.annotation['circle']['radius']), size=(5,1), key='circle_radius'),
             sg.Text('线宽：'), sg.InputText(str(config.annotation['circle']['thickness']), size=(5,1), key='circle_thickness')],
            [sg.Text('颜色：'), sg.InputText(config.annotation['circle']['color'], size=(7,1), key='circle_color')]
        ])],
        [sg.Frame('气泡注释', [
            [sg.Text('文字大小：'), sg.InputText(str(config.annotation['tooltip']['font_size']), size=(5,1), key='tooltip_font_size')],
            [sg.Text('文字色：'), sg.InputText(config.annotation['tooltip']['font_color'], size=(7,1), key='tooltip_font_color')],
            [sg.Text('背景：'), sg.InputText(config.annotation['tooltip']['bg_color'], size=(7,1), key='tooltip_bg_color')],
            [sg.Text('内边距：'), sg.InputText(str(config.annotation['tooltip']['padding']), size=(5,1), key='tooltip_padding')],
            [sg.Text('圆角：'), sg.InputText(str(config.annotation['tooltip']['border_radius']), size=(5,1), key='tooltip_border_radius')]
        ])],
        [sg.Button('保存并开始记录'), sg.Button('取消')]
    ]

    window = sg.Window('StepCapture 设置', layout, resizable=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '取消'):
            window.close()
            return
        if event == '保存并开始记录':
            # 更新配置并写回文件
            cfg_data = config._data
            cfg_data['log_level'] = values['log_level']
            c = cfg_data['annotation']['circle']
            c['radius'] = int(values['circle_radius'])
            c['thickness'] = int(values['circle_thickness'])
            c['color'] = values['circle_color']
            t = cfg_data['annotation']['tooltip']
            t['font_size'] = int(values['tooltip_font_size'])
            t['font_color'] = values['tooltip_font_color']
            t['bg_color'] = values['tooltip_bg_color']
            t['padding'] = int(values['tooltip_padding'])
            t['border_radius'] = int(values['tooltip_border_radius'])
            # 保存到默认配置（也可另存为用户自定义）
            import yaml
            with open(os.path.join(os.path.dirname(__file__), '..','configs','default.yaml'), 'w', encoding='utf-8') as f:
                yaml.safe_dump(cfg_data, f, allow_unicode=True)
            window.close()
            start_listening(config)
            break

if __name__ == '__main__':
    main()
