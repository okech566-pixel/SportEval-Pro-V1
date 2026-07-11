"""Initialize database with all tables."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os
import logging

logger = logging.getLogger(__name__)

def init_database(database_url=None):
    """Initialize database and create all tables."""
    
    if database_url is None:
        db_path = os.path.join(os.getcwd(), 'sporteval.db')
        database_url = f'sqlite:///{db_path}'
    
    logger.info(f"Initializing database at: {database_url}")
    
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
    
    logger.info("Database initialized successfully!")
    
    return engine

def get_session_maker(database_url=None):
    """Get SQLAlchemy session maker."""
    if database_url is None:
        db_path = os.path.join(os.getcwd(), 'sporteval.db')
        database_url = f'sqlite:///{db_path}'
    
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(bind=engine)
    
    return SessionLocal

def get_session(database_url=None):
    """Get a database session."""
    SessionLocal = get_session_maker(database_url)
    return SessionLocal()
