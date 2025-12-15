
def case1():
	test_cases = ["", " ", "na", "n/a", "null", 'nan', "none"]

	def is_missing(str:str):
		str = str.strip()
		return bool(str)

	for case in test_cases:
		print(f"[{case}]\tis {is_missing(case)}")

