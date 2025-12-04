# PDF-to-Image Illustration

> Transform your PDF documents into beautiful, AI-generated visual illustrations

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![Node](https://img.shields.io/badge/node-18+-green.svg)

## Overview

This application takes PDF documents, extracts key content, and generates stunning AI-powered visual illustrations to help you better imagine and understand the material.

## Features

- 📄 **PDF Upload** - Drag-and-drop or click to upload
- 🎨 **AI Illustration** - Generate beautiful visuals from text
- 🖼️ **Gallery View** - Browse and manage generated images
- 🔐 **Secure Authentication** - JWT-based user system
- ⚡ **Fast & Responsive** - Modern, optimized UI

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Vite + Vanilla JS |
| Backend | FastAPI (Python) |
| Database | SQLite |
| AI | Image Generation API |

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/PDF_image_intigration.git
cd PDF_image_intigration
```

2. **Setup backend**
```bash
python3 -m venv venv
source venv/bin/activate
cd backend
pip install -r requirements.txt
```

3. **Setup frontend**
```bash
cd frontend
npm install
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

### Running

**Backend:**
```bash
cd backend
source ../venv/bin/activate
python main.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

Visit `http://localhost:5173`

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Security](docs/SECURITY.md)
- [Deployment](docs/DEPLOYMENT.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.
