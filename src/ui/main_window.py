"""Main application window."""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QPushButton, QLineEdit, QComboBox
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
import logging

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌤️ Weather Dashboard")
        self.setGeometry(100, 100, 1200, 800)
        self.init_ui()
        self.setup_auto_refresh()
    
    def init_ui(self):
        """Initialize user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Title
        title = QLabel("🌤️ Real-Time Weather Dashboard")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Search section
        search_layout = QHBoxLayout()
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Enter city name...")
        search_input.setMaximumWidth(300)
        search_layout.addWidget(search_input)
        
        search_btn = QPushButton("🔍 Search")
        search_btn.setMaximumWidth(100)
        search_layout.addWidget(search_btn)
        
        layout.addLayout(search_layout)
        
        # Tabs
        tabs = QTabWidget()
        
        # Current Weather Tab
        current_tab = QWidget()
        current_layout = QVBoxLayout(current_tab)
        current_layout.addWidget(QLabel("📍 Current Weather"))
        current_layout.addWidget(QLabel("Loading..."))
        tabs.addTab(current_tab, "📊 Current")
        
        # Forecast Tab
        forecast_tab = QWidget()
        forecast_layout = QVBoxLayout(forecast_tab)
        forecast_layout.addWidget(QLabel("📈 5-Day Forecast"))
        forecast_layout.addWidget(QLabel("Loading..."))
        tabs.addTab(forecast_tab, "📅 Forecast")
        
        # Alerts Tab
        alerts_tab = QWidget()
        alerts_layout = QVBoxLayout(alerts_tab)
        alerts_layout.addWidget(QLabel("⚠️ Weather Alerts"))
        alerts_layout.addWidget(QLabel("No active alerts"))
        tabs.addTab(alerts_tab, "🚨 Alerts")
        
        # Analytics Tab
        analytics_tab = QWidget()
        analytics_layout = QVBoxLayout(analytics_tab)
        analytics_layout.addWidget(QLabel("📊 Analytics"))
        analytics_layout.addWidget(QLabel("Historical data will appear here"))
        tabs.addTab(analytics_tab, "📉 Analytics")
        
        layout.addWidget(tabs)
        
        # Status bar
        self.statusBar().showMessage("Ready")
    
    def setup_auto_refresh(self):
        """Setup auto-refresh timer."""
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_data)
        self.refresh_timer.start(300000)  # 5 minutes
    
    def refresh_data(self):
        """Refresh weather data."""
        logger.info("Auto-refreshing weather data")
        self.statusBar().showMessage("Refreshing...")
