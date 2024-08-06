-- Lists all shows without the genre "Comedy"

SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT title
	FROM tv_shows AS shows
		LEFT JOIN tv_show_genres AS ids
			ON shows.id = ids.show_id
		LEFT JOIN tv_genres AS genres
			ON genres.id = ids.genre_id
	WHERE genres.name LIKE "Comedy"
)
GROUP BY title
ORDER BY title;
