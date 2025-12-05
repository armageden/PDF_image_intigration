"""
PDF Processing API routes
Handles PDF upload, processing, and status tracking
"""

from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class PDFUploadResponse(BaseModel):
    """PDF upload response schema"""
    job_id: str
    filename: str
    status: str
    pages: int


class PDFStatusResponse(BaseModel):
    """PDF processing status response"""
    job_id: str
    status: str
    progress: int
    extracted_text: Optional[str] = None


@router.post("/upload", response_model=PDFUploadResponse, status_code=status.HTTP_202_ACCEPTED)
async def upload_pdf(file: UploadFile = File(...)):
    """Upload a PDF file for processing"""
    # TODO: Implement in Day 4
    if not file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
    
    return {
        "job_id": "placeholder-job-id",
        "filename": file.filename,
        "status": "processing",
        "pages": 0
    }


@router.get("/{job_id}/status", response_model=PDFStatusResponse)
async def get_pdf_status(job_id: str):
    """Get PDF processing status"""
    # TODO: Implement in Day 4
    return {
        "job_id": job_id,
        "status": "processing",
        "progress": 50,
        "extracted_text": None
    }


@router.delete("/{job_id}")
async def delete_pdf_job(job_id: str):
    """Delete a PDF job and its associated files"""
    # TODO: Implement in Day 4
    return {"message": f"Job {job_id} deleted"}
