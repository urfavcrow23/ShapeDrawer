from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ... (code for DDA line drawing window)
def DDA_win():
    root1 = tk.Tk()
    width_of_window = 1280
    height_of_window = 800
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    root1.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

    root1.title('Shape Drawer')
    root1.configure(bg="#FFFFFF")

    canvas = Canvas(
        root1,
        bg="#FFFFFF",
        width=1280,
        height=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    # BG
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Image.png")
    image_1 = canvas.create_image(
        0,
        0,
        anchor=NW,
        image=image_image_1
    )

    # Text
    canvas.create_text(
        210.0,
        20.0,
        anchor=NW,
        text="DDA Line Drawing",
        fill="#FFFFFF",
        font=("Game Of Squids", 64 * -1)
    )

    entry_image_1 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Rectangle12.png")
    entry_bg_1 = canvas.create_image(
        334.0,
        227.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=171.0,
        y=199.0,
        width=326.0,
        height=54.0
    )

    entry_image_2 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Rectangle12.png")
    entry_bg_2 = canvas.create_image(
        334.0,
        364.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=171.0,
        y=336.0,
        width=326.0,
        height=54.0
    )

    entry_image_3 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Rectangle12.png")
    entry_bg_3 = canvas.create_image(
        334.0,
        484.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=171.0,
        y=456.0,
        width=326.0,
        height=54.0
    )

    entry_image_4 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Rectangle12.png")
    entry_bg_4 = canvas.create_image(
        334.0,
        580.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=171.0,
        y=552.0,
        width=326.0,
        height=54.0
    )

    canvas.create_text(
        78.0,
        555.0,
        anchor="nw",
        text="Y1",
        fill="#FFFFFF",
        font=("Game Of Squids", 40 * -1)
    )

    canvas.create_text(
        78.0,
        339.0,
        anchor="nw",
        text="Y0",
        fill="#FFFFFF",
        font=("Game Of Squids", 40 * -1)
    )

    canvas.create_text(
        78.0,
        202.0,
        anchor="nw",
        text="X0",
        fill="#FFFFFF",
        font=("Game Of Squids", 40 * -1)
    )

    canvas.create_text(
        78.0,
        459.0,
        anchor="nw",
        text="X1",
        fill="#FFFFFF",
        font=("Game Of Squids", 40 * -1)
    )

    def on_button_click():
        # Provide initial values for x1, y1, x2, and y2
        x1, y1 = float(entry_1.get()), float(entry_2.get())
        x2, y2 = float(entry_3.get()), float(entry_4.get())

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)

        xincrement = dx / steps
        yincrement = dy / steps

        i = 0

        xcoordinates = []
        ycoordinates = []

        while i < steps:
            i += 1
            x1 = x1 + xincrement
            y1 = y1 + yincrement
            print("X1: ", x1, "Y1: ", y1)
            xcoordinates.append(x1)
            ycoordinates.append(y1)

        # Create Canvas
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')  # Set the size of the figure
        canvas = FigureCanvasTkAgg(fig, master=root1)
        # fig.patch.set_facecolor('none')
        fig.patch.set_alpha(0.0)

        # Naming the Axis
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        # Graph title
        plt.title("Result")
        # Create Toolbar
      #   toolbar = NavigationToolbar2Tk(canvas, root)  # Removed pack_toolbar=False
      #   toolbar.update()
      #   toolbar.update_idletasks()  # Added this line
        # Plot data on Matplotlib Figure
        ax.set_facecolor((0, 0, 0, 0))

        ax.plot(xcoordinates, ycoordinates)
        canvas.get_tk_widget().place(x=650, y=200)
        canvas.draw()

    # ... (rest of your code)

    button_image_1 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Button.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=on_button_click,
        relief="flat"
    )
    button_1.place(
        x= 350,
        y= 675,
        width=564.0,
        height=79.0
    )

    root1.resizable(False, False)
    root1.mainloop()