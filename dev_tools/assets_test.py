import cv2
import numpy as np

from numpy import float32, int32, uint8, fromfile
from pathlib import Path

from module.logger import logger
from module.atom.image import RuleImage
from module.atom.ocr import RuleOcr


def load_image(file: str):
    file = Path(file)
    img = cv2.imdecode(fromfile(file, dtype=uint8), -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height, width, channels = img.shape
    if height != 720 or width != 1280:
        logger.error(f'Image size is {height}x{width}, not 720x1280')
        return None
    return img


def detect_image(file: str, targe: RuleImage) -> bool:
    img = load_image(file)
    result = targe.test_match(img)
    logger.info(f'[{targe.name}]: {result}')
    return result


def detect_ocr(file: str, target: RuleOcr):
    img = load_image(file)
    return target.ocr(img)


# 图片文件路径 可以是相对路径
IMAGE_FILE = r"D:\workspaces\py\OnmyojiAutoScript\log\error\17200757427562024-07-04_14-49-02-558641.png"
if __name__ == '__main__':
    from tasks.SixRealms.assets import SixRealmsAssets
    from tasks.GameUi.assets import GameUiAssets
    targe = SixRealmsAssets.I_BACK_EXIT
    print(detect_image(IMAGE_FILE, targe))

    # ocr demo
    # from tasks.KekkaiActivation.assets import KekkaiActivationAssets
    # target = KekkaiActivationAssets.O_CARD_ALL_TIME
    # print(detect_ocr(IMAGE_FILE, target))
