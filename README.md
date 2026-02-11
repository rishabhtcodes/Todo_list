### ✅ Todo List App (Django)

A simple and responsive Todo List web application built using Django, HTML, JavaScript, and Tailwind CSS (CDN). This project helps users manage daily tasks efficiently with a clean and user-friendly interface.

🚀 Features

Add new tasks

Update existing tasks

Delete tasks

Mark tasks as completed

Responsive UI using Tailwind CSS

Django template rendering

🛠️ Technologies Used

Django (Python)

HTML

JavaScript

Tailwind CSS (CDN)

SQLite (Default Django Database)

📂 Project Structure
todo-project/
│
├── todoapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── index.html
│
├── manage.py
└── db.sqlite3

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/todo-list-django.git

2️⃣ Move into Project Folder
cd todo-list-django

3️⃣ Create Virtual Environment
python -m venv venv

4️⃣ Activate Virtual Environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

5️⃣ Install Dependencies
pip install django

6️⃣ Run Migrations
python manage.py migrate

7️⃣ Run Server
python manage.py runserver


Open browser and visit:

http://127.0.0.1:8000/

🎯 Purpose of Project

This project was created to practice Django fundamentals, backend integration with templates, and building a simple real-world task management application.

📌 Future Improvements

User authentication

Task filtering and search

Due dates and reminders

REST API integration

Drag and drop tasks
