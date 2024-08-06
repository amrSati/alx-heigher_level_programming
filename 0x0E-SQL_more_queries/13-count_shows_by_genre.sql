-- Lists all genres with thw number of shows linked to each

SELECT tv_genres.name AS genre,
	COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
	NATURAL JOIN tv_shows
	INNER JOIN tv_show_genres ids
	ON tv_genres.id = ids.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
