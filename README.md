Welcome to my watermarking program!
This python script requires python 3.0+ and the python imaging library (PIL). The basics of this program is that you input a watermark(png) file in the root folder, and all images(jpg) that you want to watermark in ./input/. Running the script will output the images in the /input/ folder as half the size, with your desired watermark.


#STEPS 


#STEP 1:
Open up your python command line, 'Anaconda Prompt' and ensure you have PIL installed. 
In the command line, type $ pip install Pillow 

**note the '$' represents the command line input

#STEP 2: 
Move this folder onto your desktop, and change the directory of the python command line to this folder by entering:
$ cd *[path to this folder]*

since you have moved this folder onto your desktop, the path to this folder should look something like this:

$ cd C:\Users\*[your username]*\Desktop\watermarker

please enter your User where it says "*[your username]*"

#STEP 3:
Move your watermark PNG image to the root folder, this means that your watermark file is in the same folder as this script, 'watermark.py'

*It is important that your watermark file is a .png*

#STEP 4:
Move all the JPEG images you want to resize and watermark into the /input/ folder or directory.

*It is important that all your images are .jpg*

#STEP 5:
Back to the python command line, you must run this script.
To run this script, you must type this into the command line

$ python watermark.py 

#STEP 6:
The python command line will prompt you with an input "Enter Your Watermark Filename"

and type the ENTIRE filename of your watermark, for example 'watermark-img.png'

This program currently does not have any error handling, so if you experience an error just run the code again and try typing your filename out again:

$ python watermark.py

#STEP 7:
If the code is run successfully, you should see all of your watermarked and resized images in /output/
