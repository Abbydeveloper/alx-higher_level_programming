-- list all shows and rows of tables contained in the db hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tb_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
