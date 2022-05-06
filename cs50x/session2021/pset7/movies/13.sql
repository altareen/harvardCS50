SELECT B.name FROM
(SELECT movies.title FROM movies JOIN stars ON movies.id=stars.movie_id JOIN people ON stars.person_id=people.id WHERE people.name='Kevin Bacon' AND people.birth=1958) AS A,
(SELECT movies.title, people.name FROM movies JOIN stars ON movies.id=stars.movie_id JOIN people ON stars.person_id=people.id) AS B
WHERE A.title=B.title AND B.name <> 'Kevin Bacon';
