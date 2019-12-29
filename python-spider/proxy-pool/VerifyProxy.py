import requests
from MysqlClient import MysqlClient

class VerifyProxy(object):
    def __init__(self):
        self.mysql = MysqlClient()

    def verify_proxy(self, scheme, ip, port):
        """
        使用百度测试代理的连通性，并返回响应时长（单位：ms）
        :param scheme:
        :param ip:
        :param port:
        :return:
        """
        proxies = {
            scheme: scheme + '://' + ip + ':' + port + '/'
        }
        response_time = 0
        status = '0'
        try:
            response = requests.get(scheme + '://www.baidu.com/get', proxies=proxies)
            if response.ok:
                response_time = round(response.elapsed.total_seconds() * 1000)
                status = '1'
            else:
                response_time = 0
                status = '0'
        except:
            pass
        return {"response_time" : response_time, "status" : status}

    def verify_all(self):
        """
        验证住方法，从数据库中获取所有代理进行验证
        :return:
        """
        results = self.mysql.find_all()
        for result in results:
            res = self.verify_proxy(result[1], result[2], result[3])
            proxy = {
                "id": result[0],
                "scheme": result[1],
                "ip": result[2],
                "port": result[3],
                "status": res["status"],
                "response_time": res["response_time"],
            }
            self.mysql.update_proxy(proxy)
            print('代理验证成功')

if __name__ == '__main__':
    VerifyProxy().verify_all()