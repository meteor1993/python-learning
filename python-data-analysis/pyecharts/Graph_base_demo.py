from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "肖恩", "symbolSize": 10},
    {"name": "海棠朵朵", "symbolSize": 20},
    {"name": "长公主", "symbolSize": 30},
    {"name": "陈萍萍", "symbolSize": 40},
    {"name": "范闲", "symbolSize": 50},
    {"name": "林婉儿", "symbolSize": 40},
    {"name": "庆帝", "symbolSize": 30},
    {"name": "范若若", "symbolSize": 20},
    {"name": "司理理", "symbolSize": 10}
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="庆余年人物关系图"))
    .render("graph_base.html")
)
