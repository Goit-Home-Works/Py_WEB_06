from .table import Table
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Teacher:
    id: int
    teacher_name: str
    subject_id: int


class TeachersTable(Table):
    def __init__(self):
        super().__init__(
            "teachers",
            {
                "id": "serial primary key",
                "teacher_name": "varchar(255) NOT NULL",
            },
            [],
        )

    def create_table(self) -> Optional[int]:
        return super().create_table()

    def get_all(self) -> List[Teacher] | None:
        rows = super().get_all()
        return [Teacher(**i) for i in rows] if rows else None

    # інші методи, які можуть бути потрібні для роботи
