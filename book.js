// # 1.图书总入口
// base_url = 'https://book.jd.com/booksort.html'
//
// # 2.爬取的是 每个小分类的 链接
// # 2.1 解析大分类的名字 -52个大分类
//     category = '//dt/a/text()'
// # 2.2 解析小分类的名字和链接 --882个
//     small_category = '//em/a/text()'
//     # 注意点: 小分类的链接 需要拼接
//     small_link = 'http:' + '//em/a/@href'
//
//     # 访问爬取 每个小分类的数据--
//     # 解析 列表页的书
//     # 解析所有的数据 --60
//     list_book = '//*[@id="plist"]/ul/li/div'
//
//     # 遍历解析 60本书 个 详细信息
// //*[@id="plist"]/ul/li/div/div[1]
// //*[@id="plist"]/ul/li/div/div[2]
// //*[@id="plist"]/ul/li/div/div[3]
// //*[@id="plist"]/ul/li/div/div[4]/span[1]
// //*[@id="plist"]/ul/li/div/div[4]/span[2]
// //*[@id="plist"]/ul/li/div/div[4]/span[3]
//     for book in list_book:
//         # 书名 './/div/div[3]/a/em/text()' #64
//         name = './/div[@class="p-name"]/a/em/text()' #69
//         # 作者 './/div[4]/span[1]/span/a/text()' #76
//         author = './/span[@class="p-bi-name"]/span/a/text()' #76
//         # 出版社 './/div[4]/span[2]/a/text()' #64
//         store = './/span[@class="p-bi-store"]/a/text()' #64
//         # 价格 './/div[2]/strong[1]/i/text()' #64
//         price = './/strong[@class="J_price"]/i/text()' #64
//         # 图片地址 './/div/a/img/@src' #56
//         default_image = './/div[@class="p-img"]/a/img/@src' #56
//
// # 3.图书列表页的翻页
//     # 解析 下一页的网址
//     next_url = '//a[@class="pn-next"]/@href'
//     如果没有值 代表当前小分类抓取完毕

// scrapy startproject BOOK
// cd BOOK
// scrapy genspider book jd.com
// scrapy crawl book