# -*- coding: utf-8 -*-
from Calibration import StereoCalibration
from Rectification import StereoRectification
import cv2 as cv
import numpy as np


# Calibration
C = StereoCalibration(patternType="chessboard",patternSize_m=0.108,cols=7,rows=6)
rms,MatrixLeft,distLeft,MatrixRight,distRight,size,R,T = C.calibrate()
# print(size)
#
# MatrixLeft = np.array([[1.05619032*1000,0.00000000,9.60179237*100],
#  [0.00000000,1.05673075*1000,6.06494462*100],
#  [0.00000000,0.00000000,1.0000000]])
# distLeft = np.array([-0.24927058,0.09027171,0.00039197,0.00039759,0.])
# MatrixRight = np.array([[1.05831037*1000,0.00000000,9.68635788*100],
#  [0.00000000,1.05914080*1000,6.10961545*100],
#  [0.00000000,0.00000000,1.000000000]])
# distRight = np.array([-2.44831330*0.1,8.16109844*0.01,3.27448320*0.0001,2.01069462*0.0001,0.000000000])
# #
# R = np.array([[ 9.99929911*0.1,-1.17966676*0.01,1.00584533*0.001],
#  [ 1.18156269*0.01,9.99697423*0.1,-2.15743721*0.01],
#  [-7.51035285*0.0001,2.15847447*0.01,9.99766740*0.1]])
#
# T = np.array([2.70617598*0.1,5.80783770*0.0001,3.57325760*0.00001])
# size = (1920, 1200)
# Visualization
# C.plotRMS()
# Rectification
R = StereoRectification(MatrixLeft,distLeft,MatrixRight,distRight,size,R,T)
# R.rectify(left,right)
left = cv.imread('data/stereo/MinnieRawLeft.png', cv.IMREAD_GRAYSCALE)
right = cv.imread('data/stereo/MinnieRawRight.png', cv.IMREAD_GRAYSCALE)

# R.display(left,right)

# 3D reconstruction
# left = cv.imread('data/stereo/MinnieRawLeft.png', cv.IMREAD_GRAYSCALE)
# right = cv.imread('data/stereo/MinnieRawRight.png', cv.IMREAD_GRAYSCALE)
            
R.displayDisparity(left,right)