# Smile-Now

[Smile-Now](https://smile-now.vercel.app/) is a web application designed to streamline dentist appointment scheduling. Built using Django for the backend and React for the frontend, Smile-Now provides an intuitive interface for managing dental appointments and ensuring smooth communication between patients and dental offices.

Table of Contents

  - Features
  - Installation
  - Usage
  - Contributing
  - License
  - Contact

### A third-level heading Features

  - User Registration and Authentication: Secure sign-up and login for patients and dental staff.
  - Appointment Scheduling: Easily book, view, and manage dental appointments.
  - Admin Dashboard: An administrative interface for managing appointments, users, and settings.

Installation

To set up the Smile-Now project locally, follow these instructions:
Backend Setup (Django)

Clone the Repository
```
git clone https://github.com/Anuoluwapo25/Smile-Now.git
cd Smile-Now/server
```

Set Up a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install Dependencies
```
pip install -r requirements.txt
```
Apply Migrations
```
python manage.py migrate
```
Run the Server
```
    python manage.py runserver
```
The Django backend should now be running at http://localhost:8000.

Frontend Setup (React)

    Navigate to the Frontend Directory


    cd ../client

Install Dependencies

    npm install

Run the Development Server

    npm start

    The React frontend should now be running at http://localhost:3000.

Usage

    Access the Application: Open your browser and go to http://localhost:3000 to interact with the Smile-Now application.
    Sign Up/Log In: Create an account or log in to access appointment scheduling features.
    Schedule an Appointment: Use the scheduling interface to book and manage your dental appointments.
    Manage Appointments: If you are a dentist or an admin, use the administrative dashboard to view and manage appointments.

Contributing

We welcome contributions to improve Smile-Now! To contribute:

    Fork the Repository: Click the "Fork" button on GitHub to create your copy of the repository.

    Create a Branch: Create a new branch for your changes.

    bash

git checkout -b feature/your-feature

Implement Your Changes: Make the necessary changes and test them.

Commit and Push: Commit your changes and push them to your forked repository.

bash

    git add .
    git commit -m "Add new feature"
    git push origin feature/your-feature

    Submit a Pull Request: Open a pull request to merge your changes into the main repository.

For detailed contributing guidelines, see the CONTRIBUTING.md file.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

This project was developed by: 
  1. Kobby Amable - Frontend Developer: amablebless@gmail.com
  2. Anuoluwapo Rebecca - Backend Developer: Anuoluwapoali25@gmail.com
  3. Temesgen Dora - Backend Developer: tdemeke36@gmail.com

For any questions or further information, feel free to reach out to us.

Thank you for using Smile-Now. We hope it helps make dental appointments easier and more accessible!
