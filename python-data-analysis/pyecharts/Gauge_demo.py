from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add("", [("完成率", 80)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    .render("gauge_base.html")
)