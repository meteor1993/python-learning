-- 因为掘金使用的是排名是掘力值，顾取出来的数据是负数
SELECT a.read_num - (
		SELECT b.read_num
		FROM spider_data b
		WHERE b.plantform = a.plantform
			AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), INTERVAL 1 DAY) 
		ORDER BY b.create_date DESC LIMIT 1
	) AS read_num, a.fans_num - (
		SELECT b.fans_num
		FROM spider_data b
		WHERE b.plantform = a.plantform
			AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), INTERVAL 1 DAY)
		ORDER BY b.create_date DESC LIMIT 1
	) AS fans_num
	, a.like_num - (
		SELECT b.like_num
		FROM spider_data b
		WHERE b.plantform = a.plantform
			AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), INTERVAL 1 DAY)
		ORDER BY b.create_date DESC LIMIT 1
	) AS like_num, (
		SELECT b.rank_num
		FROM spider_data b
		WHERE b.plantform = a.plantform
			AND DATE_FORMAT(b.create_date, '%Y-%m-%d') = date_sub(DATE_FORMAT(a.create_date, '%Y-%m-%d'), INTERVAL 1 DAY)
		ORDER BY b.create_date DESC LIMIT 1
	) - a.rank_num AS rank_num
	, a.create_date,a.plantform
FROM (SELECT * FROM spider_data ORDER BY create_date DESC LIMIT 1000000000000000) a

GROUP BY DATE_FORMAT(a.create_date, '%Y-%m-%d'), a.plantform
ORDER BY a.create_date DESC;