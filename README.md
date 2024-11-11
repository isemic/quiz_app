# Django Quiz App

A simple Django-based quiz application that allows users to answer questions, submit their responses, and view their score. The app uses Vue.js for the frontend to provide a dynamic, interactive quiz experience.

## Features

- **Quiz Interface**: Users can select answers for each question and submit the quiz.
- **Real-Time Scoring**: Upon submission, the app calculates the user's score based on correct answers.
- **Results Page**: Displays the user's score and the total number of questions.

## Technologies Used

- **Django**: Backend framework for handling data, quiz logic, and routing.
- **Vue.js**: Frontend JavaScript framework for dynamic user interface.
- **Bootstrap**: For styling the quiz interface.
- **HTML/CSS/JavaScript**: For additional frontend structure and functionality.

## Prerequisites

- Python 3.7+
- Django 3.x or higher
- Node.js and npm (for Vue.js setup, if you plan to customize the Vue components)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/django-quiz-app.git
    cd django-quiz-app
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for accessing the admin interface and adding questions):

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

### Setting Up Quiz Questions

1. Navigate to the Django admin panel at `http://127.0.0.1:8000/admin/`.
2. Log in using your superuser credentials.
3. Add questions by creating entries in the `Question` model, which should contain fields like `uid`, `question text`, `answer options`, and `correct_answer`.

### Project Structure

- `views.py`: Contains views for handling quiz submission and displaying results.
- `urls.py`: Defines the routes for quiz submission and results.
- `templates/quiz/quizques.html`: Template for the quiz page with Vue.js integrated.
- `templates/quiz/result.html`: Template for displaying quiz results.

## Usage

1. Visit `http://127.0.0

