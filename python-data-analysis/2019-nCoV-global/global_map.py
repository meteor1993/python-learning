from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import namemap

def read_country_code():
    """
    获取国家中英文字典
    :return:
    """
    country_dict = {}
    for key, val in namemap.nameMap.items():  # 将 nameMap 列表里面键值互换
        country_dict[val] = key
    return country_dict

def read_csv():
    """
    读取数据，返回国家英文名称列表和累计确诊数列表
    :return:
    """
    country_dict = read_country_code()
    data = pd.read_csv("2019-nCoV.csv", index_col=False)

    countrys_names = list()
    confirmed_count = list()

    for x in range(len(data.index)):
        if data['name'].iloc[x] in country_dict.keys():
            countrys_names.append(country_dict[data['name'].iloc[x]])
            confirmed_count.append(data['confirm'].iloc[x])
        else:
            print(data['name'].iloc[x])

    return countrys_names, confirmed_count


def draw_map():
    """
    绘制世界地图
    遇到一个很神奇的问题：
    两个列表必须写死数据地图才会渲染数据，如果数据是从方法中获得，则地图不渲染数据
    :return:
    """

    # 修复注释中的问题，原因是 confirmed_count 中的 int 是 numpy 的 int ，需转化为 python 中的 int
    # 感谢公众号的 @李康伟 同学提出
    countrys_names, confirmed_count = read_csv()
    confirmed_count_list = []
    for item in confirmed_count:
        confirmed_count_list.append(int(item))

    # countrys_names = ['United States', 'Brazil', 'Russia', 'Spain', 'United Kingdom', 'Italy', 'France', 'Germany', 'Turkey', 'Iran', 'India', 'Peru', 'Canada', 'Saudi Arabia', 'Mexico', 'Chile', 'Belgium', 'Pakistan', 'Netherlands', 'Qatar', 'Ecuador', 'Belarus', 'Sweden', 'Bangladesh', 'Singapore Rep.', 'Switzerland', 'Portugal', 'United Arab Emirates', 'Ireland', 'Indonesia', 'South Africa', 'Poland', 'Ukraine', 'Kuwait', 'Colombia', 'Romania', 'Israel', 'Japan', 'Egypt', 'Austria', 'Dominican Rep.', 'Philippines', 'Denmark', 'Argentina', 'Korea', 'Serbia', 'Panama', 'Afghanistan', 'Czech Rep.', 'Norway', 'Kazakhstan', 'Algeria', 'Nigeria', 'Morocco', 'Oman', 'Malaysia', 'Australia', 'Moldova', 'Ghana', 'Finland', 'Armenia', 'Bolivia', 'Cameroon', 'Iraq', 'Luxembourg', 'Azerbaijan', 'Honduras', 'Hungary', 'Sudan', 'Guinea', 'Uzbekistan', 'Guatemala', 'Thailand', 'Senegal', 'Greece', 'Tajikistan', 'Bulgaria', "Côte d'Ivoire", 'Djibouti', 'Croatia', 'Gabon', 'Cuba', 'Estonia', 'El Salvador', 'Iceland', 'Lithuania', 'Somalia', 'New Zealand', 'Slovakia', 'Slovenia', 'Kyrgyzstan', 'Kenya', 'Guinea Bissau', 'Lebanon', 'Sri Lanka', 'Tunisia', 'Latvia', 'Mali', 'Venezuela', 'Albania', 'Eq. Guinea', 'Niger', 'Cyprus', 'Zambia', 'Costa Rica', 'Haiti', 'Paraguay', 'Burkina Faso', 'Uruguay', 'Georgia', 'Jordan', 'Chad', 'Sierra Leone', 'Nepal', 'Jamaica', 'Tanzania', 'Ethiopia', 'Madagascar', 'Palestine', 'Togo', 'Vietnam', 'Rwanda', 'Montenegro', 'Nicaragua', 'Liberia', 'Swaziland', 'Mauritania', 'Yemen', 'Myanmar', 'Uganda', 'Mozambique', 'Mongolia', 'Brunei', 'Benin', 'Guyana', 'Cambodia', 'The Bahamas', 'Malawi', 'Libya', 'Syria', 'Angola', 'Zimbabwe', 'Burundi', 'Eritrea', 'Botswana', 'Gambia', 'Bhutan', 'East Timor', 'Namibia', 'Lao PDR', 'Fiji', 'Belize', 'Suriname', 'Papua New Guinea', 'Lesotho']
    # 
    # confirmed_count = [1666828, 347398, 335882, 281904, 258504, 229327, 182036, 179986, 155686, 133521, 131920, 115754, 85151, 70161, 65856, 65393, 56810, 54601, 45265, 42213, 36258, 35244, 33188, 32078, 31068, 30725, 30471, 28704, 24582, 21745, 21343, 20931, 20580, 20464, 20177, 17857, 16712, 16536, 16513, 16486, 14422, 13777, 11487, 11353, 11190, 11092, 10577, 9998, 8890, 8346, 8322, 8113, 7526, 7406, 7257, 7185, 7114, 6994, 6617, 6568, 6302, 5915, 4400, 4272, 3990, 3982, 3743, 3741, 3628, 3176, 3132, 3054, 3040, 2976, 2876, 2738, 2427, 2366, 2270, 2243, 1934, 1931, 1821, 1819, 1804, 1616, 1594, 1504, 1504, 1468, 1403, 1192, 1114, 1097, 1089, 1048, 1046, 1015, 1010, 989, 960, 943, 927, 920, 918, 865, 850, 814, 764, 728, 704, 648, 621, 584, 550, 509, 494, 488, 423, 373, 325, 325, 324, 279, 255, 238, 227, 212, 201, 198, 168, 141, 141, 135, 127, 124, 100, 82, 75, 70, 61, 56, 42, 39, 30, 25, 24, 24, 20, 19, 18, 18, 11, 8, 2]


    c = (
        Map()
        .add(
            "确诊人数",
            [list(z) for z in zip(countrys_names, confirmed_count_list)],
            is_map_symbol_show=False,
            maptype="world",
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)")
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全球 2019-nCoV 地图"),
            visualmap_opts=opts.VisualMapOpts(max_=1700000),
        )
        .render("map_world.html")
    )


if __name__ == '__main__':
    draw_map()

