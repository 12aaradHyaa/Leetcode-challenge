# Write your MySQL query statement below
(SELECT name as results
FROM Users
INNER JOIN MovieRating USING (user_id)
GROUP BY user_id
ORDER BY COUNT(rating) DESC, NAME
LIMIT 1)

UNION ALL

(SELECT title as results
FROM Movies
INNER JOIN MovieRating USING (movie_id)
WHERE month(created_at)="02" AND YEAR(created_at)= "2020"
GROUP BY title
order by avg(rating) DESC, title
limit  1)
