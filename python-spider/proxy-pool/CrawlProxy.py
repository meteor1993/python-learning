import requests
from pyquery import PyQuery
from MysqlClient import MysqlClient
from VerifyProxy import VerifyProxy

class CrawlProxy(object):

    def __init__(self):
        self.mysql = MysqlClient()
        self.verify = VerifyProxy()

    def get_page(self, url, charset):
        response = requests.get(url)
        response.encoding = charset
        return response.text

    def crawl_ip3366(self, page_num = 3):
        """
        获取代理 ip3366
        :param page_num:
        :return:
        """
        start_url = 'http://www.ip3366.net/?stype=1&page={}'
        urls = [start_url.format(page) for page in range(1, page_num + 1)]
        for url in urls:
            print('crawl:', url)
            html = self.get_page(url, 'gb2312')
            if html:
                d = PyQuery(html)
                trs = d('.table-bordered tbody tr').items()
                for tr in trs:
                    scheme = tr.find('td:nth-child(4)').text().lower()
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    verify_result = self.verify.verify_proxy(scheme, ip, port)

                    if verify_result["status"] == '1':
                        proxy = {
                            "scheme": scheme,
                            "ip": ip,
                            "port": port,
                            "status": verify_result["status"],
                            "response_time": verify_result["response_time"],
                        }
                        # 存入数据库
                        self.mysql.add_proxy(proxy)
                        print('代理', ip, '连通测试已通过，已保存 Mysql')
                    else:
                        print('代理', ip, '连通测试未通过')

if __name__ == '__main__':
    CrawlProxy().crawl_ip3366()