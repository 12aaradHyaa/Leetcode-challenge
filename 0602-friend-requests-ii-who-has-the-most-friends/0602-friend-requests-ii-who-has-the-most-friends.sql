# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (
    select requester_id as id from RequestAccepted
    UNION ALL
    select accepter_id from RequestAccepted
) as friend_count
group by id
ORDER BY num DESC
LIMIT 1