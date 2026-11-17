-- Shows the highest temperature of each state, sorted by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
