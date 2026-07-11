"""Utility functions for weather conversion."""

from datetime import datetime
import math


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def mps_to_kmh(mps: float) -> float:
    """Convert meters per second to kilometers per hour."""
    return mps * 3.6


def mps_to_mph(mps: float) -> float:
    """Convert meters per second to miles per hour."""
    return mps * 2.237


def degrees_to_direction(degrees: int) -> str:
    """Convert wind direction degrees to cardinal direction."""
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    index = round(degrees / 22.5) % 16
    return directions[index]


def timestamp_to_datetime(timestamp: int) -> datetime:
    """Convert Unix timestamp to datetime."""
    return datetime.fromtimestamp(timestamp)


def format_temperature(temp: float, unit: str = 'C') -> str:
    """Format temperature with unit."""
    if unit == 'F':
        temp = celsius_to_fahrenheit(temp)
    return f"{temp:.1f}°{unit}"


def format_wind_speed(speed: float, unit: str = 'kmh') -> str:
    """Format wind speed with unit."""
    if unit == 'mph':
        speed = mps_to_mph(speed)
        return f"{speed:.1f} mph"
    else:
        speed = mps_to_kmh(speed)
        return f"{speed:.1f} km/h"


def calculate_aqi(pollutants: dict) -> int:
    """Calculate Air Quality Index from pollutants."""
    # Simplified AQI calculation
    pm25 = pollutants.get('pm2_5', 0)
    pm10 = pollutants.get('pm10', 0)
    
    aqi = max(pm25 / 12, pm10 / 50) * 100
    return min(int(aqi), 500)


def get_aqi_description(aqi: int) -> str:
    """Get AQI description."""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"
