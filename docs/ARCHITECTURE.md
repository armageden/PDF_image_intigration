# PDF-to-Image Illustration Application

> Transform your PDF documents into beautiful, AI-generated visual illustrations

## 🌟 Overview

This application takes PDF documents as input, extracts the key concepts and content, then generates stunning visual illustrations using AI to help with imagination and understanding.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐    │
│  │  Upload  │ │  Gallery │ │  Auth    │ │  Settings        │    │
│  │  Module  │ │  View    │ │  Module  │ │  & Preferences   │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │ HTTPS │
                              ▼       ▼
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND (FastAPI)                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐    │
│  │  Auth    │ │  PDF     │ │  Image   │ │  File            │    │
│  │  Service │ │  Parser  │ │  Gen     │ │  Manager         │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Security Middleware                        │    │
│  │  • Rate Limiting • CORS • Input Validation • JWT Auth   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────────┐
        │  SQLite  │   │  File    │   │  AI Image    │
        │  Database│   │  Storage │   │  Generation  │
        └──────────┘   └──────────┘   └──────────────┘
```

## 📁 Project Structure

```
pdf-image-intigration/
├── docs/
│   ├── ARCHITECTURE.md     # This file
│   ├── API.md              # API documentation
│   ├── SECURITY.md         # Security documentation
│   └── DEPLOYMENT.md       # Deployment guide
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API service layer
│   │   ├── styles/         # CSS styles
│   │   └── utils/          # Utility functions
│   ├── public/
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── api/            # API routes
│   │   ├── services/       # Business logic
│   │   ├── models/         # Database models
│   │   ├── middleware/     # Security middleware
│   │   └── utils/          # Utility functions
│   ├── tests/
│   └── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🔐 Security Features

- **JWT Authentication** - Secure token-based authentication
- **Rate Limiting** - Prevent abuse and DDoS attacks
- **Input Validation** - Comprehensive validation on all inputs
- **CORS Protection** - Controlled cross-origin access
- **Secure File Handling** - Safe PDF processing and storage

## 🚀 Features

1. **PDF Upload** - Drag-and-drop or click to upload PDFs
2. **Content Extraction** - Intelligent parsing of PDF content
3. **AI Illustration** - Generate beautiful images from text
4. **Gallery View** - Browse and manage generated images
5. **Download & Share** - Export images in multiple formats
6. **User Management** - Secure user authentication

## 🛠️ Tech Stack

| Layer    | Technology        |
|----------|-------------------|
| Frontend | Vite + Vanilla JS |
| Backend  | FastAPI (Python)  |
| Database | SQLite            |
| AI       | Image Generation API |
| Auth     | JWT + bcrypt      |
