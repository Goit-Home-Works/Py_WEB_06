from typing import List, Optional
from .table import Table
from dataclasses import dataclass

@dataclass
class Subject:
    id: int
    name: str
    teacher_id: int

class SubjectsTable(Table):
    def __init__(self):
        super().__init__(
            "subjects",
            {
                "id": "serial PRIMARY KEY NOT NULL",
                "subject_name" : "VARCHAR(255) NOT NULL",
                "teacher_id"  : int,
            },
            ["FOREIGN KEY  (teacher_id) REFERENCES teachers(id)",],
        )

    def create_table(self) -> Optional[int]:
        return super().create_table()

    def get_all(self) -> List[Subject] | None:
        rows = super().get_all()
        return [Subject(**i) for i in rows] if rows else None

    # інші методи, які можуть бути потрібні для роботи
