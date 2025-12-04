# API Documentation

## Base URL
- Development: `http://localhost:8000/api/v1`
- Production: `https://your-domain.com/api/v1`

## Authentication

All authenticated endpoints require a Bearer token in the Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Endpoints

### Authentication

#### POST `/auth/register`
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123!",
  "name": "John Doe"
}
```

**Response (201):**
```json
{
  "message": "User created successfully",
  "user_id": "uuid-string"
}
```

---

#### POST `/auth/login`
Authenticate and receive access token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123!"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 900
}
```

---

#### POST `/auth/refresh`
Refresh access token (requires valid refresh token cookie).

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 900
}
```

---

### PDF Processing

#### POST `/pdf/upload`
Upload a PDF for processing. **🔐 Authenticated**

**Request:** `multipart/form-data`
- `file`: PDF file (max 50MB)

**Response (202):**
```json
{
  "job_id": "uuid-string",
  "filename": "document.pdf",
  "status": "processing",
  "pages": 12
}
```

---

#### GET `/pdf/{job_id}/status`
Check processing status. **🔐 Authenticated**

**Response (200):**
```json
{
  "job_id": "uuid-string",
  "status": "completed|processing|failed",
  "progress": 85,
  "extracted_text": "..." // Only when completed
}
```

---

### Image Generation

#### POST `/images/generate`
Generate illustration from extracted content. **🔐 Authenticated**

**Request Body:**
```json
{
  "job_id": "uuid-string",
  "style": "aesthetic|realistic|artistic|minimal",
  "sections": [0, 1, 2] // Optional: specific sections to illustrate
}
```

**Response (202):**
```json
{
  "generation_id": "uuid-string",
  "status": "generating",
  "estimated_time": 30
}
```

---

#### GET `/images/{generation_id}`
Get generated image details. **🔐 Authenticated**

**Response (200):**
```json
{
  "generation_id": "uuid-string",
  "status": "completed",
  "images": [
    {
      "id": "img-uuid",
      "url": "/images/generated/img-uuid.png",
      "thumbnail_url": "/images/thumbnails/img-uuid.png",
      "prompt_used": "...",
      "created_at": "2024-01-01T12:00:00Z"
    }
  ]
}
```

---

#### GET `/images/gallery`
Get user's generated images gallery. **🔐 Authenticated**

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20, max: 100)
- `sort` (string): Sort by `created_at|name` (default: created_at)

**Response (200):**
```json
{
  "images": [...],
  "total": 45,
  "page": 1,
  "pages": 3
}
```

---

### User Management

#### GET `/user/profile`
Get current user profile. **🔐 Authenticated**

**Response (200):**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2024-01-01T12:00:00Z",
  "usage": {
    "pdfs_processed": 15,
    "images_generated": 42
  }
}
```

---

## Error Responses

All errors follow this format:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {} // Optional additional info
  }
}
```

### Common Error Codes
| Code | HTTP Status | Description |
|------|-------------|-------------|
| `UNAUTHORIZED` | 401 | Invalid or missing authentication |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_ERROR` | 422 | Invalid request data |
| `RATE_LIMITED` | 429 | Too many requests |
| `SERVER_ERROR` | 500 | Internal server error |
