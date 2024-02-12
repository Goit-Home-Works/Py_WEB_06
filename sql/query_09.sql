-- Знайти список курсів, які відвідує студент.

SELECT s.name AS student, d.subject_name AS subject
FROM students s
LEFT JOIN grades g ON s.id = g.student_id 
LEFT JOIN subjects d ON g.subject_id = d.id 
WHERE s.id = 3
GROUP BY s.name, d.subject_name
ORDER BY d.subject_name;