from scipy.stats import norm, gamma, logistic, weibull_min, expon, trimboth, gaussian_kde, \
                        kurtosis, skew, tstd, describe, variation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
import matplotlib.pyplot as plt
from statistics import mode, _counts
from tkinter import *
import numpy as np
from PIL import ImageTk, Image


def get_mode(l):
    vals = {}
    mode = None

    for num in l:
        num = round(num, 1)
        if num in vals:
            vals[num] += 1
        else:
            vals[num] = 1

    max_val = max(vals.values())
    for k in vals.keys():
        if vals.get(k) == max_val:
            mode = k
    return mode

def dist_norm(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(norm.ppf(0.001),
                    norm.ppf(0.999), 1000)
    ax.plot(x, norm.pdf(x), 'r', lw=4, alpha=0.8)

    r = norm.rvs(size=200)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=20)

    my_density = gaussian_kde(mr, bw_method=.5)
    ax.plot(x, my_density(x), 'g', lw=2)

    kurt, sk, md, var, std, med, avg, min, max = kurtosis(mr), skew(mr), get_mode(mr), np.var(mr), np.std(mr), \
                                                 np.median(mr), np.mean(mr), np.min(mr), np.max(mr)
    stat = f'Kurtosis: {kurt}, Skewness: {sk}, Mode: {md}, Variance: {var}, Standart deviation: {std}, ' \
           f'\nMedian: {med}, Mean: {avg}, Min: {min}, Max: {max}'

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=stat)
    numbers.grid(row=1)

    file = open('dist_numbers.txt', 'w')
    file.write(str(mr))
    file.close()


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

    kurt, sk, md, var, std, med, avg, min, max = kurtosis(mr), skew(mr), get_mode(mr), np.var(mr), np.std(mr), \
                                                 np.median(mr), np.mean(mr), np.min(mr), np.max(mr)
    stat = f'Kurtosis: {kurt}, Skewness: {sk}, Mode: {md}, Variance: {var}, Standart deviation: {std}, ' \
           f'\nMedian: {med}, Mean: {avg}, Min: {min}, Max: {max}'

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=stat)
    numbers.grid(row=1)

    file = open('dist_numbers.txt', 'w')
    file.write(str(mr))
    file.close()


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

    kurt, sk, md, var, std, med, avg, min, max = kurtosis(mr), skew(mr), get_mode(mr), np.var(mr), np.std(mr), \
                                                 np.median(mr), np.mean(mr), np.min(mr), np.max(mr)
    stat = f'Kurtosis: {kurt}, Skewness: {sk}, Mode: {md}, Variance: {var}, Standart deviation: {std}, ' \
           f'\nMedian: {med}, Mean: {avg}, Min: {min}, Max: {max}'

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=stat)
    numbers.grid(row=1)

    file = open('dist_numbers.txt', 'w')
    file.write(str(mr))
    file.close()


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

    kurt, sk, md, var, std, med, avg, min, max = kurtosis(mr), skew(mr), get_mode(mr), np.var(mr), np.std(mr), \
                                                 np.median(mr), np.mean(mr), np.min(mr), np.max(mr)
    stat = f'Kurtosis: {kurt}, Skewness: {sk}, Mode: {md}, Variance: {var}, Standart deviation: {std}, ' \
           f'\nMedian: {med}, Mean: {avg}, Min: {min}, Max: {max}'

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=stat)
    numbers.grid(row=1)

    file = open('dist_numbers.txt', 'w')
    file.write(str(mr))
    file.close()


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

    kurt, sk, md, var, std, med, avg, min, max = kurtosis(mr), skew(mr), get_mode(mr), np.var(mr), np.std(mr), \
                                                 np.median(mr), np.mean(mr), np.min(mr), np.max(mr)
    stat = f'Kurtosis: {kurt}, Skewness: {sk}, Mode: {md}, Variance: {var}, Standart deviation: {std}, ' \
           f'\nMedian: {med}, Mean: {avg}, Min: {min}, Max: {max}'

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0)

    numbers = Label(graph, text=stat)
    numbers.grid(row=1)

    file = open('dist_numbers.txt', 'w')
    file.write(str(mr))
    file.close()


window = Tk()
window.geometry('600x500')
window.title("Лабораторная работа №1")
window.resizable(0, 0)

graph = Toplevel(window)
graph.title("Числа и график")

hello = Label(graph, text="Здесь что-то будет", bd=20)
hello.grid(row=0)

background_image = ImageTk.PhotoImage(Image.open("image.jpg"))
background_label = Label(image=background_image)
background_label.grid(columnspan=2, rowspan=5)

background_color = "#384c6f"
button_color = "#dabbaa"

title      = Label(window, text="Вывод графиков распределений", bd=15,
                   bg=background_color, font=("Arial Black", 12), fg='#ffffff')
title.grid(row=0, columnspan=2)

norm_d     = Button(window, text="Нормальное распределение", bd=5,
                    bg=button_color, heigh=3, width=45, font=("Arial Bold", 10))
norm_d.grid(row=1, columnspan=2)
norm_d.bind("<Button-1>", dist_norm)

gamma_d    = Button(window, text="Гамма-распределение", bd=5,
                    bg=button_color, heigh=3, width=35, font=("Arial Bold", 10))
gamma_d.grid(row=2, column=0, sticky=E)
gamma_d.bind("<Button-1>", dist_gamma)

log_d      = Button(window, text="Логистическое\nраспределение", bd=5,
                    bg=button_color, heigh=3, width=35, font=("Arial Bold", 10))
log_d.grid(row=2, column=1, sticky=W)
log_d.bind("<Button-1>", dist_log)

weibull_d  = Button(window, text="Распределение\nВейбулла", bd=5,
                    bg=button_color, heigh=3, width=35, font=("Arial Bold", 10))
weibull_d.grid(row=3, column=0, sticky=E)
weibull_d.bind("<Button-1>", dist_weibull)

exp_d      = Button(window, text="Экспоненциальное\nраспределение", bd=5,
                    bg=button_color, heigh=3, width=35, font=("Arial Bold", 10))
exp_d.grid(row=3, column=1, sticky=W)
exp_d.bind("<Button-1>", dist_exp)

window.mainloop()
