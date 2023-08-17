-- script that lists all records of the table and sort them by score                                                                                                    
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
