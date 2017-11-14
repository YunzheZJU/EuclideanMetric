# -*- coding: utf-8 -*-
import os
import config
import numpy as np

from logger import logger
from PIL import Image

samples = []


def generate_global(root_path):
    """
    根据传入的root_path建立一系列GLOBAL参数，绝对路径
    :param root_path: app.root_path
    :return: 成功则返回1，否则返回0
    """
    config.GLOBAL['ROOT_PATH'] = root_path
    config.GLOBAL['STATIC_PATH'] = os.path.join(root_path, 'static')
    config.GLOBAL['TEMP_PATH'] = os.path.join(root_path, 'temp')
    config.GLOBAL['IMAGE_PATH'] = os.path.join(root_path, 'static', 'images')
    return 1


def read_images(test=False):
    """
    读取预置图片的信息
    :return: 返回list，存储10张图片的数组
    """
    try:
        for i in range(1, 11):
            if test:
                samples.append(np.asarray(Image.open(os.path.join("static\\images", str(i) + ".jpg"))))
            else:
                samples.append(np.asarray(Image.open(os.path.join(config.GLOBAL['IMAGE_PATH'], str(i) + ".jpg"))))
        return True
    except StandardError as ex:
        logger.error(ex.message)


def calculate_distance(src):
    """
    计算输入图像与预置图片的欧式距离
    :param src:
    :return: 返回距离最短的图片编号
    """
    test = np.asarray(Image.open(src))
    result = []
    for sample in samples:
        result.append((test - sample) ** 2)
    result.sort()
    print result
    return result[0]


if __name__ == '__main__':
    read_images(test=True)
    print calculate_distance(os.path.join("temp", "test.jpg"))
