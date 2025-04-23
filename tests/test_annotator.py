import os
import tempfile
from stepcapture.annotator import annotate_image
from PIL import Image

def test_annotate_image_without_pos():
    # 创建临时纯色图
    img = Image.new('RGB', (100, 100), color='white')
    tmp_raw = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    img.save(tmp_raw)
    tmp_out = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name

    cfg = {
        'circle': {'radius':10,'thickness':1,'color':'#FF0000'},
        'tooltip': {'font_size':12,'font_color':'#000','bg_color':'#FFF','padding':2,'border_radius':2}
    }
    # 不传 pos，仅保存原图
    annotate_image(tmp_raw, tmp_out, None, '测试', cfg)
    assert os.path.exists(tmp_out)
    os.remove(tmp_raw); os.remove(tmp_out)

def test_annotate_image_with_pos():
    img = Image.new('RGB', (200, 200), color='white')
    raw = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    img.save(raw)
    out = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name

    cfg = {
        'circle': {'radius':5,'thickness':1,'color':'#00FF00'},
        'tooltip': {'font_size':10,'font_color':'#000','bg_color':'#EEE','padding':1,'border_radius':1}
    }
    annotate_image(raw, out, (50,50), '点', cfg)
    assert os.path.exists(out)
    os.remove(raw); os.remove(out)
