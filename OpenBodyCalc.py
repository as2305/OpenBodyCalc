from customtkinter import *

app = CTk()
app.geometry("600x600")
app.title("OpenBodyCalc")

tabview = CTkTabview(master=app)

#theme
set_default_color_theme("green")
set_appearance_mode("light")

tabview.pack(fill = BOTH, expand = True)

tabview.add("BMI")
tabview.add("BMR")
tabview.add("HRMAX")
tabview.add("VO2MAX")
tabview.add("About")
tabview.add("Settings")


#BMI
def CalcBMI():
    bmi_calculation = float(weight1.get()) / (float(height1.get())*float(height1.get()))
    bmi.configure(text="Your BMI is "+str(round(bmi_calculation, 1)))
    if bmi_calculation <= 18.5:
        bmi_indicator.configure(text="UNDERWEIGHT", text_color="blue")
    elif bmi_calculation <= 24.9:
        bmi_indicator.configure(text="HEALTHY", text_color="green")
    elif bmi_calculation <= 29.9:
        bmi_indicator.configure(text="OVERWEIGHT", text_color="orange")
    elif bmi_calculation > 30:
        bmi_indicator.configure(text="OBESE", text_color="red")

label1 = CTkLabel(master=tabview.tab("BMI"), text="BMI")
label1.place(relx=0.5, rely=0.3, anchor="center")

height1 = CTkEntry(master=tabview.tab("BMI"), placeholder_text="Height (meters)")
height1.place(relx=0.5, rely=0.4, anchor="center")

weight1 = CTkEntry(master=tabview.tab("BMI"), placeholder_text="Weight (kgs)")
weight1.place(relx=0.5, rely=0.5, anchor="center")

calculate1 = CTkButton(master=tabview.tab("BMI"), text="Calculate", command=CalcBMI)
calculate1.place(relx=0.5, rely=0.6, anchor="center")

bmi = CTkLabel(master=tabview.tab("BMI"), text=None)
bmi.place(relx=0.5, rely=0.7, anchor="center")

bmi_indicator = CTkLabel(master=tabview.tab("BMI"), text=None)
bmi_indicator.place(relx=0.5, rely=0.8, anchor="center")

#BMR

def calcBmr():
    gender_value = bmr_gender.get()
    if gender_value == 1:
        val = ((10*int(bmr_weight.get())) + (6.25*int(bmr_height.get())) - (5*int(bmr_age.get())) + 5)
        bmrOutput.configure(text=str(val)+" calories")
    elif gender_value == 2:
        val = ((10*int(bmr_weight.get())) + (6.25*int(bmr_height.get())) - (5*int(bmr_age.get())) - 161)
        bmrOutput.configure(text=str(val)+" calories")

bmr_label = CTkLabel(master=tabview.tab("BMR"), text="Basal Metabolic Rate")
bmr_age = CTkEntry(master=tabview.tab("BMR"), placeholder_text="Age")
bmr_gender = IntVar(value=0)
male_1 = CTkRadioButton(master=tabview.tab("BMR"), text="Male", variable= bmr_gender, value=1)
female_2 = CTkRadioButton(master=tabview.tab("BMR"), text="Female", variable= bmr_gender, value=2)
bmr_height = CTkEntry(master=tabview.tab("BMR"), placeholder_text=("Height in cm"))
bmr_weight = CTkEntry(master=tabview.tab("BMR"), placeholder_text=("Weight in kgs"))
calcBmrButton = CTkButton(master=tabview.tab("BMR"), text="Calculate", command=calcBmr)
bmrOutput = CTkLabel(master=tabview.tab("BMR"), text=None)

bmr_label.place(relx=0.5, rely=0.3, anchor="center")
bmr_age.place(relx=0.5, rely=0.4, anchor="center")
male_1.place(relx=0.5, rely=0.5, anchor="center")
female_2.place(relx=0.6, rely=0.5, anchor="center")
bmr_height.place(relx=0.5, rely=0.6, anchor="center")
bmr_weight.place(relx=0.5, rely=0.7, anchor="center")
calcBmrButton.place(relx=0.5, rely=0.8, anchor="center")
bmrOutput.place(relx=0.5, rely=0.9, anchor="center")


#HRMax
def CalcHRMax():
    hrc = 220 - int(age.get())
    hrm.configure(text="Your HR Max is "+str(hrc))


label2 = CTkLabel(master=tabview.tab("HRMAX"), text="Heart Rate Max")
label2.place(relx=0.5, rely=0.3, anchor="center")
age = CTkEntry(master=tabview.tab("HRMAX"), placeholder_text="Age")
age.place(relx=0.5, rely=0.4, anchor="center")
calculate2 = CTkButton(master=tabview.tab("HRMAX"), text="Calculate", command=CalcHRMax) 
calculate2.place(relx=0.5, rely=0.6, anchor="center")
hrm = CTkLabel(master=tabview.tab("HRMAX"), text=None)
hrm.place(relx=0.5, rely=0.7, anchor="center")

#VO2MAX

def CalcVO2MAX():
    vo2 = ((22.351*float(distance.get())) - 11.288)
    vo2m.configure(text="Your VO2Max is "+str(round(vo2,1)))

label3 = CTkLabel(master=tabview.tab("VO2MAX"), text="VO2Max (Cooper Test)")
label3.place(relx=0.5, rely=0.3, anchor="center")
distance = CTkEntry(master=tabview.tab("VO2MAX"), placeholder_text="distance run in 12 minutes (meter)")
distance.place(relx=0.5, rely=0.4, anchor="center")
calculate3 = CTkButton(master=tabview.tab("VO2MAX"), text="Calculate", command=CalcVO2MAX)
calculate3.place(relx=0.5, rely=0.6, anchor="center")
vo2m = CTkLabel(master=tabview.tab("VO2MAX"), text=None)
vo2m.place(relx=0.5, rely=0.7, anchor="center")


#About

about = CTkLabel(master=tabview.tab("About"), text="This program calculates basic health metrics.\n It is written in Python and uses CustomTkinter for GUI") 
about.place(relx=0.5, rely=0.5, anchor="center")

#Settings
def radiobutton_event():
    a = radio_var.get()
    if a == 1:
        set_appearance_mode("light")
    elif a == 2:
        set_appearance_mode("dark")

themelabel = CTkLabel(master=tabview.tab("Settings"), text="Theme: ")
themelabel.place(relx=0.3, rely=0.5, anchor="center")
radio_var = IntVar(value=0)
radiobutton_1 = CTkRadioButton(master=tabview.tab("Settings"), text="Light",command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(master=tabview.tab("Settings"), text="Dark",command=radiobutton_event, variable= radio_var, value=2)
radiobutton_1.place(relx=0.5, rely=0.5, anchor="center")
radiobutton_2.place(relx=0.7, rely=0.5, anchor="center")

fullscreenlabel = CTkLabel(master=tabview.tab("Settings"), text="Fullscreen: ")
def switch_event():
    stat = switch_var.get()
    if stat == "on":
        app.attributes("-fullscreen", "True")
    elif stat == "off":
        app.attributes("-fullscreen", "False")
switch_var = StringVar(value="off")
switch = CTkSwitch(master=tabview.tab("Settings"), text=None, command=switch_event,variable=switch_var, onvalue="on", offvalue="off")
fullscreenlabel.place(relx=0.3, rely=0.7, anchor="center")
switch.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()