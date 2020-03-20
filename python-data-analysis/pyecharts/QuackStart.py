from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis([2011,2012,2013,2014,2015,2016,2017])
bar.add_yaxis("产品销量", [58000,60200,63000,71000,84000,90500,107000])

bar.render()

# 链式调用
# bar = (
#     Bar()
#     .add_xaxis([2011,2012,2013,2014,2015,2016,2017])
#     .add_yaxis("产品销量", [58000,60200,63000,71000,84000,90500,107000])
# )
#
# bar.render()

bar = (
    Bar()
    .add_xaxis([2011,2012,2013,2014,2015,2016,2017])
    .add_yaxis("产品销量", [58000,60200,63000,71000,84000,90500,107000])
    .set_global_opts(title_opts=opts.TitleOpts(title="11 ~ 17年 xxx 公司 xx 产品销量图", subtitle="这里是副标题"))
)
bar.render('render_1.html')

# 调用方法写法，与上面的链式调用无任何区别
# bar = Bar()
# bar.add_xaxis([2011,2012,2013,2014,2015,2016,2017])
# bar.add_yaxis("产品销量", [58000,60200,63000,71000,84000,90500,107000])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="11 ~ 17年 xxx 公司 xx 产品销量图", subtitle="这里是副标题"))
# bar.render('render_1.html')

# 生成图片
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot

bar = (
    Bar()
        .add_xaxis([2011, 2012, 2013, 2014, 2015, 2016, 2017])
        .add_yaxis("产品销量", [58000, 60200, 63000, 71000, 84000, 90500, 107000])
        .set_global_opts(title_opts=opts.TitleOpts(title="11 ~ 17年 xxx 公司 xx 产品销量图", subtitle="这里是副标题"))
)
make_snapshot(snapshot, bar.render(), "bar.png")

# 使用主题
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis([2011, 2012, 2013, 2014, 2015, 2016, 2017])
        .add_yaxis("产品A", [58000, 60200, 63000, 71000, 84000, 90500, 107000])
        .add_yaxis("产品B", [78000,80200,93000,101000,64000,70500,87000])
        .set_global_opts(title_opts=opts.TitleOpts(title="11 ~ 17年 xxx 公司 xx 产品销量图", subtitle="这里是副标题"))
)

bar.render('render_2.html')