from tkinter import *
from PIL import Image, ImageTk
import cv2

root = Tk()
root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('510x350')
root.geometry('+800+110')

# # Create a Label to capture the Video frames
# label =Label(root)
# label.grid(row=0, column=0)
# width, height = 510, 350
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# # Define function to show frame
# def show_frames():
#    # Get the latest frame and convert into Image
#    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(20, show_frames)

# show_frames()

# Scan function
def Scan():
    root.disable()
    root2 = Tk()
    root2.title('Prism')
    root2.iconbitmap('Assets\logo.ico')
    root2.geometry('510x350')
    root2.geometry('+800+110')
    close = Button(root2, text='Close', command= root2.destroy, padx=10, pady=10, borderwidth=0).grid(row=0, column=0)
    read = Button(root2, text='Read', padx=10, pady=10, borderwidth=0).grid(row=0, column=3)
    showText = Text(root2, width=50, height=17)
    showText.grid(row=1, column=1)
    file = 'recognized.txt'
    openText = open(file, 'r').read()
    # openText = 'hueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee T^T'
    showText.insert(END, openText)
    # openText.close()

# Read the Image
image = Image.open('Assets\cameraIcon.png')
 
# Resize the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
scan = Button(image=img, borderwidth=0, command= Scan)
scan.image = img
scan.place(x=230, y=280)


root.mainloop()
