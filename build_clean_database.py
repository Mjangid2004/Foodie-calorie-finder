import pandas as pd

# ----------------------------
# Step 1: Load raw USDA files
# ----------------------------
food = pd.read_csv("food.csv")
nutrient = pd.read_csv("nutrient.csv")
food_nutrient = pd.read_csv("food_nutrient.csv", low_memory=False)

# ----------------------------
# Step 2: Merge dataframes
# ----------------------------
# Merge food names
df = food_nutrient.merge(food, on="fdc_id", how="left")

# Merge nutrient names
df = df.merge(nutrient, left_on="nutrient_id", right_on="id", how="left")

# Strip whitespace from nutrient names
df['name'] = df['name'].str.strip()
df['description'] = df['description'].str.strip()

# ----------------------------
# Step 3: Keep only important nutrients
# ----------------------------
important_nutrients = [
    "Energy",                     # calories
    "Protein",
    "Total lipid (fat)",
    "Carbohydrate, by difference",
    "Fiber, total dietary",
    "Sugars, total including NLEA",
    "Sodium, Na",
    "Potassium, K",
    "Cholesterol"
]

df = df[df["name"].isin(important_nutrients)]

# ----------------------------
# Step 4: Pivot table
# ----------------------------
# Each food becomes a row, each nutrient a column
clean_df = df.pivot_table(
    index="description",
    columns="name",
    values="amount",
    aggfunc='first'  # take first non-null value
).reset_index()

# ----------------------------
# Step 5: Rename columns
# ----------------------------
clean_df = clean_df.rename(columns={
    "description": "food",
    "Energy": "calories",
    "Protein": "protein_g",
    "Total lipid (fat)": "fat_total_g",
    "Carbohydrate, by difference": "carbohydrates_total_g",
    "Fiber, total dietary": "fiber_g",
    "Sugars, total including NLEA": "sugar_g",
    "Sodium, Na": "sodium_mg",
    "Potassium, K": "potassium_mg",
    "Cholesterol": "cholesterol_mg"
})

# ----------------------------
# Step 6: Clean food names
# ----------------------------
clean_df['food'] = clean_df['food'].str.strip().str.title()

# ----------------------------
# ----------------------------
# Step 7: Ensure all numeric columns exist and are valid
# ----------------------------
numeric_cols = [
    "calories", "protein_g", "fat_total_g", "carbohydrates_total_g",
    "fiber_g", "sugar_g", "sodium_mg", "potassium_mg", "cholesterol_mg"
]

# Add missing columns with 0
for col in numeric_cols:
    if col not in clean_df.columns:
        clean_df[col] = 0

# Convert all numeric columns to numbers
for col in numeric_cols:
    clean_df[col] = pd.to_numeric(clean_df[col], errors='coerce').fillna(0)
# ----------------------------
# Step 8: Remove duplicate food names
# ----------------------------
clean_df = clean_df.drop_duplicates(subset=['food'])

# ----------------------------
# Step 9: Save to CSV
# ----------------------------
clean_df.to_csv("clean_food_database.csv", index=False)

print("✅ clean_food_database.csv created successfully!")