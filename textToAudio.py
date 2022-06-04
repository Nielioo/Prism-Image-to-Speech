from tkinter import *

root2 = Toplevel()
root2.title('Prism')
root2.iconbitmap('Assets\logo.ico')
root2.geometry('510x350')
root2.geometry('+800+110')

def back():
    import scanImage
    scanImage()
    root2.destroy

close = Button(root2, text='Close', command= back, padx=10, pady=10, borderwidth=0).grid(row=0, column=0)
read = Button(root2, text='Read', padx=10, pady=10, borderwidth=0).grid(row=0, column=3)
showText = Text(root2, width=50, height=17)
showText.grid(row=1, column=1)
file = 'recognized.txt'
# openText = open(file, 'r').read()
openText = 'cannot open recognized.txt hueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee T^T'
showText.insert(END, openText)
# openText.close()
    
root2.mainloop()