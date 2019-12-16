import requests
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

sql_insert = "insert into douban2019(id, title, rate, short_comment, duration, subtype, region, release_year, create_date) values (%(id)s, %(title)s, %(rate)s, %(short_comment)s, %(duration)s, %(subtype)s, %(region)s, %(release_year)s, now())"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

flag = True

def get_movie_list(page_start):
    r = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=' + str(page_start), headers = headers)
    for item in r.json()['subjects']:
        get_movie_info(item['id'])

def get_movie_info(subject_id):
    r = requests.get('https://movie.douban.com/j/subject_abstract?subject_id=' + str(subject_id), headers=headers)

    subject = r.json()['subject']

    if subject['release_year'] != '2019':
        global flag
        flag = False
        return

    print(subject)

    insert_data = {
        "id": subject['id'],
        "title": subject['title'],
        "rate": subject['rate'],
        "short_comment": subject['short_comment']['content'],
        "duration": subject['duration'],
        "subtype": subject['subtype'],
        "region": subject['region'],
        "release_year": subject['release_year']
    }
    cursor.execute(sql_insert, insert_data)
    conn.commit()
    print(subject['title'], '写入完成')



def main():
    num = 0
    while(flag):
        get_movie_list(num)
        num += 20

if __name__ == '__main__':
    main()