# UTF art
This program creates an ui that allows the user to transform images from their computer
into UTF-8 strings and add the string into their clipboard for easy pasting.

## Requirements
* easygui
* numpy
* OpenCV-python
* pillow
* pyperclip
* tkinter

## How to use
* Import and run the start_program function from main.py:
````
from utf_imaging.main import start_program

start_program()
````

This will make the application turn up on your screen (see Figure 1).
* Click the "Choose image" button and select which image you want to use
* Set the desired pixelation using the slider
* Hit the "Pixelate" buton to render a pixelated grayscale version of the image
* Click the "Add to clipboard" button and paste wherever you want!

![UI screenshot](/utf_imaging/images/UTFGeneratorScreenshot.png "Figure 1: UI screenshot")

Here are some images generated with the application:
![Generated text example 1](/utf_imaging/images/UTFGeneratorImage.png)
![Generated text example 2](/utf_imaging/images/UTFGeneratorImageLarge.png)


