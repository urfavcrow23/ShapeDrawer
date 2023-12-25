from window1 import DDA_win
from window2 import ShapeDrawer
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def new_win():
      root = tk.Tk()
      width_of_window = 600
      height_of_window = 600
      screen_width = root.winfo_screenwidth()
      screen_height = root.winfo_screenheight()
      x_coordinate = (screen_width / 2) - (width_of_window / 2)
      y_coordinate = (screen_height / 2) - (height_of_window / 2)
      root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

      root.title('Shape Drawer')
      root.configure(bg="#FFFFFF")

      canvas = Canvas(
            root,
            bg="#FFFFFF",
            width=600,
            height=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
      )

      # BG
      canvas.place(x=0, y=0)
      image_image_1 = PhotoImage(file=r"C:\Users\Dell\Downloads\CG Project\ASSETS_PATH\Image600.png")
      image_1 = canvas.create_image(
            -5,
            0,
            anchor=NW,
            image=image_image_1
      )

      # Text
      canvas.create_text(
            60.0,
            100.0,
            anchor=NW,
            text="Choose From 2 Options:",
            fill="#FFFFFF",
            font=("Game Of Squids", 22)
      )

      def on_button_clickE1():
            # Open a new window
            root.destroy()
            DDA_win()
            root.mainloop()
            


      def on_button_clickE2():
            # Open a new window
            root.destroy()
            ShapeDrawer()
            root.mainloop()


      button_image_1 = PhotoImage(
            file=r"C:\Users\Dell\Downloads\CG Project\ASSETS_PATH\SButton.png")
      button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_clickE1,
            relief="flat"
      )
      button_1.place(
            x= 100,
            y= 400,
            width=402.0,
            height=56.0
      )

      button_image_2 = PhotoImage(
            file=r"C:\Users\Dell\Downloads\CG Project\ASSETS_PATH\SButton2.png")
      button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_clickE2,
            relief="flat"
      )
      button_2.place(
            x= 100,
            y= 250,
            width=402.0,
            height=56.0
      )

      root.resizable(False, False)

      root.mainloop()


# Main window
w = Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
w.overrideredirect(1)  # for hiding titlebar

# Frame
Frame(w, width=427, height=250, bg='#010419').place(x=0, y=0)

# Labels
label1 = Label(w, text='Shape Drawer', fg='white', bg='#010419')
label1.configure(font=("Game Of Squids", 24, "bold"))
label1.place(x=35, y=90)

label2 = Label(w, text='Loading...', fg='white', bg='#010419')
label2.configure(font=("Calibri", 11))
label2.place(x=10, y=215)

# Making animation
image_a = ImageTk.PhotoImage(Image.open('c2.png'))
image_b = ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(4):
    l1 = Label(w, image=image_a, border=0, relief=SUNKEN)
    l1.place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l2.place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l3.place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l4.place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l1.place(x=180, y=145)
    l2 = Label(w, image=image_a, border=0, relief=SUNKEN)
    l2.place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l3.place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l4.place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l1.place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l2.place(x=200, y=145)
    l3 = Label(w, image=image_a, border=0, relief=SUNKEN)
    l3.place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l4.place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l1.place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l2.place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN)
    l3.place(x=220, y=145)
    l4 = Label(w, image=image_a, border=0, relief=SUNKEN)
    l4.place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()
new_win()
w.mainloop()