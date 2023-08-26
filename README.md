# ToDoList 🗒️

A Postit-themed to-do list application built with Python and Django.

![alt text](https://github.com/LuisEduardoF/ToDoList/blob/main/todo/to_do_list/static/image_2023-08-26_003303915.png)

## About the project

ToDoList is a PostIt-themed to-do list developed to assist users who have numerous notes and need to remember a lot of things.


## Features
* ➕ **Add new notes:** Include a title, date, description, and choose a color for your note.
* ➖ **Remove notes:** Easily delete notes you no longer need.
* ❔  **Change notes:** Modify note details whenever you want.

## Setup

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/LuisEduardoF/ToDoList
   ```

2. **Navigate to the ToDoList folder:**
   ```sh
   cd ToDoList/
   ```
     
3. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**
   ```sh
   source venv/bin/activate
   ```

5. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Navigate to the 'todo' folder:**
   ```sh
   cd todo/
   ```
   
### Creating the Database

7. **Create a database and apply migrations:**
   ```sh
   ./manage.py makemigrations to_do_list
   python manage.py migrate
   ```
   
### Running the application

8. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
