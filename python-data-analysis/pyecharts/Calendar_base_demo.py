import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


begin = datetime.date(2019, 1, 1)
end = datetime.date(2019, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1, 20)]
    for i in range((end - begin).days + 1)
]

c = (
    Calendar()
    .add("", data, calendar_opts=opts.CalendarOpts(range_="2019"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2019 Github 提交情况"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20,
            min_=1,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("calendar_base.html")
)
