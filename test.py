from tkinter import * 
from PIL import Image, ImageTk
import cv2

root = Tk()
root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('1320x590')
# root.maxsize(1020, 650)
root.config(bg="skyblue")

# Create left and right frames
left_frame = Frame(root, width=410, height=590, bg='white')
left_frame.grid(row=0, column=0, padx=5, pady=5)
right_frame = Frame(root, width=310, height=590, bg='grey')
right_frame.grid(row=0, column=1, padx=5, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="TAKE A PHOTO OF DIGITAL TEXT", bg='white', fg='black').grid(row=0, column=0, padx=5, pady=5)

# Create a Label to capture the Video frames
label =Label(left_frame)
label.grid(row=1, column=0, padx=5, pady=5)
cap = cv2.VideoCapture(0)

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
image = Image.open('Assets\camera.png')

# Resize the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)

# Camera function
def Camera():
    read = Button(root, text='Read', padx=10, pady=10, borderwidth=0).grid(row=0, column=0)

# create label and add resize image
takePhoto = Button(left_frame, image=img, borderwidth=0, command= Camera)
takePhoto.image = img
takePhoto.grid(row=2, column=0)

# Read the Image
image2 = Image.open('temp.png')
# image2 = ImageTk.PhotoImage(Image.open('temp.png'))
# mylabel = Label(right_frame, image=image2).grid(row=0, column=0)

resize_image = image2.resize((410, 175))
img2 = ImageTk.PhotoImage(resize_image)
Label(right_frame, image=img2).grid(row=0, column=0, padx=5, pady=5)

# # Resize the image using resize() method
# resize_image2 = image2.resize((410, 150))
# img = ImageTk.PhotoImage(resize_image2)

# # create label and add resize image
# takePhoto = Button(image=img, borderwidth=0, command= Camera)
# takePhoto.image = img
# takePhoto.place(x=295, y=485)


showText = Text(right_frame)
showText.grid(row=1, column=0)
file = 'recognized.txt'
# openText = open(file, 'r').read()
openText = 'cannot open recognized.txt hueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee T^T'
showText.insert(END, openText)
# openText.close()


root.mainloop()