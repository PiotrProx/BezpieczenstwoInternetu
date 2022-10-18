from tkinter import *
import os
from tkinter import filedialog as fd
import customtkinter


# create a window
root = Tk()
root.title("EN-DE Cryptor")
root.geometry("800x600")
root.resizable(False, False)

#loading items
decode_icon = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\icon.png')
encode_icon = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\icon2.png')
new_icon = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\icon3.png')
background = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\bg.png')
# background2 = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\bg2.png')
select_icon = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\icon3.png')
label1 = Label(root, image=background)
label1.place(x=0, y=0)
label_select = Label(root, image=select_icon)

algorithm = 0

def clear_text():
    entry.delete(0, 'end')


def encode_window():
    decode_button2.destroy()
    encode_button2.destroy()
    label_select.place(x=324, y=230)
    select_file.place(x=330, y=150)
    entry.place(x=250, y=120)
    GCD_button.place(x=240, y=320)
    Algorytm1_button.place(x=350, y=320)
    Algorytm2_button.place(x=460, y=320)
    message.place(x=30, y=450)
    message.insert(END, "Enter your message to encrypt")
    key.place(x=30, y=490)
    key.insert(END, "Enter your key")
    run.place(x=670, y=455)
    # hide_msg.place(x=500, y=450)


def empty():
    return

def gcd_click():
    GCD_button.configure(fg_color='#666867')
    Algorytm1_button.configure(fg_color='#f0f0f0')
    Algorytm2_button.configure(fg_color='#f0f0f0')
    algorithm = 1
    print(algorithm)
    key.config(state="disabled")


def algorytm1_click():
    GCD_button.configure(fg_color='#f0f0f0')
    Algorytm1_button.configure(fg_color='#666867')
    Algorytm2_button.configure(fg_color='#f0f0f0')
    algorithm = 2
    key.config(state="disabled")


def algorytm2_click():
    GCD_button.configure(fg_color='#f0f0f0')
    Algorytm1_button.configure(fg_color='#f0f0f0')
    Algorytm2_button.configure(fg_color='#666867')
    algorithm = 3
    key.config(state="normal")


def select_file():
    clear_text()
    filetypes = (
        ('All files', '*'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    entry.insert(END, filename)


encode_button = Button(
    root,
    text="Encode",
    padx=100,
    pady=50,
    command=encode_window,
    image=decode_icon
)
decode_button = Button(
    root,
    text="Decode",
    padx=100,
    pady=50,
    image=encode_icon
)
select_file = customtkinter.CTkButton(
    master=root,
    text='Select image or sound',
    width=130,
    height=30,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=select_file
)
entry = Entry(
    root,
    width=50
)

message = Entry(
    root,
    font=35,
    width=50,
)

key = Entry(
    root,
    font=35,
    width=50
)

GCD_button = customtkinter.CTkButton(
    master=root,
    text='GCD',
    width=100,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    border_color='#000604',
    command=gcd_click
)

Algorytm1_button = customtkinter.CTkButton(
    master=root,
    text='Algorytm1',
    width=100,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=algorytm1_click
)

Algorytm2_button = customtkinter.CTkButton(
    master=root,
    text='Algorytm2',
    width=100,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=algorytm2_click
)


run = customtkinter.CTkButton(
    master=root,
    text='Encrypt',
    width=110,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=empty
)


encode_button2 = customtkinter.CTkButton(
    master=root,
    text="",
    width=50,
    height=50,
    command=encode_window,
    image=decode_icon,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3'
)
decode_button2 = customtkinter.CTkButton(
    master=root,
    text="",
    width=50,
    height=50,
    command=encode_window,
    image=encode_icon,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3'
)


select_text = Text(root)

encode_button2.place(x=140,y=200)
decode_button2.place(x=420,y=200)
# run aplication
root.mainloop()