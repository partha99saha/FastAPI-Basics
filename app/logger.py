import logging
from logging.handlers import RotatingFileHandler

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler("app.log", maxBytes=10000, backupCount=1),
        logging.StreamHandler(),  # Output to console as well
    ],
)

# Create logger object
logger = logging.getLogger(__name__)
