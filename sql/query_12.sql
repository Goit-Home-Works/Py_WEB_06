-- Оцінки студентів у певній групі з певного предмета на всіх заняттях.


WITH RankedGrades AS (
  SELECT
    gr.name AS "group",
    d.subject_name AS subject,
    s.name AS student,
    g.value AS value,
    g.date AS  date,
    ROW_NUMBER() 
    OVER (
        PARTITION BY d.subject_name, gr.name, s.name 
        ORDER BY g.date DESC
        ) AS rnk
  FROM
    grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN subjects d ON g.subject_id = d.id
    LEFT JOIN groups gr ON s.group_id = gr.id
  WHERE
    gr.id = 3 AND d.id = 3
)
SELECT
  "group",
  subject,
  student,
  value,
  date,
  rnk
FROM
  RankedGrades
 

-- ======================================================================

-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

WITH RankedGrades AS (
  SELECT
    gr.name AS "group",
    d.subject_name AS subject,
    s.name AS student,
    g.value AS value,
    g.date AS  date,
    ROW_NUMBER() 
    OVER (
        PARTITION BY d.subject_name, gr.name, s.name 
        ORDER BY g.date DESC
        ) AS rnk
  FROM
    grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN subjects d ON g.subject_id = d.id
    LEFT JOIN groups gr ON s.group_id = gr.id
  WHERE
    gr.id = 3 AND d.id = 3
)



SELECT
  "group",
  subject,
  student,
  value,
  date
FROM
  RankedGrades
WHERE
  rnk = 1
ORDER BY
  value DESC;
