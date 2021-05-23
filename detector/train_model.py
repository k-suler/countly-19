import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from engine import train_one_epoch, evaluate
import utils
import transforms as T
from PennFundanDataset import PennFudanDataset


def get_model_instance(num_classes):
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model


def get_transform(train):
    transforms = []
    # converts the image, a PIL image, into a PyTorch Tensor
    transforms.append(T.ToTensor())
    if train:
        # during training, randomly flip the training images and ground-truth for data augmentation
        transforms.append(T.RandomHorizontalFlip(0.5))
    return T.Compose(transforms)


def main():
    # train on the GPU or on the CPU, if a GPU is not available

    device = torch.device('cpu')

    # load pretraied model resnet50
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)

    num_classes = 2

    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    dataset = PennFudanDataset("PennFudanPed", get_transform(train=True))
    dataset_test = PennFudanDataset("PennFudanPed", get_transform(train=False))

    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=8, shuffle=True, num_workers=1,
        collate_fn=utils.collate_fn
    )

    data_loader_test = torch.utils.data.DataLoader(
        dataset_test, batch_size=2, shuffle=False, num_workers=1,
        collate_fn=utils.collate_fn
    )

    model = get_model_instance(num_classes)
    model.to(device)

    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, lr=0.1, momentum=0.5, weight_decay=0)

    lr_sceduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

    num_epochs = 3

    train_one_epoch(model, optimizer, data_loader, device, num_epochs, print_freq=10)
    lr_sceduler.step()
    evaluate(model, data_loader_test, device=device)

    # save trained model for inference
    torch.save(model, 'faster-rcnn-person.pt')


if __name__ == "__main__":
    main()