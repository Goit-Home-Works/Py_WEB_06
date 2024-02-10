# __init__.py
from .grades_table import GradesTable
from .students_table import StudentsTable
from .groups_table import GroupsTable
from .subjects_table import SubjectsTable
from .teachers_table import TeachersTable
from .table import Table
__all__ = [
    'GradesTable',
    'StudentsTable',
    'GroupsTable',
    'SubjectsTable',
    'TeachersTable',
]