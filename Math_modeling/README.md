## Математическое моделирование

Рассматривается уравнение диффузии в кольце:
$$\partial _{t} \mathnormal{u} = \mathnormal{D} \partial _{xx} \mathnormal{u} + \mathnormal{F(u(x,t),t)}, \quad \mathnormal{x} \in [0;2\pi]$$
Решение $\mathnormal{u(x,t)}$ для $\mathnormal{t} \in [0;\mathnormal{T}]$, отвечающее следующим граничным и начальным условиям:
$$\mathnormal{u(x,0)} = \mathnormal{u} _{0} \mathnormal{(x)}, \quad \mathnormal{x} \in [0;2\pi]$$
$$\mathnormal{u(0,t)} = \mathnormal{u(2\pi,t)}; \quad \partial _{x} \mathnormal{u(0,t)} = \partial _{x} \mathnormal{u(2\pi,t)}, \quad \mathnormal{t} \in [0;\mathnormal{T}]$$

Программа принимает на вход следующие параметры:  
  $\mathrm{D}$ – коэффициент диффузии  
  $\mathrm{N}$ – количество узлов сетки по $\mathnormal{x}$ для численного метода  
  $\mathrm{dt}$ – шаг по времени, с которым будет двигаться программа  
  $\mathrm{NT}$ – количество шагов по времени, которые будет выполнять программа  

![Скриншот окна программы](https://github.com/kalewala/msu_programming/raw/main/Math_modeling/Screen.jpg
