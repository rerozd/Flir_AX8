# Flir_AX8

Created for educational purposes.

Flir image extractor was used from https://github.com/Nervengift/read_thermal.py, no changes were used in file.


extract_images.sh is used for applying flir_image_extractor.py for every picture from specified folder.


To run on Ubuntu:

'''sh
./extract_images.sh
'''

Then move all thermal images from that folder to Thermal folder> '''mv?*thermal* /home/renvt/thermal_images/'''


Then run resize.py, that resize all pictures in Thermal folder to 640x480.
