from __future__ import print_function
from __future__ import division
from os.path import exists
import cv2
import numpy as np
import matplotlib.pyplot as plt
# leer argumentos por linea de comandos
import argparse

class VConvolutionFilter(object):
	"""A filter that applies a convolution to V (or all of BGR)."""
	def __init__(self, kernel):
		self._kernel = kernel
	def apply(self, src, dst):
		"""Apply the filter with a BGR or gray source/destination."""
		cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
	"""A sharpen filter with a 1-pixel radius."""
	def __init__(self):
		kernel = np.array([	[-1, -1, -1],
								[-1, 9, -1],
								[-1, -1, -1]])
		VConvolutionFilter.__init__(self, kernel)

class IdentityFilter(VConvolutionFilter):
	"""A sharpen filter with a 1-pixel radius."""
	def __init__(self):
		kernel = np.array([	[0, 0, 0],
								[0, 1, 0],
								[0, 0, 0]])
		VConvolutionFilter.__init__(self, kernel)

#  class FindEdgesFilter(VConvolutionFilter):
#      """An edge-finding filter with a 1-pixel radius."""
#      def __init__(self):
#          kernel = numpy.array([[-1, -1, -1],
#                                  [-1, 8, -1],
#                                  [-1, -1, -1]])
#          VConvolutionFilter.__init__(self, kernel)
#
#  class BlurFilter(VConvolutionFilter):
#      """A blur filter with a 2-pixel radius."""
#      def __init__(self):
#          kernel = numpy.array([[0.04, 0.04, 0.04, 0.04,
#                                  [0.04, 0.04, 0.04, 0.04,
#                                  [0.04, 0.04, 0.04, 0.04,
#                                  [0.04, 0.04, 0.04, 0.04,
#                                  [0.04, 0.04, 0.04, 0.04,
#          VConvolutionFilter.__init__(self, kernel)
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Algunas operaciones sobre imagenes con OpenCV',
        add_help=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE', help='archivo', type=str)
    args = vars(parser.parse_args())

    imagen = args['FILE']

    if not exists(imagen):
        raise IOError('el archivo \'{}\' no se puede leer'.format(filename))
    
    sharpen_filter = SharpenFilter()
	identity_filter = IdentityFilter()
	# leer la imagen de disco (formato BGR)
	img = cv2.imread(imagen)
	#  dst_sharpened = cv2.imread(imagen)
	dst_identity = cv2.imread(imagen)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    sharpen_filter.apply(img,dst_sharpened)
    identity_filter.apply(img,dst_identity)
    

    plt.subplot(2,3,1),plt.imshow(img)
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,2),plt.imshow(dst_sharpened)
    plt.title('sharpen filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(dst_identity)
    plt.title('identity filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(dst_identity)
    plt.title('blur filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(dst_identity)
    plt.title('identity filter'), plt.xticks([]), plt.yticks([])
    plt.show()


