import random
import time
from tkinter import *

# Initializing window
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))
# -----------------INFO TOP------------
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg="steel blue", bd=10,
                anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
lblinfo.grid(row=1, column=0)

# ---------------Calculator------------------
text_Input = StringVar()
operator = ""

text_display = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white",
                     justify='right')
text_display.grid(columnspan=4)


# Handles Calculator button clicks
def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


# Displays calculator data
def display():
    global operator
    operator = ""
    text_Input.set("")


# Handles arithmatic
def equals():
    global operator
    sum_val = str(eval(operator))

    text_Input.set(sum_val)
    operator = ""


# Handles total button click event
def ref():
    x = random.randint(12980, 50876)
    random_ref = str(x)
    rand.set(random_ref)

    # Collects number of items from input
    collect_fries = int(Fries.get())
    collect_fries_large = int(Large_fries.get())
    collect_burger = int(Burger.get())
    collect_filet = int(Filet.get())
    collect_cheese_burger = int(Cheese_burger.get())
    collect_drinks = int(Drinks.get())

    # Calculates price of items
    cost_of_fries = collect_fries * 25
    cost_of_large_fries = collect_fries_large * 40
    cost_of_burger = collect_burger * 35
    cost_of_filet = collect_filet * 50
    cost_of_cheese_burger = collect_cheese_burger * 50
    cost_of_drinks = collect_drinks * 35

    # Calculates total cost of meals
    const_of_meals = "TK." + str(
        '%.2f' % (
                cost_of_fries + cost_of_large_fries + cost_of_burger + cost_of_filet + cost_of_cheese_burger + cost_of_drinks))
    pay_tax = ((
                       cost_of_fries + cost_of_large_fries + cost_of_burger + cost_of_filet + cost_of_cheese_burger + cost_of_drinks) * 0.33)
    total_cost = (
            cost_of_fries + cost_of_large_fries + cost_of_burger + cost_of_filet + cost_of_cheese_burger + cost_of_drinks)
    ser_charge = (
            (
                    cost_of_fries + cost_of_large_fries + cost_of_burger + cost_of_filet + cost_of_cheese_burger + cost_of_drinks) / 99)
    service = "TK." + str('%.2f' % ser_charge)
    over_all_cost = "TK." + str(pay_tax + total_cost + ser_charge)
    paid_tax = "TK." + str('%.2f' % pay_tax)

    Service_Charge.set(service)
    cost.set(const_of_meals)
    Tax.set(paid_tax)
    Subtotal.set(const_of_meals)
    Total.set(over_all_cost)


def window_exit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set(0)
    Large_fries.set(0)
    Burger.set(0)
    Filet.set(0)
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set(0)
    Tax.set("")
    cost.set("")
    Cheese_burger.set(0)


# initialize ui elements
btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="powder blue",
              command=lambda: button_click(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
              command=lambda: button_click(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
              command=lambda: button_click(9))
btn9.grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="powder blue",
                  command=lambda: button_click("+"))
Addition.grid(row=2, column=3)
# ---------------------------------------------------------------------------------------------
btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
              command=lambda: button_click(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
              command=lambda: button_click(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
              command=lambda: button_click(6))
btn6.grid(row=3, column=2)

Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-", bg="powder blue",
                      command=lambda: button_click("-"))
Substraction.grid(row=3, column=3)
# -----------------------------------------------------------------------------------------------
btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
              command=lambda: button_click(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
              command=lambda: button_click(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
              command=lambda: button_click(3))
btn3.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="powder blue",
                  command=lambda: button_click("*"))
multiply.grid(row=4, column=3)
# ------------------------------------------------------------------------------------------------
btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
              command=lambda: button_click(0))
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="powder blue",
              command=display)
btnc.grid(row=5, column=1)

btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=",
                  bg="powder blue", command=equals)
btnequal.grid(columnspan=4)

Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="powder blue",
                 command=lambda: button_click("."))
Decimal.grid(row=5, column=2)

Division = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="powder blue",
                  command=lambda: button_click("/"))
Division.grid(row=5, column=3)
status = Label(f2, font=('aria', 15, 'bold'), width=16, text="-By ZB", bd=2, relief=SUNKEN)
status.grid(row=7, columnspan=3)

# ---------------------------------------------------------------------------------------
rand = StringVar()
Fries = IntVar()
Large_fries = IntVar()
Burger = IntVar()
Filet = IntVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = IntVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = IntVar()

label_reference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
label_reference.grid(row=0, column=2)
txt_reference = Label(f1, font=('ariel', 16, 'bold'), textvariable=rand, anchor="e", bd=6,
                      justify='right')
txt_reference.grid(row=0, column=3)

lblfries = Label(f1, font=('aria', 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')
txtfries.grid(row=1, column=1)

lblLargefries = Label(f1, font=('aria', 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Large_fries, bd=6, insertwidth=4, bg="powder blue",
                      justify='right')
txtLargefries.grid(row=2, column=1)

lblburger = Label(f1, font=('aria', 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')
txtburger.grid(row=3, column=1)

lblFilet = Label(f1, font=('aria', 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
lblFilet.grid(row=4, column=0)
txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')
txtFilet.grid(row=4, column=1)

lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
lblCheese_burger.grid(row=5, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                         bg="powder blue", justify='right')
txtCheese_burger.grid(row=5, column=1)

# --------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
lblDrinks.grid(row=0, column=0)
txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')
txtDrinks.grid(row=0, column=1)

lblcost = Label(f1, font=('aria', 16, 'bold'), text="cost", fg="steel blue", bd=10, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Label(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=6,
                justify='right')
txtcost.grid(row=1, column=3)

lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="steel blue", bd=10, anchor='w')
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Label(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6,
                          justify='right')
txtService_Charge.grid(row=2, column=3)

lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Label(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Label(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6,
                    justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Label(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=6,
                 justify='right')
txtTotal.grid(row=5, column=3)

# -----------------------------------------buttons------------------------------------------
lblTotal = Label(f1, text="---------------------", fg="white")
lblTotal.grid(row=6, columnspan=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                  bg="powder blue", command=ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                  bg="powder blue", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                 bg="powder blue", command=window_exit)
btnexit.grid(row=7, column=3)


def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE",
                  bg="powder blue", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
