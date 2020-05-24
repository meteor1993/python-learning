import requests
from datetime import datetime

def catch_data():
    """
    抓取当前实时数据，并返回 国家、大洲、确诊、疑似、死亡、治愈 列表
    :return:
    """
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    data = requests.post(url).json()['data']

    date_list = list()  # 日期
    name_list = list() # 国家
    continent_list = list() # 大洲
    confirm_list = list()  # 确诊
    suspect_list = list()  # 疑似
    dead_list = list()  # 死亡
    heal_list = list()  # 治愈

    for item in data:
        month, day = item['date'].split('.')
        date_list.append(datetime.strptime('2020-%s-%s' % (month, day), '%Y-%m-%d'))
        name_list.append(item['name'])
        continent_list.append(item['continent'])
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))

    return date_list, name_list, continent_list, confirm_list, suspect_list, dead_list, heal_list


def save_csv():
    """
    将数据存入 csv 文件
    :return:
    """
    date_list, name_list, continent_list, confirm_list, suspect_list, dead_list, heal_list = catch_data()
    fw = open('2019-nCoV.csv', 'w', encoding='utf-8')
    fw.write('date,name,continent,confirm,suspect,dead,heal\n')

    i = 0
    while i < len(date_list):
        date = str(date_list[i].strftime("%Y-%m-%d"))
        fw.write(date + ',' + str(name_list[i]) + ',' + str(continent_list[i]) + ',' + str(confirm_list[i]) + ',' + str(suspect_list[i]) + ',' + str(dead_list[i]) + ',' + str(heal_list[i]) + '\n')
        i = i + 1
    else:
        print("csv 写入完成")
        fw.close()


if __name__ == '__main__':
    save_csv()