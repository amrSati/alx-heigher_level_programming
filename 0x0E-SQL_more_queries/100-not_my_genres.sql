-- Lists all genres not linked to the show 'Dexter'

SELECT name
FROM tv_genres
WHERE name NOT IN (
	SELECT name
	FROM tv_genres AS genres
		LEFT JOIN tv_show_genres AS ids
			ON genres.id = ids.genre_id
		LEFT JOIN tv_shows AS shows
			ON shows.id = ids.show_id
	WHERE shows.title LIKE "Dexter"
)
GROUP BY name
ORDER BY name;
