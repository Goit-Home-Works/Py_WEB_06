-- Знайти середній бал на потоці (по всій таблиці оцінок).


SELECT ROUND(AVG(value), 2) AS average_grade
FROM grades;