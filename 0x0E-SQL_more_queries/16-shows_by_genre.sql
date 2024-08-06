-- Lists all shows and all genres linked to that show

SELECT title, name
FROM tv_shows AS shows
	LEFT JOIN tv_show_genres AS ids
		ON ids.show_id = shows.id
	LEFT JOIN tv_genres AS genres
		ON ids.genre_id = genres.id
ORDER BY title, name;
