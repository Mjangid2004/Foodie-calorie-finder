# Foodie Calorie Finder

**Foodie Calorie Finder** is a Django-based web application that allows users to search for food items and see their nutritional information and estimated calories burned for different exercises. This project uses a local CSV file (`clean_food_database.csv`) as the data source, so it works offline without needing any API keys.  

### Features
- Search for food items by name.
- Display calories and nutritional values (protein, fat, carbs, fiber, sugar, sodium, potassium, cholesterol) per 100g.
- Show estimated time to burn calories via:
  - Jog
  - Power Yoga
  - Gym Workout
  - Brisk Walk
- Includes static images for calorie burn estimation and UI enhancements.
- Fully offline using a clean CSV dataset.

---

# Run the Project Locally

Follow these steps to run the project on your machine:

# 1. Clone the repository
 bash
git clone https://github.com/yourusername/Foodie-calorie-finder.git
cd Foodie-calorie-finder-main

# 2. Activate the virtual environment
# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

If you don’t have requirements.txt, make sure Django and pandas are installed:

pip install django pandas

# 4. Apply Django migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

# 6. Open in a web browser

Go to:

http://127.0.0.1:8000

The home page will appear where you can search for food items.
for example Egg white, egg yolk, mango, rice , banana

Nutritional values and calorie burn estimates will be displayed.

# Project Structure
Foodie-calorie-finder-main/
│
├─ counter/                  # Django app
│
├─ foodie/                   # Django project settings
│
├─ static/                   # Static files (CSS, images)
│  ├─ images/
│  ├─ style.css
│
├─ clean_food_database.csv    # Food nutrition data
├─ manage.py                  # Django management file
├─ README.md
