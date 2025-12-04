# Contributing Guide

Welcome to the PDF-to-Image Illustration project! This guide covers development setup and workflows.

## Prerequisites

- **Node.js** v18+
- **Python** 3.10+
- **pip** and **npm**

## Development Setup

### 1. Clone and Setup

```bash
git clone <repository-url>
cd pdf-image-intigration
```

### 2. Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

## Running the Application

### Development Mode

**Terminal 1 - Backend:**
```bash
cd backend
source ../venv/bin/activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

The app will be available at `http://localhost:5173`

### Production Build

```bash
# Build frontend
cd frontend
npm run build

# Run backend in production
cd backend
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Testing

```bash
# Backend tests
cd backend
pytest tests/ -v

# Frontend linting
cd frontend
npm run lint
```

## Code Style

- **Python**: Follow PEP 8, use type hints
- **JavaScript**: ES6+, use JSDoc comments
- **CSS**: BEM naming convention

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes with clear commits
3. Ensure all tests pass
4. Submit PR with description of changes
