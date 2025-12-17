# from moudels.colmun_profile import ColumnProfile

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

def column_values(rows: list[dict[str,str]], col:str) -> list[str]:
    return [row.get(col, "") for row in rows]
    
def numric_stats(values: list[str]) -> dict:
    # values per column
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    
    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            print("\nNon-numric is found !!!!\n")
        else:
            nums.append(float(v))
            
    count = len(nums)
    unique = len(set(nums))
    min_num = min(nums)
    max_num = max(nums)
    mean = sum(nums) / count
    
    
    return {
        "count": count, 
        "unique": unique,
        "min_num": min_num,
        "max_num": max_num,
        "mean": mean
        }
    
    
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
    
    num_stats = numric_stats(column_values(rows, "age"))
    types = {}

    ages = []
    salaries = []
    
    for row in rows:
        print("row= ",row)
        
        age = row['age']
        salary = row['salary']
        
        if infer_type(age) == 'number':
            ages.append(int(age))
        if infer_type(salary) == 'number':
            salaries.append(int(salary))
            
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
                
    
                    

    report = {
        "rows": len(rows),
        "columns": columns,
        "notes": ["not Empty dataset"],
        "missing": missing,
        "non_empty_counts": non_empty,
        "types": types,
        "max age": max_age,
        "max salary": max_salary,
        "num stats": num_stats
    }
    return report
