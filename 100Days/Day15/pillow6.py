# 操作像素

from PIL import Image

def main():
    image = Image.open('guido.jpg')

    # 将灰色放入指定像素
    for x in range(80, 310):
        for y in range(20, 360):
            image.putpixel((x,y), (128, 128, 128))

    image.show()

if __name__ == '__main__':
    main()