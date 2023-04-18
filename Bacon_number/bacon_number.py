import json
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


G = nx.Graph()  # простой неориентированный граф
actor_list = []  # список актёров для выпадающего списка
actor_labels = dict()  # словарь для подписей актёров

# функция выбора пути к файлу
def select_file():
    way = filedialog.askopenfilename()
    entry_way.delete(0, END)
    entry_way.insert(0, f'{way}')

# функция чтения данных из выбранного файла
def read_data():
    way = str(entry_way.get())
    with open(f'{way}', 'r', encoding='utf-8') as f:  #открытие файла с данными
        actor_data = json.load(f)  # запись в переменную
    
    G.clear()  # очистка графа, если файл уже открывался
    film_list = []  # список фильмов
    for actor in actor_data:  # алгоритм формирования графа
        film_list.clear()
        for film in actor['films']:
            film_list.append(film['title'])
        i = actor_data.index(actor)
        for actor2 in actor_data[i+1:]:
            j = actor_data.index(actor2)
            for film2 in actor2['films']:
                if film2['title'] in film_list:
                    G.add_edge(i, j)

    actor_list.clear()  # очистка списка актёров, если файл уже открывался
    for actor in actor_data:
        actor_list.append(actor['name'])  # запись списка актёров
    combobox_actors["values"] = actor_list  # заполнение выпадающего списка именами актёров
    combobox_actors.set(actor_list[0])  # выбор первого актёра (Бэйкона) по умолчанию

    actor_labels.clear()  # очистка словаря, если файл уже открывался
    for actor in actor_list:  # заполнение словаря для подписей актёров
        actor_labels[actor_list.index(actor)] = actor

    graph_actor()  # визуализация графа после чтения данных из файла

# функция визуализации пустого холста под граф при запуске программы
def empty_canvas():
    fig_start = plt.figure(figsize=(6.5, 5), dpi=100)  # размер и разрешение пустого холста
    plt.axis('off')
    plt.title('Число Бейкона')  # название программы
    about = '    1. Выберите файл с данными и нажмите "LOAD"\n\
    \n\
    2. Выберите из выпадающего списка имя актёра,\n\
    нажмите "SELECT" и узнайте его число Бейкона\n\
    \n\
    \n\
    Число Бейкона — минимальное расстояние по графу\n\
    от актера до Кевина Бейкона. Вершины графа — актеры,\n\
    ребра графа — фильмы, в которых снимались два актера\n\
    одновремнно.'
    plt.text(0.5, 0.5, about, horizontalalignment='center')  # описание программы
    canvas = FigureCanvasTkAgg(fig_start, root)
    canvas.get_tk_widget().grid(row=3, columnspan=6)  # расположение в интерфейсе
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)  # стандартный тулбар matplotlib
    toolbar.update()
    toolbar.grid(row=2, column=0, columnspan=6, sticky='w')
#    plt.show()

# функция визуализации графа
def graph_actor():
    selection_actor = combobox_actors.get()  # получение выбранного актёра
    n = actor_list.index(selection_actor)  # индекс актёра - индекс узла
    actor_nodes = nx.shortest_path(G, n, 0)  # список узлов кратчайшего пути
    actor_edges = [(a,b) for a,b in zip(actor_nodes, actor_nodes[1:])]  # список рёбер кратчайшего пути
    bacon_number = len(actor_nodes)-1  # число Бейкона
    label_bacon['text'] = f'Число Бейкона для {selection_actor} - {bacon_number}'  # вывод числа Бейкона

    fig = plt.figure(figsize=(6.5, 5), dpi=100)  # размер и разрешение холста для графа

    pos=nx.spring_layout(G)
    nx.draw(G, pos, node_size=250, node_color='c', edge_color='grey')  # общий вид графа
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=actor_nodes, node_color='orangered')  # вид выбранных узлов до Бейкона
    nx.draw_networkx_edges(G, pos, edgelist=actor_edges, edge_color="red", width=3)  # вид выбранных рёбер до Бейкона
    nx.draw_networkx_labels(G, pos, labels=actor_labels)  # подписи всех узлов (имена актёров)
    
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().grid(row=3, columnspan=6)  # расположение графа в интерфейсе
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)  # стандартный тулбар matplotlib
    toolbar.update()
    toolbar.grid(row=2, column=0, columnspan=6, sticky='w')
#    plt.show()

# интерфейс
root = Tk()
root.title('Число Бейкона')
root.resizable(width=False, height=False)
label_openfile = Label(root, text='Файл:')  # Виджеты
entry_way = Entry(root, width=85)
select = Button(
    root,
    text=' ... ',
    command=select_file)
load = Button(
    root,
    text='LOAD',
    command=read_data,
    width=7)
label_pickactor = Label(root, text='Актёр:')
combobox_actors = ttk.Combobox(
    root, 
    values=actor_list,
    width=25, 
    state="readonly")
graph = Button(
    root,
    text='SELECT',
    command=graph_actor,
    width=7)
label_bacon = Label(root, text=' ')
label_autor = Label(root, text="Created by El'dar Garipov, 2022")
label_openfile.grid(row=0, column=0, sticky='e')  # расположение виджетов
entry_way.grid(row=0, column=1, columnspan=3)
select.grid(row=0, column=4, sticky='ew')
load.grid(row=0, column=5, sticky='w')
label_bacon.grid(row=1, column=0, columnspan=2, sticky='w', padx=5)
label_pickactor.grid(row=1, column=2, sticky='e')
combobox_actors.grid(row=1, column=3, sticky='e')
graph.grid(row=1, column=5, sticky='w')
label_autor.grid(row=4, column=0, columnspan=6)

empty_canvas()  # вызов функции для отображения пустого холста при запуске программы

root.mainloop()