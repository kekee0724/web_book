# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    # 第一层 爬取所有图书
    # start_urls = ['http://jd.com/']
    # 1.图书总入口
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # category_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a/text()').extract()#extract_first()
        # print('*' * 100)
        # print(category_list)
        # print('*' * 100)
        # print(response)
        # print(response.text)
        # 2.爬取的是 每个小分类的 链接
        # 2.1 解析大分类的名字 -52个大分类

        # 2.2 解析小分类的名字和链接 --882个
        # 获取所有大分类标签 dt
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt[1]')

        # 遍历52个大分类
        for dt in dt_list:
            # 完整的 图书数据 大分类 小分类 名字 作者 出版社 价格
            item = {}
            item['category'] = dt.xpath('./a/text()').extract_first()
            # 根据大分类取小分类
            em_list = dt.xpath('./following-sibling::*[1]/em')

            for em in em_list[:1]:
                item['small_category'] = em.xpath('./a/text()').extract_first()
                # 注意点: 小分类的链接 需要拼接
                small_link = 'http:' + em.xpath('./a/@href').extract_first()
                # print(item)
                # 发送 请求 获取小分类 里面 图书的列表
                yield scrapy.Request(small_link, callback=self.parse_book, meta={'book': item})

    def parse_book(self, response):
        item = response.meta.get('book')
        # 访问爬取 每个小分类的数据--
        # 解析 列表页的书
        # 解析所有的数据 --60
        list_book = response.xpath('//*[@id="plist"]/ul/li/div')

        # 遍历解析 60本书 个 详细信息
        for book in list_book[:3]:
            # 书名
            item['name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            # 作者
            item['author'] = book.xpath('.//span[@class="p-bi-name"]/span/a/text()').extract_first().strip()
            # 出版社
            item['store'] = book.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first()
            # 价格.//div[2]/strong[1]/i/text()             .//strong[@class="J_price"]/i/text()
            item['price'] = book.xpath('.//div[2]/strong[1]/i/text()').extract_first()
            # 图片地址
            item['default_image'] = 'http:' + book.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            # print(item)
            yield item    

        # 3.图书列表页的翻页
        # 解析 下一页的网址
        next_url = response.xpath('//a[@class="pn-next"]/@href')
        # 如果没有值
        # 代表当前小分类抓取完毕

# -*- coding: utf-8 -*-
# import scrapy
#
#
# class BookSpider(scrapy.Spider):
#     name = 'book'
#     allowed_domains = ['jd.com']
#     # 第一层 爬取所有图书--首页
#     start_urls = ['https://book.jd.com/booksort.html']
#
#
#     # 解析 大分类的名字  和 小分类的名字和链接
#     def parse(self, response):
#
#         # 获取所有大分类标签 dt
#         dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt[1]')
#
#         # 遍历52个大分类
#         for dt in dt_list:
#             item = {}
#             # 完整的 图书数据 大分类 小分类 名字 作者 出版社 价格
#             item['category'] = dt.xpath('./a/text()').extract_first()
#
#             # 根据大分类取小分类
#             em_list = dt.xpath('./following-sibling::*[1]/em')
#
#             for em in em_list[:1]:
#                 item['small_category'] = em.xpath('./a/text()').extract_first()
#                 # 注意点: 小分类的链接 需要拼接
#                 small_link = 'http:' + em.xpath('./a/@href').extract_first()
#
#
#                 # 发送 请求 获取小分类 里面 图书的列表
#                 yield scrapy.Request(small_link,callback=self.parse_book,meta={'book':item})
#
#     # 解析 书籍信息
#     def parse_book(self,response):
#
#         item = response.meta.get('book')
#
#         # 解析所有的数据 --60
#         list_book = response.xpath('//*[@id="plist"]/ul/li/div')
#
#         # 遍历解析 60本书 个 详细信息
#         for book in list_book[:2]:
#             # 书名
#             item['name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first()
#             # 作者
#             item['author'] = book.xpath('.//span[@class="p-bi-name"]/span/a/text()').extract_first()
#             # 出版社
#             item['store'] = book.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first()
#             # 价格
#             item['price'] = book.xpath('.//strong[@class="J_price"]/i/text()').extract_first()
#             # 图片地址
#             item['default_image'] = book.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
#
#             yield item
#
