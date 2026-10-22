# Smart IT Helpdesk

A web-based IT helpdesk system built using Python Flask and MySQL.

## Project Overview

Smart IT Helpdesk is a web application designed to help manage IT support requests in an organized way. Employees can submit tickets for technical issues, while the IT support team can view submitted tickets and update their status.

The project demonstrates how a web application can connect a frontend, a Python backend, and a MySQL database to manage support requests.

## Problem Statement

In an organization, employees may face hardware, software, or network issues. Managing these requests manually can make it difficult to track complaints and their progress.

Smart IT Helpdesk provides a simple system to submit, store, view, and track IT support tickets.

## Features

* Submit IT support tickets with a title, category, and description.
* Automatically generate a unique ticket ID.
* Store submitted tickets in a MySQL database.
* View submitted tickets in a structured table.
* Track ticket status.
* Update ticket status to Open, In Progress, or Resolved.
* Display a success message after submitting a ticket.

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Database:** MySQL
* **Development Tools:** Visual Studio Code, Git, GitHub


  ## How It Works

1. The user opens the Smart IT Helpdesk web application.
2. The user enters a ticket title, selects a category, and describes the issue.
3. The application sends the submitted ticket to the Flask backend.
4. The backend stores the ticket details in the MySQL database.
5. Each ticket receives a unique ticket ID.
6. The IT support team can view submitted tickets on the tickets page.
7. The team can update a ticket's status to Open, In Progress, or Resolved.

## Project Structure

Smart-IT-Helpdesk/
├── app.py
├── .gitignore
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    ├── index.html
    └── tickets.html

### File Description

* **app.py:** Handles application routes, ticket submission, database operations, and status updates.
* **templates/index.html:** Contains the ticket submission page.
* **templates/tickets.html:** Displays submitted tickets and status controls.
* **static/style.css:** Defines the application's visual styling.
* **static/script.js:** Contains the frontend JavaScript.
* **.gitignore:** Prevents selected local files and sensitive configuration files from being tracked by Git.

## Installation and Setup

Follow these steps to run the project on your local computer.

### Prerequisites

Make sure you have installed:

* Python
* MySQL Server
* Git
* A code editor such as Visual Studio Code

### 1. Clone the Repository

git clone https://github.com/radhikasaini24/smart-it-helpdesk.git
cd smart-it-helpdesk

### 2. Create and Activate a Virtual Environment

On Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

### 3. Install Required Packages

python -m pip install Flask mysql-connector-python python-dotenv

### 4. Configure Environment Variables

Create a .env file in the project root and add your own MySQL credentials:

DB_PASSWORD=your_mysql_password

Replace your_mysql_password with your own MySQL password. Never share or upload your actual password.

### 5. Set Up the MySQL Database

Open MySQL Workbench or another MySQL client and create the database and table required by the application.

Use the database name:

CREATE DATABASE smart_helpdesk;

USE smart_helpdesk;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    category VARCHAR(50),
    description TEXT,
    status VARCHAR(30) DEFAULT 'Open'
);




### 6. Run the Application

python app.py

Open the local address shown by Flask in your browser, usually:

http://127.0.0.1:5000

### 7. Verify Ticket Data

To view the tickets stored in the database, run the following query in MySQL Workbench:

USE smart_helpdesk;
SELECT * FROM tickets;

This query displays all tickets stored in the 'tickets' table.

