-- найти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.name AS student, ROUND(AVG(g.value), 2) AS average_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;
