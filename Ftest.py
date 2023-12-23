from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create a new window
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
    image_image_1 = PhotoImage(file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\Image600.png")
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

    def on_button_ccclick():
        # Open a new window
        root.destroy()
        new_win1()
        root.mainloop()
        


    def on_button_ccclick22():
        # Open a new window
        root.destroy()
        new_win2()
        root.mainloop()


    button_image_1 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\SButton.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=on_button_ccclick,
        relief="flat"
    )
    button_1.place(
        x= 100,
        y= 400,
        width=402.0,
        height=56.0
    )

    button_image_2 = PhotoImage(
        file=r"C:\Users\Dell\Downloads\splash_screen_2-master\ASSETS_PATH\SButton2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=on_button_ccclick22,
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

def new_win1():
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

def new_win2():
    
    class ShapeDrawer:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Shape Drawer")

            self.grid_size = 20

            self.canvas = tk.Canvas(self.root, width=500, height=500, bg="lightgray")
            self.canvas.pack()

            self.grid_lines()

            self.current_shape = None
            self.shapes = []  # List to store shapes and their respective points
            self.temp_shape_id = None  # Add temp_shape_id attribute

            self.shape_options = {
                "Line": self.canvas.create_line,
                "Rectangle": self.canvas.create_rectangle,
                "Circle": self.canvas.create_oval
            }
            self.current_shape_type = "Line"  # Set default shape

            # Add a dropdown menu for shape selection
            self.shape_var = tk.StringVar(self.root)
            self.shape_var.set(self.current_shape_type)
            shape_menu = tk.OptionMenu(self.root, self.shape_var, *self.shape_options.keys())
            shape_menu.pack()

            # Update the shape type when the menu selection changes
            self.shape_var.trace("w", self.update_shape_type)

            # Binding mouse events
            self.canvas.bind("<Button-1>", self.start_drawing)
            self.canvas.bind("<ButtonRelease-1>", self.draw_shape)

            # Create a Treeview to display shape points
            self.tree = ttk.Treeview(self.root, columns=("ID", "Type", "Start", "End"))
            self.tree.heading("#0", text="ID")
            self.tree.heading("ID", text="ID")
            self.tree.heading("Type", text="Type")
            self.tree.heading("Start", text="Start Point")
            self.tree.heading("End", text="End Point")
            self.tree.pack()

        def grid_lines(self):
            for i in range(0, 500, self.grid_size):
                line_x = self.canvas.create_line(i, 0, i, 500, fill="gray", dash=(2, 2))
                line_y = self.canvas.create_line(0, i, 500, i, fill="gray", dash=(2, 2))

                # Display numbers on the grid
                self.canvas.create_text(i + 5, 5, anchor=tk.NW, text=str(i), fill="black", font=("Helvetica", 8))
                self.canvas.create_text(5, i + 5, anchor=tk.NW, text=str(i), fill="black", font=("Helvetica", 8))

        def update_shape_type(self, *args):
            self.current_shape_type = self.shape_var.get()

        def start_drawing(self, event):
            self.start_x, self.start_y = event.x // self.grid_size * self.grid_size, event.y // self.grid_size * self.grid_size

            # Delete the previous temp_shape_id if it exists
            if self.temp_shape_id:
                self.canvas.delete(self.temp_shape_id)

            self.temp_shape_id = None  # Initialize temp_shape_id

        def draw_shape(self, event):
            x, y = event.x // self.grid_size * self.grid_size, event.y // self.grid_size * self.grid_size

            # Delete the existing temp_shape_id
            if self.temp_shape_id:
                self.canvas.delete(self.temp_shape_id)

            # Create a new temp_shape_id
            if self.current_shape_type == "Line":
                self.temp_shape_id = self.canvas.create_line(
                    self.start_x, self.start_y, x, y, width=2, fill="blue", dash=(2, 2)
                )
            else:
                self.temp_shape_id = self.shape_options[self.current_shape_type](
                    self.start_x, self.start_y, x, y, width=2, outline="blue", dash=(2, 2)
                )

            # Update the shapes list with the drawn shape
            self.shapes.append({"type": self.current_shape_type, "points": (self.start_x, self.start_y, x, y)})

            # Update the Treeview with shape points
            self.update_tree()

        def update_tree(self):
            # Clear existing items in the Treeview
            self.tree.delete(*self.tree.get_children())

            # Populate the Treeview with shape points
            for i, shape in enumerate(self.shapes, start=1):
                type_, points = shape['type'], shape['points']

                if type_ == "Line":
                    x1, y1, x2, y2 = points
                    item_values = (i, type_, f"({x1},{y1})", f"({x2},{y2})")
                elif type_ == "Rectangle":
                    x1, y1, x2, y2 = points
                    item_values = (i, type_, f"({x1},{y1})", f"({x2},{y2})")
                elif type_ == "Circle":
                    x1, y1, x2, y2 = points
                    item_values = (i, type_, f"Center: ({x1},{y1})", f"Radius: {((x1-x2)**2 + (y1-y2)**2)**0.5}")

                self.tree.insert("", "end", values=item_values)

    if __name__ == "__main__":
        app = ShapeDrawer()
        app.root.resizable(False,False)
        app.root.mainloop()

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