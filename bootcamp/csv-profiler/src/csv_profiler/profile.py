MISSING = {"","na","n/a","null","none","nan"}
def is_missing(value:str):
    if value is None:
        return True
    cleand = value.strip().casefold()
    return cleand in MISSING

def try_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"


def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {
            "rows": 0,
            "columns": {},
            "notes": ["Empty dataset"]
        }

    columns = list(rows[0].keys())
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}
    
    types = {}

    ages = []
    salaries = []
    
    for row in rows:
        print("row= ",row)
        
        age = row['age']
        salary = row['salary']
        
        if infer_type(age) == 'number':
            ages.append(age)
        if infer_type(salary) == 'number':
            salaries.append(salary)
            
    max_age = max(ages)
    max_salary = max(salaries)
    
    
    for row in rows:
        for c in columns:
            v = (row.get(c).strip() or "")
            if v == "":
                missing[c] += 1
            else:
                non_empty[c] += 1
                types[c] = infer_type(v)
                    
    print(max_age)

    return {
        "rows": len(rows),
        "columns": columns,
        "notes": ["not Empty dataset"],
        "missing": missing,
        "non_empty_counts": non_empty,
        "types": types,
        "max age": max_age,
        "max salary": max_salary
    }