import csv
import os
from collections import defaultdict
from datetime import datetime as dt


class PepParsePipeline:

    def open_spider(self, spider):
        feeds = spider.settings.get('FEEDS')
        self.output_dir = os.path.dirname(next(iter(feeds)))
        os.makedirs(self.output_dir, exist_ok=True)
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = dt.strftime(dt.now(), '%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(self.output_dir, f'status_summary_{date}.csv')
        # self.result['Total'] = sum(self.result.values())
        with open(filename, mode='w', encoding='UTF-8', newline='') as csvfile:
            breakpoint()
            # fields = ['Статус', 'Количество']
            # rows = [{fields[0]: status, fields[1]: count}
            #         for status, count in self.result.items()]
            # writer = csv.DictWriter(csvfile, fieldnames=fields)
            rows = (
                ('Статус', 'Количество'),
                *self.result.items(),
                ('Total', sum(self.result.values()))
            )
            writer = csv.DictWriter(csvfile)
            # writer.writeheader()
            writer.writerows(rows)
