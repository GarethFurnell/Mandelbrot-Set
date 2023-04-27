# Mandelbrot set
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def render_ascii_mandelbrot(xmin, xmax, ymin, ymax, width=80, height=40, max_iter=100):
    _, _, mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    for row in mandelbrot_image:
        print("".join(['#' if i == max_iter else ' ' for i in row]))

render_ascii_mandelbrot(-2.0, 1.0, -1.0, 1.0)

