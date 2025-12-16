class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        # Assign all arguments to instance attributes
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique
    
    @property
    def missing_pct(self) -> float:
        if self.total == 0:
            return 0.0
        # Calculate percentage: (missing / total) * 100
        return (self.missing / self.total) * 100
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "inferred_type": self.inferred_type,
            "total_count": self.total,
            "missing_count": self.missing,
            "missing_pct": self.missing_pct, # Access the property
            "unique_count": self.unique,
        }
    
    def __repr__(self) -> str:
        return (
            f"ColumnProfile(name='{self.name}', type='{self.inferred_type}', "
            f"total={self.total}, missing={self.missing} ({self.missing_pct:.2f}%), "
            f"unique={self.unique})"
        )

# # --- Example Usage ---
# profile = ColumnProfile(
#     name="customer_id",
#     inferred_type="integer",
#     total=1000,
#     missing=50,
#     unique=950 
# )

# print("--- Representation (__repr__) ---")
# print(profile)

# print("\n--- Property Access ---")
# print(f"Missing percentage: {profile.missing_pct:.2f}%")

# print("\n--- Dictionary Output (to_dict) ---")
# import json
# print(json.dumps(profile.to_dict(), indent=2))