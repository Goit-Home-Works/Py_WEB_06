 
from typing import List, Optional
from table import Table
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

    def create_group(self, group: Group) -> Optional[int]:
        return super().create(group.__dict__)

    def get_all_groups(self) -> List[Group] | None:
        rows = super().get_all()
        return [Group(**i) for i in rows] if rows else None

    # інші методи