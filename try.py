from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox

class Grocery:
    cartlist=[]
    amount=0

#--  page 1------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass
        sf.scr.geometry("1366x768")
        sf.scr.title("Avenue Supermarket")
        #sf.scr.resizable(False, False)
        sf.mainf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="upp.png")
        sf.l=Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.mainf2,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="back.png")
        sf.c.create_image(683,284,image=sf.back)
        sf.lab=Button(sf.mainf2,text= "Click to Login & Place Your Order",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("Cambria",30, 'bold'),fg="white",bg="#0b1335")
        sf.lab.place(x=350,y=250)
        sf.mainf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ page 2------
    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.loginf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="upp.png")
        sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("Cambria",16),justify=CENTER)
        sf.home.place(x=50,y=100)
        sf.adlog=Button(sf.loginf1,text="Admin Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("Cambria",16))
        sf.adlog.place(x=150,y=100)

        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.loginf2,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("Cambria",27))
        sf.log.place(x=59,y=105)
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#d3ede6",font=("Cambria",22))
        sf.lab1.place(x=100,y=180)
        sf.user=Entry(sf.loginf2,bg="white",font=("Cambria",22),bd=6 ,justify='left')
        sf.user.place(x=320,y=180)
        sf.lab2=Label(sf.loginf2,text="Password",bg="#d3ede6",font=("Cambria",22))
        sf.lab2.place(x=105,y=250)
        sf.pasd=Entry(sf.loginf2,bg="white",font=("Cambria",22),bd=6 ,justify='left')
        sf.pasd.place(x=320,y=250)
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="#0b1335",font=("Cambria",20),bd=4)
        sf.lg.place(x=180,y=320)

        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("Cambria",20),bd=4)
        sf.cl.place(x=450,y=320)
        sf.rg=Button(sf.loginf2,text="New to Grocery System",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("Cambria",20),bd=4)
        sf.rg.place(x=200,y=390)
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass

    def about(sf):
        sf.scr1=Tk()
        sf.scr1.title("Avenue Supermarket")
        sf.scr1.geometry("1366x768")
        #sf.scr1.resizable(False, False)
        sf.aboutf1=Frame(sf.scr1,height=150,width=1366)
        sf.c=Canvas(sf.aboutf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.aboutf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("Cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.L=Label(sf.scr1,text="Online Grocery System")
        sf.L.pack()
        sf.scr1.mainloop()

#--  page 3------
    def Adminlogin(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.adminf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.adminf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.adminf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("Cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.adminf1.pack(fill=BOTH,expand=1)
        sf.adminf2=Frame(sf.scr,height=618,width=1366)

        sf.c=Canvas(sf.adminf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(350,100,1016,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.adminf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("Cambria",27))
        sf.log.place(x=357,y=110)
        sf.lab1=Label(sf.adminf2,text="UserName",bg="#d3ede6",font=("Cambria",22))
        sf.lab1.place(x=400,y=200)
        sf.usera=Entry(sf.adminf2,bg="white",font=("Cambria",22),bd=5)
        sf.usera.place(x=650,y=200)
        sf.lab2=Label(sf.adminf2,text="Password",bg="#d3ede6",font=("Cambria",22))
        sf.lab2.place(x=405,y=270)
        sf.pasda=Entry(sf.adminf2,bg="white",font=("Cambria",22),bd=5)
        sf.pasda.place(x=650,y=270)
        sf.lg=Button(sf.adminf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.admindatabase(),font=("copper black",20,'bold'),bd=5)
        sf.lg.place(x=650,y=350)
        sf.cl=Button(sf.adminf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Login(),font=("copper black",20,'bold'),bd=5)
        sf.cl.place(x=400,y=350)

        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)
        sf.rg=Button(sf.adminf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(sf),bd=5,font=("copper black",20,'bold'))
        sf.rg.place(x=900,y=350)
        sf.adminf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultadmin(sf):
        sf.loguser=sf.usera.get()
        sf.logpass=sf.pasda.get()
        return sf.loguser,sf.logpass

#--  page 4------
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.regf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="upp.png")
        sf.ba=Label(sf.regf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.regf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",font=("cambria",16))
        sf.home.place(x=100,y=90)
        sf.regf1.pack(fill=BOTH,expand=1)

        sf.regf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.regf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.regf2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("Cambria",27))
        sf.log.place(x=480,y=120)
        sf.lab1=Label(sf.regf2,text="FirstName",bg="#d3ede6",font=("Cambria",18))
        sf.lab1.place(x=190,y=200)
        sf.first=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.first.place(x=430,y=200)
        sf.lab2=Label(sf.regf2,text="LastName",bg="#d3ede6",font=("Cambria",18))
        sf.lab2.place(x=730,y=200)
        sf.last=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.last.place(x=920,y=200)
        sf.lab3=Label(sf.regf2,text="Username",bg="#d3ede6",font=("Cambria",18))
        sf.lab3.place(x=190,y=250)
        sf.usern=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.usern.place(x=430,y=250)
        sf.lab4=Label(sf.regf2,text="Password",bg="#d3ede6",font=("Cambria",18))
        sf.lab4.place(x=730,y=250)
        sf.passd=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.passd.place(x=920,y=250)
        sf.lab5=Label(sf.regf2,text="Email",bg="#d3ede6",font=("Cambria",18))
        sf.lab5.place(x=190,y=300)
        sf.email=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.email.place(x=430,y=300)
        sf.lab6=Label(sf.regf2,text="Mobile No.",bg="#d3ede6",font=("Cambria",18))
        sf.lab6.place(x=730,y=300)
        sf.mob=Entry(sf.regf2,bg="white",width=15,font=("Cambria",18),bd=5)
        sf.mob.place(x=920,y=300)
        sf.bc=Button(sf.regf2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="#0b1335",font=("Cambria",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.regf2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Regdatabase(),font=("Cambria",18),bd=5)
        sf.rg.place(x=610,y=370)

        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.regf2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(sf),font=("Cambria",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.regf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob

#--  page 5------
    def adminmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        #sf.scr.config(bg="#f2e8b8")
        sf.scr.title("Online Grocery System")
        sf.scr.geometry("1366x768")

        sf.admainf1=Frame(sf.scr,bg="#f2e8b8",height=150,width=1366)
        sf.admainf1.pack(side=TOP,fill=BOTH)
        sf.c=Canvas(sf.admainf1,height=150,bg="#f2e8b8",width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo2.png")
        sf.c.create_image(683,50,image=sf.logo)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(900,50,text=sf.localtime,fill="white",font=("cambria",16))
        sf.c.create_text(683,125,font=( 'Cambria' ,25, 'bold','underline' ),text="Management System")
        sf.out=Button(sf.admainf1,text="Log Out",bg="#0b1335",cursor="hand2",command=lambda:sf.Adminlogin(),fg="white",bd=5,font=("cambria",16,'bold'))
        sf.out.place(x=1100,y=25)

        def Ref(sf):
            sf.con=connect("grocery.db")
##            sf.x=random.randint(100, 500)
##            sf.randomRef = str(sf.x)
            sf.cur=sf.con.cursor()
            try:
                 sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                 sf.con.commit()
            except:
                pass
            x=sf.cur.execute("select count(*) from orderdetail")
            ordno=list(x)[0][0]+1
            sf.order.set(ordno)

            sf.v1=sf.vp1.get()
            if sf.v1=="1 KG":
                sf.p1=float(sf.rice.get())*35
            else:
                sf.v1=="5 KG"
                sf.p1=float(sf.rice.get())*165
                
            sf.v2=sf.vp2.get()
            if sf.v2=="1 KG":
                sf.p2= float(sf.wheat.get())*40
            else:
                sf.v2=="5 KG"
                sf.p2= float(sf.wheat.get())*190
                
            sf.v3=sf.vp3.get()
            if sf.v3=="1 KG":
                sf.p3= float(sf.tdal.get())*110
            else:
                sf.v3=="5 KG"
                sf.p3= float(sf.tdal.get())*530
                
            sf.v4=sf.vp4.get()
            if sf.v4=="1 KG":
                sf.p4= float(sf.mdal.get())*135
            else:
                sf.v4=="5 KG"
                sf.p4= float(sf.mdal.get())*675

            sf.v5=sf.vp5.get()
            if sf.v5=="Half KG":
                sf.p5= float(sf.salt.get())*15
            else:
                sf.v5=="1 KG"
                sf.p5= float(sf.salt.get())*24
                
            sf.v6=sf.vp6.get()
            if sf.v6=="Half KG":
                sf.p6= float(sf.rcpow.get())*70
            else:
                sf.v6=="1 KG"
                sf.p6= float(sf.rcpow.get())*130
                
            sf.v7=sf.vp7.get()
            if sf.v7=="Half KG":
                sf.p7= float(sf.turm.get())*100
            else:
                sf.v7=="1 KG"
                sf.p7= float(sf.turm.get())*190

            sf.v8=sf.vp8.get()
            if sf.v8=="Half KG":
                sf.p8= float(sf.sugar.get())*20
            else:
                sf.v8=="1 KG"
                sf.p8= float(sf.sugar.get())*35

            sf.v9=sf.vp9.get()
            if sf.v9=="Half Litre":
                sf.p9= float(sf.milk.get())*30
            else:
                sf.v9=="1 Litre"
                sf.p9= float(sf.milk.get())*60
                
            sf.v10=sf.vp10.get()
            if sf.v10=="Half Litre":
                sf.p10= float(sf.yogurt.get())*18
            else:
                sf.v10=="1 Litre"
                sf.p10= float(sf.yogurt())*40
                
            sf.v11=sf.vp11.get()
            if sf.v11=="Half Litre":
                sf.p11= float(sf.bmilk.get())*10
            else:
                sf.v11=="1 Litre"
                sf.p11= float(sf.bmilk.get())*20
                
            sf.v12=sf.vp12.get()
            if sf.v12=="Half Litre":
                sf.p12= float(sf.lassi.get())*20
            else:
                sf.v12=="1 Litre"
                sf.p12= float(sf.lassi.get())*40

            sf.v13=sf.vp13.get()
            if sf.v13=="Half KG":
                sf.p13= float(sf.butter.get())*105
            else:
                sf.v13=="1 KG"
                sf.p13= float(sf.butter.get())*210

            sf.v14=sf.vp14.get()
            if sf.v14=="Half KG":
                sf.p14= float(sf.cheese.get())*230
            else:
                sf.v14=="1 KG"
                sf.p14= float(sf.cheese.get())*500

            sf.v15=sf.vp15.get()
            if sf.v15=="Half KG":
                sf.p15= float(sf.paneer.get())*140
            else:
                sf.v15=="1 KG"
                sf.p15= float(sf.paneer.get())*270

            sf.v16=sf.vp16.get()
            if sf.v16=="Half KG":
                sf.p16= float(sf.shri.get())*125
            else:
                sf.v16=="1 KG"
                sf.p16= float(sf.shri.get())*260


            sf.v25=sf.vp25.get()
            if sf.v25=="30gms":
                sf.p25= float(sf.lays.get())*10
            else:
                sf.v25=="52gms"
                sf.p25= float(sf.lays.get())*20

            sf.v26=sf.vp26.get()
            if sf.v26=="50gms":
                sf.p26= float(sf.kurkure.get())*10
            else:
                sf.v26=="140gms"
                sf.p26= float(sf.kurkure.get())*20

            sf.v27=sf.vp27.get()
            if sf.v27=="100gms":
                sf.p27= float(sf.parle.get())*10
            else:
                sf.v27=="250gms"
                sf.p27= float(sf.parle.get())*20

            sf.v28=sf.vp28.get()
            if sf.v28=="50gms":
                sf.p28= float(sf.bourbon.get())*10
            else:
                sf.v28=="100gms"
                sf.p28= float(sf.bourbon.get())*20

            sf.v29=sf.vp29.get()
            if sf.v29=="27gms":
                sf.p29= float(sf.kitkat.get())*20
            else:
                sf.v29=="126gms"
                sf.p29= float(sf.kitkat.get())*100

            sf.v30=sf.vp30.get()
            if sf.v30=="42gms":
                sf.p30= float(sf.aloo.get())*10
            else:
                sf.v30=="400gms"
                sf.p30= float(sf.aloo.get())*90

            sf.v31=sf.vp12.get()
            if sf.v31=="250gms":
                sf.p31= float(sf.laxmi.get())*90
            else:
                sf.v31=="500gms"
                sf.p31= float(sf.laxmi.get())*190

            sf.v32=sf.vp32.get()
            if sf.v32=="250gms":
                sf.p32= float(sf.chitale.get())*90
            else:
                sf.v32=="500gns"
                sf.p32= float(sf.chitale.get())*190

            sf.costofmeal = "Rs.",str('%.2f'% (sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14+sf.p15+sf.p16+sf.p25+sf.p26+sf.p27+sf.p28+sf.p29+sf.p30+sf.p31+sf.p32))
            sf.PayTax=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14+sf.p15+sf.p16+sf.p25+sf.p26+sf.p27+sf.p28+sf.p29+sf.p30+sf.p31+sf.p32)*.05)
            sf.Totalcost=(sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14+sf.p15+sf.p16+sf.p25+sf.p26+sf.p27+sf.p28+sf.p29+sf.p30+sf.p31+sf.p32)
            sf.Ser_Charge=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14+sf.p15+sf.p16+sf.p25+sf.p26+sf.p27+sf.p28+sf.p29+sf.p30+sf.p31+sf.p32)/99)
            sf.Service="Rs."+str('%.2f'% sf.Ser_Charge)
            sf.OverAllCost="Rs."+str(int(sf.PayTax + sf.Totalcost + sf.Ser_Charge))
            sf.PaidTax="Rs."+str('%.2f'% sf.PayTax)
            sf.money=int(sf.PayTax + sf.Totalcost + sf.Ser_Charge)
            sf.Service_Charge.set(sf.Service)
            sf.cost.set(sf.costofmeal)
            sf.Tax.set(sf.PaidTax)
            sf.Total.set(sf.OverAllCost) 

        def reset(sf):
            sf.rice.set("0")
            sf.wheat.set("0")
            sf.tdal.set("0")
            sf.mdal.set("0")
            sf.salt.set("0")
            sf.rcpow.set("0")
            sf.turm.set("0")
            sf.sugar.set("0")
            sf.milk.set("0")
            sf.yogurt.set("0")
            sf.bmilk.set("0")
            sf.lassi.set("0")
            sf.butter.set("0")
            sf.cheese.set("0")
            sf.paneer.set("0")
            sf.lays.set("0")
            sf.kurkure.set("0")
            sf.parle.set("0")
            sf.bourbon.set("0")
            sf.kitkat.set("0")
            sf.aloo.set("0")
            sf.laxmi.set("0")
            sf.chitale.set("0")

            sf.Total.set("0")
            sf.Service_Charge.set("0")
            sf.Tax.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")

            sf.vp1.set("1 KG")
            sf.vp2.set("1 KG")
            sf.vp3.set("1 KG")
            sf.vp4.set("1 KG")
            sf.vp5.set("Half KG")
            sf.vp6.set("Half KG")
            sf.vp7.set("Half KG")
            sf.vp8.set("Half KG")
            sf.vp9.set("Half Litre")
            sf.vp10.set("Half Litre")
            sf.vp11.set("Half Litre")
            sf.vp12.set("Half Litre")
            sf.vp13.set("Half KG")
            sf.vp14.set("Half KG")
            sf.vp15.set("Half KG")
            sf.vp16.set("Half KG")
            sf.vp25.set("30gms")
            sf.vp26.set("50gms")
            sf.vp27.set("100gms")
            sf.vp28.set("50gms")
            sf.vp29.set("42gms")
            sf.vp30.set("27gms")
            sf.vp31.set("250gms")
            sf.vp32.set("250gms")

        def price(sf):
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15,'bold'), text="Grocery", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Rice", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹35/₹165", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Wheat", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹40/₹190", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Toor Daal", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹110/₹550", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Mung Dal", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹135/₹675", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Salt", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=6, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹15/₹24", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Red Chilli", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹70/₹130", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Turmeric", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹100/₹190", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Sugar", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹20/₹35", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)

            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Dairy Products", fg="black", anchor=W)
            sf.lblinfo.grid(row=10, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Milk", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=11, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹30/₹60", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=11, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Yogurt", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹18/₹40", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chaas", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹20", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Lassi", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹20/₹40", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Butter", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=15, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹105/₹210", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=15, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Cheese", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹230/₹500", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Paneer", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹140/₹270", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Shrikhand", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹125/₹260", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=2)

            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Snacks", fg="black", anchor=W)
            sf.lblinfo.grid(row=28, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Lays", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=29, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹20", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=29, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Kurkure", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=30, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹20", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=30, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Parle-G", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=31, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹20", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=31, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Bourbon", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=32, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹20", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=32, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="KitKat", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=33, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹20/₹100", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=33, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Aloo Bhujia", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=34, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹10/₹90", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=34, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chiwda", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=35, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹90/₹190", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=35, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Bhakarwadi", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=36, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹90/₹190", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=36, column=2)

            sf.roo.mainloop()

        sf.admainf2 = Frame(sf.scr,width =1366,bg="#f2e8b8",height=618,relief=SUNKEN)
        sf.admainf2.pack(side=BOTTOM,fill=BOTH,expand=1)
        sf.rice= StringVar()
        sf.wheat = StringVar()
        sf.tdal = StringVar()
        sf.mdal= StringVar()
        sf.salt= StringVar()
        sf.rcpow = StringVar()
        sf.turm = StringVar()
        sf.sugar= StringVar()
        sf.milk = StringVar()
        sf.yogurt = StringVar()
        sf.bmilk= StringVar()
        sf.lassi= StringVar()
        sf.butter = StringVar()
        sf.cheese = StringVar()
        sf.paneer = StringVar()
        sf.shri= StringVar()
        sf.lays = StringVar()
        sf.kurkure = StringVar()
        sf.parle= StringVar()
        sf.bourbon= StringVar()
        sf.kitkat = StringVar()
        sf.aloo = StringVar()
        sf.laxmi = StringVar()
        sf.chitale= StringVar()

        sf.Total = StringVar()
        sf.Service_Charge= StringVar()
        sf.Tax = StringVar()
        sf.cost = StringVar()
        sf.order=StringVar()
        sf.Cutomer_name =StringVar()
        sf.cusmob = StringVar()

        sf.vp1=StringVar()
        sf.vp2=StringVar()
        sf.vp3=StringVar()
        sf.vp4=StringVar()
        sf.vp5=StringVar()
        sf.vp6=StringVar()
        sf.vp7=StringVar()
        sf.vp8=StringVar()
        sf.vp9=StringVar()
        sf.vp10=StringVar()
        sf.vp11=StringVar()
        sf.vp12=StringVar()
        sf.vp13=StringVar()
        sf.vp14=StringVar()
        sf.vp15=StringVar()
        sf.vp16=StringVar()
        sf.vp25=StringVar()
        sf.vp26=StringVar()
        sf.vp27=StringVar()
        sf.vp28=StringVar()
        sf.vp29=StringVar()
        sf.vp30=StringVar()
        sf.vp31=StringVar()
        sf.vp32=StringVar()
        reset(sf)
        sf.l=["Half","Full"]
        sf.ll=["250ml","600ml"]

        #grocery
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=1)
        sf.lbl1 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,20, 'bold','underline' ),bg="#f2e8b8",text="Grocery",bd=10,anchor='w')
        sf.lbl1.place(x=180,y=0)
        sf.lbl11 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl11.grid(row=1,column=0)
        sf.lbl12 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl12.grid(row=1,column=1)
        sf.lbl13 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl13.grid(row=1,column=2,padx=4)

        sf.lblvbir= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Rice:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblvbir.grid(row=2,column=0)
        sf.opvbir=OptionMenu(sf.admainf2,sf.vp1,*sf.l)
        sf.opvbir.config(width=6)
        sf.opvbir.grid(row=2,column=1)
        sf.txtvbir= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.rice, bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtvbir.grid(row=2,column=2)

        sf.lblpbir = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Wheat:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpir.grid(row=3,column=0)
        sf.oppbir=OptionMenu(sf.admainf2,sf.vp2,*sf.l)
        sf.oppbir.config(width=6)
        sf.oppbir.grid(row=3,column=1)
        sf.txtpbir = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.wheat , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpbir.grid(row=3,column=2)

        sf.lblpmak= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Toor Daal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpmak.grid(row=4,column=0)
        sf.oppmak=OptionMenu(sf.admainf2,sf.vp3,*sf.l)
        sf.oppmak.config(width=6)
        sf.oppmak.grid(row=4,column=1)
        sf.txtpmak= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.tdal ,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpmak.grid(row=4,column=2)

        sf.lblptik = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Mung Dal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblptik.grid(row=5,column=0)
        sf.opptik=OptionMenu(sf.admainf2,sf.vp4,*sf.l)
        sf.opptik.config(width=6)
        sf.opptik.grid(row=5,column=1)
        sf.txtptik = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.mdal,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtptik.grid(row=5,column=2)

        sf.lblhyder = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Salt:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblhyder.grid(row=6,column=0)
        sf.ophyder=OptionMenu(sf.admainf2,sf.vp5,*sf.l)
        sf.ophyder.config(width=6)
        sf.ophyder.grid(row=6,column=1)
        sf.txthyder = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.salt,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txthyder.grid(row=6,column=2)

        sf.lblaloob = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Red Chilli:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblaloob.grid(row=7,column=0)
        sf.opaloob=OptionMenu(sf.admainf2,sf.vp6,*sf.l)
        sf.opaloob.config(width=6)
        sf.opaloob.grid(row=7,column=1)
        sf.txtaloob = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.rcpow,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtaloob.grid(row=7,column=2)

        sf.lblsoyab = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Turmeric:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsoyab.grid(row=8,column=0)
        sf.opsoyab=OptionMenu(sf.admainf2,sf.vp7,*sf.l)
        sf.opsoyab.config(width=6)
        sf.opsoyab.grid(row=8,column=1)
        sf.txtsoyab = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.turm,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtsoyab.grid(row=8,column=2)

        sf.lblmush = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Sugar:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmush.grid(row=9,column=0)
        sf.opmush=OptionMenu(sf.admainf2,sf.vp8,*sf.l)
        sf.opmush.config(width=6)
        sf.opmush.grid(row=9,column=1)
        sf.txtmush = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.sugar,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtmush.grid(row=9,column=2)

        #dairy products
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=10,column=1)
        sf.lbl2 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,20, 'bold','underline' ),bg="#f2e8b8",text="Dairy Products",bd=10,anchor='w')
        sf.lbl2.place(x=150,y=290)
        sf.lbl21 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl21.grid(row=11,column=0)
        sf.lbl22 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl22.grid(row=11,column=1)
        sf.lbl23 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl23.grid(row=11,column=2)

        sf.lblebir= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Milk:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblebir.grid(row=12,column=0)
        sf.opebir=OptionMenu(sf.admainf2,sf.vp9,*sf.l)
        sf.opebir.config(width=6)
        sf.opebir.grid(row=12,column=1)
        sf.txtebir= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.milk , bd=6,bg="powder blue" ,justify='right')
        sf.txtebir.grid(row=12,column=2)

        sf.lblcbir = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Yogurt:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcbir.grid(row=13,column=0)
        sf.opcbir=OptionMenu(sf.admainf2,sf.vp10,*sf.l)
        sf.opcbir.config(width=6)
        sf.opcbir.grid(row=13,column=1)
        sf.txtcbir = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.yogurt , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtcbir.grid(row=13,column=2)

        sf.lblcbut= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chaas:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcbut.grid(row=14,column=0)
        sf.opcbut=OptionMenu(sf.admainf2,sf.vp11,*sf.l)
        sf.opcbut.config(width=6)
        sf.opcbut.grid(row=14,column=1)
        sf.txtcbut= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.bmilk , bd=6,bg="powder blue" ,justify='right')
        sf.txtcbut.grid(row=14,column=2)

        sf.lblctik = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Lassi:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblctik.grid(row=15,column=0)
        sf.opctik=OptionMenu(sf.admainf2,sf.vp12,*sf.l)
        sf.opctik.config(width=6)
        sf.opctik.grid(row=15,column=1)
        sf.txtctik= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.lassi , bd=6,bg="powder blue" ,justify='right')
        sf.txtctik.grid(row=15,column=2)

        sf.lblcafg = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Butter:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcafg.grid(row=16,column=0)
        sf.opcafg=OptionMenu(sf.admainf2,sf.vp13,*sf.l)
        sf.opcafg.config(width=6)
        sf.opcafg.grid(row=16,column=1)
        sf.txtcafg= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.butter , bd=6,bg="powder blue" ,justify='right')
        sf.txtcafg.grid(row=16,column=2)

        sf.lblctang = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Cheese:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblctang.grid(row=17,column=0)
        sf.opctang=OptionMenu(sf.admainf2,sf.vp14,*sf.l)
        sf.opctang.config(width=6)
        sf.opctang.grid(row=17,column=1)
        sf.txtctang= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.cheese , bd=6,bg="powder blue" ,justify='right')
        sf.txtctang.grid(row=17,column=2)

        sf.lblseek = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Paneer:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblseek.grid(row=18,column=0)
        sf.opseek=OptionMenu(sf.admainf2,sf.vp15,*sf.l)
        sf.opseek.config(width=6)
        sf.opseek.grid(row=18,column=1)
        sf.txtseek= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.paneer , bd=6,bg="powder blue" ,justify='right')
        sf.txtseek.grid(row=18,column=2)

        sf.lblprawn = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Shrikhand:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblprawn.grid(row=19,column=0)
        sf.opprawn=OptionMenu(sf.admainf2,sf.vp16,*sf.l)
        sf.opprawn.config(width=6)
        sf.opprawn.grid(row=19,column=1)
        sf.txtprawn= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.shri , bd=6,bg="powder blue" ,justify='right')
        sf.txtprawn.grid(row=19,column=2)

        #snacks
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=10,column=4)
        sf.lbl4 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,20, 'bold','underline' ),bg="#f2e8b8",text="Snacks",bd=10,anchor='w')
        sf.lbl4.place(x=500,y=290)
        sf.lbl41 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl41.grid(row=11,column=4)
        sf.lbl43 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl43.grid(row=11,column=5)

        sf.lblthum= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Lays:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblthum.grid(row=12,column=4)
        sf.opthum=OptionMenu(sf.admainf2,sf.vp25,*sf.ll)
        sf.opthum.config(width=6)
        sf.opthum.grid(row=12,column=1)
        sf.txtthum= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.lays , bd=6,bg="powder blue" ,justify='right')
        sf.txtthum.grid(row=12,column=5)

        sf.lblpep = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Kurkure:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpep.grid(row=13,column=4)
        sf.oppep=OptionMenu(sf.admainf2,sf.vp26,*sf.ll)
        sf.oppep.config(width=6)
        sf.oppep.grid(row=13,column=1)
        sf.txtpep = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.kurkure , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpep.grid(row=13,column=5)

        sf.lblcoco= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Parle-G:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcoco.grid(row=14,column=4)
        sf.opcoco=OptionMenu(sf.admainf2,sf.vp27,*sf.ll)
        sf.opcoco.config(width=6)
        sf.opcoco.grid(row=14,column=1)
        sf.txtcoco= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.parle , bd=6,bg="powder blue" ,justify='right')
        sf.txtcoco.grid(row=14,column=5)

        sf.lblspri= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Bourbon:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblspri.grid(row=15,column=4)
        sf.opspri=OptionMenu(sf.admainf2,sf.vp28,*sf.ll)
        sf.opspri.config(width=6)
        sf.opspri.grid(row=15,column=1)
        sf.txtspri= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.bourbon , bd=6,bg="powder blue" ,justify='right')
        sf.txtspri.grid(row=15,column=5)

        sf.lblseven= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="KitKat:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblseven.grid(row=16,column=4)
        sf.opseven=OptionMenu(sf.admainf2,sf.vp29,*sf.ll)
        sf.opseven.config(width=6)
        sf.opseven.grid(row=16,column=1)
        sf.txtseven= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.kitkat , bd=6,bg="powder blue" ,justify='right')
        sf.txtseven.grid(row=16,column=5)

        sf.lblfant= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Aloo Bhujia:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblfant.grid(row=17,column=4)
        sf.opfant=OptionMenu(sf.admainf2,sf.vp30,*sf.ll)
        sf.opfant.config(width=6)
        sf.opfant.grid(row=17,column=1)
        sf.txtfant= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.aloo , bd=6,bg="powder blue" ,justify='right')
        sf.txtfant.grid(row=17,column=5)

        sf.lblmiri= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chiwda:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmiri.grid(row=18,column=4)
        sf.opmiri=OptionMenu(sf.admainf2,sf.vp31,*sf.ll)
        sf.opmiri.config(width=6)
        sf.opmiri.grid(row=18,column=1)
        sf.txtmiri= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.laxmi , bd=6,bg="powder blue" ,justify='right')
        sf.txtmiri.grid(row=18,column=5)

        sf.lbllim= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Bhakarwadi:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbllim.grid(row=19,column=4)
        sf.oplim=OptionMenu(sf.admainf2,sf.vp32,*sf.ll)
        sf.oplim.config(width=6)
        sf.oplim.grid(row=19,column=1)
        sf.txtlim= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.chitale , bd=6,bg="powder blue" ,justify='right')
        sf.txtlim.grid(row=19,column=5)

        # customer
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=8)
        sf.lbl6 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,22, 'bold','underline' ),bg="#f2e8b8",text="Customer Detail",bd=10,anchor='w')
        sf.lbl6.place(x=970,y=0)
        
        sf.lblnam= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Name:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblnam.grid(row=1,column=7)
        sf.txtnam= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Cutomer_name , bd=6,width=14,bg="powder blue" ,justify='left')
        sf.txtnam.grid(row=1,column=8)


        sf.lblmob = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Mobile No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmob.grid(row=2,column=7)
        sf.txtmob = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cusmob,width=14,bd=6,bg="powder blue" ,justify='left')
        sf.txtmob.grid(row=2,column=8)

        #bill
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=3,column=8)
        sf.lbl5 = Label(sf.admainf2,pady=2, font=( 'Cambria' ,22, 'bold','underline' ),bg="#f2e8b8",text="Bill Payment",bd=10,anchor='w')
        sf.lbl5.place(x=1000,y=140)

        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cambria' ,20),width=5,bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=4,column=6)
        sf.lblord= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Order No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblord.grid(row=4,column=7)
        sf.txtord= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.order , bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txtord.grid(row=4,column=8)

        sf.lblco = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Subtotal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblco.grid(row=5,column=7)
        sf.txtco = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cost,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtco.grid(row=5,column=8)

        sf.lblser= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Service Charge:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblser.grid(row=6,column=7)
        sf.txtser= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Service_Charge ,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtser.grid(row=6,column=8)

        sf.lbltax = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Tax:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltax.grid(row=7,column=7)
        sf.txttax = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Tax, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttax.grid(row=7,column=8)

        sf.lbltot = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Total:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltot.grid(row=8,column=7)
        sf.txttot = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Total, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttot.grid(row=8,column=8)

        sf.btnprice=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PRICE", bg="powder blue",command=lambda:price(sf))
        sf.btnprice.place(x=970,y=440)

        sf.btnTotal=Button(sf.admainf2,pady=2,bd=6,fg="black",font=('ariel' ,16,'bold'),width=6, text="TOTAL", bg="powder blue",command=lambda:Ref(sf))
        sf.btnTotal.place(x=1160,y=440)

        sf.btnreset=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=lambda:reset(sf))
        sf.btnreset.place(x=970,y=500)

        sf.btnpay=Button(sf.admainf2,pady=2, bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PAY", bg="powder blue",command=lambda:sf.adminorderdetail())
        sf.btnpay.place(x=1160,y=500)

        sf.scr.mainloop()

    def resultadminorder(sf):
        r1=sf.rice.get()
        r2=sf.wheat.get()
        r3=sf.tdal.get()
        r4=sf.mdal.get()
        r5=sf.salt.get()
        r6=sf.rcpow.get()
        r7=sf.turm.get()
        r8=sf.sugar.get()
        r9=sf.milk.get()
        r10=sf.yogurt.get()
        r11-sf.bmilk.get()
        r12=sf.lassi.get()
        r13=sf.butter.get()
        r14=sf.cheese.get()
        r15=sf.paneer.get()
        r16=sf.shri.get()
        r25=sf.lays.get()
        r26=sf.kurkure.get()
        r27=sf.parle.get()
        r28=sf.bourbon.get()
        r29=sf.kitkat.get()
        r30=sf.aloo.get()
        r31=sf.laxmi.get()
        r32=sf.chitale.get()
        r33=sf.Cutomer_name.get()
        r34=sf.cusmob.get()
        r35=sf.vp1.get()
        r36=sf.vp2.get()
        r37=sf.vp3.get()
        r38=sf.vp4.get()
        r39=sf.vp5.get()
        r40=sf.vp6.get()
        r41=sf.vp7.get()
        r42=sf.vp8.get()
        r43=sf.vp9.get()
        r44=sf.vp10.get()
        r45=sf.vp11.get()
        r46=sf.vp12.get()
        r47=sf.vp13.get()
        r48=sf.vp14.get()
        r49=sf.vp15.get()
        r50=sf.vp16.get()
        r51=sf.vp25.get()
        r52=sf.vp26.get()
        r53=sf.vp27.get()
        r54=sf.vp28.get()
        r55=sf.vp29.get()
        r56=sf.vp30.get()
        r57=sf.vp31.get()
        r58=sf.vp32.get()
        r59=sf.txtvbir.get()
        r60=sf.txtpbir.get()
        r61=sf.txtpmak.get()
        r62=sf.txtptik.get()
        r63=sf.txthyder.get()
        r64=sf.txtaloob.get()
        r65=sf.txtsoyab.get()
        r66=sf.txtmush.get()
        r67=sf.txtebir.get()
        r68=sf.txtcbir.get()
        r69=sf.txtcbut.get()
        r70=sf.txtctik.get()
        r71=sf.txtcafg.get()
        r72=sf.txtctang.get()
        r73=sf.txtseek.get()
        r74=sf.txtprawn.get()
        r75=sf.txtvseek.get()
        r76=sf.txthara.get()
        r77=sf.txtpatik.get()
        r78=sf.txtvplate.get()
        r79=sf.txtctand.get()
        r80=sf.txtmseek.get()
        r81=sf.txtmsham.get()
        r82=sf.txtnplate.get()
        r83=sf.txtthum.get()
        r84=sf.txtpep.get()
        r85=sf.txtcoco.get()
        r86=sf.txtspri.get()
        r87=sf.txtseven.get()
        r88=sf.txtfant.get()
        r89=sf.txtmiri.get()
        r90=sf.txtlim.get()

        l1=[r1,r22,30]
        l2=[r2,r23,31]
        l3=[r3,r24,32]
        l4=[r4,r25,33]
        l5=[r5,r26,34]
        l6=[r6,r27,35]
        l7=[r7,r28,36]
        l8=[r8,r29,37]
        l9=[r12,r38]
        l10=[r13,r39]
        l11=[r14,r40]
        l12=[r9,r41]
        l13=[r10,r42]
        l14=[r11,r43]
        
        return r20,r21,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14

#--  page 6------        
    def menulist(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.menuf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.menuf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.menuf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.out=Button(sf.menuf1,text="Back",command=lambda:sf.birmain(),bg="#0b1335",cursor="hand2",fg="white",font=("cambria",16,'bold'))
        sf.out.place(x=150,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("cambria",16))
        sf.menuf1.pack(fill=BOTH,expand=1)

        sf.menuf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.menuf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50, 140, 1316, 420,fill="#d3ede6",outline="white",width=6)
        sf.veg=PhotoImage(file="Groc.png")
        sf.c.create_image(330,250,image=sf.veg)
        sf.vegbut=Button(sf.menuf2,text="Grocery",cursor="hand2",fg="white",command=lambda:sf.grocery(sf.x),bg="#0b1335",bd=5,font=("cambria",18,'bold'))
        sf.vegbut.place(x=270,y=350)
        sf.nonveg=PhotoImage(file="dairy.png")
        sf.c.create_image(670,250,image=sf.nonveg)
        sf.nonvegbut=Button(sf.menuf2,text="Dairy Products",cursor="hand2",fg="white",command=lambda:sf.dairy(sf.x),bg="#0b1335",bd=5,font=("cambria",18,'bold'))
        sf.nonvegbut.place(x=570,y=350)
        sf.side=PhotoImage(file="snacks.png")
        sf.c.create_image(1020,250,image=sf.side)
        sf.sidebut=Button(sf.menuf2,text="Snacks",cursor="hand2",fg="white",command=lambda:sf.snacks(sf.x),bg="#0b1335",bd=5,font=("cambria",18,'bold'))
        sf.sidebut.place(x=970,y=350)
        sf.menuf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 7------
    def birmain(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.birf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.birf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.out=Button(sf.birf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",font=("cambria",16))
        sf.out.place(x=150,y=100)
        sf.birf1.pack(fill=BOTH,expand=1)

        sf.birf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.birf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        sf.deli=PhotoImage(file="delivery.png")
        sf.c.create_image(540,260,image=sf.deli)
        sf.pic=PhotoImage(file="pick.png")
        sf.c.create_image(825,260,image=sf.pic)
        sf.de=Button(sf.birf2,text="Delivery",cursor="hand2",fg="white",command=lambda:sf.menulist("deli"),bg="#0b1335",font=("cambria",20),bd=5)
        sf.de.place(x=480,y=400)
        sf.pu=Button(sf.birf2,text="Pick Up",cursor="hand2",fg="white",command=lambda:sf.menulist("pick"),bg="#0b1335",font=("cambria",20),bd=5)
        sf.pu.place(x=770,y=400)
        sf.c.create_rectangle(405,125,678,465,outline="black",width=2)
        sf.c.create_rectangle(688,125,960,465,outline="black",width=2)
        sf.birf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 8------
    def grocery(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.vegf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.vegf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.vegf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.vegf1.pack(fill=BOTH,expand=1)
        sf.vegf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.vegf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.vegf2,text="GROCERY",bg="#9db1f2",font=("Cambria",22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(100, 40, 1200, 540,fill="#d3ede6",outline="white",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q5=StringVar()
        sf.q6=StringVar()
        sf.q7=StringVar()
        sf.q8=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        sf.q5.set("0")
        sf.q6.set("0")
        sf.q7.set("0")
        sf.q8.set("0")

        #grocery-1
        sf.c.create_rectangle(110, 50, 1190, 170,width=2)
        sf.vegb=PhotoImage(file="rice.png")
        sf.c.create_image(170,110,image=sf.vegb)
        sf.c.create_text(280,80,text="Rice",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,80,text="₹35/₹165",fill="#ff3838",font=("cambria",17,'bold'))
        #ch1=sf.check(sf.vegf2,100)
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.vegf2,text = "1 KG",value=10,variable=sf.v1)
        sf.C11.place(x=250,y=100)
        sf.C12 = Radiobutton(sf.vegf2, text = "5 KG",value = 20, variable =sf.v1)
        sf.C12.place(x=350,y=100)
        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()
        sf.c.create_text(290,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty1=Entry(sf.vegf2,textvariable=sf.q1,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty1.place(x=350,y=140)
        sf.add1=Button(sf.vegf2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add1.place(x=450,y=120)
        def addch1():
            if sf.v1.get()==10:
                ch1="1 KG"
                pric1=35
            else:
                sf.v1.get()==20
                ch1="5 KG"
                pric1=165
            sf.addlist(["Rice",ch1,sf.q1.get(),pric1*int(sf.q1.get())])

        #grocery-2
        sf.c.create_rectangle(110, 170, 1190, 290,width=2)
        sf.vag=PhotoImage(file="wheat.png")
        sf.c.create_image(170,230,image=sf.vag)
        sf.c.create_text(290,200,text="Wheat",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,200,text="₹40/₹190",fill="#ff3838",font=("cambria",17,'bold'))
##        ch2=sf.check(sf.vegf2,220)
        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.vegf2,text = "1 KG",value=10,variable=sf.v2)
        sf.C21.place(x=250,y=220)
        sf.C22 = Radiobutton(sf.vegf2, text = "5 KG",value = 20, variable =sf.v2)
        sf.C22.place(x=350,y=220)
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()
        sf.c.create_text(290,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty2=Entry(sf.vegf2,textvariable=sf.q2,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty2.place(x=350,y=260)
        sf.add2=Button(sf.vegf2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add2.place(x=450,y=240)
        def addch2():
            if sf.v2.get()==10:
                ch2="1 KG"
                pric2=40
            else:
                sf.v2.get()==20
                ch2="5 KG"
                pric2=190
            sf.addlist(["Wheat",ch2,sf.q2.get(),pric2*int(sf.q2.get())])

        #grocery-3
        sf.c.create_rectangle(110, 290, 1190, 410,width=2)
        sf.pep=PhotoImage(file="toor.png")
        sf.c.create_image(170,350,image=sf.pep)
        sf.c.create_text(310,320,text="Toor Daal",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,320,text="₹110/₹550",fill="#ff3838",font=("cambria",17,'bold'))
        #ch3=sf.check(sf.vegf2,340)
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.vegf2,text = "1 KG",value=10,variable=sf.v3)
        sf.C31.place(x=250,y=340)
        sf.C32 = Radiobutton(sf.vegf2, text = "5 KG",value = 20, variable =sf.v3)
        sf.C32.place(x=350,y=340)
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.c.create_text(290,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty3=Entry(sf.vegf2,textvariable=sf.q3,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty3.place(x=350,y=380)
        sf.add3=Button(sf.vegf2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add3.place(x=450,y=360)
        def addch3():
            if sf.v3.get()==10:
                ch3="1 KG"
                pric3=110
            else:
                sf.v3.get()==20
                ch3="5 KG"
                pric3=550
            sf.addlist(["Toor Daal",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        #grocery-4
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.mag=PhotoImage(file="moong.png")
        sf.c.create_image(170,470,image=sf.mag)
        sf.c.create_text(310,440,text="Mung Dal",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,440,text="₹135/₹675",fill="#ff3838",font=("cambria",17,'bold'))
        #ch4=sf.check(sf.vegf2,460)
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.vegf2,text = "1 KG",value=10,variable=sf.v4)
        sf.C41.place(x=250,y=460)
        sf.C42 = Radiobutton(sf.vegf2, text = "5 KG",value = 20, variable =sf.v4)
        sf.C42.place(x=350,y=460)
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()
        
        sf.c.create_text(290,500,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty4=Entry(sf.vegf2,textvariable=sf.q4,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty4.place(x=350,y=500)
        sf.add4=Button(sf.vegf2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add4.place(x=450,y=480)
        def addch4():
            if sf.v4.get()==10:
                ch4="1 KG"
                pric4=135
            else:
                sf.v4.get()==20
                ch4="5 KG"
                pric4=675
            sf.addlist(["Mung Dal",ch4,sf.q4.get(),pric4*int(sf.q4.get())])

        #grocery-5
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.vhy=PhotoImage(file="salt.png")
        sf.c.create_image(700,110,image=sf.vhy)
        sf.c.create_text(800,80,text="Salt",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,80,text="₹15/₹24",fill="#ff3838",font=("cambria",17,'bold'))
        #ch5=sf.check(sf.vegf2,460)
        sf.v5=IntVar()
        sf.C51=Radiobutton(sf.vegf2,text = "1/2 KG",value=10,variable=sf.v5)
        sf.C51.place(x=780,y=100)
        sf.C52 = Radiobutton(sf.vegf2, text = "1 KG",value = 20, variable =sf.v5)
        sf.C52.place(x=880,y=100)
        sf.C51.select()
        sf.C51.deselect()    
        sf.C51.invoke()
        
        sf.c.create_text(820,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty5=Entry(sf.vegf2,textvariable=sf.q5,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty5.place(x=880,y=140)
        sf.add5=Button(sf.vegf2,text="ADD",command=lambda:addch5(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add5.place(x=980,y=120)
        def addch5():
            if sf.v5.get()==10:
                ch5="Half KG"
                pric5=170
            else:
                sf.v5.get()==20
                ch5="1 KG"
                pric5=230
            sf.addlist(["Salt",ch5,sf.q5.get(),pric5*int(sf.q5.get())])

        #grocery-6
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.aloo=PhotoImage(file="red chilli.png")
        sf.c.create_image(700,230,image=sf.aloo)
        sf.c.create_text(840,200,text="Red Chilli",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,200,text="₹70/₹130",fill="#ff3838",font=("cambria",17,'bold'))
        #ch4=sf.check(sf.vegf2,220)
        sf.v6=IntVar()
        sf.C61=Radiobutton(sf.vegf2,text = "1/2 KG",value=10,variable=sf.v6)
        sf.C61.place(x=780,y=220)
        sf.C62 = Radiobutton(sf.vegf2, text = "1 KG",value = 20, variable =sf.v6)
        sf.C62.place(x=880,y=220)
        sf.C61.select()
        sf.C61.deselect()    
        sf.C61.invoke()
        
        sf.c.create_text(820,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty6=Entry(sf.vegf2,textvariable=sf.q6,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty6.place(x=880,y=260)
        sf.add6=Button(sf.vegf2,text="ADD",command=lambda:addch6(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add6.place(x=980,y=240)
        def addch6():
            if sf.v6.get()==10:
                ch6="1/2 KG"
                pric6=70
            else:
                sf.v6.get()==20
                ch6="1 KG"
                pric6=130
            sf.addlist(["Red Chilli",ch6,sf.q6.get(),pric6*int(sf.q6.get())])

        #grocery-7
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.soya=PhotoImage(file="turm.png")
        sf.c.create_image(700,350,image=sf.soya)
        sf.c.create_text(840,320,text="Turmeric",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,320,text="₹100/₹190",fill="#ff3838",font=("cambria",17,'bold'))
        #ch7=sf.check(sf.vegf2,340)
        sf.v7=IntVar()
        sf.C71=Radiobutton(sf.vegf2,text = "1/2 KG",value=10,variable=sf.v7)
        sf.C71.place(x=780,y=340)
        sf.C72 = Radiobutton(sf.vegf2, text = "1 KG",value = 20, variable =sf.v7)
        sf.C72.place(x=880,y=340)
        sf.C71.select()
        sf.C71.deselect()    
        sf.C71.invoke()
        
        sf.c.create_text(820,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty7=Entry(sf.vegf2,textvariable=sf.q7,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty7.place(x=880,y=380)
        sf.add7=Button(sf.vegf2,text="ADD",command=lambda:addch7(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add7.place(x=980,y=360)
        def addch7():
            if sf.v7.get()==10:
                ch7="1/2 KG"
                pric7=100
            else:
                sf.v7.get()==20
                ch7="1 KG"
                pric7=190
            sf.addlist(["Turmeric",ch7,sf.q7.get(),pric7*int(sf.q7.get())])

        #grocery-8
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.mush=PhotoImage(file="sugar.png")
        sf.c.create_image(700,470,image=sf.mush)
        sf.c.create_text(820,440,text="Sugar",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,440,text="₹20/₹35",fill="#ff3838",font=("cambria",17,'bold'))
        #ch8=sf.check(sf.vegf2,460)
        sf.v8=IntVar()
        sf.C81=Radiobutton(sf.vegf2,text = "1/2 KG",value=10,variable=sf.v8)
        sf.C81.place(x=780,y=460)
        sf.C82 = Radiobutton(sf.vegf2, text = "1 KG",value = 20, variable =sf.v8)
        sf.C82.place(x=880,y=460)
        sf.C81.select()
        sf.C81.deselect()    
        sf.C81.invoke()
        
        sf.c.create_text(820,500,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty8=Entry(sf.vegf2,textvariable=sf.q8,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty8.place(x=880,y=500)
        sf.add8=Button(sf.vegf2,text="ADD",command=lambda:addch8(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add8.place(x=980,y=480)
        def addch8():
            if sf.v8.get()==10:
                ch8="1/2 KG"
                pric8=20
            else:
                sf.v8.get()==20
                ch8="1 KG"
                pric8=35
            sf.addlist(["Sugar",ch8,sf.q8.get(),pric8*int(sf.q8.get())])
            
                    
        sf.con=Button(sf.vegf2,text="Confirm",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.con.place(x=1220,y=250)
        sf.more=Button(sf.vegf2,text="Add More",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.more.place(x=1220,y=350)
        sf.vegf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

##----page 9 ------
    
    def addlist(sf,q):
        if q[-2]!="0" and q[-2].isdigit():
            sf.cartlist.append(q)
            sf.amount=sf.amount+q[-1]
            messagebox.showinfo("Cart","Item Successfully added")
        else:
            messagebox.showinfo("Cart","Enter Valid Quantity to add")
        print(sf.cartlist,sf.amount)

#--  page 10------
    def dairy(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.nonvegf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.nonvegf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="back.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.nonvegf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("cambria",16))
        sf.nonvegf1.pack(fill=BOTH,expand=1)
        sf.nonvegf2=Frame(sf.scr,height=618,width=1366)      
        sf.c=Canvas(sf.nonvegf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.nonvegf2,text="DAIRY PRODUCTS",bg="#9db1f2",font=("Cambria",22))
        sf.log.place(x=580,y=4)
        sf.c.create_rectangle(100, 40, 1200, 540,fill="#d3ede6",outline="white",width=6)
        sf.q9=StringVar()
        sf.q10=StringVar()
        sf.q11=StringVar()
        sf.q12=StringVar()
        sf.q13=StringVar()
        sf.q14=StringVar()
        sf.q15=StringVar()
        sf.q16=StringVar()
        sf.q9.set("0")
        sf.q10.set("0")
        sf.q11.set("0")
        sf.q12.set("0")
        sf.q13.set("0")
        sf.q14.set("0")
        sf.q15.set("0")
        sf.q16.set("0")

        #dairy-1
        sf.c.create_rectangle(110, 50, 1190, 170,width=2)
        sf.delu=PhotoImage(file="milk.png")
        sf.c.create_image(170,110,image=sf.delu)
        sf.c.create_text(275,80,text="Milk",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,80,text="₹30/₹60",fill="#ff3838",font=("cambria",17,'bold'))
        #ch6=sf.check(sf.nonvegf2,100)
        sf.v9=IntVar()
        sf.C91=Radiobutton(sf.nonvegf2,text = "1/2 Litre",value=10,variable=sf.v9)
        sf.C91.place(x=250,y=100)
        sf.C92 = Radiobutton(sf.nonvegf2, text = "1 Litre",value = 20, variable =sf.v9)
        sf.C92.place(x=350,y=100)
        sf.C91.select()
        sf.C91.deselect()    
        sf.C91.invoke()
        sf.c.create_text(290,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty9=Entry(sf.nonvegf2,textvariable=sf.q9,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty9.place(x=350,y=140)
        sf.add9=Button(sf.nonvegf2,text="ADD",command=lambda:addch9(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add9.place(x=450,y=120)
        def addch9():
            if sf.v9.get()==10:
                ch9="Half Litre"
                pric9=30
            else:
                sf.v9.get()==20
                ch9="1 Litre"
                pric9=60
            sf.addlist(["Milk",ch9,sf.q9.get(),pric9*int(sf.q9.get())])

        #dairy-2
        sf.c.create_rectangle(110, 170, 1190, 290,width=2)
        sf.vag=PhotoImage(file="curd.png")
        sf.c.create_image(170,230,image=sf.vag)
        sf.c.create_text(290,200,text="Yogurt",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,200,text="₹18/₹40",fill="#ff3838",font=("cambria",17,'bold'))
        #ch10=sf.check(sf.nonvegf2,220)
        sf.v10=IntVar()
        sf.C101=Radiobutton(sf.nonvegf2,text = "1/2 Litre",value=10,variable=sf.v10)
        sf.C101.place(x=250,y=220)
        sf.C102 = Radiobutton(sf.nonvegf2, text = "1 Litre",value = 20, variable =sf.v10)
        sf.C102.place(x=350,y=220)
        sf.C101.select()
        sf.C101.deselect()    
        sf.C101.invoke()
        sf.c.create_text(290,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty10=Entry(sf.nonvegf2,textvariable=sf.q10,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty10.place(x=350,y=260)
        sf.add10=Button(sf.nonvegf2,text="ADD",command=lambda:addch10(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add10.place(x=450,y=240)
        def addch10():
            if sf.v10.get()==10:
                ch10="Half Litre"
                pric10=18
            else:
                sf.v10.get()==20
                ch10="1 Litre"
                pric10=40
            sf.addlist(["Yogurt",ch10,sf.q10.get(),pric10*int(sf.q10.get())])

        #dairy-3
        sf.c.create_rectangle(110, 290, 1190, 410,width=2)
        sf.pep=PhotoImage(file="bmilk.png")
        sf.c.create_image(170,350,image=sf.pep)
        sf.c.create_text(290,320,text="Chaas",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,320,text="₹10/₹20",fill="#ff3838",font=("cambria",17,'bold'))
        #ch11=sf.check(sf.nonvegf2,340)
        sf.v11=IntVar()
        sf.C111=Radiobutton(sf.nonvegf2,text = "1/2 Litre",value=10,variable=sf.v11)
        sf.C111.place(x=250,y=340)
        sf.C112 = Radiobutton(sf.nonvegf2, text = "1 Litre",value = 20, variable =sf.v11)
        sf.C112.place(x=350,y=340)
        sf.C111.select()
        sf.C111.deselect()    
        sf.C111.invoke()
        sf.c.create_text(290,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty11=Entry(sf.nonvegf2,textvariable=sf.q11,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty11.place(x=350,y=380)
        sf.add11=Button(sf.nonvegf2,text="ADD",command=lambda:addch11(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add11.place(x=450,y=360)
        def addch11():
            if sf.v11.get()==10:
                ch11="Half Litre"
                pric11=10
            else:
                sf.v11.get()==20
                ch11="1 Litre"
                pric11=20
            sf.addlist(["Chaas",ch11,sf.q11.get(),pric11*int(sf.q11.get())])
            
        #dairy-4
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.mag=PhotoImage(file="lassi.png")
        sf.c.create_image(170,470,image=sf.mag)
        sf.c.create_text(270,440,text="Lassi",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,440,text="₹20/₹40",fill="#ff3838",font=("cambria",17,'bold'))
        #ch12=sf.check(sf.nonvegf2,460)
        sf.v12=IntVar()
        sf.C121=Radiobutton(sf.nonvegf2,text = "1/2 Litre",value=10,variable=sf.v12)
        sf.C121.place(x=250,y=460)
        sf.C122 = Radiobutton(sf.nonvegf2, text = "1 Litre",value = 20, variable =sf.v12)
        sf.C122.place(x=350,y=460)
        sf.C121.select()
        sf.C121.deselect()    
        sf.C121.invoke()
        
        sf.c.create_text(290,500,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty12=Entry(sf.nonvegf2,textvariable=sf.q12,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty12.place(x=350,y=500)
        sf.add12=Button(sf.nonvegf2,text="ADD",command=lambda:addch12(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add12.place(x=450,y=480)
        def addch12():
            if sf.v12.get()==10:
                ch12="Half Litre"
                pric12=20
            else:
                sf.v12.get()==20
                ch12="1 Litre"
                pric12=40
            sf.addlist(["Lassi",ch12,sf.q12.get(),pric12*int(sf.q12.get())])

        #dairy-5
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.afg=PhotoImage(file="butter.png")
        sf.c.create_image(700,110,image=sf.afg)
        sf.c.create_text(820,80,text="Butter",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,80,text="₹105/₹210",fill="#ff3838",font=("cambria",17,'bold'))
        #ch13=sf.check(sf.nonvegf2,460)
        sf.v13=IntVar()
        sf.C131=Radiobutton(sf.nonvegf2,text = "1/2 KG",value=10,variable=sf.v13)
        sf.C131.place(x=780,y=100)
        sf.C132 = Radiobutton(sf.nonvegf2, text = "1 KG",value = 20, variable =sf.v13)
        sf.C132.place(x=880,y=100)
        sf.C131.select()
        sf.C131.deselect()    
        sf.C131.invoke()
        
        sf.c.create_text(820,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty13=Entry(sf.nonvegf2,textvariable=sf.q13,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty13.place(x=880,y=140)
        sf.add13=Button(sf.nonvegf2,text="ADD",command=lambda:addch13(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add13.place(x=980,y=120)
        def addch13():
            if sf.v13.get()==10:
                ch13="Half KG"
                pric13=105
            else:
                sf.v13.get()==20
                ch12="1 KG"
                pric13=210
            sf.addlist(["Butter",ch13,sf.q13.get(),pric13*int(sf.q13.get())])

        #dairy-6
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.tangdi=PhotoImage(file="cheese.png")
        sf.c.create_image(700,230,image=sf.tangdi)
        sf.c.create_text(820,200,text="Cheese",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,200,text="₹230/₹500",fill="#ff3838",font=("cambria",17,'bold'))
        #ch14=sf.check(sf.nonvegf2,220)
        sf.v14=IntVar()
        sf.C141=Radiobutton(sf.nonvegf2,text = "1/2 KG",value=10,variable=sf.v14)
        sf.C141.place(x=780,y=220)
        sf.C142 = Radiobutton(sf.nonvegf2, text = "1 KG",value = 20, variable =sf.v14)
        sf.C142.place(x=880,y=220)
        sf.C141.select()
        sf.C141.deselect()    
        sf.C141.invoke()
        
        sf.c.create_text(820,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty14=Entry(sf.nonvegf2,textvariable=sf.q14,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty14.place(x=880,y=260)
        sf.add14=Button(sf.nonvegf2,text="ADD",command=lambda:addch14(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add14.place(x=980,y=240)
        def addch14():
            if sf.v14.get()==10:
                ch14="Half KG"
                pric14=230
            else:
                sf.v14.get()==20
                ch14="1 KG"
                pric14=290
            sf.addlist(["Cheese",ch14,sf.q14.get(),pric14*int(sf.q14.get())])

        #dairy-7
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.soya=PhotoImage(file="paneer.png")
        sf.c.create_image(700,350,image=sf.soya)
        sf.c.create_text(820,320,text="Paneer",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,320,text="₹140/₹270",fill="#ff3838",font=("cambria",17,'bold'))
        #ch15=sf.check(sf.nonvegf2,340)
        sf.v15=IntVar()
        sf.C151=Radiobutton(sf.nonvegf2,text = "1/2 KG",value=10,variable=sf.v15)
        sf.C151.place(x=780,y=340)
        sf.C152 = Radiobutton(sf.nonvegf2, text = "1 KG",value = 20, variable =sf.v15)
        sf.C152.place(x=880,y=340)
        sf.C151.select()
        sf.C151.deselect()    
        sf.C151.invoke()
        
        sf.c.create_text(820,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty15=Entry(sf.nonvegf2,textvariable=sf.q15,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty15.place(x=880,y=380)
        sf.add15=Button(sf.nonvegf2,text="ADD",command=lambda:addch15(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add15.place(x=980,y=360)
        def addch15():
            if sf.v15.get()==10:
                ch15="Half KG"
                pric15=140
            else:
                sf.v15.get()==20
                ch15="1 KG"
                pric15=270
            sf.addlist(["Paneer",ch15,sf.q15.get(),pric15*int(sf.q15.get())])

        #dairy-8
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.praw=PhotoImage(file="shri.png")
        sf.c.create_image(700,470,image=sf.praw)
        sf.c.create_text(840,440,text="Shrikhand",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,440,text="₹125/₹260",fill="#ff3838",font=("cambria",17,'bold'))
        #ch16=sf.check(sf.nonvegf2,460)
        sf.v16=IntVar()
        sf.C161=Radiobutton(sf.nonvegf2,text = "1/2 KG",value=10,variable=sf.v16)
        sf.C161.place(x=780,y=460)
        sf.C162 = Radiobutton(sf.nonvegf2, text = "1 KG",value = 20, variable =sf.v16)
        sf.C162.place(x=880,y=460)
        sf.C161.select()
        sf.C161.deselect()    
        sf.C161.invoke()
        
        sf.c.create_text(820,500,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty16=Entry(sf.nonvegf2,textvariable=sf.q16,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty16.place(x=880,y=500)
        sf.add16=Button(sf.nonvegf2,text="ADD",command=lambda:addch16(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add16.place(x=980,y=480)
        def addch16():
            if sf.v16.get()==10:
                ch16="Half KG"
                pric16=125
            else:
                sf.v16.get()==20
                ch16="1 KG"
                pric16=260
            sf.addlist(["Shrikhand",ch16,sf.q16.get(),pric16*int(sf.q16.get())])

        sf.con=Button(sf.nonvegf2,text="Confirm",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.con.place(x=1220,y=250)
        sf.more=Button(sf.nonvegf2,text="Add More",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.more.place(x=1220,y=350)
        sf.nonvegf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 11------
    def snacks(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.bevf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.bevf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.bevf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("cambria",16))
        sf.bevf1.pack(fill=BOTH,expand=1)
        sf.bevf2=Frame(sf.scr,height=618,width=1366)   
        sf.c=Canvas(sf.bevf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.bevf2,text="SNACKS",bg="#9db1f2",font=("Cambria",22))
        sf.log.place(x=520,y=4)
        sf.c.create_rectangle(100, 40, 1200, 540,fill="#d3ede6",outline="white",width=6)
        sf.q25=StringVar()
        sf.q26=StringVar()
        sf.q27=StringVar()
        sf.q28=StringVar()
        sf.q29=StringVar()
        sf.q30=StringVar()
        sf.q31=StringVar()
        sf.q32=StringVar()
        sf.q25.set("0")
        sf.q26.set("0")
        sf.q27.set("0")
        sf.q28.set("0")
        sf.q29.set("0")
        sf.q30.set("0")
        sf.q31.set("0")
        sf.q32.set("0")

        #snacks-1
        sf.c.create_rectangle(110, 50, 1190, 170,width=2)
        sf.thup=PhotoImage(file="lays.png")
        sf.c.create_image(170,110,image=sf.thup)
        sf.c.create_text(275,80,text="Lays",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,80,text="₹10/₹20",fill="#ff3838",font=("cambria",17,'bold'))
        #ch25=sf.check(sf.bevf2,100)
        sf.v25=IntVar()
        sf.C251=Radiobutton(sf.bevf2,text = "30gms",value=10,variable=sf.v25)
        sf.C251.place(x=250,y=100)
        sf.C252 = Radiobutton(sf.bevf2, text = "52gms",value = 20, variable =sf.v25)
        sf.C252.place(x=350,y=100)
        sf.C251.select()
        sf.C251.deselect()    
        sf.C251.invoke()
        sf.c.create_text(290,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty25=Entry(sf.bevf2,textvariable=sf.q25,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty25.place(x=350,y=140)
        sf.add25=Button(sf.bevf2,text="ADD",command=lambda:addch25(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add25.place(x=450,y=120)
        def addch25():
            if sf.v25.get()==10:
                ch25="30gms"
                pric25=10
            else:
                sf.v25.get()==20
                ch25="52gms"
                pric25=20
            sf.addlist(["Lays",ch25,sf.q25.get(),pric25*int(sf.q25.get())])

        #snacks-2
        sf.c.create_rectangle(110, 170, 1190, 290,width=2)
        sf.peps=PhotoImage(file="kurkure.png")
        sf.c.create_image(170,230,image=sf.peps)
        sf.c.create_text(295,200,text="Kurkure",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,200,text="₹10/₹20",fill="#ff3838",font=("cambria",17,'bold'))
        #ch26=sf.check(sf.bevf2,220)
        sf.v26=IntVar()
        sf.C261=Radiobutton(sf.bevf2,text = "50gms",value=10,variable=sf.v26)
        sf.C261.place(x=250,y=220)
        sf.C262 = Radiobutton(sf.bevf2, text = "140gms",value = 20, variable =sf.v26)
        sf.C262.place(x=350,y=220)
        sf.C261.select()
        sf.C261.deselect()    
        sf.C261.invoke()
        sf.c.create_text(290,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty26=Entry(sf.bevf2,textvariable=sf.q26,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty26.place(x=350,y=260)
        sf.add26=Button(sf.bevf2,text="ADD",command=lambda:addch26(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add26.place(x=450,y=240)
        def addch26():
            if sf.v26.get()==10:
                ch26="50gms"
                pric26=10
            else:
                sf.v26.get()==20
                ch26="140gms"
                pric26=20
            sf.addlist(["Kurkure",ch26,sf.q26.get(),pric26*int(sf.q26.get())])

        #snacks-3
        sf.c.create_rectangle(110, 290, 1190, 410,width=2)
        sf.coca=PhotoImage(file="parle.png")
        sf.c.create_image(170,350,image=sf.coca)
        sf.c.create_text(295,320,text="Parle-G",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,320,text="₹10/₹20",fill="#ff3838",font=("cambria",17,'bold'))
        #ch27=sf.check(sf.bevf2,340)
        sf.v27=IntVar()
        sf.C271=Radiobutton(sf.bevf2,text = "100gms",value=10,variable=sf.v27)
        sf.C271.place(x=250,y=340)
        sf.C272 = Radiobutton(sf.bevf2, text = "250gms",value = 20, variable =sf.v27)
        sf.C272.place(x=350,y=340)
        sf.C271.select()
        sf.C271.deselect()    
        sf.C271.invoke()
        sf.c.create_text(290,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty27=Entry(sf.bevf2,textvariable=sf.q27,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty27.place(x=350,y=380)
        sf.add27=Button(sf.bevf2,text="ADD",command=lambda:addch27(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add27.place(x=450,y=360)
        def addch27():
            if sf.v27.get()==10:
                ch27="100gms"
                pric27=10
            else:
                sf.v27.get()==20
                ch27="250gms"
                pric27=20
            sf.addlist(["Parle-G",ch27,sf.q27.get(),pric27*int(sf.q27.get())])

        #snacks-4
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.sprit=PhotoImage(file="bourbon.png")
        sf.c.create_image(170,470,image=sf.sprit)
        sf.c.create_text(295,440,text="Bourbon",fill="#000000",font=("Cambria",20))
        sf.c.create_text(570,440,text="₹10/₹20",fill="#ff3838",font=("cambria",17,'bold'))
        #ch28=sf.check(sf.bevf2,460)
        sf.v28=IntVar()
        sf.C281=Radiobutton(sf.bevf2,text = "50gms",value=10,variable=sf.v28)
        sf.C281.place(x=250,y=460)
        sf.C282 = Radiobutton(sf.bevf2, text = "100gms",value = 20, variable =sf.v28)
        sf.C282.place(x=350,y=460)
        sf.C281.select()
        sf.C281.deselect()    
        sf.C281.invoke()     
        sf.c.create_text(290,500,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty28=Entry(sf.bevf2,textvariable=sf.q28,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty28.place(x=350,y=500)
        sf.add28=Button(sf.bevf2,text="ADD",command=lambda:addch28(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add28.place(x=450,y=480)
        def addch28():
            if sf.v28.get()==10:
                ch28="50gms"
                pric28=10
            else:
                sf.v28.get()==20
                ch28="100gms"
                pric28=20
            sf.addlist(["Bourbon",ch28,sf.q28.get(),pric28*int(sf.q28.get())])

        #snacks-5
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.seup=PhotoImage(file="kitkat.png")
        sf.c.create_image(700,110,image=sf.seup)
        sf.c.create_text(820,80,text="KitKat",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,80,text="₹20/₹100",fill="#ff3838",font=("cambria",17,'bold'))
        #ch29=sf.check(sf.bevf2,460)
        sf.v29=IntVar()
        sf.C291=Radiobutton(sf.bevf2,text = "42gms",value=10,variable=sf.v29)
        sf.C291.place(x=780,y=100)
        sf.C292 = Radiobutton(sf.bevf2, text = "400gms",value = 20, variable =sf.v29)
        sf.C292.place(x=880,y=100)
        sf.C291.select()
        sf.C291.deselect()    
        sf.C291.invoke()      
        sf.c.create_text(820,150,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty29=Entry(sf.bevf2,textvariable=sf.q29,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty29.place(x=880,y=140)
        sf.add29=Button(sf.bevf2,text="ADD",command=lambda:addch29(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add29.place(x=980,y=120)
        def addch29():
            if sf.v29.get()==10:
                ch29="42gms"
                pric29=20
            else:
                sf.v29.get()==20
                ch29="400gms"
                pric29=100
            sf.addlist(["KitKat",ch29,sf.q29.get(),pric29*int(sf.q29.get())])

        #snacks-6
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.fan=PhotoImage(file="aloo.png")
        sf.c.create_image(700,230,image=sf.fan)
        sf.c.create_text(840,200,text="Aloo Bhujia",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,200,text="₹20/₹90",fill="#ff3838",font=("cambria",17,'bold'))
        #ch30=sf.check(sf.bevf2,220)
        sf.v30=IntVar()
        sf.C301=Radiobutton(sf.bevf2,text = "27gms",value=10,variable=sf.v30)
        sf.C301.place(x=780,y=220)
        sf.C302 = Radiobutton(sf.bevf2, text = "126gms",value = 20, variable =sf.v30)
        sf.C302.place(x=880,y=220)
        sf.C301.select()
        sf.C301.deselect()    
        sf.C301.invoke()
        sf.c.create_text(820,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty30=Entry(sf.bevf2,textvariable=sf.q30,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty30.place(x=880,y=260)
        sf.add30=Button(sf.bevf2,text="ADD",command=lambda:addch30(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add30.place(x=980,y=240)
        def addch30():
            if sf.v30.get()==10:
                ch30="27gms"
                pric30=10
            else:
                sf.v30.get()==20
                ch30="126gms"
                pric30=90
            sf.addlist(["Aloo Bhujia",ch30,sf.q30.get(),pric30*int(sf.q30.get())])

        #snacks-7
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.mir=PhotoImage(file="laxmi.png")
        sf.c.create_image(700,350,image=sf.mir)
        sf.c.create_text(820,320,text="Chiwda",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,320,text="₹90/₹190",fill="#ff3838",font=("cambria",17,'bold'))
        #ch31=sf.check(sf.bevf2,220)
        sf.v31=IntVar()
        sf.C311=Radiobutton(sf.bevf2,text = "250gms",value=10,variable=sf.v31)
        sf.C311.place(x=780,y=340)
        sf.C312 = Radiobutton(sf.bevf2, text = "500gms",value = 20, variable =sf.v31)
        sf.C312.place(x=880,y=340)
        sf.C311.select()
        sf.C311.deselect()    
        sf.C311.invoke()
        sf.c.create_text(820,390,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty31=Entry(sf.bevf2,textvariable=sf.q31,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty31.place(x=880,y=380)
        sf.add31=Button(sf.bevf2,text="ADD",command=lambda:addch31(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add31.place(x=980,y=360)
        def addch31():
            if sf.v31.get()==10:
                ch31="250gms"
                pric31=90
            else:
                sf.v31.get()==20
                ch31="500gms"
                pric31=190
            sf.addlist(["Chiwda",ch31,sf.q31.get(),pric31*int(sf.q31.get())])

        #snacks-8
        sf.c.create_rectangle(110, 410, 1190, 530,width=2)
        sf.limc=PhotoImage(file="chitale.png")
        sf.c.create_image(700,470,image=sf.limc)
        sf.c.create_text(850,440,text="Bhakarwadi",fill="#000000",font=("Cambria",20))
        sf.c.create_text(1110,440,text="₹90/₹190",fill="#ff3838",font=("cambria",17,'bold'))
        #ch32=sf.check(sf.bevf2,460)
        sf.v32=IntVar()
        sf.C321=Radiobutton(sf.bevf2,text = "250gms",value=10,variable=sf.v32)
        sf.C321.place(x=780,y=460)
        sf.C322 = Radiobutton(sf.bevf2, text = "500gms",value = 20, variable =sf.v32)
        sf.C322.place(x=880,y=460)
        sf.C321.select()
        sf.C321.deselect()    
        sf.C321.invoke()
        sf.c.create_text(820,270,text="Quantity : ",fill="#000000",font=("cambria",12))
        sf.qty32=Entry(sf.bevf2,textvariable=sf.q32,bg="#aae2d7",font=("cambria",12),width=4,)
        sf.qty32.place(x=880,y=500)
        sf.add32=Button(sf.bevf2,text="ADD",command=lambda:addch32(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("cambria",12,'bold'))
        sf.add32.place(x=980,y=460)
        def addch32():
            if sf.v32.get()==10:
                ch32="250gms"
                pric32=90
            else:
                sf.v32.get()==20
                ch32="500gms"
                pric32=190
            sf.addlist(["Limca",ch32,sf.q32.get(),pric32*int(sf.q32.get())])

        sf.con=Button(sf.bevf2,text="Confirm",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.con.place(x=1220,y=250)
        sf.more=Button(sf.bevf2,text="Add More",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.more.place(x=1220,y=350)
        sf.bevf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
        
#--  page 12------
    def Address(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Online Grocery System")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.addf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.addf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.out=Button(sf.addf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",font=("cambria",16))
        sf.out.place(x=1200,y=100)
        sf.addf1.pack(fill=BOTH,expand=1)

        sf.addf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.addf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.addf2,text="Address",fg="white",bg="#0b1335",width=20,font=("cambria",27))
        sf.log.place(x=480,y=110)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.lab1=Label(sf.addf2,text="City",bg="#d3ede6",font=("Cambria",18))
        sf.lab1.place(x=190,y=200)
        sf.city=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.city.place(x=430,y=200)
        sf.lab2=Label(sf.addf2,text="Locality",bg="#d3ede6",font=("Cambria",18))
        sf.lab2.place(x=730,y=200)
        sf.loc=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.loc.place(x=918,y=200)
        sf.lab3=Label(sf.addf2,text="Building Name",bg="#d3ede6",font=("Cambria",18))
        sf.lab3.place(x=190,y=250)
        sf.buil=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.buil.place(x=430,y=250)
        sf.lab4=Label(sf.addf2,text="House No.",bg="#d3ede6",font=("Cambria",18))
        sf.lab4.place(x=730,y=250)
        sf.hou=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.hou.place(x=918,y=250)
        sf.lab5=Label(sf.addf2,text="Landmark",bg="#d3ede6",font=("Cambria",18))
        sf.lab5.place(x=190,y=300)
        sf.lan=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.lan.place(x=430,y=300)
        sf.lab6=Label(sf.addf2,text="Name",bg="#d3ede6",font=("Cambria",18))
        sf.lab6.place(x=730,y=300)
        sf.name=Entry(sf.addf2,bg="white",width=15,font=("cambria",18),bd=5)
        sf.name.place(x=918,y=300)
        sf.bc=Button(sf.addf2,text="Back",command=lambda:sf.Orderde(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("cambria",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.addf2,text="Order Now",command=lambda:sf.orderpay(sf.x),cursor="hand2",fg="white",bg="#0b1335",font=("cambria",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.city.delete(0,END)
            sf.loc.delete(0,END)
            sf.buil.delete(0,END)
            sf.hou.delete(0,END)
            sf.lan.delete(0,END)
            sf.name.delete(0,END)
        sf.cl=Button(sf.addf2,text="Clear",command=lambda:clear(sf),cursor="hand2",fg="white",bg="#0b1335",font=("cambria",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.addf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

        
#--  page 13------
    def Orderde(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Avenue Supermarket")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.ordf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.ordf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="upp.png")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.ordf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("cambria",16))
        sf.ordf1.pack(fill=BOTH,expand=1)
        
        sf.ordf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.ordf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="back.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.ordf2,text="YOUR ORDER",bg="#9db1f2",font=("Cambria",22))
        sf.log.place(x=450,y=4)
        sf.c.create_rectangle(150, 50, 1000, 500,fill="#d3ede6",outline="white",width=6)
        sf.amt=sf.amount
        sf.text="Total : "+str(sf.amt)
        sf.tot=Label(sf.ordf2,text=sf.text,bg="#f2da9d",width=12,font=("Cambria",22))
        sf.tot.place(x=1100,y=200)
        if sf.x=="deli":
            sf.y=sf.Address
        if sf.x=="pick":
            sf.y=sf.orderpay
        sf.pay=Button(sf.ordf2,text="Pay",command=lambda:sf.y(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.pay.place(x=1100,y=250)
        sf.exi=Button(sf.ordf2,text="Add more",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cambria",18,'bold'))
        sf.exi.place(x=1100,y=300)
        sf.c.create_text(600,80,text="Item\t\tSize\t\tQuantity\t\tPrice",font=("Cambria",18))
        sf.c.create_text(500,90,text="_____________________________________________________________________________",font=("Cambria",18))
        y=100
        for i in sf.cartlist:
            y+=30
            s=i[0]+"\t\t\t"+i[1]+"\t"+i[2]+"\t\t"+str(i[3])
            sf.c.create_text(605,y,text=s,font=("cambria",16))
            
        sf.ordf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

 #-----  database-------               
    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("grocery.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome to the Online Grocery System")            
            sf.birmain()

    def Regdatabase(sf):
        sf.credreg=sf.resultreg()
        sf.con=connect("grocery.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and mob=%r "%(sf.credreg[0],sf.credreg[5]))
        if list(x)[0][0]==0:
            if sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2],sf.credreg[3],sf.credreg[4],sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")

    def admindatabase(sf):
        sf.credadm=sf.resultadmin()
        sf.con=connect("grocery.db")
        sf.cur=sf.con.cursor()
        x=sf.cur.execute("select count(*) from admin where username=%r and password=%r"%(sf.credadm[0],sf.credadm[1]))
        if list(x)[0][0]==0:
            if sf.credadm[0]=="" or sf.credadm[1]=="":
                messagebox.showinfo("Admin","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Admin","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Admin","You have Successfully Log In")            
            sf.adminmain()

    def adminorderdetail(sf):
        sf.credadmord=sf.resultadminorder()
        if sf.money!=0 and sf.credadmord[0]!="" and sf.credadmord[1]!="":
            if messagebox.askyesno("Pay","Want to make payment"):
                sf.con=connect("grocery.db")
                sf.cur=sf.con.cursor()
                od=[]
                try:
                    sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                except:
                    pass
                for i in sf.credadmord[3:]:
                    if i[-1]!="0":
                        od.append(i)
                a=sf.credadmord[0]
                b=sf.credadmord[1]
                print(a,b,str(sf.money),od)
                s="insert into orderdetail(name,mobile,money,orderdet) values(%r,%r,%r,%r)"%(a,b,str(sf.money),str(od))
                sf.cur.execute(s)
                sf.con.commit()
                messagebox.showinfo("Pay","Successfully Paid")
        else:
            messagebox.showinfo("Pay","Enter Customer's Name and Mobile No  and  Order Something")
    #except:
         #   messagebox.showinfo("Pay","Enter Total button then Pay button")
    def orderpay(sf,x):
        
        messagebox.showinfo("Pay","Cash on Delivery")
        
x=Grocery()
x.main()
