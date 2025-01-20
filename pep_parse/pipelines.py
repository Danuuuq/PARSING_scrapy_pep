from collections import defaultdict
from datetime import datetime as dt
import os


class PepParsePipeline:

    def open_spider(self, spider):
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        feeds = spider.settings.get('FEEDS')
        output_dir = os.path.dirname(next(iter(feeds)))
        date = dt.strftime(dt.now(), '%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(output_dir, f'status_summary_{date}.csv')
        self.result['Total'] = sum(self.result.values())
        with open(filename, mode='w', encoding='UTF-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.result.items():
                f.write(f'{status},{count}\n')
