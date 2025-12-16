print("\n\n")
def case1():
	test_cases = ["", " ", "na", "n/a", "null", 'nan', "none"]

	def is_missing(str:str):
		str = str.strip()
		return bool(str)

	for case in test_cases:
		print(f"[{case}]\tis {is_missing(case)}")


# import time

# start = time.perf_counter_ns()
# time.sleep(2)
# end = time.perf_counter_ns()

# elapsed_ms = (end - start) / 1_000_000

# print(f"{elapsed_ms:.2f}")

# ---------------------------



class Person:
    def __init__(self, name:str, age: int):
        self.name = name
        # The setter is automatically called here, which sets self._age
        self.age = age 
        
    @property
    def age(self):
        # 1. FIX: Return the private attribute _age
        return self._age 
    
    @age.setter
    def age(self, value:int):
        assert 0 <= value <= 200, "Age must be between 0 and 200."
        self._age = value
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __eq__(self, other):
        # It's generally better to compare against another Person object
        if isinstance(other, Person):
            return self.age == other.age
        # 2. FIX: Access the property as an attribute (self.age)
        return self.age == other 

# --- Execution ---

p1 = Person("ali", 20)
p2 = Person("khalid", 21)

print(p1) # Calls p1.__repr__ internally
print(p2) # Calls p2.__repr__ internally

# 3. FIX: Use the built-in repr() or str() function, or just print the object.
# The original attempt print(p2.repr()) would raise an AttributeError because 'repr' is not a method.

# Corrected comparison logic:
print(f"Is {p1.name} equal to {p2.name} in age? = {p1 == p2}") 
# OR comparing p1's age to a raw value
print(f"Is {p1.name}'s age equal to 20? = {p1 == 20}")





    