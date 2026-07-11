"""Main entry point for Weather Dashboard application."""

import sys
import logging
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main application entry point."""
    try:
        logger.info("Starting Weather Dashboard...")
        
        from PyQt6.QtWidgets import QApplication
        from src.ui.main_window import MainWindow
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        
        logger.info("Application started successfully")
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
