"""Weather API client."""

import os
import logging
import aiohttp
import asyncio
from typing import Dict, Optional, List
from datetime import datetime
import requests

logger = logging.getLogger(__name__)


class WeatherAPIClient:
    """Client for OpenWeatherMap API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize API client."""
        self.api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
        self.base_url = os.getenv('OPENWEATHER_BASE_URL', 'https://api.openweathermap.org/data/2.5')
        
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not configured")
        
        self.timeout = 10
    
    def get_current_weather(self, city: str, units: str = 'metric') -> Optional[Dict]:
        """Get current weather for a city."""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'units': units,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"Weather fetched for {city}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather for {city}: {e}")
            return None
    
    def get_forecast(self, city: str, units: str = 'metric') -> Optional[Dict]:
        """Get 5-day weather forecast."""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': city,
                'units': units,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"Forecast fetched for {city}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching forecast for {city}: {e}")
            return None
    
    def get_air_quality(self, lat: float, lon: float) -> Optional[Dict]:
        """Get air quality data."""
        try:
            url = f"{self.base_url}/air_pollution"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"Air quality fetched for coordinates ({lat}, {lon})")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching air quality: {e}")
            return None
    
    def get_geocoding(self, city: str, limit: int = 1) -> Optional[List[Dict]]:
        """Get coordinates from city name."""
        try:
            url = "https://api.openweathermap.org/geo/1.0/direct"
            params = {
                'q': city,
                'limit': limit,
                'appid': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"Geocoding result for {city}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error geocoding {city}: {e}")
            return None


class AsyncWeatherAPIClient:
    """Async client for OpenWeatherMap API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize async API client."""
        self.api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
        self.base_url = os.getenv('OPENWEATHER_BASE_URL', 'https://api.openweathermap.org/data/2.5')
        self.timeout = aiohttp.ClientTimeout(total=10)
    
    async def get_current_weather(self, city: str, units: str = 'metric') -> Optional[Dict]:
        """Async get current weather."""
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                url = f"{self.base_url}/weather"
                params = {
                    'q': city,
                    'units': units,
                    'appid': self.api_key
                }
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        logger.info(f"Weather fetched async for {city}")
                        return await response.json()
                    else:
                        logger.error(f"API error: {response.status}")
                        return None
                        
        except asyncio.TimeoutError:
            logger.error("Request timeout")
            return None
        except Exception as e:
            logger.error(f"Error fetching weather: {e}")
            return None
