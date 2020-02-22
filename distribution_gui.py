from scipy.stats import norm, gamma, logistic, weibull_min, expon, trimboth, gaussian_kde
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np


def dist_norm(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(norm.ppf(0.001),
                    norm.ppf(0.999), 1000)
    ax.plot(x, norm.pdf(x), 'r', lw=4, alpha=0.8)

    vals = norm.ppf([0.001, 0.5, 0.999])
    np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))

    r = norm.rvs(size=1000)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=25)

    my_density = gaussian_kde(mr, bw_method=.45)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2)


def dist_gamma(event):
    fig, ax = plt.subplots(1, 1)
    a = 2
    x = np.linspace(gamma.ppf(0.001, a),
                    gamma.ppf(0.999, a), 1000)
    rv = gamma(a)
    ax.plot(x, rv.pdf(x), 'r', lw=4, alpha=0.8)

    vals = gamma.ppf([0.001, 0.5, 0.999], a)
    np.allclose([0.001, 0.5, 0.999], gamma.cdf(vals, a))

    r = gamma.rvs(a, size=1000)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=25)

    my_density = gaussian_kde(mr, bw_method=.35)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2)


def dist_log(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(logistic.ppf(0.001),
                    logistic.ppf(0.999), 1000)
    ax.plot(x, logistic.pdf(x), 'r', lw=4, alpha=0.8)

    vals = logistic.ppf([0.001, 0.5, 0.999])
    np.allclose([0.001, 0.5, 0.999], logistic.cdf(vals))

    r = logistic.rvs(size=1000)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=25)

    my_density = gaussian_kde(mr, bw_method=.45)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2)


def dist_exp(event):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(expon.ppf(0.001), expon.ppf(0.999), 1000)

    ax.plot(x, expon.pdf(x), 'r', lw=4, alpha=0.8)
    vals = expon.ppf([0.001, 0.5, 0.999])
    np.allclose([0.001, 0.5, 0.999], expon.cdf(vals))

    r = expon.rvs(size=1000)
    mr = trimboth(r, .025)

    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=25)

    my_density = gaussian_kde(mr, bw_method=.35)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2)


def dist_weibull(event):
    fig, ax = plt.subplots(1, 1)
    c = 2
    x = np.linspace(weibull_min.ppf(0.001, c),
                    weibull_min.ppf(0.999, c), 1000)
    rv = weibull_min(c)
    ax.plot(x, rv.pdf(x), 'r', lw=4, alpha=0.8)

    vals = weibull_min.ppf([0.001, 0.5, 0.999], c)
    np.allclose([0.001, 0.5, 0.999], weibull_min.cdf(vals, c))

    r = weibull_min.rvs(c, size=1000)
    mr = trimboth(r, .025)
    ax.hist(mr, density=True, histtype='bar', alpha=0.5, bins=25)

    my_density = gaussian_kde(mr, bw_method=.45)
    ax.plot(x, my_density(x), 'g', lw=2)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2)



window = Tk()
window.geometry('1200x560')

title = Label(window, text="Вывод графиков распределений")
title.grid(row=0, columnspan=2)

norm_d = Button(window, text="Нормальное распределение")
norm_d.grid(row=1, columnspan=2)
norm_d.bind("<Button-1>", dist_norm)
gamma_d = Button(window, text="Гамма-распределение")
gamma_d.grid(row=2, column=0)
gamma_d.bind("<Button-1>", dist_gamma)
log_d = Button(window, text="Логистическое распределение")
log_d.grid(row=2, column=1)
log_d.bind("<Button-1>", dist_log)
weibull_d = Button(window, text="Распределение Вейбулла")
weibull_d.grid(row=3, column=0)
weibull_d.bind("<Button-1>", dist_weibull)
exp_d = Button(window, text="Экспоненциальное распределение")
exp_d.grid(row=3, column=1)
exp_d.bind("<Button-1>", dist_exp)

window.mainloop()