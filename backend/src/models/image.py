"""
Generated Image model for storing AI-generated illustrations
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from src.models.database import Base


class ImageStyle(str, enum.Enum):
    """Style of generated image"""
    AESTHETIC = "aesthetic"
    REALISTIC = "realistic"
    ARTISTIC = "artistic"
    MINIMAL = "minimal"


class ImageStatus(str, enum.Enum):
    """Status of image generation"""
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class GeneratedImage(Base):
    """Generated image model"""
    
    __tablename__ = "generated_images"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    pdf_job_id = Column(String(36), ForeignKey("pdf_jobs.id"), nullable=True, index=True)
    
    # Image information
    filename = Column(String(255), nullable=False)
    thumbnail_filename = Column(String(255), nullable=True)
    style = Column(Enum(ImageStyle), default=ImageStyle.AESTHETIC)
    
    # Generation details
    status = Column(Enum(ImageStatus), default=ImageStatus.GENERATING)
    prompt_used = Column(Text, nullable=True)
    source_text = Column(Text, nullable=True)
    section_index = Column(String(50), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="generated_images")
    pdf_job = relationship("PDFJob", back_populates="generated_images")
    
    def __repr__(self):
        return f"<GeneratedImage(id={self.id}, style={self.style})>"
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            "id": self.id,
            "filename": self.filename,
            "thumbnail_filename": self.thumbnail_filename,
            "style": self.style.value if self.style else None,
            "status": self.status.value if self.status else None,
            "prompt_used": self.prompt_used,
            "section_index": self.section_index,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "url": f"/static/generated/{self.filename}" if self.filename else None,
            "thumbnail_url": f"/static/thumbnails/{self.thumbnail_filename}" if self.thumbnail_filename else None
        }
