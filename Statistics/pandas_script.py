"""
Реализован скрипт только для предложенного файла (mtesrl_20150626_MD0000600002_stats.txt)
В случае использования других входных файлов потребуется поменять параметры чтения внутри main.py
Выходные данные записываются в два файла такого же формата как входной файл:
 - df_event.txt - статистика по каждому типу транзакций EVENT: min=110 50%=112 90%=122 99%=140 99.9%=145
   (де-факто там только ORDER, но благодаря группировке отображались бы и другие)
 - df_table.txt - таблица с времен ответа на транзакцию, кратным 5 и т.д.
"""

import pandas as pd
from numpy import cumsum


# чтение данных из файла
df = pd.read_csv(
    'Statistics/mtesrl_20150626_MD0000600002_stats.txt',
    sep="\t",
    skiprows=1,
    header=1,
    usecols=['EVENT', 'AVGTSMR'],
    skipfooter=2,
    engine='python'
    )

# вывод информации по EVENT
df_event = df.groupby('EVENT')['AVGTSMR'].describe(percentiles=[0.5, 0.9, 0.99, 0.999])
print(df_event.iloc[:, 3:8])
df_event.iloc[:, 3:8].to_csv('Statistics/df_event.txt', sep='\t')  # сохрание в файл

# вывод таблицы
df_avgtsmr = df['AVGTSMR'].sort_values(ascending=True)
df_1 = pd.Series(sorted(df_avgtsmr - df_avgtsmr%5))
df_2 = df_1.value_counts()[:]
df_2 = df_2.reset_index(drop=True)
df_3 = df_2 / len(df_1) * 100
df_4 = cumsum(df_3)
df_1 = df_1.unique()
table = {'ExecTime':df_1, 'TransNo':df_2, 'Weight,%':df_3, 'Percent':df_4}
df_table = pd.DataFrame(table)
df_table = df_table.round(decimals=2)
print(df_table)
df_table.to_csv('Statistics/df_table.txt', index=False, sep='\t')  # сохрание в файл