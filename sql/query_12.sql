-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT gr.name AS "group", 
	s.name as student, 
	d.subject_name AS subject, 
	t.teacher_name AS teacher, 
	value, 
	date
FROM grades g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE gr.id = 3 AND d.id = 3  
AND date = (
	SELECT MAX(date)
	FROM grades g
	LEFT JOIN students s ON s.id = g.student_id 
	WHERE s.group_id = 3 AND g.subject_id = 1
)
ORDER BY value DESC;
