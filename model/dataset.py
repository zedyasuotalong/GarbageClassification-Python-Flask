import torch
from PIL import Image
import os
import glob
from torch.utils.data import Dataset
import random
import torchvision.transforms as transforms
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


class GarbageLoader(Dataset):
    def __init__(self, txt_path, train_flag=True):
        self.imgs_info = self.get_images(txt_path)
        self.train_flag = train_flag

        self.train_tf = transforms.Compose([
            transforms.Resize(224),
            transforms.RandomHorizontalFlip(),
            transforms.RandomVerticalFlip(),
            transforms.ToTensor(),

        ])
        self.val_tf = transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
        ])

    def get_images(self, txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            imgs_info = f.readlines()
            imgs_info = list(map(lambda x: x.strip().split(' ', 1), imgs_info))
            print(imgs_info)
        return imgs_info

    def padding_black(self, img):
        w, h = img.size
        scale = 224. / max(w, h)
        img_fg = img.resize([int(x) for x in [w * scale, h * scale]])
        size_fg = img_fg.size
        size_bg = 224
        img_bg = Image.new("RGB", (size_bg, size_bg))
        img_bg.paste(img_fg, ((size_bg - size_fg[0]) // 2, (size_bg - size_fg[1]) // 2))
        img = img_bg
        return img

    def __getitem__(self, index):
        img_path, label = self.imgs_info[index]
        print(img_path)
        img = Image.open(img_path)
        img = img.convert('RGB')
        img = self.padding_black(img)
        if self.train_flag:
            img = self.train_tf(img)
        else:
            img = self.val_tf(img)
        label = int(label)

        return img, label

    def __len__(self):
        return len(self.imgs_info)


# if __name__ == "__main__":
#     train_dataset = GarbageLoader("train.txt", True)
#     print("数据个数：", len(train_dataset))
#     train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=1, shuffle=True)
#     for image, label in train_loader:
#         print(image.shape)
#         print(label)


from torchvision.datasets import ImageFolder
from torchvision.transforms import Compose
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from sklearn.model_selection import train_test_split

BATCH_SIZE = 64
IMAGE_RESIZE = 224


class ImageLoader(Dataset):
    def __init__(self, datasets, transform=None):
        self.datasets = datasets
        self.transform = transform

    def __len__(self):
        return len(self.datasets)

    def padding_black(self, img):
        w, h = img.size
        scale = 224. / max(w, h)
        img_fg = img.resize([int(x) for x in [w * scale, h * scale]])
        size_fg = img_fg.size
        size_bg = 224
        img_bg = Image.new("RGB", (size_bg, size_bg))
        img_bg.paste(img_fg, ((size_bg - size_fg[0]) // 2, (size_bg - size_fg[1]) // 2))
        img = img_bg
        return img

    def __getitem__(self, item):  # 对象[index] -> (data, label)
        image = Image.open(self.datasets[item][0])
        class_category = self.datasets[item][1]
        image = image.convert('RGB')
        image = self.padding_black(image)
        if self.transform:
            image = self.transform(image)

        return image, class_category


def load_dataset(data_dir):
    """
    加载本地目录的所有数据, 并对数据进行划分(训练, 验证和测试)
    :param data_dir: str, 数据所在的根目录
    :return: train_loader, val_loader, test_loader
    """
    all_data = ImageFolder(data_dir)
    train_data, val_data, train_label, val_label = train_test_split(all_data.imgs, all_data.targets, test_size=0.2,
                                                                    random_state=24)

    train_transform = Compose([
        transforms.RandomRotation(10),
        transforms.RandomHorizontalFlip(),
        transforms.Resize(IMAGE_RESIZE),
        transforms.CenterCrop(IMAGE_RESIZE),
        # .........
        transforms.ToTensor(),  # Tensor, [0, 1]
        # image normalization: output[channel] = (input[channel] - mean[channel]) / std[channel]
        transforms.Normalize([0.4878, 0.4545, 0.4168],  # RGB mean, 所有训练数据中R通道平均值/255=0.4878....
                             [0.2623, 0.2555, 0.2577])  # RGB std
    ])
    # 训练数据ImageLoader
    train_dataset = ImageLoader(train_data, train_transform)

    # 验证; 4500
    val_transform = Compose([
        transforms.Resize(IMAGE_RESIZE),
        transforms.CenterCrop(IMAGE_RESIZE),
        transforms.ToTensor(),
        transforms.Normalize([0.4878, 0.4545, 0.4168],  # RGB mean, 所有训练数据中R通道平均值/255=0.4878....
                             [0.2623, 0.2555, 0.2577])  # RGB std
    ])
    # 验证数据ImageLoader
    val_dataset = ImageLoader(val_data, val_transform)

    # 创建DataLoader
    train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(dataset=val_dataset, batch_size=BATCH_SIZE, shuffle=True)

    return train_loader, val_loader, len(all_data.classes)


if __name__ == "__main__":
    train_loader, val_loader, num_classes = load_dataset('./垃圾图片库')
    img, label = next(iter(train_loader))
    print(img.size(), type(img))
    print(label, type(label))
    print(img)

    for image, label in val_loader:
        print(image)
        print('label ---->', label)
        break
