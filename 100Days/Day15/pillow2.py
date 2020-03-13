# 剪裁图像

from PIL import Image

def main():
    image = Image.open('guido.jpg')
    rect = 80, 20, 310, 360

    image.crop(rect).show()

if __name__ == '__main__':
    main()