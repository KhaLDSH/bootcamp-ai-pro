from __future__ import annotations

from csv import DictReader
from pathlib import Path

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = DictReader(f)
        return [dict(row) for row in reader]


# import csv

# def read_csv_rows(file_path):
#     rows = []
#     try:
#         with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
#             reader = csv.reader(csv_file)
            
#             for row in reader:
#                 rows.append(row)

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except PermissionError:
#         print(f"Error: No permission to read '{file_path}'.")
#     except Exception as e:
#         print(f"Unexpected error: {e}")
        
#     return rows