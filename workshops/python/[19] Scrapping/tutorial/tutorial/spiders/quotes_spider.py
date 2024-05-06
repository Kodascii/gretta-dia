from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        with open('./tutorial/spiders/urls.txt', 'rt', encoding='utf-8') as f:
            urls = f.readlines()

        for url in urls:
            print(f'==> url: {url}')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")