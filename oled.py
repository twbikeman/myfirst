import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import subprocess

RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width,height))
draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height),outline = 0, fill = 0)
font = ImageFont.load_default()

cmd = "hostname -I"
IP = subprocess.check_output(cmd, shell = True)
draw.text((0,0),"IP: " + IP.decode('utf-8'),font = font, fill = 255)



disp.image(image)
disp.display()

