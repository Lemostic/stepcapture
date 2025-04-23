from PIL import Image, ImageDraw, ImageFont

def annotate_image(raw_path, out_path, pos, text, cfg):
    """
    - raw_path: 原始截图
    - out_path: 注释后输出
    - pos: (x,y)，若为 None，仅保存原图
    - text: 注释文字
    - cfg: cfg.annotation 配置
    """
    img = Image.open(raw_path).convert('RGB')
    draw = ImageDraw.Draw(img)
    if pos:
        x, y = pos
        c = cfg['circle']
        # 圈注
        draw.ellipse(
            [(x-c['radius'], y-c['radius']), (x+c['radius'], y+c['radius'])],
            outline=c['color'], width=c['thickness']
        )
        # 气泡
        tcfg = cfg['tooltip']
        font = ImageFont.load_default()
        tw, th = draw.textsize(text, font=font)
        pad = tcfg['padding']
        bx0, by0 = x+c['radius']+pad, y-th//2-pad
        bx1, by1 = bx0+tw+2*pad, by0+th+2*pad
        draw.rounded_rectangle(
            [(bx0, by0), (bx1, by1)],
            radius=tcfg['border_radius'],
            fill=tcfg['bg_color'],
            outline=c['color'],
            width=1
        )
        draw.text((bx0+pad, by0+pad), text, fill=tcfg['font_color'], font=font)
    # 保存
    img.save(out_path)
