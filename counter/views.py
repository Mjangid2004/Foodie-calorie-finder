from django.shortcuts import render
from django.conf import settings
import pandas as pd
import os


def home(request):
    context = {}
    query = ""

    if request.method == "POST":
        query = request.POST.get("query", "").strip()
        context["query"] = query

        if query:
            try:
                # ✅ Correct path to CSV
                file_path = os.path.join(
                    settings.BASE_DIR,
                    "counter",
                    "clean_food_database.csv"
                )

                df = pd.read_csv(file_path)

                # Clean column names
                df.columns = df.columns.str.strip()

                # Case-insensitive search
                result = df[df["food"].str.lower().str.contains(query.lower(), na=False)]

                if not result.empty:
                    food_data = result.iloc[0]

                    # ✅ Extract nutrition values safely
                    calories = float(food_data["calories"])

                    context.update({
                        "calories": round(calories, 2),
                        "protein": round(float(food_data["protein_g"]), 2),
                        "fat": round(float(food_data["fat_total_g"]), 2),
                        "carbs": round(float(food_data["carbohydrates_total_g"]), 2),
                        "fiber": round(float(food_data["fiber_g"]), 2),
                        "sugar": round(float(food_data["sugar_g"]), 2),
                        "sodium": round(float(food_data["sodium_mg"]), 2),
                        "potassium": round(float(food_data["potassium_mg"]), 2),
                        "cholesterol": round(float(food_data["cholesterol_mg"]), 2),
                    })

                    # ✅ Exercise burn rates (calories burned per minute)
                    jog_burn = 10
                    yoga_burn = 5
                    gym_burn = 8
                    walk_burn = 4

                    # ✅ Calculate minutes required
                    context.update({
                        "jog_minutes": round(calories / jog_burn, 1),
                        "yoga_minutes": round(calories / yoga_burn, 1),
                        "gym_minutes": round(calories / gym_burn, 1),
                        "walk_minutes": round(calories / walk_burn, 1),
                    })

                else:
                    context["error"] = "Food not found."

            except Exception as e:
                context["error"] = "Something went wrong while reading the database."
                print("CSV ERROR:", e)

    return render(request, "home.html", context)