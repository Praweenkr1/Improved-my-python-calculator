import tkinter as tk

window = tk.Tk()

window.title("my calculator")
window.geometry("600x600")

display = tk.Entry(window,font =("agency fb",55),justify="right")       

display.pack(anchor="w", padx=10)



    #def  creates a number like a button so when we click it it outputs a number . means i am defining/creating a function .
def button_click(number):
    display.insert(tk.END,number)  #tk.END means it will insert the number at the end of the display

button_frame = tk.Frame(window)
button_frame.pack(anchor="w", padx=10, pady=10)


button00 = tk.Button(button_frame,text="00",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("00"))
button00.grid(row=3, column=0, padx=3, pady=3)

button1 = tk.Button(button_frame,text="1",font=("agency fb",40),
                    width=4, height=1,
                    command=lambda: button_click("1"))

#command=lambda: button click("1") means when we click the button it will call the function button_click and pass the value "1" to it.
button_decimal = tk.Button(button_frame,text=".",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("."))
button_decimal.grid(row=3, column=2, padx=3, pady=3)

button1.grid(row=0, column=0, padx=3, pady=3)  #grid means it will place the button in the grid layout at row 0 and column 0.

button2 = tk.Button(button_frame,text="2",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("2"))
button2.grid(row=0, column=1, padx=3, pady=3)

button3 = tk.Button(button_frame,text="3",font=("agency fb",40),
                    width=4,height=1,  
                    command=lambda: button_click("3"))

button3.grid(row=0, column=2, padx=3, pady=3)

button4 = tk.Button(button_frame,text="4",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("4"))
button4.grid(row=1, column=0, padx=3, pady=3)

button5 = tk.Button(button_frame,text="5",font=("agency fb",40),
                    width=4,height=1,   
                    command=lambda: button_click("5"))
button5.grid(row=1, column=1, padx=3, pady=3)

button6 = tk.Button(button_frame,text="6",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("6"))
button6.grid(row=1, column=2, padx=3, pady=3)

button7 = tk.Button(button_frame,text="7",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("7"))
button7.grid(row=2, column=0, padx=3, pady=3)

button8 = tk.Button(button_frame,text="8",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("8"))
button8.grid(row=2, column=1, padx=3, pady=3)

button9 = tk.Button(button_frame,text="9",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("9"))
button9.grid(row=2, column=2, padx=3, pady=3)

button0 = tk.Button(button_frame,text="0",font=("agency fb",40),
                    width=4,height=1,
                    command=lambda: button_click("0"))
button0.grid(row=3, column=1, padx=3, pady=3)




window.mainloop()