import requests
from pyquery import PyQuery
import pymysql

# 数据库连接
def connect():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='password',
                           database='test',
                           charset='utf8mb4')

    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}

connection = connect()
conn, cursor = connection['conn'], connection['cursor']

sql_insert = "INSERT INTO `lianjia` VALUES (%(id)s, %(danjia)s, %(zongjia)s, %(quyu)s, %(xiaoqu)s, %(huxing)s, %(louceng)s, %(jianmian)s, %(jiegou)s, %(taoneimianji)s, %(jianzhuleixing)s, %(chaoxiang)s, %(jianzhujiegou)s, %(zhuangxiu)s, %(tihubili)s, %(dianti)s, %(chanquan)s, %(guapaishijian)s, %(jiaoyiquanshu)s, %(shangcijiaoyi)s, %(fangwuyongtu)s, %(fangwunianxian)s, %(chanquansuoshu)s, %(diyaxinxi)s, now())"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

def get_outer_list(maxNum):
    list = []
    for i in range(1, maxNum + 1):
        url = 'https://sh.lianjia.com/ershoufang/pg' + str(i)
        print('正在爬取的链接为： %s' %url)
        response = requests.get(url, headers=headers)
        print('正在获取第 %d 页房源' % i)
        doc = PyQuery(response.text)
        num = 0
        for item in doc('.sellListContent li').items():
            num += 1
            list.append(item.attr('data-lj_action_housedel_id'))
        print('当前页面房源共 %d 套' %num)
    return list

def get_inner_info(list):
    for i in list:
        try:
            response = requests.get('https://sh.lianjia.com/ershoufang/' + str(i) + '.html', headers=headers)
            doc = PyQuery(response.text)

            # 基本属性解析
            base_li_item = doc('.base .content ul li').remove('.label').items()
            base_li_list = []
            for item in base_li_item:
                base_li_list.append(item.text())

            # 交易属性解析
            transaction_li_item = doc('.transaction .content ul li').items()
            transaction_li_list = []
            for item in transaction_li_item:
                transaction_li_list.append(item.children().not_('.label').text())

            insert_data = {
                "id": i,
                "danjia": doc('.unitPriceValue').remove('i').text(),
                "zongjia": doc('.price .total').text() + '万',
                "quyu": doc('.areaName .info').text(),
                "xiaoqu": doc('.communityName .info').text(),
                "huxing": base_li_list[0],
                "louceng": base_li_list[1],
                "jianmian": base_li_list[2],
                "jiegou": base_li_list[3],
                "taoneimianji": base_li_list[4],
                "jianzhuleixing": base_li_list[5],
                "chaoxiang": base_li_list[6],
                "jianzhujiegou": base_li_list[7],
                "zhuangxiu": base_li_list[8],
                "tihubili": base_li_list[9],
                "dianti": base_li_list[10],
                "chanquan": base_li_list[11],
                "guapaishijian": transaction_li_list[0],
                "jiaoyiquanshu": transaction_li_list[1],
                "shangcijiaoyi": transaction_li_list[2],
                "fangwuyongtu": transaction_li_list[3],
                "fangwunianxian": transaction_li_list[4],
                "chanquansuoshu": transaction_li_list[5],
                "diyaxinxi": transaction_li_list[6]
            }
            cursor.execute(sql_insert, insert_data)
            conn.commit()
            print(i, '：写入完成')
        except:
            print(i, '：写入异常')
            continue


def main():
    lists = get_outer_list(100)
    print('共计获取房源：', len(list(set(lists))))
    get_inner_info(list(set(lists)))

if __name__ == '__main__':
    main()