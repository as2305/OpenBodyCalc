from customtkinter import *

app = CTk()
app.geometry("600x600")
app.title("OpenBodyCalc")

tabview = CTkTabview(master=app)

tabview.pack(fill = BOTH, expand = True)

tabview.add("BMI")
tabview.add("HRMax")
tabview.add("Tab 3")


#BMI
def test():
    bmi_calculation = float(weight1.get()) / (float(height1.get())*float(height1.get()))
    bmi.configure(text="Your BMI is "+str(bmi_calculation))

label1 = CTkLabel(master=tabview.tab("BMI"), text="BMI")
label1.place(relx=0.5, rely=0.3, anchor="center")

height1 = CTkEntry(master=tabview.tab("BMI"), placeholder_text="Height in meter")
height1.place(relx=0.5, rely=0.4, anchor="center")

weight1 = CTkEntry(master=tabview.tab("BMI"), placeholder_text="Weight in kgs")
weight1.place(relx=0.5, rely=0.5, anchor="center")

calculate1 = CTkButton(master=tabview.tab("BMI"), text="Calculate", command=test)
calculate1.place(relx=0.5, rely=0.6, anchor="center")

bmi = CTkLabel(master=tabview.tab("BMI"), text=None)
bmi.place(relx=0.5, rely=0.7, anchor="center")

#HRMax
def CalcHRMax():
    hrc = 220 - int(age.get())
    hrm.configure(text=hrc)


label2 = CTkLabel(master=tabview.tab("HRMax"), text="Heart Rate Max")
label2.place(relx=0.5, rely=0.3, anchor="center")
age = CTkEntry(master=tabview.tab("HRMax"), placeholder_text="Age")
age.place(relx=0.5, rely=0.4, anchor="center")
calculate2 = CTkButton(master=tabview.tab("HRMax"), text="Calculate", command=CalcHRMax) 
calculate2.place(relx=0.5, rely=0.6, anchor="center")
hrm = CTkLabel(master=tabview.tab("HRMax"), text=None)
hrm.place(relx=0.5, rely=0.7, anchor="center")
app.mainloop()