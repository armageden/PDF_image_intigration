"""
PDF Job model for tracking PDF processing tasks
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from src.models.database import Base


class JobStatus(str, enum.Enum):
    """Status of a PDF processing job"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class PDFJob(Base):
    """PDF processing job model"""
    
    __tablename__ = "pdf_jobs"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    
    # File information
    original_filename = Column(String(255), nullable=False)
    stored_filename = Column(String(255), nullable=False)
    file_size = Column(Integer, nullable=False)
    page_count = Column(Integer, default=0)
    
    # Processing status
    status = Column(Enum(JobStatus), default=JobStatus.PENDING)
    progress = Column(Integer, default=0)  # 0-100
    error_message = Column(Text, nullable=True)
    
    # Extracted content
    extracted_text = Column(Text, nullable=True)
    extracted_sections = Column(Text, nullable=True)  # JSON string of sections
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="pdf_jobs")
    generated_images = relationship("GeneratedImage", back_populates="pdf_job", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<PDFJob(id={self.id}, status={self.status})>"
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            "id": self.id,
            "original_filename": self.original_filename,
            "file_size": self.file_size,
            "page_count": self.page_count,
            "status": self.status.value,
            "progress": self.progress,
            "error_message": self.error_message,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }
