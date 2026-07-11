"""Database models for weather data."""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class WeatherData(Base):
    """Store historical weather data."""
    __tablename__ = "weather_data"
    
    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    country = Column(String(50))
    temperature = Column(Float)
    feels_like = Column(Float)
    humidity = Column(Integer)
    pressure = Column(Integer)
    wind_speed = Column(Float)
    wind_direction = Column(Integer)
    description = Column(String(255))
    icon = Column(String(10))
    cloud_cover = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)


class ForecastData(Base):
    """Store weather forecast data."""
    __tablename__ = "forecast_data"
    
    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    forecast_date = Column(DateTime, nullable=False)
    temperature = Column(Float)
    temp_max = Column(Float)
    temp_min = Column(Float)
    humidity = Column(Integer)
    description = Column(String(255))
    icon = Column(String(10))
    wind_speed = Column(Float)
    rain_probability = Column(Float)
    clouds = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    """Weather alerts and warnings."""
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    alert_type = Column(String(50))  # 'severe', 'warning', 'info'
    title = Column(String(255), nullable=False)
    description = Column(Text)
    severity = Column(String(20))
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)


class Location(Base):
    """Saved locations."""
    __tablename__ = "locations"
    
    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    country = Column(String(50))
    latitude = Column(Float)
    longitude = Column(Float)
    is_favorite = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
