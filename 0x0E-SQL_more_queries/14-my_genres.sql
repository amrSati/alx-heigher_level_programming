-- Lists all genres of the show 'Dexter'

SELECT name
FROM tv_genres genres
	INNER JOIN tv_show_genres ids
		ON genres.id = ids.genre_id
	RIGHT JOIN tv_shows shows
		ON shows.id = ids.show_id
WHERE shows.title LIKE "Dexter"
GROUP BY name
ORDER BY name;
