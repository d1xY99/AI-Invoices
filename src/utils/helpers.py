"""
Pomocne funkcije - Formatiranje, validacija, konverzija.
"""


def format_currency(amount: float, currency: str = "EUR") -> str:
    """Formatiraj iznos s oznakom valute."""
    # TODO: Formatiraj iznos (2 decimale, separator za tisuce)
    pass


def validate_oib(oib: str) -> bool:
    """Provjeri valjanost OIB-a (11 znamenki + kontrolna)."""
    # TODO: Provjera duljine (11 znamenki)
    # TODO: Provjera formata (ISO 7064, MOD 11,10)
    pass


def validate_invoice_number(invoice_number: str) -> bool:
    """Provjeri format broja racuna."""
    # TODO: Provjera da nije prazan
    # TODO: Provjera formata (regex)
    pass
