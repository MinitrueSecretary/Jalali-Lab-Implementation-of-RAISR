from skimage.metrics import peak_signal_noise_ratio as psnr

import cv2
import numpy as np

l = []
for i in range(1,107):
    data_path = f'evalData/Non-Covid ({i}).png'
    result_path = f'evalResult/Non-Covid ({i})_result.png'
    data = cv2.imread(data_path)
    result = cv2.imread(result_path)
    # print(data.shape)
    result = cv2.resize(result, (data.shape[1], data.shape[0]))
    print(psnr(data, result))
    l.append(psnr(data, result))
print(f'Mean PSNR : {np.mean(l)}')