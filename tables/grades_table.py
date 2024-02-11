from typing import List, Optional
from .table import Table
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
                "id": "serial primary key",
                "value": "integer NOT NULL",
                "date": "timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL",
            },
            [
                {"FOREIGN KEY": "student_id", "REFERENCES": "students(id)"},
                {"FOREIGN KEY": "subject_id", "REFERENCES": "subjects(id)"},
            ],
        )

    def create_table(self) -> Optional[int]:
        return super().create_table()

    def get_all(self) -> List[Grade] | None:
        rows = super().get_all()
        return [Grade(**i) for i in rows] if rows else None

    # інші методи, які можуть бути потрібні для роботи
