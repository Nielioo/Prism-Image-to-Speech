import cv2
import pytesseract

from googletrans import Translator
from gtts import gTTS

import numpy as np

from tkinter import *
from PIL import Image, ImageTk

import os
import threading
from playsound import playsound

from memory_profiler import profile

# Locate tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

def image_to_text(image) -> str:
	image_data = np.asarray(image)

	# Resize image
	resize_image = cv2.resize(image_data, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

	# Grayscaling
	grayscale_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

	# Thresholding
	threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

	# Dilate
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
	dilate_image = cv2.dilate(threshold_image, rect_kernel, iterations=1)

	# Inverse
	inverse_image = 255 - dilate_image

	text = pytesseract.image_to_string(inverse_image)

	# cv2.imwrite('Storage/image.png', image)
	# cv2.imwrite('Storage/resize.png', resize_image)
	# cv2.imwrite('Storage/grayscale.png', grayscale_image)
	# cv2.imwrite('Storage/threshold.png', threshold_image)
	# cv2.imshow('image', inverse_image)
	return text

def text_to_speech(text):
	# Detect language
	translator = Translator()
	lang = translator.detect(text).lang

	# Get audio from gTTS
	audio = gTTS(text=text, lang=lang, slow=False, tld="com")
	return audio

# Const
audio_filename = 'Storage/speech.mp3'

# Image placeholder
image_placeholder = Image.open('Assets/image_placeholder.png')

# Initialize the camera ----------------------------------------------------------------------------------------------------
cam_port = 0
cap = cv2.VideoCapture(cam_port)

# Get image from camera
def get_cam_image():
    # Get the latest frame and convert into Image
	result, capImage = cap.read()
	
	if not result:
		print("An error occured while capturing video from the camera")
		return result, image_placeholder

	cv2image = cv2.cvtColor(capImage, cv2.COLOR_BGR2RGB)

	return result, cv2image

# Convert cvImage as ImageTk
def image_to_imagetk(image):
	img = Image.fromarray(image)
	# Convert image to PhotoImage
	imgtk = ImageTk.PhotoImage(image=img)
	return imgtk
# Initialize the camera ----------------------------------------------------------------------------------------------------


# Initialize window --------------------------------------------------------------------------------------------------------
root = Tk()
root.title('Prism')
root.iconbitmap('Assets/logo.ico')
root.geometry('1180x300')
root.maxsize(1180, 300)
root.config(bg="skyblue")
# Initialize window --------------------------------------------------------------------------------------------------------


# Create frames ------------------------------------------------------------------------------------------------------------
left_frame = Frame(root, width=410, height=450, bg='white')
left_frame.grid(row=0, column=0, padx=5, pady=5)
middle_frame = Frame(root, width=410, height=450, bg='white')
middle_frame.grid(row=0, column=1, padx=5, pady=5)
right_frame = Frame(root, width=410, height=450, bg='white')
right_frame.grid(row=0, column=2, padx=5, pady=5)

# customize frame
# Label(left_frame, text="TAKE A PHOTO OF DIGITAL TEXT", bg='white',
#       fg='black').grid(row=0, column=0, padx=5, pady=5)
# Label(middle_frame, text="PHOTO RESULT", bg='white',
#       fg='black').grid(row=0, column=0, padx=5, pady=5)
# Label(right_frame, text="IMAGE TO TEXT", bg='white',
#       fg='black').grid(row=0, column=0, padx=5, pady=5)
# Create frames ------------------------------------------------------------------------------------------------------------


# Webcams ------------------------------------------------------------------------------------------------------------------
# Create a Label to capture the Video frames
label = Label(left_frame, width=370, height=210)
label.grid(row=1, column=0, padx=5, pady=5)

# Define function to show frame
def show_frames():
	# Get image from camera
	result, image = get_cam_image()

	if result:
		imagetk = image_to_imagetk(image=image)
		label.configure(image=imagetk)
		label.image = imagetk

    # Repeat after an interval to capture continiously
	label.after(20, show_frames)


# Run the function once
show_frames()
# Webcams ------------------------------------------------------------------------------------------------------------------


# Show the Image result ----------------------------------------------------------------------------------------------------
# Create a Label for image result
imagetk_placeholder = ImageTk.PhotoImage(image_placeholder)
image_frame = Label(middle_frame, image=imagetk_placeholder, width=350, height=210)
image_frame.grid(row=1, column=0, padx=5, pady=5)

@profile(precision=4)
def capture_image():
	# Get image from camera
	result, image = get_cam_image()

	if result:
		imagetk = image_to_imagetk(image=image)
		image_frame.configure(image=imagetk)
		image_frame.image = imagetk
# show the Image result ----------------------------------------------------------------------------------------------------


# show text result  --------------------------------------------------------------------------------------------------------
# Create a Label for text result
text_frame = Text(right_frame, width=50, height=14)
text_frame.grid(row=1, column=0)

@profile(precision=4)
def scan_image():
    # Get image from captured image
	imagetk = image_frame.image
	imagepil = ImageTk.getimage(imagetk)
	image_array = np.array(imagepil)
	image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

    # Get text from image
	text = image_to_text(image)
	text = text.strip()

	# Insert text to frame
	text_frame.delete('1.0', END)
	text_frame.insert(END, text)

@profile(precision=4)
def read_text():
	# Get text from recognized text
	text = text_frame.get('1.0', END)
	text = text.strip()

	if not text:
		text = 'No text input'
		text_frame.delete('1.0', END)
		text_frame.insert(END, text)
	
	# Play audio
	audio = text_to_speech(text=text)

	# Remove old file if exist
	file_exists = os.path.exists(audio_filename)
	if file_exists:
		os.remove(audio_filename)

	audio.save(audio_filename)
	play = threading.Thread(target=playsound, args=(audio_filename,))
	play.start()
# show text result  --------------------------------------------------------------------------------------------------------


# buttons ------------------------------------------------------------------------------------------------------------------
# capture = Button(left_frame, text='Take a Photo', padx=10, pady=10,
#                borderwidth=0, command=capture_image).grid(row=2, column=0, padx=5, pady=5)
# scan = Button(middle_frame, text='Scan Image', padx=10, pady=10,
#               borderwidth=0, command=scan_image).grid(row=2, column=0, padx=5, pady=5)
# read = Button(right_frame, text='Read Text', padx=10, pady=10, borderwidth=0, command=read_text).grid(row=2, column=0, padx=5, pady=5)

camera = Image.open('Assets/camera.png')
scan = Image.open('Assets/scan.png')
play = Image.open('Assets/play.png')

# Resize the button image
resize_camera = camera.resize((50, 50))
resize_scan = scan.resize((50, 50))
resize_play = play.resize((50, 50))

cmra = ImageTk.PhotoImage(resize_camera)
scn = ImageTk.PhotoImage(resize_scan)
ply = ImageTk.PhotoImage(resize_play)

# photo = Button(left_frame, text='Take a Photo', padx=10, pady=10, borderwidth=0, command=Camera).grid(row=2, column=0, padx=5, pady=5)
takePhoto = Button(left_frame, image=cmra, bg = '#ffffff', borderwidth=0, command= capture_image)
takePhoto.image = cmra
takePhoto.grid(row=2, column=0, padx=5, pady=5)

scanPhoto = Button(middle_frame, image=scn, bg = '#ffffff', borderwidth=0, command= scan_image)
scanPhoto.image = scn
scanPhoto.grid(row=2, column=0, padx=5, pady=5)

playAudio = Button(right_frame, image=ply, bg = '#ffffff', borderwidth=0, command= read_text)
playAudio.image = ply
playAudio.grid(row=2, column=0, padx=5, pady=5)
# buttons -------------------------------------------------------------------------------------------------------------------


# Custom window exit -------------------------------------------------------------------------------------------------------
def on_closing():
    # Turning camera off
    cap.release()
    # Destory window
    root.destroy()

# Set the custome window exit
root.protocol("WM_DELETE_WINDOW", on_closing)
# Custom window exit -------------------------------------------------------------------------------------------------------

n_rows = 3
n_columns = 3
for i in range(n_rows):
    root.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    root.grid_columnconfigure(i,  weight =1)

# Run application
root.mainloop()