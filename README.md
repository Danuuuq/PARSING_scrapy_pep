# Парсер PEP на Scrapy

Этот проект Scrapy предназначен для парсинга информации о PEP (Предложениях по улучшению Python) с [peps.python.org](https://peps.python.org/). Паук собирает данные о каждом PEP, включая его номер, название и текущий статус, а затем сохраняет результаты в файлы CSV.

## Структура проекта

- **spiders/pep_spider.py**: Содержит основного паука (`PepSpider`), который парсит список PEP и их подробности.
- **pipelines.py**: Пайплайн для агрегации и сохранения количества PEP по статусам в конце процесса парсинга.

## Паук: `PepSpider`

Паук `PepSpider` парсит главную страницу PEP и собирает следующие данные для каждого PEP со страницы каждого PEP:

- **Номер PEP**: Извлекается из названия PEP (например, "PEP 123").
- **Название PEP**: Полное название PEP.
- **Статус PEP**: Текущий статус PEP (например, Active, Final и т.д.).

### Логика работы паука

1. **Начальный URL**: `https://peps.python.org/`
2. **Шаг 1**: Парсит индекс PEP и собирает ссылки на страницы отдельных PEP.
3. **Шаг 2**: Переходит по каждой ссылке PEP и извлекает соответствующие данные (номер, название и статус).
4. **Шаг 3**: Возвращает извлеченные данные в виде `PepParseItem` для дальнейшей обработки в пайплайне.

## Пайплайн: PepParsePipeline

Пайплайн обрабатывает каждый элемент и отслеживает количество PEP для каждого статуса. Когда паук завершает работу, он сохраняет сводный CSV-файл с количеством PEP по статусам.

### Логика работы пайплайна:  
1. **Открытие паука**: Инициализация словаря для подсчета количества PEP по каждому статусу.
2. **Обработка элемента**: Для каждого элемента (PEP) увеличивается соответствующий счётчик по статусу.
3. **Закрытие паука**: Когда все элементы обработаны, сохраняет результаты в сводный CSV-файл.

## Вывод:
- CSV-файл с именем *pep_<timestamp>.csv*, содержащий все PEP и их статусы.
- Сводный CSV-файл с именем *status_summary_<timestamp>.csv*, содержащий количество PEP по статусам.
- Файлы CSV сохраняются в директории *results*.

### Пример собранных данных

```csv
number,name,status
1,PEP 1 – PEP Purpose and Guidelines,Active
```

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/pep_scraper.git
    cd pep_scraper
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск парсера

Для запуска паука и парсинга данных PEP используйте следующую команду:

```bash
scrapy crawl pep
```

Это сгенерирует два CSV-файла в директории `results`:

1. **pep_<timestamp>.csv**: Список всех PEP и их данные.
2. **status_summary_<timestamp>.csv**: Сводка статусов PEP.

## Запуск тестов

Если у вас настроены тесты (например, с использованием `pytest`), вы можете запустить их командой:

```bash
pytest
```
