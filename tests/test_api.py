"""Tests for Weather API client."""

import pytest
from unittest.mock import Mock, patch
from src.api.api_client import WeatherAPIClient


class TestWeatherAPIClient:
    """Test cases for WeatherAPIClient."""
    
    @pytest.fixture
    def client(self):
        """Create API client instance."""
        return WeatherAPIClient(api_key="test_key")
    
    @patch('src.api.api_client.requests.get')
    def test_get_current_weather_success(self, mock_get, client):
        """Test successful weather fetch."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'name': 'London',
            'main': {'temp': 18, 'humidity': 65},
            'weather': [{'description': 'Cloudy', 'icon': '02d'}]
        }
        mock_get.return_value = mock_response
        
        result = client.get_current_weather('London')
        assert result is not None
        assert result['name'] == 'London'
    
    @patch('src.api.api_client.requests.get')
    def test_get_current_weather_error(self, mock_get, client):
        """Test weather fetch error handling."""
        mock_get.side_effect = Exception("API Error")
        
        result = client.get_current_weather('London')
        assert result is None
