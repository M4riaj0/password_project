"""
README Password Generator
This project is a password manager implementing fastAPI, in which you can create a user and generate passwords for him randomly and allows you to make CRUD requests

## Installation
1. Clone the repository: `git clone https://github.com/M4riaj0/password_project.git`
2. Navigate to the project directory: `cd your-repo`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Execution
1. Run the project: `uvicorn main:app --reload`

## Functionality
This project implements the following functionalities:
- Feature 1: user authentication:
    register_user() -> Registers a user, with the username and variables to generate a random password, checks if the username is already taken and adds it to the database
    login_for_access_token() ->  generates the acces token for the authentication of the user

- Feature 2: Create password.
    createPassword(password: Password, current_user: user_dependency) -> Creates a password for the current user

- Feature 3: Read.
    getPasswords(current_user: user_dependency) -> Obtains all the passwords of the current user

- Feature 4: Uptade.
    updatePassword(id_password: int, password: Password, current_user: user_dependency) -> updates a selected password
    
- Feature 5: Delete.
    deletePassword(id_password: int, current_user: user_dependency) -> Deletes a selected password.

"""
