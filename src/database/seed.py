"""Populate database with sample data."""

from datetime import datetime, date, timedelta
from .models import (
    Establishment, User, Teacher, Class, Student, Event,
    Bareme, UserRoleEnum, GenderEnum, EventCategoryEnum
)
from .init_db import get_session
import json
import logging

logger = logging.getLogger(__name__)

def seed_database():
    """Add sample data to database."""
    
    session = get_session()
    
    try:
        # Check if data already exists
        if session.query(Establishment).first():
            logger.info("Database already seeded, skipping...")
            return
        
        # 1. Create Establishment
        establishment = Establishment(
            name="Lycée National El Kamel",
            address="123 Avenue Mohammed V",
            city="Casablanca",
            phone="+212 5 22 123 456",
            email="info@lycee-kamel.ma",
            director_name="Mr. Hassan Bennani"
        )
        session.add(establishment)
        session.flush()
        
        # 2. Create Admin User
        admin = User(
            username="admin",
            email="admin@lycee-kamel.ma",
            password_hash="hashed_password_here",
            first_name="Admin",
            last_name="System",
            role=UserRoleEnum.ADMIN,
            establishment_id=establishment.id
        )
        session.add(admin)
        session.flush()
        
        # 3. Create Teacher
        teacher_user = User(
            username="teacher_eps",
            email="teacher@lycee-kamel.ma",
            password_hash="hashed_password_here",
            first_name="Ahmed",
            last_name="Bouazza",
            role=UserRoleEnum.TEACHER,
            establishment_id=establishment.id
        )
        session.add(teacher_user)
        session.flush()
        
        teacher = Teacher(
            user_id=teacher_user.id,
            establishment_id=establishment.id,
            specialty="Athlétisme",
            years_experience=10
        )
        session.add(teacher)
        session.flush()
        
        # 4. Create Class
        class_3a = Class(
            name="3ème A",
            level="3ème",
            establishment_id=establishment.id,
            teacher_id=teacher.id,
            academic_year="2024-2025"
        )
        session.add(class_3a)
        session.flush()
        
        # 5. Create Students
        students_data = [
            {"first_name": "Mohamed", "last_name": "Ali", "gender": GenderEnum.MALE},
            {"first_name": "Fatima", "last_name": "Hassan", "gender": GenderEnum.FEMALE},
            {"first_name": "Ahmad", "last_name": "Karim", "gender": GenderEnum.MALE},
            {"first_name": "Laila", "last_name": "Ibrahim", "gender": GenderEnum.FEMALE},
            {"first_name": "Hassan", "last_name": "Samir", "gender": GenderEnum.MALE},
        ]
        
        students = []
        for i, data in enumerate(students_data):
            student = Student(
                first_name=data["first_name"],
                last_name=data["last_name"],
                birth_date=date(2009, 6, 15) + timedelta(days=i*30),
                gender=data["gender"],
                massar_code=f"MASSAR{1000001+i}",
                height=165 + i * 2,
                weight=60 + i * 3,
                class_id=class_3a.id,
                establishment_id=establishment.id
            )
            session.add(student)
            students.append(student)
        
        session.flush()
        
        # 6. Create Events
        events_data = [
            {
                "name": "100m Sprint",
                "category": EventCategoryEnum.SPRINT,
                "event_type": "speed",
                "unit": "seconds",
                "description": "100 meter sprint race"
            },
            {
                "name": "Long Jump",
                "category": EventCategoryEnum.JUMPING,
                "event_type": "power",
                "unit": "meters",
                "description": "Long jump competition"
            },
            {
                "name": "Shot Put",
                "category": EventCategoryEnum.THROWING,
                "event_type": "power",
                "unit": "meters",
                "description": "Shot put throwing"
            },
            {
                "name": "800m Run",
                "category": EventCategoryEnum.LONG_DISTANCE,
                "event_type": "endurance",
                "unit": "seconds",
                "description": "800 meter distance run"
            },
        ]
        
        events = []
        for event_data in events_data:
            event = Event(**event_data)
            session.add(event)
            events.append(event)
        
        session.flush()
        
        # 7. Create Baremes
        bareme_100m_m = Bareme(
            event_id=events[0].id,
            name="Barème 100m Garçons",
            gender=GenderEnum.MALE,
            age_min=13,
            age_max=16,
            scoring_table=json.dumps({
                "10.0": 100, "10.5": 90, "11.0": 80,
                "11.5": 70, "12.0": 60, "12.5": 50,
                "13.0": 40, "14.0": 30
            }),
            official_standard=True
        )
        
        bareme_100m_f = Bareme(
            event_id=events[0].id,
            name="Barème 100m Filles",
            gender=GenderEnum.FEMALE,
            age_min=13,
            age_max=16,
            scoring_table=json.dumps({
                "11.0": 100, "11.5": 90, "12.0": 80,
                "12.5": 70, "13.0": 60, "13.5": 50,
                "14.0": 40, "15.0": 30
            }),
            official_standard=True
        )
        
        session.add(bareme_100m_m)
        session.add(bareme_100m_f)
        
        session.commit()
        logger.info("Database seeded successfully with sample data!")
        
    except Exception as e:
        session.rollback()
        logger.error(f"Error seeding database: {e}", exc_info=True)
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()
