# NE1-FREELANCE: A Professional Web-Based Freelancing Platform Built with Django
![image](https://user-images.githubusercontent.com/62683196/216718671-c5618604-ad2c-4723-b191-1feb053ed94e.png)

NE1-FREELANCE is a feature-rich and user-friendly open source freelancing platform designed to make the job search process more efficient and accessible. Built with the robust and reliable Django framework, this project delivers a seamless experience for freelancers and employers alike.

## Key Features
- Secure User Authentication: Effortless sign-up, login, and logout with user-friendly interface.
- Job Listing Management: Create, edit, and delete job listings with ease.
- Search Functionality: Find the perfect job quickly with advanced search options such as job title, description, and category.
- User-Friendly Display: View job listings in a visually appealing grid format with key details such as job title, description, category, user, and price.

## Getting Started
Before setting up the project locally, make sure you have the following software installed on your computer:
- Python 3.x
- pip (Python package manager)
- virtualenv (optional but recommended)

Here's a step-by-step guide to setting up NE1-FREELANCE on your local machine:

1. Clone the repository to your local machine by running the following command in your terminal or via the GitHub application:
``` git clone https://github.com/A-Hazzard/NE1-FREELANCE.git ```

2. Navigate to the project directory: 
``` cd NE1-FREELANCE ```
### Note: Steps 3 and 4 are optional but highly recommended for optimal performance.

3. Create a virtual environment:
``` python3 -m venv virtual_environment ``` where ``` virtual_environment ``` is the name of your virtual environment. You can name it anything you like.

4. Activate the virtual environment:
- For Unix/Linux-based systems: ``` source virtual_environment/bin/activate ```
- For Windows systems: ``` .\virtual_environment\Scripts\activate ```

5. Install the required packages:
``` pip install -r requirements.txt ```

6. Apply database migrations:
``` python manage.py migrate ```

7. Start the development server:
``` python manage.py runserver ```

8. Open your web browser and access the platform at the [localhost URL](http://localhost:8000), typically "localhost:8000".

### Important Note: The website will not function as intended without running the development server. Additionally, much of the CSS was built with SASS, so you will need to install a SASS compiler if you plan on making style changes.

## Contributions Welcome
NE1-FREELANCE is an open source project and contributions from the community are always welcome. If you would like to contribute or have any questions, feel free to fork the repository and make changes, or get in touch with the author via social media links on their profile.

## Author
Aaron Hazzard
