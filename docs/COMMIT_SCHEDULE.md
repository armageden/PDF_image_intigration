# GitHub Commit Schedule

This document outlines the planned commit schedule for building this project over multiple days to maintain a consistent GitHub streak.

## Overview

**Total Duration**: ~10 days  
**Commits per day**: 1-3 meaningful commits  
**Goal**: Natural development progression with proper git history

---

## Day 1: Project Setup & Documentation
**Date**: December 5, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Initial commit - project structure | README.md, .gitignore |
| 2 | Add architecture documentation | docs/ARCHITECTURE.md |
| 3 | Add API and security docs | docs/API.md, docs/SECURITY.md |

---

## Day 2: Backend Foundation
**Date**: December 6, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Set up FastAPI project | backend/main.py, requirements.txt |
| 2 | Add database models | backend/src/models/ |
| 3 | Add configuration and utils | backend/src/config.py, .env.example |

---

## Day 3: Authentication System
**Date**: December 7, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Implement auth service | backend/src/services/auth_service.py |
| 2 | Add auth API routes | backend/src/api/auth.py |
| 3 | Add security middleware | backend/src/middleware/ |

---

## Day 4: PDF Processing
**Date**: December 8, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add PDF service | backend/src/services/pdf_service.py |
| 2 | Add PDF API routes | backend/src/api/pdf.py |
| 3 | Add file management utils | backend/src/utils/file_utils.py |

---

## Day 5: Image Generation
**Date**: December 9, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add image generation service | backend/src/services/image_service.py |
| 2 | Add image API routes | backend/src/api/images.py |
| 3 | Add backend tests | backend/tests/ |

---

## Day 6: Frontend Setup
**Date**: December 10, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Initialize Vite project | frontend/package.json, vite.config.js |
| 2 | Add design system CSS | frontend/src/styles/ |
| 3 | Add base HTML and routing | frontend/index.html |

---

## Day 7: Frontend Components
**Date**: December 11, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add auth pages | frontend/src/pages/login.*, register.* |
| 2 | Add API service layer | frontend/src/services/ |
| 3 | Add navbar component | frontend/src/components/ |

---

## Day 8: Core Features UI
**Date**: December 12, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add upload interface | frontend/src/pages/upload.* |
| 2 | Add drag-and-drop component | frontend/src/components/upload-zone.js |
| 3 | Add progress indicators | frontend/src/components/progress.js |

---

## Day 9: Gallery & Polish
**Date**: December 13, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add gallery page | frontend/src/pages/gallery.* |
| 2 | Add image card components | frontend/src/components/image-card.js |
| 3 | Add responsive styles and animations | frontend/src/styles/ |

---

## Day 10: Deployment & Final
**Date**: December 14, 2024

| Commit | Description | Files |
|--------|-------------|-------|
| 1 | Add Docker configuration | Dockerfile, docker-compose.yml |
| 2 | Add deployment docs | docs/DEPLOYMENT.md, CONTRIBUTING.md |
| 3 | Final polish and README update | README.md |

---

## Git Commands Quick Reference

```bash
# Stage files
git add <files>

# Commit with message
git commit -m "type: description"

# Push to remote
git push origin main
```

## Commit Message Format

Use conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance
