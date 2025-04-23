import threading
import time
from datetime import datetime
from pynput import mouse, keyboard

from .recorder import Recorder

class Listener:
    """统一启动鼠标和键盘监听，控制录制流程"""
    def __init__(self, config):
        self.config = config
        self.recorder = Recorder(config)
        self._running = True
        self._paused = False
        self._keys = set()
        # 定义热键
        self._stop_keys = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='s')}
        self._pause_keys = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='p')}

    def _on_click(self, x, y, button, pressed):
        if not pressed or self._paused:
            return
        if self.config.log_level in ('all', 'mouse'):
            self.recorder.record_mouse(x, y, button)

    def _on_press(self, key):
        self._keys.add(key)
        # 停止
        if self._stop_keys <= self._keys:
            self._running = False
            return False
        # 暂停/继续
        if self._pause_keys <= self._keys:
            self._paused = not self._paused
            state = '暂停' if self._paused else '继续'
            print(f'已{state}记录')
            return
        # 普通键盘
        if not self._paused and self.config.log_level in ('all', 'keyboard'):
            self.recorder.record_keyboard(key)

    def _on_release(self, key):
        if key in self._keys:
            self._keys.remove(key)

    def start(self):
        """启动监听线程，直至停止"""
        print('开始记录：Ctrl+Shift+P 暂停/继续；Ctrl+Shift+S 停止并导出')
        with mouse.Listener(on_click=self._on_click) as ml,\
             keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as kl:
            while self._running:
                time.sleep(0.1)
        ml.stop()
        kl.stop()
        self.recorder.finish()

def start_listening(config):
    Listener(config).start()
