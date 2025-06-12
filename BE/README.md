# Vute Backend

A FastAPI-based backend service for user authentication and management.

## Features
- User registration and authentication
- JWT token-based authentication
- Password reset functionality
- Email notifications
- SQLite database (configurable for other databases)
- Comprehensive API documentation
- CORS support
- Environment-based configuration

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Vute_BE
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create .env file with required environment variables:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///./vute.db
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-email-password
   MAIL_FROM=your-email@example.com
   MAIL_PORT=587
   MAIL_SERVER=smtp.gmail.com
   ```

5. Initialize the database:
   ```bash
   python recreate_db.py
   ```

6. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints
- POST `/api/v1/auth/register` - Register a new user
- POST `/api/v1/auth/login` - Login and get access token
- POST `/api/v1/auth/forgot-password` - Request password reset
- POST `/api/v1/auth/reset-password` - Reset password
- GET `/api/v1/auth/debug/user/{email}` - Check user existence

## Testing
Run the test script:
```bash
python test_api.py
```

## Project Structure
```
Vute_BE/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── auth.py
│   │   ├── core/
│   │   │   ├── security.py
│   │   │   └── email.py
│   │   ├── models/
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   └── token.py
│   │   ├── database.py
│   │   ├── config.py
│   │   └── main.py
│   ├── test/
│   ├── requirements.txt
│   ├── README.md
│   └── .gitignore
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.