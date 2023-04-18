## Статистика

Есть лог-файл с временами обработки транзакций, который формируется при выполнении тестовых скриптов. Файл имеет заголовок и табулированные данные по результатам обработке транзакций.

Пример файла:  
[26-06-15 14:10:27.725094] Statistics gathering started  
TIME	EVENT	CALLCNT	FILLCNT	AVGSIZE	MAXSIZE	AVGFULL	MAXFULL	MINFULL	AVGDLL	MAXDLL	AVGTRIP	MAXTRIP	AVGTEAP	MAXTEAP	AVGTSMR	MAXTSMR	MINTSMR  
[14:10:27]	ORDER					518			42		0		0		476  
[14:10:27]	ORDER					323			10		0		0		313  
[14:10:27]	ORDER					225			8		0		0		217  

Значения полей:  
EVENT – Наименование транзакции  
AVGTSMR – Время ответа торговой системы на транзакцию, в микросекундах  
Остальные поля опускаем.  

По каждому типу транзакций (EVENT) необходима следующая информация:  
  EVENTNAME – Название транзакции  
  min=110 – Минимальное время ответа на транзакцию в микросекундах  
  50%=112 – Медиана  
  90%=122 – 90% результатов меньше 122 микросекунд  
  99%=140 – 99% результатов меньше 140 микросекунд  
  99.9%=145 – 99.9% результатов меньше 145 микросекунд  

И таблица:  
| ExecTime | TransNo | Weight,% | Percent |
|:---------|:-------:| :-------:|:-------:|
| 110      | 430768  | 43.08    | 43.08   |
| 115      | 486144  | 48.61    | 91.69   |
| 120      | 70935   | 7.09     | 98.78   |
| 125      | 9164    | 0.92     | 99.70   |

EXECTIME – Время ответа на транзакцию, кратное 5 микросекундам  
TRANSNO – Количество транзакций с таким временем  
Weight – Процент от общего количества транзакций  
Percent – Процент от общего количества транзакций, имеющих время ответа <= EXECTIME

Реализован скрипт на Python для формирования статистики с выводом в консоль и сохранением в текстовых файлах аналогично оригинальному формату.