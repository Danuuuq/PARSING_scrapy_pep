import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css(
            'section[id="index-by-category"] tbody tr td a::attr(href)')
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.xpath('//h1[contains(., "PEP")]/text()').get()
        number = re.search(r'PEP (\d+)', name)
        status = response.css('dt:contains("Status") + dd')
        data = {
            'number': number[1],
            'name': name,
            'status': status.css('abbr::text').get(),
        }
        yield PepParseItem(data)
