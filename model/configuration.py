import torch.cuda

IMAGE_RESIZE = 224
EPOCH = 20
BATCH_SIZE = 64
LEARNING_RATE = 0.001

IMAGE_PATH = './垃圾图片库'
DEVICE = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
print(DEVICE)

import os
import codecs  # 读取文件夹中的文件名


def write_dir():
    folder = './垃圾图片库'
    filenames = os.listdir(folder)
    # 将文件名写入 txt 文件
    txt_file = './垃圾类别.txt'
    with codecs.open(txt_file, 'w', 'utf-8') as f:
        for filename in sorted(filenames):
            f.write(filename + '\n')
