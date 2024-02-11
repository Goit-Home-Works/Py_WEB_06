-- Знайти які курси читає певний викладач.

SELECT teachers.teacher_name, subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
ORDER BY teachers.teacher_name, subjects.subject_name;
