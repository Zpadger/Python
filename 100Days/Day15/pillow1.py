# Image类，读取和处理图像

from PIL import Image

def main():

    image = Image.open('guido.jpg')
    # image.format, image.size, image.mode('JPEG', (500,750), 'RGB')

    image.show()

if __name__ == '__main__':
    main()