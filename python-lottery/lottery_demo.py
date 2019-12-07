import random
import pymysql

# 获取中奖配置
def get_lottery_rate():
    conn = pymysql.connect(host='114.67.111.196', port = 3306, user='root', password='wsy@123456', database='test', charset='utf8mb4')
    try:
        sql = 'SELECT * FROM rate order by id asc '
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

# 判断中奖函数
def lottery():
    config = get_lottery_rate()
    flag = random.randint(1, config[0][2])
    if flag <= config[0][1]:
        return 1
    elif flag > config[0][1] and flag <= (config[1][1] + config[0][1]):
        return 2
    elif flag > (config[1][1] + config[0][1]) and flag <= (config[2][1] + config[1][1]):
        return 3
    else:
        return 0

# 判断会员等级中奖率过滤
# 会员等级 1.白银会员 2.黄金会员 3. 钻石会员
def vip_lottery(level):
    rate = random.randint(1, 10)
    # 如果是钻石会员，直接进入抽奖函数
    if level == 3:
        return lottery()
    # 如果是黄金会员， 50% 概率进入抽奖函数
    elif level == 2:
        if rate <= 5:
            return lottery()
        else:
            return 0
    # 如果是白银会员， 20% 概率进入抽奖函数
    elif level == 1:
        if rate <= 2:
            return lottery()
        else:
            return 0
    # 如果是其他，直接返回未中奖
    else:
        return 0

# 批量测试方法
def test():
    # 一等奖中奖次数
    a = 0
    # 二等奖中奖次数
    b = 0
    # 三等奖中奖次数
    c = 0
    # 未中奖次数
    d = 0
    # 循环次数
    e = 0
    for i in range(1000):
        e += 1
        print('当前循环次数：', e)
        result = lottery()
        print('当前中奖结果：', result)
        if (result == 1):
            a += 1
        elif (result == 2):
            b += 1
        elif (result == 3):
            c += 1
        else:
            d += 1

    print('一等奖中奖：', a, '，二等奖中奖次数：', b, '，三等奖中奖次数：', c, '，未中奖次数：', d)

# 会员制中奖测试方法
def test_vip():
    print('请输入您当前的会员等级：1.白银会员 2.黄金会员 3. 钻石会员')
    level = input()
    result = vip_lottery(int(level))
    if (result == 1):
        print('恭喜您中了一等奖')
    elif (result == 2):
        print('恭喜您中了二等奖')
    elif (result == 3):
        print('恭喜您中了三等奖')
    else:
        print('未中奖，谢谢惠顾')

if __name__ == '__main__':
    test_vip()