🚀 Smart Loans – Blockchain Lending Platform

Built with FastAPI, SQLAlchemy, SQLite, and Web3 (Ganache)

Smart Loans is a decentralized loan management system that simulates a blockchain-integrated financial platform. Users can create accounts, transfer ETH, request loans, and repay them — while admins manage approvals, monitor overdue loans, and apply penalties for missed payments.

🔥 Features
👤 User Features

Create an account linked to an Ethereum address

Sync real ETH balance from Ganache

Transfer ETH between users

Request loans with duration and interest options

Repay active loans

View loan status, remaining balance, and repayment info

🔐 Authentication

Register new users

OAuth2 login with JWT tokens

Protected routes

Role-based access (User/Admin)

🛠 Admin Features

View all users, accounts, and loans

Approve or reject loans

Transfer ETH to borrowers on approval

Detect overdue loans

Automatically punish missed payments with penalties

⚙️ Tech Stack

FastAPI

SQLAlchemy

SQLite

Web3.py

Ganache

JWT Authentication

## Project Structure

Smart Loans/
│── main.py
│── database.py
│── models.py
│── enums.py
│── smartloans.db
│
├── contract/
│   ├── connect.py
│   ├── contract.py
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── admin.py
│
└── README.md

 ##

🧪 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Ganache

Ensure Ganache is running at:

http://127.0.0.1:7545

3️⃣ Launch FastAPI
uvicorn main:app --reload

4️⃣ Open API Docs
http://127.0.0.1:8000/docs

📬 Contact

Created as part of an academic project.
Open for improvements and contributions!
