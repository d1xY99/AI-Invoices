"""
Konfiguracijske pomocne funkcije - Ucitavanje env varijabli i postavki.
"""

import os
from dotenv import load_dotenv


def load_config() -> dict:
    """Ucitaj konfiguraciju aplikacije iz okruzenja i zadanih vrijednosti."""
    load_dotenv()

    # TODO: Ucitaj API kljuc iz env ili Streamlit secrets
    # TODO: Ucitaj zadanu valutu, jezik, postavke modela
    # TODO: Validiraj da su obavezne postavke prisutne
    # TODO: Postavi putanju do Excel datoteke

    return {
        "api_key": os.getenv("ANTHROPIC_API_KEY", ""),
        "model": os.getenv("AI_MODEL", "claude-sonnet-4-20250514"),
        "default_currency": os.getenv("DEFAULT_CURRENCY", "EUR"),
        "excel_path": os.getenv("EXCEL_PATH", "data/racuni.xlsx"),
    }
