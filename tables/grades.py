
from typing import List, Optional
from table import Table
from dataclasses import dataclass

@dataclass
class Grade:
    """A class representing a grade."""
    id: int
    value: int
    date: str
    student_id : int
    subject_id : int

class GradesTable(Table):
    def __init__(self):
        super().__init__(
            "grades",
            {
                "id": "serial PRIMARY KEY NOT NULL",
                "value" : "integer NOT NULL",
                "date"  : "timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL",
                "student_id" : "integer REFERENCES students(id)",
                "subject_id" : "integer REFERENCES subjects(id)"
            },
            []
        )

    def create_grade(self, grade: Grade) -> Optional[int]:
        return super().create(grade.__dict__)

    def get_all_grades(self) -> List[Grade] | None:
        rows = super().get_all()
        return [Grade(**i) for i in rows] if rows else None

    # інші методи, які можуть бути потрібні для роботи