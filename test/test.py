# Created by kekee0724 with Pycharm
# https://fe-api.zhaopin.com/c/i/city-page/user-city?ipCity=武汉
# https://dict.zhaopin.cn/dict/dictOpenService/getDict?dictNames=region_relation,education,recruitment,education_specialty,industry_relation,careet_status,job_type_parent,job_type_relation

"""
本次的数据爬取只做简单的反爬虫预防策略
"""
import requests
import os
import json

class siper(object):
    def __init__(self):
        self.header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Origin":"https://sou.zhaopin.com",
            "Host":"fe-api.zhaopin.com",
            "Accept-Encoding":"gzip, deflate, br"
        }
        print("职位查询程序开始······")
        # 打开文件
        self.file = "result.json"
        path = os.getcwd()
        pathfile = os.path.join(path,self.file)
        self.fp = open(pathfile,"w",encoding="utf-8")
        self.fp.write("[\n")

    def get_response(self,url):
        return requests.get(url=url,headers = self.header)

    def get_citycode(self,city):
        url = "https://fe-api.zhaopin.com/c/i/city-page/user-city?ipCity={}".format(city)
        response = self.get_response(url)
        result = json.loads(response.text)
        return result['data']['code']

    def parse_data(self,url):
        response = self.get_response(url)
        result = json.loads(response.text)['data']['results']
        items = []
        for i in result:
            item = {}
            item['职位'] = i['jobName']
            item['工资'] = i['salary']
            item['招聘状态'] = i['timeState']
            item['经验要求'] = i['workingExp']['name']
            item['学历要求'] = i['eduLevel']['name']
            items.append(item)
        return items

    def save_data(self,items):
        num = 0
        for i in items:
            num = num + 1
            self.fp.write(json.dumps(i,ensure_ascii=False))
            if num == len(items):
                self.fp.write("\n")
            else:
                self.fp.write(",\n")
            print("%s--%s"%(str(num),str(i)))

    def end(self):
        self.fp.write("]")
        self.fp.close()
        print("职位查询程序结束······")
        print("数据已写入到{}文件中······".format(self.file))

    def main(self):
        try:
            cityname = input("请输入你要查询的城市的名称（市级城市）：")
            city = self.get_citycode(cityname)
            url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=200&cityId={}&workExperience=-1&education=5&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3".format(
                city)
            items = self.parse_data(url)
            self.save_data(items)
            self.end()
        except Exception as e:
            print("城市输入错误！！！（强制退出程序）")
            print(e)
            os._exit(0)


if __name__ == '__main__':
    siper = siper()
    siper.main()