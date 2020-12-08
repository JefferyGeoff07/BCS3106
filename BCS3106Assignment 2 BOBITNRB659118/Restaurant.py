from tkinter import *
import random

root = Tk()
root.geometry("1000x750+0+0")
root.title("SWAHILI RESTAURANT")
root.config(bg="#FFEBCD")

Tops=Frame(root,width=600, height=300,bg="#FFEBCD" , bd=20,relief="flat")
Tops=Frame(root,width=600, height=300,bg="#FFEBCD" , bd=20,relief="flat")
Tops.pack(side=TOP)
LblTitle=Label(Tops,font=("Comic Sans MS",30,'bold'),text= "Swahili Cuisine Restaurant",bg="#FFEBCD",bd=10,anchor='w')
LblTitle.grid(row=0,column=0)

f1 = Frame(root, width=300, height=300,bg="#FFEBCD", relief="ridge")
f1.pack(side=LEFT)
f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

text_Input=StringVar()
operator =""
txtdisplay = Entry(f2,font=('Comic Sans MS' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(13980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(ChipsMasala.get())
    col= float(BeefCurry.get())
    cob= float(Beverage.get())
    cofi= float(FishTilapia.get())
    cochi= float(ChickenBiryani.get())
    codr= float(Pilau.get())

    costofChickenBiryani = cof*25
    costofChipsMasala = col*250
    costofPilau = cob*300
    costofFishTilapia = cofi*500
    costofBeefCurry = cochi*350
    costofBeverage = codr*100

    costofmeal = "Ksh.",str('%.2f'% (costofChipsMasala + costofChickenBiryani +  costofPilau + costofFishTilapia+ costofBeefCurry + costofBeverage  ))
    PayTax=((costofChickenBiryani +  costofPilau + costofChipsMasala + costofFishTilapia + costofBeefCurry + costofBeverage)*0.2)
    Totalcost=(costofChickenBiryani + costofChipsMasala + costofFishTilapia + costofBeefCurry + costofBeverage)
    Ser_Charge=((costofChickenBiryani +  costofPilau + costofChipsMasala + costofFishTilapia + costofBeefCurry + costofBeverage  )/50)
    Service = "Ksh.", str('%.2f' % Ser_Charge)
    OverAllCost="ksh.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="ksh.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    ChickenBiryani.set("")
    BeefBiryani.set("")
    BeefCurry.set("")
    FishTilapia.set("")
    ChipsMasala.set("")
    Pilau.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Beverage.set("")
    Tax.set("")
    cost.set("")

btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="7",bg="#FFEBCD", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="8",bg="#FFEBCD", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="9",bg="#FFEBCD", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="+",bg="#FFEBCD", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="4",bg="#FFEBCD" ,command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="5",bg="#FFEBCD", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="6",bg="#FFEBCD", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="-",bg="#FFEBCD", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="1",bg="#FFEBCD", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="2",bg="#FFEBCD", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="3",bg="#FFEBCD", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="*",bg="#FFEBCD", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="0",bg="#FFEBCD", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="c",bg="#FFEBCD", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="=",bg="#FFEBCD",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text=".",bg="#FFEBCD", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('Comic Sans MS', 20 ,'bold'),text="/",bg="#FFEBCD", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)


rand= StringVar()
ChickenBiryani=StringVar()
BeefBiryani=StringVar()
BeefCurry=StringVar()
FishTilapia=StringVar()
ChipsMasala=StringVar()
Pilau=StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Beverage = StringVar()
Tax = StringVar()
cost = StringVar()


lblreference = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Order No.",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="#FAEBD7",
                     justify='right')
txtreference.grid(row=0, column=1)

lblChickenBiryani = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="ChickenBiryani",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblChickenBiryani.grid(row=1, column=0)
txtChickenBiryani = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=ChickenBiryani, bd=6, insertwidth=4, bg="#FAEBD7",
                 justify='right')
txtChickenBiryani.grid(row=1, column=1)

lblChipsMasala = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="ChipsMasala",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblChipsMasala.grid(row=2, column=0)
txtChipsMasala = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=ChipsMasala, bd=6, insertwidth=4, bg="#FAEBD7",
                      justify='right')
txtChipsMasala.grid(row=2, column=1)

lblFishTilapia = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Fish Tilapia", bg="#FAEBD7",fg="black", bd=10, anchor='w')
lblFishTilapia.grid(row=3, column=0)
txtFishTilapia = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=FishTilapia, bd=6, insertwidth=4, bg="#FAEBD7",
                  justify='right')
txtFishTilapia.grid(row=3, column=1)


lblBeefCurry = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Beef Curry",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblBeefCurry.grid(row=4, column=0)
txtBeefCurry = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=BeefCurry, bd=6, insertwidth=4, bg="#FAEBD7",
                 justify='right')
txtBeefCurry.grid(row=4, column=1)

lblPilau = Label(f1, font=('aria', 16, 'bold'), text="Pilau",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblPilau.grid(row=5, column=0)
txtPilau = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=Pilau, bd=6, insertwidth=4,
                         bg="#FAEBD7", justify='right')
txtPilau.grid(row=5, column=1)


lblBeverage = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Beverage",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblBeverage.grid(row=0, column=2)
txtBeverage = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=Beverage, bd=6, insertwidth=4, bg="#FAEBD7",
                  justify='right')
txtBeverage.grid(row=0, column=3)

lblcost = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="cost",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="#FAEBD7",
                justify='right')
txtcost.grid(row=1, column=3)

lblService_Charge = Label(f1, font=('Comic Sans MS', 16, 'bold'),bg="#FAEBD7", text="Service Charge", fg="black", bd=10, anchor='w')
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Entry(f1, font=('', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                          bg="#FAEBD7", justify='right')
txtService_Charge.grid(row=2, column=3)


lblTax = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Tax",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="#FAEBD7", justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Subtotal",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="#FAEBD7",
                    justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(f1, font=('Comic Sans MS', 16, 'bold'), text="Total",bg="#FAEBD7", fg="black", bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('Comic Sans MS', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="#FAEBD7",
                 justify='right')
txtTotal.grid(row=5, column=3)


btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('Comic Sans MS', 16, 'bold'), width=10, text="TOTAL",
                  bg="#FAEBD7", command=Ref)
btnTotal.grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('Comic Sans MS', 16, 'bold'), width=10, text="Cancel Order",
                  bg="#FAEBD7", command=Reset)
btnReset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('Comic Sans MS', 16, 'bold'), width=10, text="EXIT",
                 bg="#FAEBD7", command=exit)
btnexit.grid(row=7, column=3)


def price():
    roo = Tk()
    roo.geometry("600x400+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="_____________", fg="grey", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Chicken Biryani", fg="black", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="350", fg="black", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Chips Masala", fg="black", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="250", fg="black", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Beef Curry", fg="black", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="350", fg="black", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Fish Tilapia", fg="black", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="500", fg="black", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Pilau", fg="black", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="300", fg="black", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="Beverages", fg="black", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('Comic Sans MS', 15, 'bold'), text="100", fg="black", anchor=W)
    lblinfo.grid(row=6, column=3)

    root.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('Comic Sans MS', 16, 'bold'), width=10, text="PRICE",
                  bg="#FAEBD7", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
