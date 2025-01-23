import csv
import os
from collections import defaultdict
from datetime import datetime as dt


class PepParsePipeline:

    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    @classmethod
    def from_crawler(cls, crawler):
        feeds = crawler.settings.get('FEEDS')
        return cls(os.path.dirname(next(iter(feeds))))

    def open_spider(self, spider):
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = dt.strftime(dt.now(), '%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(self.output_dir, f'status_summary_{date}.csv')
        with open(filename, mode='w', encoding='UTF-8', newline='') as csvfile:
            rows = (
                ('Статус', 'Количество'),
                *self.result.items(),
                ('Total', sum(self.result.values()))
            )
            writer = csv.writer(csvfile)
            writer.writerows(rows)
