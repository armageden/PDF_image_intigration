# Deployment Guide

This guide covers deploying the PDF-to-Image Illustration application.

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- Domain name (for production)
- SSL certificates (Let's Encrypt recommended)

## Local Deployment

### Using Docker Compose

```bash
# Build containers
docker-compose build

# Start services
docker-compose up -d

# Check status
docker-compose ps
docker-compose logs -f
```

### Manual Deployment

**Backend:**
```bash
cd backend
source ../venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build
npm run preview
```

## Production Deployment

### Environment Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Configure production values:
```bash
# Required
SECRET_KEY=<generate-with: python -c "import secrets; print(secrets.token_hex(32))">
DATABASE_URL=sqlite:///./data/app.db
AI_API_KEY=<your-api-key>
ALLOWED_ORIGINS=https://yourdomain.com

# Optional
DEBUG=false
LOG_LEVEL=warning
```

### SSL/HTTPS Setup

For production, use a reverse proxy (nginx or Caddy) with SSL:

```nginx
# Example nginx config
server {
    listen 443 ssl;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    location /api {
        proxy_pass http://localhost:8000;
    }
    
    location / {
        root /path/to/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

### Health Monitoring

The API exposes a health endpoint:
```bash
curl http://localhost:8000/health
```

Set up monitoring alerts for this endpoint.

## Rollback Procedure

If deployment fails:

```bash
# Stop current containers
docker-compose down

# Checkout previous version
git checkout <previous-tag>

# Rebuild and restart
docker-compose build
docker-compose up -d
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port already in use | `lsof -i :8000` to find process |
| Database locked | Restart backend service |
| Frontend not building | Clear `node_modules` and reinstall |
