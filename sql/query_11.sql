-- Середній бал, який певний викладач ставить певному студентові.

SELECT s.name as student, t.teacher_name AS teacher, ROUND(AVG(g.value), 2) as average_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE s.id = 13 AND t.id = 4
GROUP BY s.name, t.teacher_name
ORDER BY average_grade DESC;

-- Середній бал з окремого предмета, 
--  який певний викладач ставить певному студенту.

SELECT d.subject_name as subject, s.name as student, t.teacher_name AS teacher, ROUND(AVG(g.value), 2) as average_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE s.id = 13 AND t.id = 4
GROUP BY d.subject_name, s.name, t.teacher_name
ORDER BY average_grade DESC;
