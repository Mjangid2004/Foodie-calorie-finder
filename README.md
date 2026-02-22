🍎 Foodie Calorie Finder

Foodie Calorie Finder is a Django-based web application that allows users to search for food items and view detailed nutritional information along with estimated calorie burn times for different exercises.

The project works completely offline using a local CSV dataset — no API keys required.

✨ Features

🔎 Search food items (case-insensitive)

🥗 Displays nutrition per 100g:

Calories

Protein

Fat

Carbohydrates

Fiber

Sugar

Sodium

Potassium

Cholesterol

📊 Interactive nutrient Bar Graph (Chart.js)

🔥 Estimated calorie burn time for:

Jog

Power Yoga

Gym Workout

Brisk Walk

⚠️ Health Alerts:

High Sodium (> 200 mg)

High Sugar (> 300 mg)

🌙 Dark Mode toggle

🎨 Smooth animations & improved UI

🖼 Static exercise images included

💻 Fully offline (CSV-based dataset)

🛠 Tech Stack

Backend: Django

Frontend: HTML, CSS, JavaScript

Charts: Chart.js (CDN)

Data Handling: Pandas

Database: CSV file

🚀 Run Locally
1️⃣ Clone the repository
git clone https://github.com/yourusername/Foodie-calorie-finder.git
cd Foodie-calorie-finder-main
2️⃣ Activate virtual environment

Windows

.\venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt

If no requirements file:

pip install django pandas
4️⃣ Run migrations
python manage.py migrate
5️⃣ Start server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000
📁 Project Structure
Foodie-calorie-finder-main/
│
├─ counter/
│   ├─ templates/home.html
│   ├─ clean_food_database.csv
│   └─ views.py
│
├─ foodie/
├─ static/
│   ├─ images/
│   └─ style.css
│
├─ manage.py
├─ README.md
└─ .gitignore
