 Django Chatbot
Project Overview
This project is an offline chatbot built using Django, designed to interact with users without requiring an internet connection by giving predifined responses. It uses a local database (db.sqlite3) to store conversation history and manage user interactions. The chatbot can be used for simple question-answering, FAQs, or interactive demonstrations in an offline environment.

Project Structure
graphql
Copy code
parent_directory/
│
├── myapp/          # Django application containing views, models, templates, and static files
├── myproject/      # Django project configuration files (settings.py, urls.py, wsgi.py, etc.)
├── db.sqlite3      # SQLite database storing chatbot data and conversation history
└── manage.py       # Django management script for running and managing the project

Features
Offline functionality – works without an internet connection.
User interaction with chatbot via web interface.
Stores conversation history in SQLite database (db.sqlite3).
Built using Django framework for scalability and modularity.

Usage
Enter your queries in the chat interface.
The chatbot will respond based on the predefined logic or stored database responses.
Conversation history is saved automatically in db.sqlite3.


Enhancing the user interface.

Improving database interaction or chatbot logic.
