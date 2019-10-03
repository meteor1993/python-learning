-- 因为掘金使用的是排名是掘力值，顾取出来的数据是负数
SELECT
	a.read_num - (SELECT b.read_num FROM spider_data b WHERE b.plantform = 'cnblog' AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), interval 1 day)) AS read_num,
	a.fans_num - (SELECT b.fans_num FROM spider_data b WHERE b.plantform = 'cnblog' AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), interval 1 day)) AS fans_num,
	a.like_num - (SELECT b.like_num FROM spider_data b WHERE b.plantform = 'cnblog' AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), interval 1 day)) AS like_num,
	(SELECT b.rank_num FROM spider_data b WHERE b.plantform = 'cnblog' AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), interval 1 day)) - a.rank_num AS rank_num,
	a.create_date
FROM
	spider_data a
WHERE
	a.plantform = 'cnblog' 
GROUP BY
	DATE_FORMAT(a.create_date, '%Y-%m-%d');