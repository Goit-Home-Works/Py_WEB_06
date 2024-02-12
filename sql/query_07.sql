-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.name AS student, gr.name AS "group",  d.subject_name AS subject, g.value as value
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects d ON g.subject_id = d.id
LEFT JOIN groups gr ON s.group_id = gr.id
WHERE d.id = 2 AND gr.id = 1
ORDER BY value DESC;
