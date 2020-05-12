from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

shanghai_list = ['黄浦区', '徐汇区', '长宁区', '静安区', '普陀区', '虹口区', '杨浦区', '闵行区', '宝山区', '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区', '浦东新区']

shanghai_people = [65.38, 108.44, 69.4, 106.28, 128.19, 79.7, 131.27, 254.35, 204.23, 158.89, 80.5, 176.22, 121.9, 115.2, 68.81, 555.02]

BAIDU_LINK='https://baike.baidu.com/item/%E4%B8%8A%E6%B5%B7%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92/7426389?fr=aladdin'

c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, bg_color='#404a59', width='800px', height='450px'))
    .add("常住人口", [list(z) for z in zip(shanghai_list, shanghai_people)], "上海")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="上海地图-常住人口（单位：万人）",
            subtitle="常住人口数据来自百度百科",
            subtitle_link=BAIDU_LINK,
        ),
        visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_shanghai.html")
)