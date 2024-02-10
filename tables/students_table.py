from typing import List, Optional
from .table import Table
from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    group_id: int

class StudentsTable(Table):
    def __init__(self):
        super().__init__(
            "students",
            {
                "id": "serial PRIMARY KEY NOT NULL",
                "name": "varchar(255) NOT NULL",
                "group_id": int
            },
            ["FOREIGN KEY  (group_id) REFERENCES groups(id)"],
        )

    def create_table(self) -> Optional[int]:
        return super().create_table()

    def get_all(self) -> List[Student] | None:
        rows = super().get_all()
        return [Student(**i) for i in rows] if rows else None

    # інші методи, які можуть бути потрібні для роботи зі студентами
