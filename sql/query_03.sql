-- Знайти середній бал у групах з певного предмета.

-- ********************************************

SELECT d.subject_name AS subject, gr.name AS "group", ROUND(AVG(g.value), 2) AS average_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE g.subject_id = 2
GROUP BY gr.id, d.subject_name
ORDER BY average_grade DESC;

