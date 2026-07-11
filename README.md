# 🌤️ Weather Dashboard

A professional real-time weather monitoring application with API integration, data visualization, and weather alerts.

## ✨ Features

- 🌍 Real-time weather data from OpenWeatherMap API
- 📊 Interactive weather charts and graphs
- 🌡️ Temperature, humidity, pressure monitoring
- 💨 Wind speed and direction
- 🌧️ Precipitation forecasts
- 🔔 Weather alerts and warnings
- 📍 Multi-location tracking
- 🗺️ Weather maps integration
- 📱 Responsive dashboard
- 💾 Data persistence
- 📈 Historical data analysis
- 🎨 Beautiful UI with PyQt6

## 🛠️ Tech Stack

- **Backend**: FastAPI / Flask
- **Frontend**: PyQt6 / React
- **API**: OpenWeatherMap
- **Database**: SQLite / PostgreSQL
- **Visualization**: Plotly / Matplotlib
- **Async**: aiohttp / asyncio

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/okech566-pixel/Weather-Dashboard.git
cd Weather-Dashboard

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup configuration
cp .env.example .env
# Edit .env with your API keys

# Run application
python app.py
```

## 🔑 API Configuration

Get free API key from [OpenWeatherMap](https://openweathermap.org/api)

```env
OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_BASE_URL=https://api.openweathermap.org/data/2.5
```

## 📁 Project Structure

```
Weather-Dashboard/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── weather_service.py
│   │   └── api_client.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── widgets/
│   │   │   ├── weather_card.py
│   │   │   ├── forecast_panel.py
│   │   │   └── alerts_panel.py
│   │   └── styles.qss
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── operations.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── converters.py
│   │   └── validators.py
│   └── main.py
├── tests/
│   ├── test_api.py
│   ├── test_weather_service.py
│   └── test_database.py
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

## 🚀 Usage

### Basic Usage

```python
from src.api.weather_service import WeatherService

service = WeatherService(api_key="your_key")

# Get current weather
weather = service.get_current_weather("London")
print(f"Temperature: {weather['temp']}°C")
print(f"Description: {weather['description']}")

# Get forecast
forecast = service.get_forecast("London", days=5)
for day in forecast:
    print(f"{day['date']}: {day['temp_max']}°C - {day['description']}")
```

## 📊 Dashboard Features

### Current Weather Card
- Temperature display
- Weather condition with icon
- Feels like temperature
- Humidity percentage
- Wind speed and direction

### Forecast Panel
- 5-day or 7-day forecast
- Hour-by-hour breakdown
- Precipitation probability
- Wind gusts

### Alerts Panel
- Severe weather warnings
- Temperature extremes
- Air quality index
- UV index

### Analytics
- Historical temperature trends
- Humidity patterns
- Precipitation charts
- Wind rose diagram

## 🔄 Data Flow

```
OpenWeatherMap API
        ↓
   API Client
        ↓
 Weather Service (Processing)
        ↓
   Database (Caching)
        ↓
    UI Dashboard
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_weather_service.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

## 📝 Configuration

### Environment Variables

```env
# API Configuration
OPENWEATHER_API_KEY=your_api_key
OPENWEATHER_BASE_URL=https://api.openweathermap.org/data/2.5
REFRESH_INTERVAL=300  # seconds

# Database
DATABASE_URL=sqlite:///weather.db

# Application
DEBUG=False
THEME=dark  # light/dark
TEMP_UNIT=C  # C/F
```

## 🎨 UI Preview

```
┌─────────────────────────────────────┐
│  Weather Dashboard                  │
├─────────────────────────────────────┤
│                                     │
│  📍 London, UK                      │
│  🌤️  Partly Cloudy                  │
│  🌡️  18°C (Feels: 16°C)             │
│  💧 65% | 💨 12 km/h NW             │
│                                     │
├─────────────────────────────────────┤
│  5-Day Forecast                     │
├─────────────────────────────────────┤
│  Mon: 20°C ⛅ | Tue: 18°C 🌧️        │
│  Wed: 19°C ⛅ | Thu: 21°C ☀️        │
│  Fri: 22°C ☀️                       │
│                                     │
└─────────────────────────────────────┘
```

## 🔐 Security

- API keys stored in environment variables
- Input validation on all user inputs
- Rate limiting on API calls
- HTTPS only for API communications
- No sensitive data in logs

## 📚 API Reference

### Current Weather
```python
weather_service.get_current_weather(city: str) -> Dict
```

### Forecast
```python
weather_service.get_forecast(city: str, days: int = 5) -> List[Dict]
```

### Air Quality
```python
weather_service.get_air_quality(city: str) -> Dict
```

### Alerts
```python
weather_service.get_alerts(city: str) -> List[Dict]
```

## 🐛 Troubleshooting

### "API Key Invalid"
- Verify API key in .env file
- Check OpenWeatherMap account status
- Ensure free tier limits not exceeded

### "Connection Timeout"
- Check internet connection
- Verify API endpoint URL
- Check firewall settings

### "No Data Displayed"
- Clear browser cache
- Restart application
- Check database connection

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

MIT License - see LICENSE file

## 📞 Support

For issues and questions:
- Open GitHub Issue
- Email: support@weatherdash.com
- Documentation: https://docs.weatherdash.com

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Voice alerts
- [ ] Custom notifications
- [ ] Weather statistics
- [ ] Climate comparison
- [ ] Export data to CSV/PDF
- [ ] API for third-party integration
- [ ] Multi-language support

---

**Made with ❤️ by Omar Chabane**
