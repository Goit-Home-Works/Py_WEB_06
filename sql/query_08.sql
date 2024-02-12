-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.teacher_name AS teacher, d.subject_name AS subject, ROUND(AVG(value),2) as average_grade
FROM grades g 
LEFT JOIN subjects d ON g.subject_id  = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE t.id = 3

GROUP BY d.id, t.teacher_name;
