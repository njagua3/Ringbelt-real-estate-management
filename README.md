# Ringbelt-real-estate-management

# Tenant Management System

This is a full-stack web application built using Flask for the backend and React.js for the frontend. The system allows managing tenants, landlords, and properties, with features to track rent payments and manage relationships between tenants and landlords.

## Features

- Full CRUD operations for tenants, landlords, and properties.
- Rent payment tracking with due date on the 5th of each month.
- Responsive UI with navigation using React Router.
- Form validation using Formik and Yup.
- Data fetched dynamically from the backend using Axios.

## Installation

### Backend (Flask)
1. Navigate to the backend directory:
   ```bash
   cd backend
Install the dependencies:
bash
Copy code
pipenv install
Run the Flask app:
bash
Copy code
python app.py
Frontend (React)
Navigate to the frontend directory:
bash
Copy code
cd frontend
Install the dependencies:
bash
Copy code
npm install
Run the React app:
bash
Copy code
npm start
Technologies Used
Backend: Flask, SQLAlchemy, Marshmallow
Frontend: React, React Router, Axios, Formik, Yup
Database: SQLite