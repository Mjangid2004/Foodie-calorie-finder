# views.py
from django.shortcuts import render
import pandas as pd
import os

# Load CSV once when Django starts
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "clean_food_database.csv")
df = pd.read_csv(file_path)

# Rename columns to match template (optional)
df.rename(columns={
    "carbs": "carbohydrates_total_g",
    "protein": "protein_g",
    "fat": "fat_total_g",
    "fiber": "fiber_g",
    "sugar": "sugar_g",
    "sodium": "sodium_mg",
    "potassium": "potassium_mg",
    "cholesterol": "cholesterol_mg"
}, inplace=True)

def home(request):
    query = request.POST.get("query", "").strip()
    matches = []

    if query:
        result = df[df["food"].str.contains(query, case=False, na=False)]
        print("Search query:", query)
        print("Matches found:", len(result))

        if not result.empty:
            # Convert matches to a list of dicts
            matches = result.to_dict('records')

    return render(request, "home.html", {
        "api": matches,
        "search_query": query
    })