from tkinter import * 
from pynput import keyboard, mouse
import pyperclip
import os
import picker

def slide(value):
    R=r_Scale.get()
    G=g_Scale.get()
    B=b_Scale.get()
    print(f'{R},{G},{B}')
    hex = "#%02x%02x%02x" % (R, G, B)
    rgb = f'{R},{G},{B}'
    print(f"{rgb}, {hex}")
    colorLabel.config(bg=hex)
    hex_entry.delete(0, END)
    hex_entry.insert(0, hex)
    rgb_entry.delete(0, END)
    rgb_entry.insert(0, rgb)

# def slide(red,green,blue):
#     R=red
#     G=green
#     B=blue
#     rgb = f'{R},{G},{B}'
#     hex = "#%02x%02x%02x" % (R, G, B)
#     print(f"{rgb}, {hex}")
#     colorLabel.config(bg=hex)
#     hex_entry.delete(0, END)
#     hex_entry.insert(0, hex)
#     rgb_entry.delete(0, END)
#     rgb_entry.insert(0, rgb)

def hex_copy():
    pyperclip.copy(hex_entry.get())

def rgb_copy():
    pyperclip.copy(rgb_entry.get())

def realtime():
    with keyboard.Listener(on_release = picker.onRel) as ky:
        with mouse.Listener(on_click = picker.onClick) as ms:
            ky.join()
            ms.join()

root = Tk()
root.config(bg='#6B8790')

root.title("Color Picker by Dimas")
root.geometry("350x500+100+100")

colorLabel = Label(root, bg="black", width=37, height=9, bd=2, relief=RAISED)
colorLabel.pack(pady=5)

frame = Frame(root, bd=2, relief=SUNKEN)
frame.pack(pady=5)

r_label = Label(frame, text="R", fg="red", font=('arial', 10, 'bold'))
r_label.grid(row=0,column=0)

r_Scale = Scale(frame, from_=0, to=255, length=210, fg="red", orient=HORIZONTAL,command=slide)
r_Scale.grid(row=0,column=1)

g_label = Label(frame, text="G", fg="green", font=('arial', 10, 'bold'))
g_label.grid(row=1,column=0)

g_Scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL,command=slide)
g_Scale.grid(row=1,column=1)

b_label = Label(frame, text="B", fg='blue', font=('arial', 10, 'bold'))
b_label.grid(row=2,column=0)

b_Scale = Scale(frame, from_=0, to=255, length=210,fg='blue', orient=HORIZONTAL,command=slide)
b_Scale.grid(row=2,column=1)

my_frame = Frame(root, bd=2, relief=SUNKEN)
my_frame.pack(pady=5)

hex_label = Label(my_frame, text="Hex Code :", font=('arial', 10, 'bold'))
hex_label.grid(row=0,column=0)

hex_entry = Entry(my_frame, width=12, font=('arial', 10))
hex_entry.grid(row=0,column=1,padx=5)
hex_entry.insert(END, '#000000')

copyButton1=Button(my_frame,text='Copy', font=('arial', 10, 'bold'),command=hex_copy)
copyButton1.grid(row=1,columnspan=2,pady=7)

rbg_label = Label(my_frame, text="RGB Code :", font=('arial', 10, 'bold'))
rbg_label.grid(row=2,column=0)

rgb_entry = Entry(my_frame, width=12, font=('arial', 10))
rgb_entry.grid(row=2,column=1,padx=5)
rgb_entry.insert(END,'0,0,0')

copyButton2=Button(my_frame,text='Copy', font=('arial', 10, 'bold'),command=rgb_copy)
copyButton2.grid(row=3,columnspan=2,pady=7)

l_ontime = Button(my_frame, text= 'Go Realtime!', font=('arial', 10, 'bold'), command=realtime)
l_ontime.grid(row=4, columnspan=2, pady=7)



root.mainloop()

