# Lemniscate Curve
from Tkinter import *
root = Tk()
# create the root window
root.title('Lemniscate Curve')
canvas = Canvas(root, width =800, height=600)
def showAbout():
    t1 = Toplevel(root)
    t1.geometry("430x300")
   
    t1.title('About Lemniscate')
    Label(t1, text='Draw Lemniscate Curve', font=("Arial", 14)).pack(pady=30)  # Can you get ride of the 'pack'?
    Label(t1, text='Programer: Dan Webb', font=("Arial", 14)).pack()
    
# create a menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
#menu.add_cascade(label="About", menu=filemenu)
menu.add_command(label="About", command=showAbout)
#canvas.create_bitmap(355, 53, bitmap='questhead')
canvas.create_line(50, 280, 750, 280, width=2)  # fill='purple'
canvas.create_line(400, 50, 400, 510, width=2)
def CalulateY(x):
    a = 300.0
    yh = 120.0
    yl = 0.0
    y = 125.0
    for i in range(0,20):
        dhl = yh - yl
        if (dhl < 0.1):
            return y
        y = (yh + yl) / 2.0
        x2 = x*x
        y2 = y*y
        t = x2 + y2
        dif = t * t - a * a * (x2 - y2)
        if (dif > 0):
            yh = y;
        else:
            yl = y;
XplotS = 400
YplotS = 280
XplotS2 = 400
YplotS2 = 280
XplotS3 = 400
YplotS3 = 280
XplotS4 = 400
YplotS4 = 280
for x in range(1,301):
    y = CalulateY(x)
    XplotE = 400 + x
    YplotE = 280 + y
    canvas.create_line(XplotS, YplotS, XplotE, YplotE, width=2, fill='purple')
    XplotS = XplotE
    YplotS = YplotE
    XplotE2 = 400 + x
    YplotE2 = 280 - y
    canvas.create_line(XplotS2, YplotS2, XplotE2, YplotE2, width=2, fill='purple')
    XplotS2 = XplotE2
    YplotS2 = YplotE2
    XplotE3 = 400 - x
    YplotE3 = 280 + y
    canvas.create_line(XplotS3, YplotS3, XplotE3, YplotE3, width=2, fill='purple')
    XplotS3 = XplotE3
    YplotS3 = YplotE3
    XplotE4 = 400 - x
    YplotE4 = 280 - y
    canvas.create_line(XplotS4, YplotS4, XplotE4, YplotE4, width=2, fill='purple')
    XplotS4 = XplotE4
    YplotS4 = YplotE4    
     
canvas.pack()
root.mainloop()