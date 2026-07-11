"""Tests for Weather Service."""

import pytest
from unittest.mock import Mock, patch
from src.api.weather_service import WeatherService


class TestWeatherService:
    """Test cases for WeatherService."""
    
    @pytest.fixture
    def service(self):
        """Create weather service instance."""
        return WeatherService(api_key="test_key")
    
    def test_parse_weather(self, service):
        """Test weather data parsing."""
        raw_data = {
            'name': 'London',
            'sys': {'country': 'GB'},
            'main': {'temp': 18, 'feels_like': 16, 'humidity': 65},
            'weather': [{'description': 'Cloudy', 'icon': '02d'}],
            'wind': {'speed': 5, 'deg': 230}
        }
        
        result = service._parse_weather(raw_data)
        assert result['city'] == 'London'
        assert result['temp'] == 18
        assert result['humidity'] == 65
    
    def test_get_weather_icon(self, service):
        """Test weather icon conversion."""
        assert service.get_weather_icon('01d') == '☀️'
        assert service.get_weather_icon('10d') == '🌦️'
        assert service.get_weather_icon('11d') == '⛈️'
    
    def test_get_alert_level(self, service):
        """Test alert level calculation."""
        assert service.get_alert_level(-15, 60, 10) == 'critical'
        assert service.get_alert_level(5, 60, 10) == 'normal'
        assert service.get_alert_level(18, 95, 10) == 'info'
