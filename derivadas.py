from __future__ import print_function
from __future__ import division
from os.path import exists
import cv2
import numpy as np
import matplotlib.pyplot as plt
# leer argumentos por linea de comandos
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Algunas operaciones sobre imágenes con OpenCV',
        add_help=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE', help='archivo', type=str)
    args = vars(parser.parse_args())

    imagen = args['FILE']

    if not exists(imagen):
        raise IOError('el archivo \'{}\' no se puede leer'.format(filename))

    # leer la imagen de disco (formato BGR)
    img = cv2.imread(imagen,0)

    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,5),plt.imshow(sobely,cmap = 'gray')
    plt.title(' X + Y '), plt.xticks([]), plt.yticks([])

    plt.show()


