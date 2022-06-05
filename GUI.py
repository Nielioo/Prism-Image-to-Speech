from tkinter import *
from PIL import Image, ImageTk
import cv2

def takePhoto():
    # Create Frame widget
    leftFrame = Frame(root, width=200, height=400)
    leftFrame.grid(row=0, column=0, padx=10, pady=5)
    
    # Create a Label to capture the Video frames
    label =Label(root)
    label.grid(row=0, column=0)
    # width, height = 410, 350
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

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

    # Camera function
    def Camera():
        read = Button(root2, text='Read', padx=10, pady=10, borderwidth=0).grid(row=0, column=3)
        showText = Text(root2, width=50, height=17)
        showText.grid(row=1, column=1)
        file = 'recognized.txt'
        # openText = open(file, 'r').read()
        openText = 'hueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee T^T'
        showText.insert(END, openText)
        # openText.close()

    # Read the Image
    image = Image.open('Assets\camera.png')
    
    # Resize the image using resize() method
    resize_image = image.resize((50, 50))
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    takePhoto = Button(image=img, borderwidth=0, command= Camera)
    takePhoto.image = img
    takePhoto.place(x=295, y=485)
    text = Text(root, text='sjcnsncpnscpna').grid(row=0, column=1)
    

def showImage():
     imageFrame = LabelFrame(root, padx=20, pady=20, bg='black').grid(row=0, column=1)

# def imageToText():
#     ni

# def textToSpeech():
#     sz


root = Tk()
root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('1020x540')
root.geometry('+300+110')
takePhoto()

root.mainloop()
