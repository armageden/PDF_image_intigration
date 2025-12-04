# Security Documentation

## Overview

This document outlines the security measures implemented in the PDF-to-Image Illustration Application.

## Authentication System

### JWT Token Strategy

```
┌─────────────────────────────────────────────────────────┐
│                    Token Flow                           │
├─────────────────────────────────────────────────────────┤
│  1. User logs in with email/password                    │
│  2. Server validates credentials                        │
│  3. Server issues:                                      │
│     • Access Token (15 min expiry, in response)         │
│     • Refresh Token (7 days expiry, httpOnly cookie)    │
│  4. Client uses access token for API calls              │
│  5. When access token expires, use refresh token        │
│  6. Refresh token rotation on each refresh              │
└─────────────────────────────────────────────────────────┘
```

### Password Security

- **Hashing**: bcrypt with 12 salt rounds
- **Requirements**:
  - Minimum 12 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character

## API Security

### Rate Limiting

| Endpoint Category | Rate Limit | Window |
|-------------------|------------|--------|
| Authentication    | 5 requests | 1 minute |
| PDF Upload        | 10 requests | 1 hour |
| Image Generation  | 20 requests | 1 hour |
| General API       | 100 requests | 1 minute |

### CORS Configuration

```python
CORS_CONFIG = {
    "allow_origins": ["http://localhost:5173"],  # Add production domains
    "allow_credentials": True,
    "allow_methods": ["GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Authorization", "Content-Type"],
}
```

### Input Validation

#### PDF Upload Validation
1. File extension must be `.pdf`
2. MIME type must be `application/pdf`
3. File size limit: 50MB
4. PDF structure validation using PyPDF2
5. Malicious content scanning

#### Request Validation
- All inputs sanitized against XSS
- SQL injection prevented via parameterized queries
- Path traversal prevention

## File Security

### Upload Handling

```python
# File storage structure
uploads/
├── {user_id}/
│   ├── pdfs/
│   │   └── {uuid}.pdf      # Original PDFs
│   └── generated/
│       └── {uuid}.png      # Generated images
```

### Security Measures

1. **Filename Sanitization**: All uploaded filenames are replaced with UUIDs
2. **Isolated Processing**: Each PDF processed in isolated environment
3. **Temporary File Cleanup**: Automatic cleanup after processing
4. **Access Control**: Users can only access their own files

## Secure Headers

All responses include security headers:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## Environment Variables

### Required Secrets

```bash
# .env file (NEVER commit to git)
SECRET_KEY=<random-256-bit-key>
DATABASE_URL=sqlite:///./app.db
AI_API_KEY=<your-api-key>
ALLOWED_ORIGINS=http://localhost:5173
```

### Key Generation

```bash
# Generate secure secret key
python -c "import secrets; print(secrets.token_hex(32))"
```

## Threat Mitigation

| Threat | Mitigation |
|--------|------------|
| Brute Force | Rate limiting + account lockout |
| Session Hijacking | httpOnly cookies + token rotation |
| XSS | Input sanitization + CSP headers |
| CSRF | SameSite cookies + token validation |
| SQL Injection | Parameterized queries (SQLAlchemy) |
| File Upload Attacks | Validation + isolated processing |

## Incident Response

1. **Detection**: Monitor logs for suspicious activity
2. **Containment**: Rate limit/block affected IPs
3. **Eradication**: Patch vulnerabilities
4. **Recovery**: Restore from backups if needed
5. **Lessons Learned**: Update security measures
