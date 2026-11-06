import win32gui
import win32con
import ctypes
import time
import sys

user32 = ctypes.windll.user32

q = user32.MessageBoxW(
    0,
    "AVISO você acaba de executar um arquivo de GDI. Se vc ver um cmd aberto, não feche",
    "primeiro aviso",
    0x34 # this code means ( yes/no with warning icon )
    )
if q!=6:
    sys.exit(0)
else:
    pass

q = user32.MessageBoxW(
    0,
    "Mas ele não afeta seu pc se querer continuar clique em sim",
    "Ultimo aviso",
    0x34 # this code means ( yes/no with warning icon )
    )
if q!=6:
    sys.exit(0)
else:
    pass

w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # gets screen resolution

while True:
    hdc = win32gui.GetDC(0)
    win32gui.BitBlt(hdc, 1, 1, w, h, hdc, 0, 0, win32con.SRCINVERT)
    win32gui.ReleaseDC(0, hdc)
    time.sleep(0.02)
    
import random
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
while True:
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)