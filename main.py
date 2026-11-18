# Credits to Ma'am Hala for the teaching materials.

import tkinter as tk
from tkinter import ttk
import openpyxl
from datetime import datetime
from tkinter import messagebox

def load_data():
    path = "C:/Users/rican/AppData/Local/Programs/Python/Python313/success/project1/Forest-ttk-theme-master/Forest-ttk-theme-master/attendance_sheet.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)
    

def insert_row():
    name = name_entry.get()
    section = section_combobox.get()
    date = date_entry.get()
    if not date.strip():
        messagebox.showerror("Error", "Date and Time field cannot be empty.")
        return

    if not name.strip() or name == "Name":
        messagebox.showerror("Error", "Name field cannot be empty.")
        return

    if not subject_spinbox.get().isdigit():
        messagebox.showerror("Error", "No. of Subjects must be a number.")
        return
    
    subject = int(subject_spinbox.get())
    status = "Present" if a.get() else "Absent"

    print(name, section, date, subject, status)

    # Insert row into Excel sheet
    path = "C:/Users/rican/AppData/Local/Programs/Python/Python313/success/project1/Forest-ttk-theme-master/Forest-ttk-theme-master/attendance_sheet.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    row_values = [name, section, date, subject, status]
    sheet.append(row_values)
    workbook.save(path)

    # Insert row into treeview
    treeview.insert('', tk.END, values=row_values)

    # Clear the values
    name_entry.delete(0, "end")
    name_entry.insert(0, "Name")
    section_combobox.set(section_list[0])
    subject_spinbox.delete(0, "end")
    subject_spinbox.insert(0, "No. of Subjects")
    checkbutton.state(["!selected"])
    date_entry.delete(0, tk.END)
    

def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def update_datetime():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    date_entry.delete(0, tk.END)
    date_entry.insert(0, current_time)

root = tk.Tk()
root.title("Attendance Sheet")

logo = tk.PhotoImage(file="attendance_logo.png")
root.iconphoto(True, logo)

style = ttk.Style(root)

# Black and white themes
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")


# Section list dropdown menu
section_list = ["Aristotle", "Descartes", "Kant", "Nietzsche", "Sartre"]

frame = ttk.Frame(root)
frame.pack()

# Insert Row Frame
widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

# Name
name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,"Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0, column=0, padx=10, pady=(0,5), sticky="ew")

# Section 
section_combobox = ttk.Combobox(widgets_frame, values=section_list)
section_combobox.current(0)
section_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Date and Time Frame
datetime_frame = ttk.Frame(widgets_frame)
datetime_frame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

# Date and time entry automatically filled with current date and time
date_entry = ttk.Entry(datetime_frame, width=25)
date_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

# Date now buttons
date_now_button = ttk.Button(
    datetime_frame,
    text="DateNow",
    command=update_datetime
)
date_now_button.pack(side="right", padx=5, pady=5)

# No. subjects
subject_spinbox = ttk.Spinbox (widgets_frame, from_ =1,  to=100)
subject_spinbox.insert(0,"No. of Subjects")
subject_spinbox.bind("<FocusIn>", lambda g: subject_spinbox.delete('0','end'))
subject_spinbox.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# Present, Absent checkbutton (Status)
a = tk.BooleanVar()

checkbutton = ttk.Checkbutton(widgets_frame, text="Present", variable =a)
checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# Submit button
button = ttk.Button(widgets_frame, text="Submit", command=insert_row)
button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# Separator line
separator = ttk.Separator(widgets_frame)
separator.grid(row=6, column=0, padx=(20,10), pady=10, sticky="ew")

# Mode switch
mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

# Data frame
treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)

# Scrollbar
treeScroll.pack(side="right", fill="y")

# Heading of the data table
cols = ("Name", "Section", "Date and Time", "No. of Subjects", "Status")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=13)

# Size of each column
treeview.column("Name", width=100)
treeview.column("Section", width=100)
treeview.column("Date and Time", width=150)
treeview.column("No. of Subjects", width=100)
treeview.column("Status", width=100)
treeview.pack()

# Syncronize the scrollbar with the data table
treeScroll.config(command=treeview.yview)
load_data()


root.mainloop()




