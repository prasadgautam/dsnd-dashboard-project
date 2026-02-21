import pytest
from pathlib import Path
import sqlite3

# Using pathlib create a project_root
# variable set to the absolute path
# for the root of this project
project_root = Path(__file__).resolve().parents[1]

# apply the pytest fixture decorator
# to a `db_path` function
@pytest.fixture
def db_path():

    # Using the `project_root` variable
    # return a pathlib object for the `employee_events.db` file
    return project_root / "python-package" / "employee_events" / "employee_events.db"

# Define a function called
# `test_db_exists`
# This function should receive an argument
# with the same name as the 
# fixture you created above
def test_db_exists(db_path):

    assert db_path.exists()

def _table_exists(db_path: Path, table_name: str) -> bool:
    con = sqlite3.connect(db_path)
    try:
        cur = con.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (table_name,),
        )
        return cur.fetchone() is not None
    finally:
        con.close()

def test_employee_table_exists(db_path):
    assert _table_exists(db_path, "employee")

def test_team_table_exists(db_path):
    assert _table_exists(db_path, "team")

def test_employee_events_table_exists(db_path):
    assert _table_exists(db_path, "employee_events")
