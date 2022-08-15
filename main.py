import tkinter as tk
from src.spline import interpolate

HEIGHT = 600

root = tk.Tk()
canvas = tk.Canvas(root, bg="#11171B", width=600, height=HEIGHT)
canvas.pack()

points = [[100, 100], [200, 300], [400, 500], [500, 300], [300, 100]]
interpolate(points, 0.5, canvas, HEIGHT)

root.mainloop()
