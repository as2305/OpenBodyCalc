from customtkinter import *

app = CTk()
app.geometry("900x600")
app.title("OpenBodyCalc")

tabview = CTkTabview(master=app)

tabview.pack(padx=20, pady=20)

tabview.add("BMI")
tabview.add("Tab 2")
tabview.add("Tab 3")

label = CTkLabel(master=tabview.tab("BMI"), text="test")
label.pack(padx=20, pady=20)

height1 = CTkEntry(master=tabview.tab("BMI"), placeholder_text="Enter your height...")
height1.pack(padx=30, pady=30)

app.mainloop()