from tkinter import *
import os
from tkinter import filedialog as fd
import customtkinter
import EncryptMessageInImage_Key
from tkinter.messagebox import showinfo
import EncryptMessage
import DecryptMessage


# create a window
root = Tk()
root.title("EN-DE Cryptor")
root.geometry("800x600")
root.resizable(False, False)

#loading items
decode_icon = PhotoImage(file=r'icon.png')
encode_icon = PhotoImage(file=r'icon2.png')
new_icon = PhotoImage(file=r'icon3.png')
background = PhotoImage(file=r'bg.png')
# background2 = PhotoImage(file=r'E:\Szyfrator-Deszyfrator\Gui\bg2.png')
select_icon = PhotoImage(file=r'icon3.png')
label_select = Label(root, image=select_icon)

canvas = Canvas(root, width=800, height=600)
canvas.pack()
canvas.background = background
bg = canvas.create_image(0, 0, anchor=NW, image=background)

algorithm = 0
isHideMsg = IntVar()
isHideKey = IntVar()

def main_window():
    canvas.delete("chose")
    forget_all_widgets()
    clear_text()
    encode_button2.place(x=140, y=200)
    decode_button2.place(x=420, y=200)


def clear_text():
    entry_file_textbox.delete(0, 'end')
    message_textbox.delete(0, 'end')
    key_textbox.delete(0, 'end')


def hide_message():
    if isHideMsg.get() == 0:
        message_textbox.config(show='')
    if isHideMsg.get() == 1:
        message_textbox.config(show='*')


def hide_key():
    if isHideKey.get() == 0:
        key_textbox.config(show='')
    if isHideKey.get() == 1:
        key_textbox.config(show='*')

def encode_window():
    canvas.create_text(55, 30, text='encode mode', font=('Helvetica', 12), fill='white', tag="chose")
    canvas.create_text(404, 250, text='Chose algorithm:', font=('Helvetica', 26), fill='black', tag="chose")
    canvas.create_text(400, 250, text='Chose algorithm:', font=('Helvetica', 25), fill='white', tag="chose")
    canvas.create_text(450, 290, text='for images\t              for .wav', font=('Helvetica', 14), fill='white', tag="chose")
    forget_all_widgets()
    label_select.place(x=324, y=230)
    select_file.place(x=330, y=150)
    entry_file_textbox.place(x=250, y=120)
    GCD_button.place(x=180, y=320)
    Algorytm1_button.place(x=290, y=320)
    Algorytm2_button.place(x=400, y=320)
    Wave_button.place(x=530, y=320)
    message_textbox.place(x=30, y=450)
    message_textbox.insert(END, "Enter your message to encrypt")
    key_textbox.place(x=30, y=490)
    key_textbox.insert(END, "Import your key or generate new")
    key_textbox.config(state="disable")
    run_encoding_button.place(x=670, y=455)
    hide_msg.place(x=500, y=447)
    hide_key.place(x=500, y=487)
    generate_key_button.place(x=150, y=520)
    insert_key_button.place(x=30, y=520)
    back_button.place(x=750, y=560)


def decode_window():
    canvas.create_text(404, 250, text='Chose algorithm:', font=('Helvetica', 26), fill='black', tag="chose")
    canvas.create_text(400, 250, text='Chose algorithm:', font=('Helvetica', 25), fill='white', tag="chose")
    canvas.create_text(450, 290, text='for images\t              for .wav', font=('Helvetica', 14), fill='white', tag="chose")
    canvas.create_text(55, 30, text='decode mode', font=('Helvetica', 12), fill='white', tag="chose")
    forget_all_widgets()
    label_select.place(x=324, y=230)
    select_file.place(x=330, y=150)
    entry_file_textbox.place(x=250, y=120)
    GCD_button.place(x=180, y=320)
    Algorytm1_button.place(x=290, y=320)
    Algorytm2_button.place(x=400, y=320)
    Wave_button.place(x=530, y=320)
    message_textbox.place(x=30, y=450)
    message_textbox.insert(END, "Here will be your message")
    key_textbox.place(x=30, y=490)
    key_textbox.insert(END, "Import key")
    key_textbox.config(state="disable")
    run_decoding_button.place(x=670, y=455)
    hide_msg.place(x=500, y=447)
    hide_key.place(x=500, y=487)
    insert_key_button.place(x=30, y=520)
    back_button.place(x=750, y=560)



def empty():
    return

def gcd_click():
    GCD_button.configure(fg_color='#666867')
    Algorytm1_button.configure(fg_color='#f0f0f0')
    Algorytm2_button.configure(fg_color='#f0f0f0')
    Wave_button.configure(fg_color='#f0f0f0')
    global algorithm
    algorithm = 1
    key_textbox.config(state="disabled")
    insert_key_button.configure(state=DISABLED)


def algorytm1_click():
    GCD_button.configure(fg_color='#f0f0f0')
    Algorytm1_button.configure(fg_color='#666867')
    Algorytm2_button.configure(fg_color='#f0f0f0')
    Wave_button.configure(fg_color='#f0f0f0')
    global algorithm
    algorithm = 2
    key_textbox.config(state="disabled")
    insert_key_button.configure(state=DISABLED)


def algorytm2_click():
    GCD_button.configure(fg_color='#f0f0f0')
    Algorytm1_button.configure(fg_color='#f0f0f0')
    Algorytm2_button.configure(fg_color='#666867')
    Wave_button.configure(fg_color='#f0f0f0')
    global algorithm
    algorithm = 3
    key_textbox.config(state="normal")
    insert_key_button.configure(state=NORMAL)

def wave_click():
    GCD_button.configure(fg_color='#f0f0f0')
    Algorytm1_button.configure(fg_color='#f0f0f0')
    Algorytm2_button.configure(fg_color='#f0f0f0')
    Wave_button.configure(fg_color='#666867')
    global algorithm
    algorithm = 4
    key_textbox.config(state="normal")
    insert_key_button.configure(state=DISABLED)


def select_file():
    entry_file_textbox.config(state="normal")
    clear_text()
    filetypes = (
        ('All files', '*'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    entry_file_textbox.insert(END, filename)
    entry_file_textbox.config(state="disabled")


def select_key():
    key_textbox.config(state="normal")
    clear_text()
    filetypes = (
        ('All files', '*'),
    )
    path = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)
    key = path
    if key:
        showinfo(
            title='Info',
            message="Key imported"
        )
    else:
        showinfo(
            title='Info',
            message="Incorrect key"
        )
    key_textbox.delete(0, 'end')
    key_textbox.insert(END, key)
    key_textbox.config(state = "disabled")


def generate_key():
    key_textbox.config(state="normal")
    key = EncryptMessageInImage_Key.generate_key()
    key_textbox.delete(0, 'end')
    key_textbox.insert(END, key)
    showinfo(
        title='Info',
        message="Wygenerowano klucz"
    )
    key_textbox.config(state="disable")

def run_enconding(algorithm):
    print("algorytm = ", algorithm)
    message = message_textbox.get()
    path = entry_file_textbox.get()
    if not os.path.exists(os.path.dirname(path)):
        showinfo(
            title='Info',
            message="Select file to decode message"
        )
        return
    if not algorithm:
        showinfo(
            title='Info',
            message="Chose algorithm"
        )
    if message == '':
        showinfo(
            title='Info',
            message="Message is empty"
        )
        return
    if algorithm == 1:
        EncryptMessage.encrypt_message_GCD(path, message)
        showinfo(
            title='Info',
            message="Message encoded"
        )
    if algorithm == 2:
        EncryptMessage.encrypt_message_without_key(path, message)
        showinfo(
            title='Info',
            message="Message encoded"
        )
    if algorithm == 3:
        key = key_textbox.get()
        try:
            EncryptMessage.encrypt_message_key(key, path, message)
            showinfo(
                title='Info',
                message="Message encoded"
            )
        except:
            showinfo(
                title='Info',
                message="Invalid key!"
            )
    if algorithm == 4:
        if path.split('.')[1] != 'wav':
            showinfo(
                title='Info',
                message="Invalid file type for this algorithm"
            )
            return
        EncryptMessage.encrypt_message_in_audio(path, message)
        showinfo(
            title='Info',
            message="Message encoded"
        )


def run_deconding(algorithm):
    print("algorytm = ", algorithm)
    path = entry_file_textbox.get()
    if not os.path.exists(os.path.dirname(path)):
        showinfo(
            title='Info',
            message="Select file to encode message"
        )
        return

    if not algorithm:
        showinfo(
            title='Info',
            message="Chose algorithm"
        )
    if algorithm == 1:
        try:
            msg = DecryptMessage.decrypt_image_GCD(path)
            print(msg)
        except:
            showinfo(
                title='Info',
                message="Cant decode the message"
            )
            return
    if algorithm == 2:
        try:
            msg = DecryptMessage.decrypt_message_without_key(path)
        except:
            showinfo(
                title='Info',
                message="Cant decode the message"
            )
            return
    if algorithm == 3:

        key_path = key_textbox.get()
        try:
            msg = DecryptMessage.decrypt_message_key(key_path, path)
        except:
            showinfo(
                title='Info',
                message="Cant decode the message"
            )
            return
    if algorithm == 4:
        try:
            msg = DecryptMessage.decrypt_message_in_audio(path)
        except:
            showinfo(
                title='Info',
                message="Cant decode the message"
            )
            return
    showinfo(
        title='Info',
        message="Message decoded"
    )
    message_textbox.insert(END, msg)

def forget_all_widgets():
    decode_button2.place_forget()
    encode_button2.place_forget()
    label_select.place_forget()
    select_file.place_forget()
    entry_file_textbox.place_forget()
    GCD_button.place_forget()
    Algorytm1_button.place_forget()
    Algorytm2_button.place_forget()
    message_textbox.place_forget()
    key_textbox.place_forget()
    run_encoding_button.place_forget()
    run_decoding_button.place_forget()
    hide_msg.place_forget()
    hide_key.place_forget()
    generate_key_button.place_forget()
    insert_key_button.place_forget()
    back_button.place_forget()
    Wave_button.place_forget()


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
entry_file_textbox = Entry(
    root,
    width=50
)

message_textbox = Entry(
    root,
    font=35,
    width=50
)

key_textbox = Entry(
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
Wave_button = customtkinter.CTkButton(
    master=root,
    text='Wave',
    width=100,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=wave_click
)

run_encoding_button = customtkinter.CTkButton(
    master=root,
    text='Encrypt',
    width=110,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=lambda *args: run_enconding(algorithm)
)


run_decoding_button = customtkinter.CTkButton(
    master=root,
    text='Decrypt',
    width=110,
    height=50,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=lambda *args: run_deconding(algorithm)
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
    command=decode_window,
    image=encode_icon,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3'
)
hide_msg = Checkbutton(
    root,
    text='Hide message',
    variable=isHideMsg,
    onvalue=1,
    offvalue=0,
    command=hide_message
)

hide_key = Checkbutton(
    root,
    text='Hide key',
    variable=isHideKey,
    onvalue=1,
    offvalue=0,
    command=hide_key,
    padx=15,
)

generate_key_button = customtkinter.CTkButton(
    master=root,
    text='Generate key',
    width=100,
    height=30,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=generate_key
)


insert_key_button = customtkinter.CTkButton(
    master=root,
    text='Import key',
    width=100,
    height=30,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=select_key
)

back_button = customtkinter.CTkButton(
    master=root,
    text='Back',
    width=30,
    height=30,
    fg_color='#f0f0f0',
    hover_color='#c3c3c3',
    command=main_window
)

select_text = Text(root)
main_window()

# run aplication
root.mainloop()