# AI Service Landing Page

A modern, responsive landing page for an AI service built with Vue.js and FastAPI.

## Project Structure
```
.
├── frontend/          # Vue.js frontend application
└── backend/          # FastAPI backend application
```

## Features
- Modern, responsive design
- Interactive UI components
- FastAPI backend with AI service integration
- Real-time data processing
- RESTful API endpoints

## Tech Stack
- Frontend:
  - Vue.js 3
  - Vite
  - TailwindCSS
  - Vue Router
  - Axios

- Backend:
  - FastAPI
  - Python 3.8+
  - Uvicorn
  - Pydantic

## Getting Started

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\bin\activate.bat
pip install -r requirements.txt
uvicorn main:app --reload
```

## Development
- Frontend runs on: http://localhost:5173
- Backend runs on: http://localhost:8000
- API documentation: http://localhost:8000/docs 
