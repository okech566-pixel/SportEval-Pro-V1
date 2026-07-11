"""Database operations and utilities."""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from .init_db import get_session
from .models import Student, Assessment, Event, Bareme, AuditLog, User

logger = logging.getLogger(__name__)


class StudentService:
    """Service for student operations."""
    
    @staticmethod
    def get_all_students(class_id: Optional[int] = None):
        """Get all students or by class."""
        session = get_session()
        try:
            query = session.query(Student)
            if class_id:
                query = query.filter_by(class_id=class_id)
            return query.all()
        finally:
            session.close()
    
    @staticmethod
    def get_student(student_id: int) -> Optional[Student]:
        """Get student by ID."""
        session = get_session()
        try:
            return session.query(Student).filter_by(id=student_id).first()
        finally:
            session.close()
    
    @staticmethod
    def create_student(data: Dict) -> Optional[Student]:
        """Create new student."""
        session = get_session()
        try:
            student = Student(**data)
            session.add(student)
            session.commit()
            logger.info(f"Student created: {student.first_name} {student.last_name}")
            return student
        except Exception as e:
            session.rollback()
            logger.error(f"Error creating student: {e}")
            return None
        finally:
            session.close()
    
    @staticmethod
    def update_student(student_id: int, data: Dict) -> bool:
        """Update student information."""
        session = get_session()
        try:
            student = session.query(Student).filter_by(id=student_id).first()
            if not student:
                return False
            
            for key, value in data.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            
            session.commit()
            logger.info(f"Student updated: {student_id}")
            return True
        except Exception as e:
            session.rollback()
            logger.error(f"Error updating student: {e}")
            return False
        finally:
            session.close()


class AssessmentService:
    """Service for assessment operations."""
    
    @staticmethod
    def create_assessment(data: Dict) -> Optional[Assessment]:
        """Create new assessment."""
        session = get_session()
        try:
            assessment = Assessment(**data)
            session.add(assessment)
            session.commit()
            logger.info(f"Assessment created for student {data.get('student_id')}")
            return assessment
        except Exception as e:
            session.rollback()
            logger.error(f"Error creating assessment: {e}")
            return None
        finally:
            session.close()
    
    @staticmethod
    def get_student_assessments(student_id: int) -> List[Assessment]:
        """Get all assessments for a student."""
        session = get_session()
        try:
            return session.query(Assessment).filter_by(student_id=student_id).all()
        finally:
            session.close()
    
    @staticmethod
    def calculate_gpi(mpi: float, ssi: float, epi: float, esi: float, api: float) -> float:
        """Calculate Global Performance Index."""
        gpi = (mpi * 0.2 + ssi * 0.2 + epi * 0.2 + esi * 0.2 + api * 0.2)
        return round(gpi, 2)


class EventService:
    """Service for event operations."""
    
    @staticmethod
    def get_all_events() -> List[Event]:
        """Get all events."""
        session = get_session()
        try:
            return session.query(Event).all()
        finally:
            session.close()
    
    @staticmethod
    def get_event(event_id: int) -> Optional[Event]:
        """Get event by ID."""
        session = get_session()
        try:
            return session.query(Event).filter_by(id=event_id).first()
        finally:
            session.close()
    
    @staticmethod
    def get_baremes_for_event(event_id: int) -> List[Bareme]:
        """Get all baremes for an event."""
        session = get_session()
        try:
            return session.query(Bareme).filter_by(event_id=event_id).all()
        finally:
            session.close()


class AuditService:
    """Service for audit logging."""
    
    @staticmethod
    def log_action(user_id: int, action: str, table_name: str, record_id: int,
                   old_values: Dict = None, new_values: Dict = None, ip_address: str = None):
        """Log a database action for audit trail."""
        session = get_session()
        try:
            audit_log = AuditLog(
                user_id=user_id,
                action=action,
                table_name=table_name,
                record_id=record_id,
                old_values=json.dumps(old_values) if old_values else None,
                new_values=json.dumps(new_values) if new_values else None,
                ip_address=ip_address
            )
            session.add(audit_log)
            session.commit()
            logger.info(f"Audit log: {action} on {table_name}#{record_id}")
        except Exception as e:
            session.rollback()
            logger.error(f"Error logging audit: {e}")
        finally:
            session.close()
