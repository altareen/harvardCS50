SELECT A.title FROM
(SELECT movies.title FROM movies JOIN stars ON movies.id=stars.movie_id JOIN people ON stars.person_id=people.id WHERE people.name='Johnny Depp') AS A,
(SELECT movies.title FROM movies JOIN stars ON movies.id=stars.movie_id JOIN people ON stars.person_id=people.id WHERE people.name='Helena Bonham Carter') AS B
WHERE A.title=B.title;
