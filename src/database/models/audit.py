"""
Author: Nguyen Khac Trung Kien
"""
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import Relationship

"""
Use for tracking entity creation and update time
"""

class AuditCreation:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
class AuditUpdate:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
