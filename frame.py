from tkinter import *
root=Tk()
root.geometry("500x400")
root.resizable(False,False)

frame=Frame(root,bg="pink",height="400",width="250")
frame.place(x=0,y=0)
frame1=Frame(root,bg="green",height="400",width="250")
frame1.place(x=250,y=0)

root.mainloop()
