from typing import List, Optional
from .table import Table
from dataclasses import dataclass

@dataclass
class Group:
    id: int
    name: str

class GroupsTable(Table):
    def __init__(self):
        super().__init__(
            "groups",
            {
                "id": "serial PRIMARY KEY NOT NULL",
                "name": "varchar(255) NOT NULL",
            },
            []
        )

    def create_table(self) -> Optional[int]:
        return super().create_table()

    def get_all(self) -> List[Group] | None:
        rows = super().get_all()
        return [Group(**i) for i in rows] if rows else None

    # інші методи
