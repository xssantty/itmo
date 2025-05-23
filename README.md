Черток Герман Константинович 474391, Застенская Анастасия Романовна 474288

Анализ IT-вакансий по данным hh.ru

Этот проект представляет собой исследование рынка труда с использованием данных о вакансиях, собранных с одного или нескольких сайтов по поиску работы (например, hh.ru, Superjob, Работа.ру). Под основу мы взяли hh.ru. 
Основная цель — извлечь полезную информацию из вакансий: уровень зарплат, востребованные навыки, региональное распределение и требования к опыту.

Проектанализирует: 
Названия вакансий
Географическое расположение (города / регионы)
Зарплатные вилки
Требуемый опыт
Работодатели
Ключевые навыки

Структура проекта:
itmo_project/
├── data/
│   └── vacancies_raw.json       #исходные данные с вакансиями
├── dashboard/
│   └── app.py                   #основной скрипт анализа и визуализации
├── notebooks/
│   └── job_analysis.ipynb       #интерактивный Jupyter Notebook с EDA
└── README.md                   

1. Установите зависимости:
```bash
pip install -r requirements.txt
```
2. Запустите сбор данных (если хотите обновить):
```bash
python scripts/hh_parser.py
```
3. Откройте ноутбук:
```bash
jupyter notebook notebooks/job_analysis.ipynb
```
В ходе нашей исследовательской работы было выявленно: 
1. Заработная плата существенно выше у специалистов с большим опытом: от 200 000 до 600 000 рублей.
2. Навыки работодателей выявить затруднительно — во многих вакансиях поле с ключевыми навыками либо не заполнено, либо указано неполно.
3. Москва лидирует по количеству IT-вакансий — значительно опережая другие регионы.
4. Наивысшую зарплату получают кандидаты с опытом более 6 лет.
