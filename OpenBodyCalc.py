from customtkinter import *

app = CTk()
app.geometry("500x500")
app.title("OpenBodyCalc")

tabview = CTkTabview(master=app)
tabview.configure(segmented_button_selected_color="green")

#theme
set_default_color_theme("green")
set_appearance_mode("system")

tabview.pack(fill = BOTH, expand = True)

t1=tabview.add("BMI")
t2=tabview.add("BMR")
t3=tabview.add("HRMAX")
t4=tabview.add("VO2MAX")
t5=tabview.add("Settings")
t6=tabview.add("About")



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

label1 = CTkLabel(master=t1, text="BMI")
label1.place(relx=0.5, rely=0.2, anchor="center")

height1 = CTkEntry(master=t1, placeholder_text="Height (meters)")
height1.place(relx=0.5, rely=0.3, anchor="center")

weight1 = CTkEntry(master=t1, placeholder_text="Weight (kgs)")
weight1.place(relx=0.5, rely=0.4, anchor="center")

calculate1 = CTkButton(master=t1, text="Calculate", command=CalcBMI)
calculate1.place(relx=0.5, rely=0.5, anchor="center")

bmi = CTkLabel(master=t1, text=None)
bmi.place(relx=0.5, rely=0.7, anchor="center")

bmi_indicator = CTkLabel(master=t1, text=None)
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

bmr_label = CTkLabel(master=t2, text="Basal Metabolic Rate")
bmr_age = CTkEntry(master=t2, placeholder_text="Age")
bmr_gender = IntVar(value=0)
male_1 = CTkRadioButton(master=t2, text="Male", variable= bmr_gender, value=1)
female_2 = CTkRadioButton(master=t2, text="Female", variable= bmr_gender, value=2)
bmr_height = CTkEntry(master=t2, placeholder_text=("Height in cm"))
bmr_weight = CTkEntry(master=t2, placeholder_text=("Weight in kgs"))
calcBmrButton = CTkButton(master=t2, text="Calculate", command=calcBmr)
bmrOutput = CTkLabel(master=t2, text=None)

bmr_label.place(relx=0.5, rely=0.2, anchor="center")
bmr_age.place(relx=0.5, rely=0.3, anchor="center")
male_1.place(relx=0.45, rely=0.4, anchor="center")
female_2.place(relx=0.6, rely=0.4, anchor="center")
bmr_height.place(relx=0.5, rely=0.5, anchor="center")
bmr_weight.place(relx=0.5, rely=0.6, anchor="center")
calcBmrButton.place(relx=0.5, rely=0.7, anchor="center")
bmrOutput.place(relx=0.5, rely=0.8, anchor="center")


#HRMax
def CalcHRMax():
    hrc = 220 - int(age.get())
    hrm.configure(text="Your HR Max is "+str(hrc))


label2 = CTkLabel(master=t3, text="Heart Rate Max")
label2.place(relx=0.5, rely=0.2, anchor="center")
age = CTkEntry(master=t3, placeholder_text="Age")
age.place(relx=0.5, rely=0.3, anchor="center")
calculate2 = CTkButton(master=t3, text="Calculate", command=CalcHRMax) 
calculate2.place(relx=0.5, rely=0.4, anchor="center")
hrm = CTkLabel(master=t3, text=None)
hrm.place(relx=0.5, rely=0.5, anchor="center")

#VO2MAX

def CalcVO2MAX():
    vo2 = ((22.351*float(distance.get())) - 11.288)
    vo2m.configure(text="Your VO2Max is "+str(round(vo2,1)))

label3 = CTkLabel(master=t4, text="VO2Max (Cooper Test)")
label3.place(relx=0.5, rely=0.2, anchor="center")
distance = CTkEntry(master=t4, placeholder_text="Distance in KM")
distance.place(relx=0.5, rely=0.3, anchor="center")
calculate3 = CTkButton(master=t4, text="Calculate", command=CalcVO2MAX)
calculate3.place(relx=0.5, rely=0.4, anchor="center")
vo2m = CTkLabel(master=t4, text=None)
vo2m.place(relx=0.5, rely=0.7, anchor="center")


#About

about = CTkLabel(master=t6, text="This program calculates basic health metrics.\n It is written in Python and uses CustomTkinter for GUI.") 
about.place(relx=0.5, rely=0.2, anchor="center")

#Settings

def apply():
    a = radio_var.get()
    b = switch_var.get()
    if a == 1 and b:
        set_appearance_mode("system")
    elif a == 2:
        set_appearance_mode("light")
    elif a == 3:
        set_appearance_mode("dark")
    if b == "on":
        app.attributes("-fullscreen", "True")
    elif b == "off":
        app.attributes("-fullscreen", "False")

themelabel = CTkLabel(master=t5, text="Theme: ")
themelabel.place(relx=0.3, rely=0.2, anchor="center")
radio_var = IntVar(value=1)
radiobutton_1 = CTkRadioButton(master=t5, text="System", variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(master=t5, text="Light", variable= radio_var, value=2)
radiobutton_3 = CTkRadioButton(master=t5, text="Dark", variable= radio_var, value=3)
radiobutton_1.place(relx=0.5, rely=0.2, anchor="center")
radiobutton_2.place(relx=0.7, rely=0.2, anchor="center")
radiobutton_3.place(relx=0.5, rely=0.3, anchor="center")

fullscreenlabel = CTkLabel(master=t5, text="Fullscreen: ")
switch_var = StringVar(value="off_")
switch = CTkSwitch(master=t5, text=None,variable=switch_var, onvalue="on", offvalue="off")
fullscreenlabel.place(relx=0.3, rely=0.4, anchor="center")
switch.place(relx=0.5, rely=0.4, anchor="center")

apply_btn = CTkButton(master=t5, text="Apply", command=apply)
apply_btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()