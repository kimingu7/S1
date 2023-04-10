SELECT *
FROM users
WHERE country NOT IN ('경기도', '강원도') AND age BETWEEN 20 AND 30
ORDER BY age;