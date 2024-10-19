import customtkinter as tk
from tkinter import messagebox as mbx
from tkinter.simpledialog import askstring as ast

revisite = "Thankyou for shopping and please visit again!!"

amount = 0
total_bill = 0
t_cash = 0
total = 0

root = tk.CTk()
root.config(height=600,width=950)
root.resizable(False,False)

def a(t_cash,total,amount):
        if total <= 0:
            temp_variable_1 = f'''
            Total money entered : {t_cash}
            Total bill          : {t_cash-total}
            Your change         : {total}\n{revisite}
            '''
            mbx.showinfo("vending machine",temp_variable_1)
            root.destroy()
        else:
             x = mbx.askyesno("vending machine",f"You still have {total}\nDo you want to continue?")
             if x:
                  pass
             else:
                    temp_variable_1 = f'''
                    Total money entered : {t_cash}
                    Total bill          : {t_cash-total}
                    Your change         : {total}\n{revisite}
                    '''
                    mbx.showinfo("vending machine",temp_variable_1)
                    root.destroy()
        
class main:
    def __init__(self) :
         self.amount = amount
         self.total_bill = total_bill
         self.t_cash = t_cash
         self.total = total
         self.cash = 0
         exit_button = tk.CTkButton(master=root,text="Exit",command=lambda:a(self.t_cash,self.total,amount),\
                                    font=("Roboto",16,"bold"),fg_color="red")
         exit_button.place(x=300,y=400)

    def chocolate(self):
            try:
                self.amount = int(money_entery.get())
                self.total += self.amount
                self.t_cash += self.amount
            except:
                 pass
            money_entery.delete("0","end")
            total_money_label.configure(text=f"Remaining money {self.total}")
            bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")


            if self.total > 10:
                mbx.showinfo("vending machine","You got chocolate!!")
                self.total -= 10
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total == 10:
                mbx.showinfo("vending machine","You got chocolate!!")
                self.total -= 10
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total < 10:
                mbx.showwarning("vending machine","Insuficient money!!")
                ch = mbx.askyesno("vending machine","Do you want any item?")
                if not ch:
                    a(self.t_cash,self.total,self.amount)
                else:
                     mbx.showinfo("vending machine",f"Then enter {10-self.total}rs")



    def chips(self):
            try:
                self.amount = int(money_entery.get())
                self.total += self.amount
                self.t_cash += self.amount
            except:
                 pass
            money_entery.delete("0","end")
            total_money_label.configure(text=f"Remaining money {self.total}")
            bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")


            if self.total > 20:
                mbx.showinfo("vending machine","You got chips!!")
                self.total -= 20
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total == 20:
                mbx.showinfo("vending machine","You got chips!!")
                self.total -= 20
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total < 20:
                mbx.showwarning("vending machine","Insuficient money!!")
                ch = mbx.askyesno("vending machine","Do you want any item?")
                if not ch:
                    a(self.t_cash,self.total,self.amount)
                else:
                     mbx.showinfo("vending machine",f"Then enter {20-self.total}rs")



    def milkshake(self):
            try:
                self.amount = int(money_entery.get())
                self.total += self.amount
                self.t_cash += self.amount
            except:
                 pass
            money_entery.delete("0","end")
            total_money_label.configure(text=f"Remaining money {self.total}")
            bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")


            if self.total > 30:
                mbx.showinfo("vending machine","You got milkshake!!")
                self.total -= 30
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total == 30:
                mbx.showinfo("vending machine","You got milkshake!!")
                self.total -= 30
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total < 30:
                mbx.showwarning("vending machine","Insuficient money!!")
                ch = mbx.askyesno("vending machine","Do you want any item?")
                if not ch:
                    a(self.t_cash,self.total,self.amount)
                else:
                     mbx.showinfo("vending machine",f"Then enter {30-self.total}rs")



    def water(self):
            try:
                self.amount = int(money_entery.get())
                self.total += self.amount
                self.t_cash += self.amount
            except:
                 pass
            money_entery.delete("0","end")
            total_money_label.configure(text=f"Remaining money {self.total}")
            bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")


            if self.total > 15:
                mbx.showinfo("vending machine","You got water!!")
                self.total -= 15
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total == 15:
                mbx.showinfo("vending machine","You got water!!")
                self.total -= 15
                total_money_label.configure(text=f"Remaining money {self.total}")
                bill_money_label.configure(text=f"Your total bill {self.t_cash-self.total}")
                

            elif self.total < 15:
                mbx.showwarning("vending machine","Insuficient money!!")
                ch = mbx.askyesno("vending machine","Do you want any item?")
                if not ch:
                    a(self.t_cash,self.total,self.amount)
                else:
                     mbx.showinfo("vending machine",f"Then enter {15-self.total}rs")


m = main()

total_money_label = tk.CTkLabel(master=root,text=f"Remaining money {amount}",font=("monserrat",16,"bold"))
total_money_label.place(x=15,y=10)

bill_money_label = tk.CTkLabel(master=root,text=f"Your total bill {total_bill}",font=("monserrat",16,"bold"))
bill_money_label.place(x=600,y=10)

label_info = tk.CTkLabel(master=root,text="Enter the money",font=("monserrat",16,"bold"))
label_info.place(x=309,y=75)

money_entery = tk.CTkEntry(master=root,font=("monserrat",16),justify="center")
money_entery.place(x=300,y=120)


chocolate_button = tk.CTkButton(master=root,text="chocolate 10rs",command=m.chocolate,font=("Roboto",16,"bold"))
chocolate_button.place(x=100,y=200)

chips_button = tk.CTkButton(master=root,text="chips 20rs",command=m.chips,font=("Roboto",16,"bold"))
chips_button.place(x=525,y=200)

milkshake_button = tk.CTkButton(master=root,text="milkshake 30rs",command=m.milkshake,font=("Roboto",16,"bold"))
milkshake_button.place(x=100,y=280)

water_button = tk.CTkButton(master=root,text="water 15rs",command=m.water,font=("Roboto",16,"bold"))
water_button.place(x=525,y=280)

root.mainloop()