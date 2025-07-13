import logging
import os
from datetime import datetime

# Ensure the logs directory exists
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Create a log file with today's date
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),      # Log to file
        logging.StreamHandler()             # Also log to console
    ]
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
