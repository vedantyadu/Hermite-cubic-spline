
def interpolate(points, tension, canvas, height):
    
    c = tension

    for i in range(0, len(points) - 1):
        
        t = 0
        
        if i == 0:
            tangentx1 = 0
            tangenty1 = 0
            tangentx2 = (points[i + 2][0] - points[i][0]) * c
            tangenty2 = (points[i + 2][1] - points[i][1]) * c
        elif i == len(points) - 2:
            tangentx1 = (points[i + 1][0] - points[i - 1][0]) * c
            tangenty1 = (points[i + 1][1] - points[i - 1][1]) * c
            tangentx2 = 0
            tangenty2 = 0
        else:
            tangentx1 = (points[i + 1][0] - points[i - 1][0]) * c
            tangenty1 = (points[i + 1][1] - points[i - 1][1]) * c
            tangentx2 = (points[i + 2][0] - points[i][0]) * c
            tangenty2 = (points[i + 2][1] - points[i][1]) * c


        while t <= 1:
            tt = t ** 2
            ttt = t ** 3
            h1 = (2*(ttt)) - (3*(tt)) + 1
            h2 = (-2 * (ttt)) + (3*(tt))
            h3 = (ttt) - (2*(tt)) + t
            h4 = (ttt) - (tt)
            x = h1 * points[i][0] + h2 * points[i + 1][0] + h3 * tangentx1 + h4 * tangentx2
            y = h1 * points[i][1] + h2 * points[i + 1][1] + h3 * tangenty1 + h4 * tangenty2
            putPixel(x, y, "#2a4978", 2, height, canvas)
            t += 0.005
    
    for point in points:
        canvas.create_oval(point[0] - 5, height - point[1] - 5, point[0] + 5, height - point[1] + 5, fill="#94b2e0", outline="")


def putPixel(x, y, color, size, height, canvas):
    canvas.create_rectangle(x, height - y, x + size, height - y - size, fill=color, outline="")

