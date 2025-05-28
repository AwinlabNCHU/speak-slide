from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="AI Service API",
    description="Backend API for AI Service Landing Page",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js development server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactRequest(BaseModel):
    email: str
    message: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to AI Service API"}

@app.post("/api/contact")
async def contact(request: ContactRequest):
    try:
        # Here you would typically process the contact request
        # For example, sending an email or storing in a database
        return {
            "status": "success",
            "message": "Thank you for your interest! We'll get back to you soon."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/features")
async def get_features():
    return {
        "features": [
            {
                "id": 1,
                "title": "Real-time Processing",
                "description": "Process data in real-time with our advanced AI algorithms.",
                "icon": "lightning"
            },
            {
                "id": 2,
                "title": "Secure & Reliable",
                "description": "Enterprise-grade security with 99.9% uptime guarantee.",
                "icon": "shield"
            },
            {
                "id": 3,
                "title": "Easy Integration",
                "description": "Seamlessly integrate with your existing systems and workflows.",
                "icon": "sync"
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 