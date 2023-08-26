# ToDoList 🗒️

A Postit based to-do list application built with Python and Django.

## About the project

ToDoList is a PostIt themed to-do list, developed to help user that user hundreds of notes to remember a lot of things.

## Features
* ➕ Add new notes with title, date, description and the color
* ➖ Remove notes
* ❔ Change notes

## Setup

## Installation

1. Clone the repository:
- ```git clone https://github.com/LuisEduardoF/ToDoList```

2. Enter in ToDoList folder:
- ```cd ToDoList/``` 

2. Create a virtual environment:
- ```python3 -m venv venv```


3. Activate the virtual environment:
- ```source venv/bin/activate```


4. Install the dependencies:

- ```pip install -r requirements.txt```

5. Enter in todo folder:
- ```cd todo/```

5. Create a database:
- ```./manage.py makemigrations to_do_list```
flask db init


6. Run the migrations:

flask db migrate


7. Seed the database:

flask db seed


8. Run the application:

flask run
