-- Список курсів, які певному студенту читає певний викладач.


SELECT d.subject_name AS subject, s.name AS student, t.teacher_name AS teacher
FROM subjects d
LEFT JOIN students s ON s.id = d.teacher_id
LEFT JOIN teachers t ON d.teacher_id = t.id
WHERE s.id = 3 AND t.id = 3
ORDER BY subject;
