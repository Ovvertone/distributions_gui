from scipy.stats import norm, gamma, logistic, weibull_min, expon, trimboth, gaussian_kde
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from pillow import ImageTk, Image


def dist_norm(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(norm.ppf(0.001),
                    norm.ppf(0.999), 1000)
    ax.plot(x, norm.pdf(x), 'r', lw=4, alpha=0.8)

    r = norm.rvs(size=200)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.45)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=mr)
    numbers.grid(row=4, columnspan=2)


def dist_gamma(event):
    fig, ax = plt.subplots(1, 1)
    a = 2
    rv = gamma(a)
    x = np.linspace(gamma.ppf(0.001, a),
                    gamma.ppf(0.999, a), 1000)
    ax.plot(x, rv.pdf(x), 'r', lw=4, alpha=0.8)

    r = gamma.rvs(a, size=200)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.5)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=mr)
    numbers.grid(row=4, columnspan=2)


def dist_log(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(logistic.ppf(0.001),
                    logistic.ppf(0.999), 1000)
    ax.plot(x, logistic.pdf(x), 'r', lw=4, alpha=0.8)

    r = logistic.rvs(size=200)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.45)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=mr)
    numbers.grid(row=1)


def dist_exp(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(expon.ppf(0.001),
                    expon.ppf(0.999), 1000)
    ax.plot(x, expon.pdf(x), 'r', lw=4, alpha=0.8)

    r = expon.rvs(size=200)
    mr = trimboth(r, .025)

    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.35)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=mr)
    numbers.grid(row=4, columnspan=2)


def dist_weibull(event):
    fig, ax = plt.subplots(1, 1)
    c = 2
    x = np.linspace(weibull_min.ppf(0.001, c),
                    weibull_min.ppf(0.999, c), 1000)
    rv = weibull_min(c)
    ax.plot(x, rv.pdf(x), 'r', lw=4, alpha=0.8)

    r = weibull_min.rvs(c, size=200)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.5)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=mr)
    numbers.grid(row=4, columnspan=2)


window = Tk()
window.geometry('600x600')
window.title("Лабораторная работа №1")
window.resizable(0, 0)

graph = Toplevel(window)
graph.title("Числа и график")

hello = Label(graph)

background_image = ImageTk.PhotoImage(Image.open("image.jpg"))
background_label = Label(image=background_image)
background_label.grid(columnspan=2, rowspan=5)

title     = Label(window, text="Вывод графиков распределений", bd=15)
title.grid(row=0, columnspan=2)

norm_d    = Button(window, text="Нормальное распределение", bd=5, width=82)
norm_d.grid(row=1, columnspan=2)
norm_d.bind("<Button-1>", dist_norm)

gamma_d   = Button(window, text="Гамма-распределение", bd=5, width=40)
gamma_d.grid(row=2, column=0, sticky=E)
gamma_d.bind("<Button-1>", dist_gamma)

log_d     = Button(window, text="Логистическое распределение", bd=5, width=40)
log_d.grid(row=2, column=1, sticky=W)
log_d.bind("<Button-1>", dist_log)

weibull_d = Button(window, text="Распределение Вейбулла", bd=5, width=40)
weibull_d.grid(row=3, column=0, sticky=E)
weibull_d.bind("<Button-1>", dist_weibull)

exp_d     = Button(window, text="Экспоненциальное распределение", bd=5, width=40)
exp_d.grid(row=3, column=1, sticky=W)
exp_d.bind("<Button-1>", dist_exp)

window.mainloop()
