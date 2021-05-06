#!/bin/bash

for image_set in $(find /home/renvt/flir_images/ -name '*.jpg')
do
  python /home/renvt/flir_image_extractor.py -i "$image_set"
done
