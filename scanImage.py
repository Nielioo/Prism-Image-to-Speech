from tkinter import *
from PIL import Image, ImageTk
import cv2

def scan():
    import textToAudio
    textToAudio()
    root.destroy()


root = Tk()
root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('510x350')
root.geometry('+800+110')

# Create a Label to capture the Video frames
label =Label(root)
label.grid(row=0, column=0)
width, height = 510, 350
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()

# Read the Image
image = Image.open('Assets\cameraIcon.png')
 
# Resize the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
scan_btn = Button(root, image=img, borderwidth=0, command= scan)
scan_btn.image = img
scan_btn.place(x=230, y=280)

root.mainloop()