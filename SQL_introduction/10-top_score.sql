-- Lists all records of the table second_table.
-- Records are ordered by descending score.
-- The database name will be passed as an argument of the mysql command.
-- Records should be ordered by score (top first).
SELECT `score`, `name`
FROM `second_table` 
ORDER BY `score` DESC;
