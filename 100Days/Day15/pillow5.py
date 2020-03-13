# 旋转和翻转

from PIL import Image

def main():
    image = Image.open('guido.jpg')
    # 旋转180°
    image.rotate(180).show()
    # 左右翻转
    image.transpose(Image.FLIP_LEFT_RIGHT).show()

if __name__ == '__main__':
    main()