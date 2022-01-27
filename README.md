# Simulink_Xbox_Joystick

Public code for XBox Controller Simulink Model, allowing use according to the MIT Open License.

These instructions assume Python 2.7 due to compatibility constraints with ROS Melodic

Installation
====

1. Create a Python 2.7 virtual environment (if desired)
2. Install XInput-Python: py -2.7 -m pip install XInput-Python 
3. Because the Xinput Library was written for Python 3+, the modified version of the library (XInput_edit.py) was composed and must be copied from this directory into:C:\Python27\Lib\site-packages, and renamed to XInput.py, replacing the file already present.


Use
====

The buttons can be used to control the left and right vibration. The input values can also be modulated.

Additional buttons and functions can be mapped 