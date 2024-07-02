import pyqrcode
import png
from pyqrcode import QRCODE
s =""
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 0)