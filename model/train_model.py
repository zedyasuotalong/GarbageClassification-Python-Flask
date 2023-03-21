import copy
import torch.optim as optim
from torchvision import models
import torch.nn as nn
import torch
from torchvision.models import ResNet50_Weights, ResNet101_Weights
from torch.utils.tensorboard import SummaryWriter
import time
import datetime
from configuration import *

# EPOCHS = 10
# LEARNING_RATE = 0.001
# DEVICE = 'mps'
MODEL_PATH = 'Garbage_Classification214_ResNet50_new.pt'


def validate(model_device, val_loader, device):
    total = 0
    correct = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            labels = labels.to(device)
            result = model_device(images)
            _, pred = torch.max(result, dim=1)
            total += result.size(0)
            correct += torch.sum(pred == labels)

    return correct * 100 / total


def train(model, train_loader, val_loader, num_epoch, lr, device, train_writer):
    accuracies = []
    running_loss = 0.0
    model_device = model.to(device)  # 将模型对象以及参数copy到mps(Mac)
    loss_fn = nn.CrossEntropyLoss().to(device)
    optimizer = optim.Adam(model_device.parameters(), lr=lr)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)
    best_model = model_device
    max_accuracy = 0.0

    for epoch in range(num_epoch):
        start = time.time()
        model_device.train()
        for i, data in enumerate(train_loader):
            images, labels = data
            images = images.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            pred_value = model_device(images)
            loss = loss_fn(pred_value, labels)
            running_loss += loss.item()
            loss.backward()
            optimizer.step()
            print(f'Epoch:{epoch + 1:2d}/{num_epoch}', "batch:{} loss:{}".format(i + 1, loss))

            if i % 100 == 99:
                running_loss /= 100
                tb_x = epoch * len(train_loader) + i + 1  # the x-axis of tensorboard
                train_writer.add_scalar('Loss/train', running_loss, tb_x)
                running_loss = 0.0
        end = time.time()
        print("training time:", format_time(end - start))

        # 计算在验证数据集上的识别准确率
        print("Validating......")
        model_device.eval()
        accuracy = float(validate(model_device, val_loader, device))
        train_writer.add_scalar('Accuracy/EPOCH', accuracy, epoch + 1)
        accuracies.append(accuracy)
        if accuracy > max_accuracy:
            best_model = copy.deepcopy(model)
            max_accuracy = accuracy
            print('Saving best model with accuracy on validation dataset {}%'.format(accuracy))

        print('Epoch --> {} Accuracy --> {:.2f}%'.format(epoch + 1, accuracy))

        scheduler.step()

    return best_model, accuracies


def format_time(time):
    elapsed_rounded = int(round((time)))
    # Normalize to standard time format -----> hh:mm:ss
    return str(datetime.timedelta(seconds=elapsed_rounded))


if __name__ == '__main__':
    from dataset import load_dataset

    train_loader, val_loader, num_classes = load_dataset('./垃圾图片库')
    # train_loader, val_loader, num_classes = load_dataset('/Users/eugenewong/Downloads/datasets/imagenet')

    model = models.resnet50(weights=ResNet50_Weights.DEFAULT)
    fc_inputs = model.fc.in_features
    model.fc = nn.Linear(fc_inputs, num_classes)

    timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
    writer = SummaryWriter('Writers/Garbage_Trainer_{}'.format(timestamp))
    # tensorboard --logdir=logs
    # replace the logs with your writers' path

    best_model, accuracies = train(model, train_loader, val_loader, EPOCH, LEARNING_RATE, DEVICE, writer)
    torch.save(best_model.state_dict(), MODEL_PATH)
    print(accuracies)
    writer.close()
