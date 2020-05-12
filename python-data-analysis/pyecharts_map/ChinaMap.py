from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Map(init_opts=opts.InitOpts(
        theme=ThemeType.DARK,
        bg_color='#404a59'
    ))
    .add(
        "中国地图",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        "china"
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图-示例"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("china_map.html")
)