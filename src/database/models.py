"""Complete database models for SportEval Pro."""

from sqlalchemy import Column, Integer, String, Date, Float, Text, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

# ==================== ENUMERATIONS ====================

class GenderEnum(enum.Enum):
    MALE = "M"
    FEMALE = "F"

class UserRoleEnum(enum.Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    INSPECTOR = "inspector"
    DIRECTOR = "director"
    STUDENT = "student"

class EventCategoryEnum(enum.Enum):
    SPRINT = "sprint"
    LONG_DISTANCE = "long_distance"
    JUMPING = "jumping"
    THROWING = "throwing"
    SWIMMING = "swimming"
    TEAM_SPORT = "team_sport"
    GYMNASTICS = "gymnastics"
    CROSSFIT = "crossfit"
    MILITARY = "military"

# ==================== BASE TABLES ====================

class Establishment(Base):
    """School/Institution information."""
    __tablename__ = "establishments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    address = Column(String(255))
    city = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    director_name = Column(String(150))
    seal = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base):
    """User accounts (Admin, Teachers, Inspectors, etc.)."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    role = Column(Enum(UserRoleEnum), nullable=False)
    establishment_id = Column(Integer, ForeignKey("establishments.id"))
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Teacher(Base):
    """Physical Education Teachers."""
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    specialty = Column(String(100))
    signature_path = Column(String(500))
    diplomas = Column(Text)
    years_experience = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Class(Base):
    """School classes."""
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    level = Column(String(20))
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    academic_year = Column(String(20))
    student_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Student(Base):
    """Student information."""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    massar_code = Column(String(50), unique=True)
    photo_path = Column(String(500))
    
    height = Column(Float)
    weight = Column(Float)
    
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    
    medical_notes = Column(Text)
    has_medical_conditions = Column(Boolean, default=False)
    medical_conditions_details = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ==================== SPORTS & EVENTS ====================

class Event(Base):
    """Sports events/exercises."""
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    category = Column(Enum(EventCategoryEnum), nullable=False)
    event_type = Column(String(50))
    unit = Column(String(50))
    gender_specific = Column(Boolean, default=True)
    min_age = Column(Integer)
    max_age = Column(Integer)
    description = Column(Text)
    criteria = Column(Text)
    examples = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Bareme(Base):
    """Scoring scales/benchmarks."""
    __tablename__ = "baremes"
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String(150))
    gender = Column(Enum(GenderEnum), nullable=False)
    age_min = Column(Integer)
    age_max = Column(Integer)
    scoring_table = Column(Text, nullable=False)
    official_standard = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ==================== ASSESSMENTS ====================

class Assessment(Base):
    """Student performance assessments."""
    __tablename__ = "assessments"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    
    performance_value = Column(Float, nullable=False)
    raw_score = Column(Float)
    adjusted_score = Column(Float)
    
    mpi = Column(Float)
    ssi = Column(Float)
    epi = Column(Float)
    esi = Column(Float)
    api = Column(Float)
    gpi = Column(Float)
    
    assessment_date = Column(Date, nullable=False)
    assessment_mode = Column(String(20))
    observations = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class StudentProgress(Base):
    """Historical tracking of student progress."""
    __tablename__ = "student_progress"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    
    performance_value = Column(Float)
    score = Column(Float)
    assessment_date = Column(Date, nullable=False)
    academic_year = Column(String(20))
    
    created_at = Column(DateTime, default=datetime.utcnow)


# ==================== REPORTS ====================

class Report(Base):
    """Generated reports."""
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    report_type = Column(String(50))
    format = Column(String(20))
    
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    
    file_path = Column(String(500))
    content = Column(Text)
    
    signed = Column(Boolean, default=False)
    signature_date = Column(DateTime)
    seal_applied = Column(Boolean, default=False)
    qr_code = Column(String(500))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ==================== AI & STATISTICS ====================

class AIAnalysis(Base):
    """AI analysis results and recommendations."""
    __tablename__ = "ai_analysis"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    analysis_type = Column(String(100))
    
    findings = Column(Text)
    recommendations = Column(Text)
    confidence_score = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)


class Statistics(Base):
    """Cached statistics for performance."""
    __tablename__ = "statistics"
    
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    establishment_id = Column(Integer, ForeignKey("establishments.id"))
    
    metric_name = Column(String(100))
    metric_value = Column(Float)
    academic_year = Column(String(20))
    
    created_at = Column(DateTime, default=datetime.utcnow)


# ==================== AUDIT & HISTORY ====================

class AuditLog(Base):
    """System audit trail."""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(100))
    table_name = Column(String(50))
    record_id = Column(Integer)
    old_values = Column(Text)
    new_values = Column(Text)
    ip_address = Column(String(50))
    
    created_at = Column(DateTime, default=datetime.utcnow)


class Backup(Base):
    """Backup history."""
    __tablename__ = "backups"
    
    id = Column(Integer, primary_key=True)
    backup_type = Column(String(50))
    file_path = Column(String(500))
    file_size = Column(Integer)
    backup_date = Column(DateTime, nullable=False)
    restored = Column(Boolean, default=False)
    restored_date = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
