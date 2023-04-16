import numpy as np
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation


# функция решения уравнения
def math_mod():
    N = int(entry_N.get())
    M = int(entry_NT.get())
    dt = float(entry_dt.get())
    x = np.linspace(0, 2*np.pi, N)
    u0 = np.sin(5*x)
    u = u0
    fu = np.fft.fft(u0)
    l = np.empty(N)  # ???
    h = 2*np.pi/N
    D = float(entry_D.get())
    for i in range(N//2):
        l[i] = (4*D/(h**2)*(np.sin(i*h/4)**2))
        l[i-1] = l[i]
    Z = np.empty((N, M))
    Z[0] = u0

    def F(u,t):
        F = np.sin(0.1*u+t)
        return F

    for m in range(1, M):
        t = m*dt
        t_prev = (m-1)*dt
        F1 = F(u, t_prev)
        F2 = F(u, t)
        us = u
        S = 2
        Fs = np.fft.fft((F1+F2)/2)
        for s in range(S):
            fus = ((2-dt*l)*fu+dt*Fs)/(2+dt*l)
            us = np.fft.ifft(fus)
            Fs = np.fft.fft((F1+F(us, t))/2)
        Z[m] = us
        u = us
        fu = fus
    return Z

# функция построения графика
def run_math_mod(): 
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    if rb.get() == 0:  # если выбрана тепловая карта
        fig.colorbar(ax.contourf(math_mod()))
    elif rb.get() == 1:  # если выбрана анимация
        M = int(entry_NT.get())
        Z = math_mod()
        N = int(entry_N.get())
        t = np.arange(0, M, 1)
        line, = ax.plot(t, Z[0, :M])
        def init():
            ax.set_xlim(0, M)
            ax.set_ylim(Z.min(), Z.max())
            return line,
        def animate(i):
            line.set_ydata(Z[i, :M])
            return line,
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().grid(row=4, columnspan=4)
    if rb.get() == 1:
        anim = FuncAnimation(fig, animate, np.arange(1, M), 
                    init_func=init, repeat=True, blit=False, interval=30)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)  # стандартный тулбар для графика
    toolbar.update()
    toolbar.grid(row=3, columnspan=4)

root = Tk()
canvas = None
root.title('Математическое моделирование')
root.resizable(width=False, height=False)
root_name = Label(text='Уравнение диффузии в кольце')
root_name.grid(row=0, columnspan=4)
label_D = Label(root, text='Коэффициент диффузии D:')  # виджеты ввода параметров
entry_D = Entry(root, width=7)
label_N = Label(root, text='Количество узлов сетки N:')
entry_N = Entry(root, width=7)
label_dt = Label(root, text='Шаг по времени dt:')
entry_dt = Entry(root, width=7)
label_NT = Label(root, text='Количество шагов по времени NT:')
entry_NT = Entry(root, width=7)
entry_D.insert(0,'0.01')  # значения по умолчанию
entry_N.insert(0,'1001')
entry_dt.insert(0,'0.1')
entry_NT.insert(0,'1001')
label_D.grid(row=1, column=0, sticky='e')  # расположение виджетов в окне
entry_D.grid(row=1, column=1, sticky='w')
label_N.grid(row=1, column=2, sticky='e')
entry_N.grid(row=1, column=3, sticky='w')
label_dt.grid(row=2, column=0, sticky='e')
entry_dt.grid(row=2, column=1, sticky='w')
label_NT.grid(row=2, column=2, sticky='e')
entry_NT.grid(row=2, column=3, sticky='w')
rb = IntVar()  # выбор варианта отрисовки графика
rb.set(0)  # по умолчанию выбрана тепловая карта
rb_0 = Radiobutton(
    master=root,
    text='Тепловая карта',
    variable=rb,
    value=0)
rb_1 = Radiobutton(
    master=root,
    text='Анимация',
    variable=rb,
    value=1)
rb_0.grid(row=5, column=0)
rb_1.grid(row=5, column=1)
# кнопка для вызова функции отрисовки графика
run = Button(
    master=root,
    text='Run',
    command=run_math_mod,
    width=10,
    padx = 5, pady = 5)
run.grid(row=5, column=2, sticky='e')

run_math_mod()  # отрисовка графика после запуска

root.mainloop()
