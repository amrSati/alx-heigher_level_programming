-- Lists all genres by their rating

SELECT name, SUM(rate) AS rating
FROM tv_genres AS genres
	LEFT JOIN tv_show_genres AS ids
		ON genres.id = ids.genre_id
	INNER JOIN tv_show_ratings AS ratings
		ON ratings.show_id = ids.show_id
GROUP BY name
ORDER BY rating DESC;
