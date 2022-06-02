from tkinter import *
root = Tk()

root.title('Prism')
root.iconbitmap('Assets\logo.ico')
root.geometry('310x580')

# test = Label(root, text='helloooo :3').pack()
test = Label(root, text='helloooo :3').grid(row=0, column=0)
test2 = Label(root, text='hehehehe :3').grid(row=0, column=1)


root.mainloop()
