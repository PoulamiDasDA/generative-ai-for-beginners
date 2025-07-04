# Flask Hello API - Best Practices Implementation

## Overview
This is an improved version of a simple Flask "Hello, World!" application that implements industry best practices for production-ready code.

## 🚀 What Was Added (Best Practices)

### 1. **Input Validation & Security**
- ✅ Input sanitization to prevent XSS attacks
- ✅ Parameter length limits (max 50 characters)
- ✅ Character validation (only safe characters allowed)
- ✅ Security headers (X-Frame-Options, X-XSS-Protection, etc.)

### 2. **Error Handling**
- ✅ Custom error handlers for 404 and 500 errors
- ✅ Try-catch blocks in endpoints
- ✅ Consistent JSON error responses

### 3. **Configuration Management**
- ✅ Environment-based configuration (.env file)
- ✅ Separate config classes for dev/prod/test
- ✅ Environment variable support

### 4. **Logging & Monitoring**
- ✅ Structured logging with timestamps
- ✅ Request logging for debugging
- ✅ Error logging for troubleshooting

### 5. **API Design**
- ✅ Consistent JSON responses
- ✅ Health check endpoint (`/health`)
- ✅ Proper HTTP status codes
- ✅ API documentation in docstrings

### 6. **Testing Infrastructure**
- ✅ Unit tests with unittest framework
- ✅ Test cases for valid/invalid inputs
- ✅ Error handling tests

### 7. **Dependencies Management**
- ✅ requirements.txt with pinned versions
- ✅ python-dotenv for environment variables

## 📁 Project Structure
```
/05-advanced-prompts/python/
├── aoai-assignment.py      # Main Flask application
├── config.py               # Configuration management
├── test_app.py            # Unit tests
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md             # This file
```

## 🔧 Installation & Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python aoai-assignment.py
   ```

3. **Run tests:**
   ```bash
   python -m unittest test_app.py
   ```

## 🌐 API Endpoints

### GET /
Greet a user by name.

**Parameters:**
- `name` (optional): Name to greet (max 50 chars, safe characters only)

**Examples:**
```bash
curl http://127.0.0.1:5000/                    # Returns: {"message": "Hello, World!", "name": "World"}
curl http://127.0.0.1:5000/?name=John          # Returns: {"message": "Hello, John!", "name": "John"}
curl http://127.0.0.1:5000/?name=<script>      # Returns: 400 error
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy", 
  "service": "flask-hello-app"
}
```

## 🔒 Security Features

- **XSS Prevention**: Input sanitization removes dangerous characters
- **Security Headers**: Prevents clickjacking and content sniffing
- **Input Validation**: Strict validation of user input
- **Error Handling**: No sensitive information leaked in errors

## 🏗️ Production Considerations

For production deployment, consider:

1. **Use a WSGI server** (Gunicorn, uWSGI)
2. **Set up reverse proxy** (Nginx)
3. **Configure proper logging** (centralized logging)
4. **Set strong SECRET_KEY**
5. **Enable HTTPS**
6. **Set up monitoring** (health checks, metrics)

## 📊 Original vs Improved

| Aspect | Original | Improved |
|--------|----------|----------|
| Lines of code | 11 | ~100 |
| Security | ❌ No protection | ✅ Multiple layers |
| Error handling | ❌ Basic | ✅ Comprehensive |
| Testing | ❌ None | ✅ Unit tests |
| Configuration | ❌ Hardcoded | ✅ Environment-based |
| Logging | ❌ None | ✅ Structured logging |
| API design | ❌ Plain text | ✅ JSON responses |
| Documentation | ❌ None | ✅ Full documentation |
