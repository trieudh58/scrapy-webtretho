import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['webtretho.com']
    # f2956
    # root_url = 'http://zaodich.webtretho.com/forum/f2956/'

    # f2516
    # root_url = 'http://zaodich.webtretho.com/forum/f2516/'

    # f2923
    # root_url = 'http://zaodich.webtretho.com/forum/f2923/'

    # f3499
    # root_url = 'http://www.webtretho.com/forum/f3499/'

    # f630
    root_url = 'http://www.webtretho.com/forum/f630/'

    start_urls = []

    url = ''
    # f2956
    # for i in range(0, 144):

    # f2516
    # for i in range(0, 322):

    # f2923
    # for i in range(0, 236):

    # f3499
    # for i in range(0, 17):

    # f2484
    # root_url = 'http://zaodich.webtretho.com/forum/f2484/'

    # f630
    for i in range(0, 146):

    # f2484
    # for i in range(0, 100):
        url = root_url + 'index' + str(i) + '.html'
        start_urls.append(url)

    def parse(self, response):
        for href in response.xpath('//div[@class="titleTypPost"]/div/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

        # file_name = response.url.split('/')[-2] + '.html'
        # with open(file_name, 'wb') as f:
        #     f.write(response.body)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[@class="content"]/div'):
            body = ''
            arr = map(unicode.strip, sel.xpath('blockquote[@class="postcontent restore"]/text()').extract())

            for x in arr:
                if x != '' and x != ' ':
                    x = x.rstrip('\n')
                    body = body + x

            # print body
            length = len(body)
            # length = len(arr)
            if 10 < length < 5000:
                item = DmozItem()
                item['post_id'] = sel.xpath('@id').extract()
                item['post_body'] = body
                yield item
            else:
                continue
