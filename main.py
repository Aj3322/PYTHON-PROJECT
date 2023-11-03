from tkinter import *
import tkinter as tk
import pandas as pd
import statistics
#######
#  Title: Measure of Central Tendancy and Dispersion
# 
# @author : Ajay Kumar(11222721), Alok Kumar(11222512), Riya Bansal(11222720), Gaytri (112225)
# 
# @version 1.00	15.09.2023 -  Updated Code
########
def calculate_central_tendency():
    selected_option = ct_var.get()
    input_numbers = number_text.get("1.0", "end-1c").split()
    numbers = [float(x) for x in input_numbers]

    result = None

    if selected_option == 1:  # Arithmetic Mean
        result = sum(numbers) / len(numbers)
    elif selected_option == 2:  # Median
        result = statistics.median(numbers)
    elif selected_option == 3:  # Mode
        result = statistics.mode(numbers)

    if result is not None:
        ct_result_label.config(text=f"Central Tendency Result: {result}", fg="green")
    else:
        ct_result_label.config(text="Invalid input or selection", fg="red")

def calculate_dispersion():
    selected_option = disp_var.get()
    input_numbers = number_text.get("1.0", "end-1c").split()
    numbers = [float(x) for x in input_numbers]

    result = None

    if selected_option == 1:  # Variance
        result = statistics.variance(numbers)
    elif selected_option == 2:  # Standard Deviation
        result = statistics.stdev(numbers)
    elif selected_option == 3:  # Range
        result = max(numbers) - min(numbers)

    if result is not None:
        disp_result_label.config(text=f"Dispersion Result: {result}", fg="blue")
    else:
        disp_result_label.config(text="Invalid input or selection", fg="red")

root = Tk()
root.title("Calculator: Central Tendency and Dispersion")
root.minsize(500, 500)
root.maxsize(1200, 988)
root.configure(bg="lightblue")

title_label = Label(
    text='Central Tendency and Dispersion Calculator', font=('Arial', 16), bg="lightblue")
title_label.pack()

number_label = Label(
    text='Enter your Numbers:', font=('Arial', 10), bg="lightblue")
number_label.place(x=10, y=75)
number_text = Text(height=1, width=30)
number_text.place(x=180, y=75)



# Central Tendency Calculation
ctLabel = Label(
    text='Central Tendency', font=('Arial', 12), bg="lightblue")
ctLabel.place(x=10, y=150)
ct_var = IntVar()
ct_var.set(1)

r1_ct = Radiobutton(
    text="Arithmetic Mean", variable=ct_var, value=1, bg="lightblue")
r1_ct.place(x=10, y=200)
r2_ct = Radiobutton(text="Median", variable=ct_var, value=2, bg="lightblue")
r2_ct.place(x=10, y=220)
r3_ct = Radiobutton(text="Mode", variable=ct_var, value=3, bg="lightblue")
r3_ct.place(x=10, y=240)

ct_result_label = Label(
    text="", font=('Arial', 12), bg="lightblue")
ct_result_label.pack(pady=5)

ct_calculate_button = Button(
    text='Calculate Central Tendency', command=calculate_central_tendency, bg="green", fg="white")
ct_calculate_button.pack(pady=235, side=tk.TOP)



# Dispersion Calculation

dispLabel = Label(
    text='Dispersion', font=('Arial', 12), bg="lightblue")
dispLabel.place(x=10, y=370)
disp_var = IntVar()
disp_var.set(1)

r1_disp = Radiobutton(
    text="Variance", variable=disp_var, value=1, bg="lightblue")
r1_disp.place(x=10, y=420)
r2_disp = Radiobutton(
    text="Standard Deviation", variable=disp_var, value=2, bg="lightblue")
r2_disp.place(x=10, y=440)
r3_disp = Radiobutton(
    text="Range", variable=disp_var, value=3, bg="lightblue")
r3_disp.place(x=10, y=460)

disp_calculate_button = Button(
    text='Calculate Dispersion', command=calculate_dispersion, bg="blue", fg="white")
disp_calculate_button.pack(pady=0, side=tk.TOP)

disp_result_label = Label(
    text="", font=('Arial', 12), bg="lightblue")
disp_result_label.pack(pady=20)

quitButton = Button(
    text='Press to exit', command=root.destroy, bg="red", fg="white")
quitButton.pack(padx=5, pady=0, side=tk.BOTTOM)
title_label = Label(
    text="Author: Ajay Kumar , Alok Kumar , Riya , Gaytri ", font=("Arial", 12), bg="lightblue")
title_label.pack()

root.mainloop()
