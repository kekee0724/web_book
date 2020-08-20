// # 1.图书总入口
// base_url = 'https://book.jd.com/booksort.html'
//
// # 2.爬取的是 每个小分类的 链接
// # 2.1 解析大分类的名字 -52个大分类
//
// # 2.2 解析小分类的名字和链接 --882个
//     # 获取所有大分类标签 dt
//     dt_list = '//*[@id="booksort"]/div[2]/dl/dt'
//
//     # 遍历52个大分类
//     for dt in dt_list:
//         category = './a/text()'
//         # 根据大分类取小分类
//         em_list = './following-sibling::*[1]/em'
//
//         for em in em_list:
//             small_category = './a/text()'
//             # 注意点: 小分类的链接 需要拼接
//             small_link = 'http:' + './a/@href'
//
//     # 访问爬取 每个小分类的数据--
//     # 解析 列表页的书
//     # 解析所有的数据 --60
//     list_book = '//*[@id="plist"]/ul/li/div'
//
//     # 遍历解析 60本书 个 详细信息
//     for book in list_book:
//         # 书名
//         name = './/div[@class="p-name"]/a/em/text()'
//         # 作者
//         author = './/span[@class="p-bi-name"]/span/a/text()'
//         # 出版社
//         store = './/span[@class="p-bi-store"]/a/text()'
//         # 价格
//         price = './/strong[@class="J_price"]/i/text()'
//         # 图片地址
//         default_image = './/div[@class="p-img"]/a/img/@src'
//
// # 3.图书列表页的翻页
//     # 解析 下一页的网址
//     next_url = '//a[@class="pn-next"]/@href'
//     如果没有值 代表当前小分类抓取完毕
