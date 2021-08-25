from pynput import keyboard, mouse
from PIL import ImageGrab

def getHex(rgb):
    return '%02X%02X%02X'%rgb

def getRGB(x,y):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    return (r,g,b)

def onClick(x,y, button, pressed):
	if pressed and button == mouse.Button.left:
		print(f'RGB = {getRGB(x,y)}\t| HEX=#{getHex(getRGB(x,y))}')

def onRel(key):
	if key == keyboard.Key.esc:
		mlstnr.stop()
		return False

if __name__ == '__main__':
    with keyboard.Listener(on_release = onRel) as klstnr:
        with mouse.Listener(on_click = onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()

