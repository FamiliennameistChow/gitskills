# from sys import argv
#
# try:
#     port = int(argv[argv.index('-P') + 1])
# except ValueError:
#     port = 5008
# except IndexError:
#     port = 5008
# finally:
#     print("Web Port:", port)

import cv2
import numpy as np

fs = cv2.FileStorage('abc.xml', cv2.FileStorage_WRITE)
fs.write('mat1', np.random.uniform(0, 1, [2, 2]))
fs.release()
fs2 = cv2.FileStorage('abc.xml', cv2.FileStorage_READ)
mat1 = fs2.getNode('mat1').mat()
print(mat1)
