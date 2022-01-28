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

Simulation Pacing is active and fixed step sizes are used, which result in more deterministic behaviour due to the asynchronous polling of the joystick. Pacing may be turned off, but the behaviour is untested.

The buttons can be used to control the left and right vibration. The input values can also be modulated but the effect is not extremely percievable.

Additional buttons and functions can be easily mapped by inspecting the XInput-Python code, as well as the Matlab Function in the Simulink Block.