-- lists the number of records with the same score in the table second_table
-- Displays score and number of records for this score with the label number.
SELECT score, COUNT(*) AS count FROM second_table GROUP BY score ORDER BY score DESC;
