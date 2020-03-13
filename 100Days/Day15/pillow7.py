# 滤镜效果

from PIL import Image, ImageFilter

def main():

    image = Image.open('guido.jpg')

    # 提取轮廓
    image.filter(ImageFilter.CONTOUR).show()

if __name__ == '__main__':
    main()