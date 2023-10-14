from tkinter import *
from tkinter import ttk
import tkinter as tk

#from func_add_row import add_row
from func_new_info_enter import submit
from func_update_table import update_table
from func_update_table import read_data
from func_excel import excel

stock_file = "stock.txt" #stock file name!!! 


root = tk.Tk()
root.title("Stok Takip Programı") #program name!!!
root.geometry("1920x1080")
root.config(background="#f1f5f1")
root.tk.call("tk", "scaling", 1.5)

###################################################
new_line = list()
previous_data = list()
lines = list()

def add_row(table_name):
    global pre, after

    #"Tarih", "Lokasyon", "İrsaliye No", "Önceki Miktar", "İşlem", "Sonraki Miktar"

    n = read_data(stock_file)

    try:
        pre = n[combobox.get()][-1][-1]
    except KeyError:
        return

    try:
        date = date_var.get()
        location = location_var.get()
        number = number_var.get()#irsaliye
        effect = effect_var.get()
        after = float(pre) + float(effect)
    except ValueError:
        return

    new_line.append(date)
    new_line.append(location)
    new_line.append(number)
    new_line.append(pre)
    new_line.append(effect)
    new_line.append(after)

    if float(effect) < 0:
        table_name.insert('', 'end', values=(date, location, number, pre, effect, after), tags="negative")
    else:
        table_name.insert('', 'end', values=(date, location, number, pre, effect, after), tags="positive")
    
        
    with open(stock_file, "r+") as file:
        for line in file:
            lines.append(line.strip())
            
    open(stock_file, 'w').close()        
            
    for data in lines:
        name, rows = data.strip().split("=")
        

        if name == combobox.get():
            rows = eval(rows)
            rows.append(new_line)
            string = str(name) + "=" + str(rows)
            previous_data.append(string)
        else:
            previous_data.append(data)
            
    with open(stock_file, "a") as file:
        for i in previous_data:
            file.write(i + "\n")
            
    names = read_data(stock_file)
    stock = names[combobox.get()]
    s = 0
    for i in stock:
        s = s + float(i[-2])

    current_label.configure(text=s)

    previous_data.clear()
    new_line.clear()
    lines.clear()
            

# Create a frame for the first set of widgets
stock_frame = ttk.Frame(root)
stock_frame.pack(side="top", )

current_header = Label(stock_frame, text="Stokta:", font=(15))
current_header.pack(side=LEFT)

current_label = Label(stock_frame, text=0, font=(17), )
current_label.pack(side=LEFT, ipadx=10)

# Create a Combobox widget

names = read_data(stock_file)
names_original = names.copy()
names = [i for i in names]






combo_var = StringVar()
combobox = ttk.Combobox(stock_frame, textvariable=combo_var, values=names)
combobox.pack(side=LEFT)
combobox.bind("<<ComboboxSelected>>", lambda event : update_table(combo_var.get(), table,current_label, stock_file))




####################################################################

#"Tarih", "Lokasyon", "İrsaliye No", "Önceki Miktar", "İşlem", "Sonraki Miktar"

# Create a frame for the first set of widgets
entry_frame = ttk.Frame(root)
entry_frame.pack(side="top",)

# Create StringVar variables to store user inputs
date_var = StringVar()
location_var = StringVar()
number_var = StringVar()
effect_var = StringVar()

# Create labels and entry fields for user inputs
date_label = Label(entry_frame, text="Tarih")
date_label.pack(side=LEFT)
date_entry = Entry(entry_frame, textvariable=date_var)
date_entry.pack(side=LEFT)

location_label = Label(entry_frame, text="Lokasyon")
location_label.pack(side=LEFT)
location_entry = Entry(entry_frame, textvariable=location_var)
location_entry.pack(side=LEFT)

number_label = Label(entry_frame, text="İrsaliye No")
number_label.pack(side=LEFT)
number_entry = Entry(entry_frame, textvariable=number_var)
number_entry.pack(side=LEFT)

effect_label = Label(entry_frame, text="İşlem")
effect_label.pack(side=LEFT)
effect_entry = Entry(entry_frame, textvariable=effect_var)
effect_entry.pack(side=LEFT)

# Add a "Add Row" button
add_button = Button(entry_frame, text="Satır Ekle", command=lambda: add_row(table))
add_button.pack(side=LEFT)

###################################################

excel_button = Button(stock_frame, text="Excel'e aktar", command=lambda: excel(stock_file), background="#1d6f42", foreground="#FbFFFF")
excel_button.pack(side=LEFT)

# Create StringVar variables to store user inputs
name_var = StringVar()
stock_var = StringVar()

# Create labels and entry fields for user inputs
name_label = Label(stock_frame, text="Mal İsmi:")
name_label.pack(side=LEFT)

name_entry = Entry(stock_frame, textvariable=name_var)
name_entry.pack(side=LEFT)

stock_label = Label(stock_frame, text="Miktar:")
stock_label.pack(side=LEFT)

stock_entry = Entry(stock_frame, textvariable=stock_var)
stock_entry.pack(side=LEFT)
#####################################################################

SI_label = Label(stock_frame, text="Birim")
SI_label.pack(side=LEFT)

combobox_SI = ttk.Combobox(stock_frame, values="kg L adet paket")
combobox_SI.pack(side=LEFT)


######################################################################


# Create a submit button
submit_button = Button(stock_frame, text="Ekle", command=lambda: submit(name_var, stock_var, combobox, combobox_SI.get(), stock_file))
submit_button.pack()

###################################################

# Create a Treeview widget
table = ttk.Treeview(root, columns=("Tarih", "Lokasyon", "İrsaliye No", "Önceki Miktar", "İşlem", "Sonraki Miktar"), show="headings")

# Set column headings
table.heading("Tarih", text="Tarih", anchor="center")
table.heading("Lokasyon", text="Lokasyon", anchor="center")
table.heading("İrsaliye No", text="İrsaliye No", anchor="center")
table.heading("Önceki Miktar", text="Önceki Miktar", anchor="center")
table.heading("İşlem", text="İşlem", anchor="center")
table.heading("Sonraki Miktar", text="Sonraki Miktar", anchor="center")

# Layout the Treeview widget
table.pack(fill=BOTH,  pady=10)# padx=10, pady=100)  # Expand only along Y-axis

# Change the background and foreground colors
table.tag_configure("positive", background="#7CFC00")
table.tag_configure("negative", background="#FA8072")

# Pack the Treeview widget
table.pack(fill=BOTH, expand=True, pady=10)

#################################################################################

root.mainloop()