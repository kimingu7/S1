SELECT first_name, phone, country
FROM users
WHERE phone LIKE '%-51__-%' AND country NOT LIKE '서울';