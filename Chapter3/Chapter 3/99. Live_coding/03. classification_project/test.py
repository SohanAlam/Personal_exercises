import os

img_folder = 'img'

classes = os.listdir(img_folder)

paths = ['train', 'test', 'val']

# folder structure like this:   datasets/train/0
#                               datasets/train/1
#                               datasets/test/0
#                               datasets/test/1


for item in paths:
    for cl in classes:
        print(f'mkdir ./datasets/{item}/{cl}')


