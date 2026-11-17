-- Lists records of second_table reaching 10 or more, best first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
