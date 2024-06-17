-- Lists all records of the table
SELECT score,name FROM second_table
WHERE NOT name = NULL
ORDER BY score DESC;
