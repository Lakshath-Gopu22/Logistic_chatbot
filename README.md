🚚 JackShelby AI – Logistics Customer Support Chatbot

An AI-powered logistics support assistant that helps customers track orders, check delivery status, request cancellations, and get logistics insights using natural language.

The system uses a React frontend, FastAPI backend, SQLite database, and a locally hosted Mistral LLM via Ollama.

🌐 Live Demo

Frontend (Vercel)

https://jackshelby-ai.in

Backend API (Render)

https://jackshelby-chatbot.onrender.com
📌 Project Objective

Customer support teams in logistics companies receive thousands of repetitive queries like:

Where is my order?

When will my package arrive?

Can I cancel my order?

Is my shipment delayed?

This project automates those interactions using AI + workflow automation, improving response time and reducing manual support workload.

🧠 Key Features
Customer Features

Login authentication

Order history dashboard

Real-time order tracking

Order cancellation eligibility check

AI chatbot for natural language queries

Admin Features

Order analytics dashboard

Customer insights

Delivered / delayed / returned metrics

Refund tracking

AI Chatbot Capabilities

Understands logistics questions

Uses order context for responses

Generates responses using Mistral LLM

🏗 System Architecture
User
  ↓
Domain (jackshelby-ai.in)
  ↓
Vercel (React Frontend)
  ↓
Render (FastAPI Backend)
  ↓
ngrok Tunnel
  ↓
Ollama Runtime
  ↓
Mistral 7B LLM
  ↓
SQLite Database
⚙ Tech Stack

Frontend

React

TailwindCSS

Vercel Hosting

Backend

FastAPI

Python

SQLAlchemy

Database

SQLite

AI Layer

Ollama

Mistral 7B LLM

Infrastructure

Vercel

Render

ngrok

📂 Project Structure
Logistic_chatbot
│
├── backend
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── seed.py
│   ├── ai_engine.py
│   └── requirements.txt
│
├── react_frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── api.js
│   └── package.json
│
└── README.md
🚀 Running the Project Locally
1️⃣ Clone repository
git clone https://github.com/YOUR_USERNAME/Logistic_chatbot.git
cd Logistic_chatbot
2️⃣ Run Backend
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs
3️⃣ Run Frontend
cd react_frontend

npm install
npm start

Frontend runs at:

http://localhost:3000
🤖 Running the AI Model

Install Ollama:

https://ollama.com

Start the model:

ollama run mistral

Expose the local AI service:

ngrok http 11434

Update ai_engine.py with the ngrok URL.

🧪 Demo Accounts

Customer

username: luffy
password: onepiece
username: eren
password: aot

Admin

username: admin
password: admin123
📊 Example AI Query

User:

Where is my order?

AI Response:

Your order ORD102 is currently in transit from Chennai and is expected to arrive in Coimbatore by tomorrow.
🔐 Security & Validation

CORS enabled for frontend access

Input validation using Pydantic

Database session management with SQLAlchemy

⚠ Limitations

Current AI architecture runs locally.

If the laptop running Ollama stops:

AI responses will stop

Frontend and backend will still work.

🔮 Future Improvements

Deploy LLM on GPU server

Implement RAG with order database

Real-time shipment tracking integration

Multi-language support

Vector database for knowledge retrieval

🎓 Academic Use

This project was built as a portfolio / academic project demonstrating AI-assisted logistics support automation.
