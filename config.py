import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")
    ADMIN_CHAT_IDS: list = [int(id) for id in os.getenv("ADMIN_CHAT_IDS", "").split(",") if id]
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Path'ler
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    INPUT_DIR = DATA_DIR / "input"
    OUTPUT_DIR = DATA_DIR / "output"
    GROUPS_DIR = DATA_DIR / "groups"
    LOGS_DIR = DATA_DIR / "logs"
    
    def __post_init__(self):
        # Dizinleri oluştur
        for directory in [self.INPUT_DIR, self.OUTPUT_DIR, self.GROUPS_DIR, self.LOGS_DIR]:
            directory.mkdir(parents=True, exist_ok=True)

# Global config instance
config = Config()
