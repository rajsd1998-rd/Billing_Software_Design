from tkinter import *

class Billing_Software:

    def __init__(self,root):
        self.root = root 

        self.root.geometry("1350x720+0+0")

        self.root.title("Billing Software")

        bg_color = "#925F29"

        title=Label(self.root,text="Billing Software", bd=7,relief=GROOVE, bg=bg_color,fg="white", font=("times new roman",25,"bold")).pack(fill=X)


        #===================================Variables======================================================================
        

        #customer

        self.c_name = StringVar()

        self.c_phone = StringVar()

        self.c_bill = StringVar()

        self.c_button = StringVar()


        #Cosmetic
        self.deo = IntVar()

        self.soap = IntVar()

        self.cream  = IntVar()

        self.facewash =IntVar()

        self.hairspray = IntVar()

        self.Belts = IntVar()


        #Groveries

        self.sugar= IntVar()

        self.daal  = IntVar()

        self.foodoil =IntVar()

        self.rice = IntVar()

        self.flour = IntVar()

        self.nut =    IntVar()


        #Cold-drinks

        self.limca = IntVar()

        self.pepsi  = IntVar()

        self.thumbsup =IntVar()

        self.cocacola = IntVar()


        #TotalArea
        self.Total_cosm = StringVar()

        self.Total_groceries = StringVar()

        self.Total_colddrink = StringVar()



        self.Tax_cosm = StringVar()

        self.Tax_groceries = StringVar()

        self.Tax_colddrink = StringVar()




        #=============================customer Details=====================================================================

        f1 = LabelFrame(self.root,text="Customer Details", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)

        f1.place(x=0, y=60,relwidth=1)


        cname_label = Label(f1,text="Customer Details:-" ,bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=3)

        cname_text = Entry(f1,width=15,bd=7,textvariable = self.c_name, font="Arial 15").grid(row=0,column=1,padx=10,pady=3)


        cphone_label= Label(f1,text="Customer Phone No:-",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=2,padx=10,pady=3)

        cphone_text = Entry(f1,width=15,bd=7,textvariable = self.c_phone, font="Arial 15").grid(row=0,column=3,padx=10,pady=3)


        cbill_label = Label(f1,text="Customer Bill No:-",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=3)

        cbill_text = Entry(f1,width=15,bd=7,textvariable = self.c_bill, font="Arial 15").grid(row=0,column=5,padx=10,pady=3)


        cbutt = Button(f1,text="Search",textvariable = self.c_button,fg="black", width=10,bd=5,font=("Arial 12")).grid(row=0,column=6,padx=10,pady=3)


        #===================================Cosmetics=======================================================================


        f2=LabelFrame(self.root,text="Cosmetics", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)

        f2.place(x=0, y=140,width=325,height=350,relwidth=1)


        soap_label = Label(f2,text="Bath Soap",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)

        soap_text = Entry(f2,width=10,bd=5,textvariable = self.soap, font="Arial 15").grid(row=0,column=1,padx=10,pady=10)


        cream_label = Label(f2,text="Face Cream",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)

        cream_text = Entry(f2,width=10,bd=5,textvariable = self.cream, font="Arial 15").grid(row=1,column=1,padx=10,pady=10)


        facewash_label = Label(f2,text="Face Wash",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10)

        facewash_text = Entry(f2,width=10,bd=5,textvariable = self.facewash, font="Arial 15").grid(row=2,column=1,padx=10,pady=10)


        hairspray_label = Label(f2,text="Hair Spray",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10)

        hairspray_text = Entry(f2,width=10,bd=5,textvariable = self.hairspray, font="Arial 15").grid(row=3,column=1,padx=10,pady=10)


        Deo_label = Label(f2,text="Deo",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10)

        Deo_text = Entry(f2,width=10,bd=5,textvariable = self.deo, font="Arial 15").grid(row=5,column=1,padx=10,pady=10)


        Belts_label = Label(f2,text="Belts",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10)

        Belts_text = Entry(f2,width=10,bd=5,textvariable = self.Belts, font="Arial 15").grid(row=4,column=1,padx=10,pady=10)


        #=======================================Grocery==============================================================================================


        f3=LabelFrame(self.root,text="Groceries", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)

        f3.place(x=330, y=140,width=325,height=350)


        sugar_label = Label(f3,text="Sugar",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)

        sugar_text = Entry(f3,width=10,textvariable = self.sugar,bd=5, font="Arial 15").grid(row=0,column=1,padx=10,pady=10)


        daal_label = Label(f3,text="Daal",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10)

        daal_text = Entry(f3,width=10,bd=5,textvariable = self.daal, font="Arial 15").grid(row=1,column=1,padx=10,pady=10)


        foodoil_label = Label(f3,text="Food Oil",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10)

        foodoil_text = Entry(f3,width=10,bd=5,textvariable = self.foodoil, font="Arial 15").grid(row=2,column=1,padx=10,pady=10)


        rice_label = Label(f3,text="Rice",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10)

        rice_text = Entry(f3,width=10,bd=5,textvariable = self.rice, font="Arial 15").grid(row=3,column=1,padx=10,pady=10)


        flour_label = Label(f3,text="Wheat Flour",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10)

        flour_text = Entry(f3,width=10,bd=5,textvariable = self.flour, font="Arial 15").grid(row=4,column=1,padx=10,pady=10)


        nuts_label = Label(f3,text="Peanuts",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10)

        nuts_text = Entry(f3,width=10,bd=5,textvariable = self.nut, font="Arial 15").grid(row=5,column=1,padx=10,pady=10)


        #=========================Cold Drinks=======================================================

        f4=LabelFrame(self.root,text="Cold Drinks", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)

        f4.place(x=660, y=140,width=325,height=350)


        soap_label = Label(f4,text="Limca",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=20)

        soap_text = Entry(f4,width=10,bd=5,textvariable = self.limca, font="Arial 15").grid(row=0,column=1,padx=10,pady=20)


        cream_label = Label(f4,text="Pepsi",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=20)

        cream_text = Entry(f4,width=10,bd=5,textvariable = self.pepsi, font="Arial 15").grid(row=1,column=1,padx=10,pady=20)


        facewash_label = Label(f4,text="Thumbs up",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=20)

        facewash_text = Entry(f4,width=10,bd=5,textvariable = self.thumbsup, font="Arial 15").grid(row=2,column=1,padx=10,pady=20)


        hairspray_label = Label(f4,text="Coca Cola",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=20)

        hairspray_text = Entry(f4,width=10,bd=5,textvariable = self.cocacola, font="Arial 15").grid(row=3,column=1,padx=10,pady=20)


        #==============================Bill Area========================================================

        f5=LabelFrame(self.root,text="Bill Area",bd=7, font=("times new roman",15,"bold"),fg="Black")

        f5.place(x=995, y=140,width=330,height=540)


        #==================================Total Area======================================================

        f6=LabelFrame(self.root,text="Total Area", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)

        f6.place(x=0, y=495,width=600,height=200)


        Tcosmetic_label = Label(f6,text="Total Cosmetic", bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=0,column=0,padx=10,pady=10)

        Tcosmetic_text = Entry(f6,width=10,bd=5,textvariable = self.Total_cosm, font="Arial 15").grid(row=0,column=1,padx=10,pady=7)


        Taxcosm_label = Label(f6,text="Tax Cosmetic",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=0,column=2,padx=10,pady=10)

        Taxcosm_text = Entry(f6,width=10,bd=5,textvariable = self.Tax_cosm, font="Arial 15").grid(row=0,column=3,padx=10,pady=7)


        Tgrocery_label = Label(f6,text="Total Grocerie",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=10)

        Tgrocery_text = Entry(f6,width=10,bd=5,textvariable = self.Total_groceries, font="Arial 15").grid(row=1,column=1,padx=10,pady=7)


        Taxgrocery_label = Label(f6,text="Tax Grocerie",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=1,column=2,padx=10,pady=10)

        Taxgrocery_text = Entry(f6,width=10,bd=5,textvariable = self.Tax_groceries, font="Arial 15").grid(row=1,column=3,padx=10,pady=7)


        Tcold_label = Label(f6,text="Total Cold Drinks",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=10)

        Tcold_text = Entry(f6,width=10,bd=5,textvariable = self.Total_colddrink, font="Arial 15").grid(row=2,column=1,padx=10,pady=7)


        Taxcold_label = Label(f6,text="Tax Cold Drinks",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=2,column=2,padx=10,pady=10)

        Taxcold_text = Entry(f6,width=10,bd=5,textvariable = self.Tax_colddrink, font="Arial 15").grid(row=2,column=3,padx=10,pady=7)


        #===========================================Buttons===========================================================================================

        f7 = LabelFrame(bd=7,bg=bg_color)

        f7.place(x=605,y=495,width=380,height=130)

        Total_button = Button(f7,text="Total", width=13,bd=3, font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=7)

        Gbill_button = Button(f7,text="Generate Bill",width=13,bd=3, font=("times new roman",15,"bold")).grid(row=0,column=1,padx=10,pady=7)

        Gbill_button = Button(f7,text="Clear",width=13,bd=3, font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=7)

        Gbill_button = Button(f7,text="Exit",width=13,bd=3, font=("times new roman",15,"bold")).grid(row=1,column=1,padx=10,pady=7)


        f7 = LabelFrame(bd=7,bg=bg_color)

        f7.place(x=605,y=628,width=380,height=70)

        Print_Bill = Button(f7,text="PRINT BILL",width=28,bd=3, font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=7)



root = Tk()

obj = Billing_Software(root)
root.mainloop()