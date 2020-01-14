import requests
from pyquery import PyQuery
import xlsxwriter

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'cookie': '__jsluid_s=6fc5b4a3b5235afbfdafff4bbf7e6dbd; PHPSESSID=v9hm8hc3s56ogrn8si12fejdm3; mfw_uuid=5e1db855-ab4a-da12-309c-afb9cf90d3dd; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.baidu.com%2Flink%22%3Bs%3A1%3A%22t%22%3Bi%3A1579006045%3B%7D; oad_n=a%3A5%3A%7Bs%3A5%3A%22refer%22%3Bs%3A21%3A%22https%3A%2F%2Fwww.baidu.com%22%3Bs%3A2%3A%22hp%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A3%3A%22oid%22%3Bi%3A1026%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222020-01-14+20%3A47%3A25%22%3B%7D; __mfwothchid=referrer%7Cwww.baidu.com; __omc_chl=; __mfwc=referrer%7Cwww.baidu.com; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1579006048; uva=s%3A264%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222020-01-14%22%3Bs%3A2%3A%22lt%22%3Bi%3A1579006046%3Bs%3A10%3A%22last_refer%22%3Bs%3A137%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuR5Oj9n_xm4TSj7_1drQ1HRnFTYNM0M2TCljkjVrdIiUE-B2qPgh0MifEkceLE_U%26wd%3D%26eqid%3D93c920a80002dc72000000035e1db85c%22%3Bs%3A5%3A%22rhost%22%3Bs%3A13%3A%22www.baidu.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1579006046%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5e1db855-ab4a-da12-309c-afb9cf90d3dd; UM_distinctid=16fa418373e40f-070db24dfac29d-c383f64-1fa400-16fa418373fe31; __jsluid_h=b3f11fd3c79469af5c49be9ecb7f7b86; __omc_r=; __mfwa=1579006047379.58159.3.1579011903001.1579015057723; __mfwlv=1579015057; __mfwvn=2; CNZZDATA30065558=cnzz_eid%3D448020855-1579003717-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1579014923; bottom_ad_status=0; __mfwb=5e663dbc8869.7.direct; __mfwlt=1579019025; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1579019026; __jsl_clearance=1579019146.235|0|fpZQ1rm7BHtgd6GdjVUIX8FJJ9o%3D'
}


s = requests.Session()


value = []

def getList(maxNum):
    """
    获取列表页面数据
    :param maxNum: 最大抓取页数
    :return:
    """
    url = 'http://www.mafengwo.cn/gonglve/'
    s.get(url, headers = headers)
    for page in range(1, maxNum + 1):
        data = {'page': page}
        response = s.post(url, data = data, headers = headers)
        doc = PyQuery(response.text)
        items = doc('.feed-item').items()
        for item in items:
            if item('.type strong').text() == '游记':
                # 如果是游记，则进入内页数据抓取
                inner_url = item('a').attr('href')
                getInfo(inner_url)


def getInfo(url):
    """
    获取内页数据
    :param url: 内页链接
    :return:
    """
    response = s.get(url, headers = headers)
    doc = PyQuery(response.text)
    title = doc('title').text()
    # 获取数据采集区
    item = doc('.tarvel_dir_list')
    if len(item) == 0:
        return
    time = item('.time').text()
    day = item('.day').text()
    people = item('.people').text()
    cost = item('.cost').text()
    # 数据格式化
    if time == '':
        pass
    else:
        time = time.split('/')[1] if len(time.split('/')) > 1 else ''

    if day == '':
        pass
    else:
        day = day.split('/')[1] if len(day.split('/')) > 1 else ''

    if people == '':
        pass
    else:
        people = people.split('/')[1] if len(people.split('/')) > 1 else ''

    if cost == '':
        pass
    else:
        cost = cost.split('/')[1] if len(cost.split('/')) > 1 else ''


    value.append([title, time, day, people, cost, url])


def write_excel_xlsx(value):
    """
    数据写入Excel
    :param value:
    :return:
    """
    index = len(value)

    workbook = xlsxwriter.Workbook('mfw.xlsx')
    sheet = workbook.add_worksheet()
    for i in range(1, index + 1):
        row = 'A' + str(i)
        sheet.write_row(row, value[i - 1])
    workbook.close()
    print("xlsx格式表格写入数据成功！")


def main():
    getList(5)
    write_excel_xlsx(value)

if __name__ == '__main__':
    main()