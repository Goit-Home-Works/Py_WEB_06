-- Define the variable

-- DO $$ 
-- DECLARE
--     x INT := 2;
--     result RECORD;
-- BEGIN
--     -- Your query using the variable
--     SELECT INTO result 
--         s.name AS student, 
--         d.subject_name AS subject, 
--         ROUND(AVG(g.value), 2) AS average_grade
--     FROM grades g
--     LEFT JOIN students s ON s.id = g.student_id 
--     LEFT JOIN subjects d ON g.subject_id = d.id
--     WHERE g.subject_id = x
--     GROUP BY s.id, d.subject_name, s.name
--     ORDER BY average_grade DESC
--     LIMIT 1;

--     -- Print the result
--     RAISE NOTICE 'Result: %', result;
-- END $$;


-- ********************************************
-- Знайти студента із найвищим середнім балом з певного предмета

SELECT s.name AS student, d.subject_name AS subject, ROUND(AVG(g.value), 2) AS average_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id
WHERE g.subject_id = 1
GROUP BY s.id, d.subject_name, s.name
ORDER BY average_grade DESC
LIMIT 1;


-- -- Знайти студента із найвищим середнім балом по кожному предмету


-- SELECT  DISTINCT ON (d.subject_name)
-- s.name AS student, d.subject_name AS subject, ROUND(AVG(g.value), 2) AS average_grade
-- FROM grades g
-- LEFT JOIN students s ON s.id = g.student_id 
-- LEFT JOIN subjects d ON g.subject_id = d.id
-- GROUP BY d.subject_name, s.id, s.name
-- ORDER BY d.subject_name, average_grade DESC;
