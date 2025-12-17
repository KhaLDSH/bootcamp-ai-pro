from __future__ import annotations

import csv
from pathlib import Path


def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")
    
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        # return list of dicts, where each dict present a recored
        # print(rows)
    
    if not rows:
        raise ValueError("CSV has no data rows")
    
    return rows
        
        
# read_csv_rows("d.csv")


