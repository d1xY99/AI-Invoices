"""
Excel Export servis - Izvoz prepoznatih racuna u Excel tablicu (.xlsx).
"""

from typing import Optional


class ExcelExporter:
    """Upravljanje izvozom racuna u Excel tablicu."""

    def __init__(self, file_path: str = "data/racuni.xlsx"):
        # TODO: Postavi putanju do Excel datoteke
        # TODO: Kreiraj direktorij ako ne postoji
        # TODO: Ucitaj postojecu datoteku ako postoji (openpyxl)
        pass

    def add_invoice(self, invoice_data: dict) -> bool:
        """Dodaj jedan racun kao novi red u Excel tablicu.

        Args:
            invoice_data: Podaci racuna (broj, datum, dobavljac, stavke, iznos, PDV...)

        Returns:
            True ako je uspjesno dodano
        """
        # TODO: Otvori ili kreiraj Excel workbook
        # TODO: Spremi datoteku
        pass

    def add_multiple_invoices(self, invoices: list[dict]) -> int:
        """Dodaj vise racuna odjednom u Excel tablicu.

        Args:
            invoices: Lista podataka racuna

        Returns:
            Broj uspjesno dodanih racuna
        """
        # TODO: Iteriraj kroz listu i pozovi add_invoice za svaki
        # TODO: Vrati broj uspjesno dodanih
        pass

    def get_as_bytes(self) -> bytes:
        """Vrati Excel datoteku kao bajtove za preuzimanje u Streamlitu.

        Returns:
            Excel datoteka kao bytes
        """
        # TODO: Ucitaj workbook
        # TODO: Spremi u BytesIO buffer
        # TODO: Vrati bajtove
        pass

    def read_existing(self) -> list[dict]:
        """Procitaj postojece racune iz Excel tablice.

        Returns:
            Lista racuna kao dict
        """
        # TODO: Ucitaj Excel datoteku s pandas (read_excel)
        # TODO: Pretvori DataFrame u listu dictova
        # TODO: Vrati praznu listu ako datoteka ne postoji
        pass
