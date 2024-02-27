# PioneerQRNav
![image](https://github.com/syauqibilfaqih/PioneerQRNav/assets/70939903/e1bed9ed-37e4-4d7f-9a90-f00cc6783d9a)

A repository to run Pioneer p3dx simulation and navigate it using QR Codes for educational purpose in Madrasah Technonatura Jogja. This was tested on Windows 10 with Python 3.7 and CoppeliaSim 4.1.0

## Installation
1.  Clone this project using this command:
```
git clone https://github.com/syauqibilfaqih/PioneerQRNav.git
```
2. Install required libraries
```
pip install -r requirements.txt
```
or you can just install them manually:
```
pip install numpy
```
```
pip install opencv-python
```

## Usage
1. Open the CoppeliaSim simulation file in folder coppeliaSimFiles
2. run `main.py` code

## Documentation
Here are some function to use in this repository
### Pioneer
- `move_pioneer(left_speed,right_speed)` : to move the robot and adjust the speed
### qrscanner
#### Properties
- `camera_id` : specify camera to be used
- `delay` : delay value for waitKey() function
- `window_name` : the name of window that will be appeared
#### Functions
- `qr_detect()` : to return the data of qr detected
- `open_window()` : to show real time camera capture
- `destroy_windows()` : to destroy all window camera capture display

## Contact us
Should you have any question, don't hesitate to contact me at alisyauqibilfaqih@gmail.com
