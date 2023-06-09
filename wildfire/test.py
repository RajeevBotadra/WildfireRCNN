import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import cv2
import time

# Root directory of the project
ROOT_DIR = os.path.abspath("../")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "wildfire/"))  # To find local version
import wildfire

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join("guitar", "mask_rcnn_guitar.h5")


# Directory of images to run detection on
IMAGE_DIR = os.path.join(".", "dataset/val")

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True, exclude=[ "mrcnn_class_logits", "mrcnn_bbox_fc", "mrcnn_bbox", "mrcnn_mask"])

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'guitar']

# Load a random image from the images folder

from datetime import datetime

frame = skimage.io.imread("./guitar/my_strat.jpeg")

start = datetime.now()
results = model.detect([frame], verbose=1)
end = datetime.now()

print("Detection took")
print(end - start)

# Visualize results
r = results[0]
#print(class_names[int(r['class_ids'][0])])
print(results)
visualize.display_instances(frame, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])