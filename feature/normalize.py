from torchvision import transforms


def normalize(seed, img_dim):
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    '''
    train_transforms = transforms.Compose([transforms.Resize(256),
                                           transforms.CenterCrop(img_dim),
                                           transforms.RandomHorizontalFlip(),  # 隨機要不要左右顛倒
                                           transforms.ToTensor(),
                                           normalize,
                                           ])
    '''
    if seed % 2 == 0:
        train_transforms = transforms.Compose([transforms.Resize(256),
                                               transforms.CenterCrop(img_dim),
                                               transforms.RandomHorizontalFlip(p=1),  # 隨機要不要左右顛倒
                                               transforms.ToTensor(),
                                               normalize,
                                               ])
    else:
        train_transforms = transforms.Compose([transforms.Resize(256),
                                               transforms.CenterCrop(img_dim),
                                               transforms.RandomHorizontalFlip(p=0),  # 隨機要不要左右顛倒
                                               transforms.ToTensor(),
                                               normalize,
                                               ])

    return train_transforms
