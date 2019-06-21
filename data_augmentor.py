import Augmentor
import sys
import os
dir = os.path.abspath(os.path.join(sys.path[0], "../..", "MaskRCNN", "dataset", "6060"))
# for parent, dirnames, filenames in os.walk(dir):
#     print(filenames)
#     print(dirnames)
#     print(parent)
#     for filename in filenames:
#         dir = os.path.join(parent, filename)
#         print(dir)

p = Augmentor.Pipeline(dir)
# p.rotate90(probability=0.5)
# p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)
p.sample(200)