-- Lists all genres of the show 'Dexter'

SELECT title
FROM tv_shows shows
	INNER JOIN tv_show_genres ids
		ON shows.id = ids.show_id
	RIGHT JOIN tv_genres genres
		ON genres.id = ids.genre_id
WHERE genres.name LIKE "Comedy"
GROUP BY title
ORDER BY title;
