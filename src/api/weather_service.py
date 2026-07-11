"""Weather API service."""

import logging
from typing import Dict, Optional, List
from datetime import datetime, timedelta
from .api_client import WeatherAPIClient

logger = logging.getLogger(__name__)


class WeatherService:
    """Service for weather operations."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize weather service."""
        self.client = WeatherAPIClient(api_key)
        self.cache = {}
        self.cache_duration = 300  # 5 minutes
    
    def get_current_weather(self, city: str) -> Optional[Dict]:
        """Get current weather with caching."""
        cache_key = f"weather_{city}"
        
        # Check cache
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if (datetime.now() - timestamp).seconds < self.cache_duration:
                logger.info(f"Returning cached weather for {city}")
                return cached_data
        
        # Fetch from API
        data = self.client.get_current_weather(city)
        
        if data:
            self.cache[cache_key] = (data, datetime.now())
            return self._parse_weather(data)
        
        return None
    
    def get_forecast(self, city: str, days: int = 5) -> Optional[List[Dict]]:
        """Get weather forecast."""
        data = self.client.get_forecast(city)
        
        if data:
            return self._parse_forecast(data, days)
        
        return None
    
    def _parse_weather(self, data: Dict) -> Dict:
        """Parse raw weather data."""
        return {
            'city': data.get('name'),
            'country': data.get('sys', {}).get('country'),
            'temp': data.get('main', {}).get('temp'),
            'feels_like': data.get('main', {}).get('feels_like'),
            'temp_min': data.get('main', {}).get('temp_min'),
            'temp_max': data.get('main', {}).get('temp_max'),
            'pressure': data.get('main', {}).get('pressure'),
            'humidity': data.get('main', {}).get('humidity'),
            'description': data.get('weather', [{}])[0].get('description'),
            'icon': data.get('weather', [{}])[0].get('icon'),
            'wind_speed': data.get('wind', {}).get('speed'),
            'wind_deg': data.get('wind', {}).get('deg'),
            'cloud_cover': data.get('clouds', {}).get('all'),
            'sunrise': data.get('sys', {}).get('sunrise'),
            'sunset': data.get('sys', {}).get('sunset'),
            'timestamp': datetime.now().isoformat()
        }
    
    def _parse_forecast(self, data: Dict, days: int) -> List[Dict]:
        """Parse forecast data."""
        forecasts = []
        
        for item in data.get('list', [])[:days * 8]:  # 8 items per day
            forecast = {
                'date': datetime.fromtimestamp(item.get('dt')).isoformat(),
                'temp': item.get('main', {}).get('temp'),
                'temp_max': item.get('main', {}).get('temp_max'),
                'temp_min': item.get('main', {}).get('temp_min'),
                'humidity': item.get('main', {}).get('humidity'),
                'description': item.get('weather', [{}])[0].get('description'),
                'icon': item.get('weather', [{}])[0].get('icon'),
                'wind_speed': item.get('wind', {}).get('speed'),
                'rain': item.get('rain', {}).get('3h', 0),
                'clouds': item.get('clouds', {}).get('all')
            }
            forecasts.append(forecast)
        
        return forecasts
    
    def get_weather_icon(self, icon_code: str) -> str:
        """Convert weather icon code to emoji."""
        icon_map = {
            '01d': '☀️',
            '01n': '🌙',
            '02d': '⛅',
            '02n': '🌤️',
            '03d': '☁️',
            '03n': '☁️',
            '04d': '☁️',
            '04n': '☁️',
            '09d': '🌧️',
            '09n': '🌧️',
            '10d': '🌦️',
            '10n': '🌧️',
            '11d': '⛈️',
            '11n': '⛈️',
            '13d': '❄️',
            '13n': '❄️',
            '50d': '🌫️',
            '50n': '🌫️',
        }
        return icon_map.get(icon_code, '🌡️')
    
    def get_alert_level(self, temp: float, humidity: float, wind_speed: float) -> str:
        """Determine alert level based on conditions."""
        if temp < -10 or temp > 40:
            return 'critical'
        if temp < 0 or temp > 35:
            return 'warning'
        if wind_speed > 20:
            return 'warning'
        if humidity > 90:
            return 'info'
        return 'normal'
