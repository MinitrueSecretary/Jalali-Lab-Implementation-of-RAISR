from pydicom import dcmread, dcmwrite
import cv2
import numpy as np
import os

def readdcm(dcm_path):
    # Input: dcm_path: path to dcm file
    # Output: np.array of the dcm file
    dcm = dcmread(dcm_path)
    return dcm.pixel_array

# get list of all dcm files in the folder DicomFiles
#use os.walk to get all files in the subfolders
dcm_files = []
for root, dirs, files in os.walk('DicomFiles'):
    for f in files:
        if f.endswith('.dcm'):
            dcm_files.append(os.path.join(root, f))
print(len(dcm_files))
# read all dcm files and save as png in the folder testData
for dcm_file in dcm_files:
    dcm = readdcm(dcm_file)
    cv2.imwrite('testData/' + os.path.splitext(os.path.basename(dcm_file))[0] + '.png', dcm)