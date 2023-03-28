import torch
from sklearn.model_selection import train_test_split
from torchvision.datasets import ImageFolder
from torchvision.transforms import Compose
import torchvision.transforms as transforms
import torch.nn as nn
from PIL import Image
from torchvision import models
from model.configuration import *
from utils.debug import DEBUG


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
    DEBUG(img_path=img_path)
    img = Image.open(img_path)
    DEBUG(img=img)
    img = transform(img)
    img = torch.reshape(img, (1, 3, 224, 224))

    # load model
    new_model = models.resnet50(weights=None)
    fc_inputs = new_model.fc.in_features
    new_model.fc = nn.Linear(fc_inputs, 214)
    new_model.load_state_dict(torch.load("model/Garbage_Classification_Mode_ResNet50.pt", map_location='cpu'))
    new_model.eval()
    with torch.no_grad():
        output = new_model(img)
    _, pred = torch.max(output, dim=1)

    DEBUG(type_of_pred_1=type(pred))
    pred = int(pred)
    DEBUG(pred=pred)
    DEBUG(type_of_pred_1=type(pred))

    return pred


if __name__ == '__main__':

    """
    new_model = models.resnet50(weights=None)
    fc_inputs = new_model.fc.in_features
    new_model.fc = nn.Linear(fc_inputs, 214)
    new_model.load_state_dict(torch.load("D:/企业实训/本地项目/GarbageClassification-Flask/model/Garbage_Classification_Mode_ResNet50.pt",
                                         map_location='cpu'))
    new_model.eval()
    """
    print(predict_category("static/20230220-141754.jpg"))
