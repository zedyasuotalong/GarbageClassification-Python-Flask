import torch
from sklearn.model_selection import train_test_split
from torchvision.datasets import ImageFolder
from torchvision.transforms import Compose
import torchvision.transforms as transforms
import torch.nn as nn
from PIL import Image
from torchvision import models
from configuration import *


def predict_category(img_path):
    """
    :param img_path: string like './垃圾图片库/可回收垃圾_灯罩/img_灯罩_232.jpeg'
    :return: category
    """

    transform = Compose([
        transforms.Resize(IMAGE_RESIZE),
        transforms.CenterCrop(IMAGE_RESIZE),
        transforms.ToTensor(),
        transforms.Normalize([0.4878, 0.4545, 0.4168],  # RGB mean, 所有训练数据中R通道平均值/255=0.4878....
                             [0.2623, 0.2555, 0.2577])  # RGB std
    ])

    # prepare data
    img = Image.open(img_path)
    img = transform(img)
    img = torch.reshape(img, (1, 3, 224, 224))

    # load model
    new_model = models.resnet50(weights=None)
    fc_inputs = new_model.fc.in_features
    new_model.fc = nn.Linear(fc_inputs, 214)
    new_model.load_state_dict(torch.load("Garbage_Classification_Mode_ResNet50.pt"))

    new_model.eval()
    with torch.no_grad():
        output = new_model(img)
    _, pred = torch.max(output, dim=1)

    return pred


if __name__ == '__main__':
    all_data = ImageFolder('/Users/eugenewong/Downloads/datasets/imagenet')
    train_data, val_data, train_label, val_label = train_test_split(all_data.imgs,
                                                                    all_data.targets,
                                                                    test_size=0.2,
                                                                    random_state=24)
    print(train_data[100][0])
    print(predict_category(train_data[1000][0]))