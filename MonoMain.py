# -*- coding: utf-8 -*-
from Calibration import MonoCalibration
from Rectification import MonoRectification


# Acquisition
C = MonoCalibration()
C.acquire()
# Calibration
rms,Matrix,distCoef,size = C.calibrate()

# Visualization
C.visualizeBoards()
C.plotRMS()
# Rectification
R = MonoRectification(Matrix,distCoef,size)
R.display()
