from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ... (code for interactive shape drawing window)

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