from tkinter import * 
from PIL import Image, ImageTk
import cv2
import pyttsx3
import googletrans

root = Tk()
root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('1180x320')
# root.maxsize(1520, 450)
root.config(bg="skyblue")

# Create frames ------------------------------------------------------------------------------------------------------------
left_frame = Frame(root, width=410, height=450, bg='white')
left_frame.grid(row=0, column=0, padx=5, pady=5)
middle_frame = Frame(root, width=410, height=450, bg='white')
middle_frame.grid(row=0, column=1, padx=5, pady=5)
right_frame = Frame(root, width=410, height=450, bg='white')
right_frame.grid(row=0, column=2, padx=5, pady=5)

# customize frame
Label(left_frame, text="TAKE A PHOTO OF DIGITAL TEXT", bg='white', fg='black').grid(row=0, column=0, padx=5, pady=5)
Label(middle_frame, text="PHOTO RESULT", bg='white', fg='black').grid(row=0, column=0, padx=5, pady=5)
Label(right_frame, text="IMAGE TO TEXT", bg='white', fg='black').grid(row=0, column=0, padx=5, pady=5)
# Create frames ------------------------------------------------------------------------------------------------------------

# webcams ------------------------------------------------------------------------------------------------------------------
# Create a Label to capture the Video frames
label =Label(left_frame, width=370, height=210)
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
# webcams ------------------------------------------------------------------------------------------------------------------

# show the Image result ----------------------------------------------------------------------------------------------------
image2 = Image.open('temp.png')
resize_image = image2.resize((350, 210))
img2 = ImageTk.PhotoImage(resize_image)
Label(middle_frame, image=img2).grid(row=1, column=0, padx=5, pady=5)
# show the Image result ----------------------------------------------------------------------------------------------------

# button functions ---------------------------------------------------------------------------------------------------------
def Camera():
        bryan = 'tolong~ T^T'
def Scan():
        bryan = 'tolong~ T^T'
def Audio():
        bryan = 'tolong~ T^T'
    
# button functions ---------------------------------------------------------------------------------------------------------

# buttons ------------------------------------------------------------------------------------------------------------------
# # Read the button Image
# image = Image.open('Assets\camera.png')

# # Resize the button image
# resize_image = image.resize((50, 50))
# img = ImageTk.PhotoImage(resize_image)

photo = Button(left_frame, text='Take a Photo', padx=10, pady=10, borderwidth=0, command=Camera).grid(row=2, column=0, padx=5, pady=5)
# takePhoto = Button(left_frame, image=img, borderwidth=0, command= Camera)
# takePhoto.image = img
# takePhoto.grid(row=2, column=0)
scan = Button(middle_frame, text='Scan Image', padx=10, pady=10, borderwidth=0, command=Scan).grid(row=2, column=0, padx=5, pady=5)
read = Button(right_frame, text='Read Text', padx=10, pady=10, borderwidth=0, command=Audio).grid(row=2, column=0, padx=5, pady=5)
# buttons -------------------------------------------------------------------------------------------------------------------

# show file recognize.txt ---------------------------------------------------------------------------------------------------
showText = Text(right_frame, width=50, height=14)
showText.grid(row=1, column=0)
file = 'recognized.txt'
openText = open(file, 'r').read()
showText.insert(END, openText)
# show file recognize.txt ---------------------------------------------------------------------------------------------------

root.mainloop()