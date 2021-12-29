# Flir_AX8

## yCreated for educational purposes.
You can find my Bachelor's thesis here: [LINK](https://digikogu.taltech.ee/et/Item/c58c0dcf-f5a6-4210-9108-4a259b3dee0e)

Flir image extractor was used from https://github.com/Nervengift/read_thermal.py, no changes were used in file.


extract_images.sh is used for applying flir_image_extractor.py for every picture from specified folder.


To run on Ubuntu: ./extract_images.sh

Then move all thermal images from that folder to Thermal folder> mv?*thermal* /home/renvt/thermal_images/


Then run resize.py, that resize all pictures in Thermal folder to 640x480.
