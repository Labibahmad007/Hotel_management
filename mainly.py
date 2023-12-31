from subprocess import call

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


# Check in GUI
def click_checking():
    print('call checking_gui_and_program')
    call(["python", "checkin_gui_and_program.py"])


# List GUI
def click_list():
    print('call click list')
    call(["python", "listgui.py"])


# Check Out GUI
def click_checkout():
    print('call click_checkout')
    call(["python", "checkoutgui.py"])


# GET Info GUI
def click_getinfo():
    print('call click_getinfo')
    call(["python", "getinfoui.py"])


# Restaurant Service GUI
def click_restaurant_service():
    print('call click restaurant')
    call(["python", "restrudant.py"])


# Pharmacy Service GUI
def click_pharmacy_service():
    call(["python", "pharmacy.py"])


# Room service GUI
def click_room_service():
    call(["python", "contact.py"])


class HotelManagement:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff'  # X11 color: 'white'
        _ana1color = '#ffffff'  # X11 color: 'white'
        _ana2color = '#ffffff'  # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("HOTEL MANAGEMENT")
        # root.configure(background="#d9d9d9")
        root.configure(background="blue")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.menubar = Menu(root, font=font9, bg=_bgcolor, fg=_fgcolor)
        root.configure(menu=self.menubar)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.10, relwidth=0.86)  # 0.86
        self.Message6.configure(background=_bgcolor)
        # self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME TO OUR HOTEL''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.12, height=60, width=566)  # 0.17/75
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="steel blue")
        # self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''1.CHECK INN''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checking)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.23, height=50, width=566)  # 93#65
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="steel blue")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''2.SHOW GUEST LIST''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.33, height=50, width=566)  # 93/47
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="steel blue")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''3.CHECK OUT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.43, height=50, width=566)  # 93/61
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="steel blue")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''4.GET INFO''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.18, rely=0.53, height=55, width=566)  # 103/75
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="steel blue")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''5.RESTAURANT SERVICE''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=click_restaurant_service)

        self.Button7 = Button(self.Frame1)
        self.Button7.place(relx=0.18, rely=0.64, height=55, width=566)  # 93/89
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="steel blue")
        self.Button7.configure(disabledforeground="#bfbfbf")
        self.Button7.configure(font=font14)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''6.EMERGENCY SERVICE''')
        self.Button7.configure(width=566)
        self.Button7.configure(command=click_pharmacy_service)

        self.Button8 = Button(self.Frame1)
        self.Button8.place(relx=0.18, rely=0.76, height=55, width=566)  # 93/89
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="steel blue")
        self.Button8.configure(disabledforeground="#bfbfbf")
        self.Button8.configure(font=font14)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''7.ROOM SERVICE''')
        self.Button8.configure(width=566)
        self.Button8.configure(command=click_room_service)

        self.Button9 = Button(self.Frame1)
        self.Button9.place(relx=0.18, rely=0.88, height=65, width=566)  # 103/1.05
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="steel blue")
        self.Button9.configure(disabledforeground="#bfbfbf")
        self.Button9.configure(font=font14)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''8.EXIT''')
        self.Button9.configure(width=566)
        self.Button9.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    Guest = HotelManagement()
