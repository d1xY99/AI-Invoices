"""
PDF Generator servis - Generiranje PDF racuna iz strukturiranih podataka.
"""


class PDFGenerator:
    """Generiraj profesionalne PDF racune iz prepoznatih/uredenih podataka."""

    def __init__(self, template_dir: str = "assets/templates"):
        # TODO: Ucitaj Jinja2 predloske
        # TODO: Postavi WeasyPrint ili alternativni PDF renderer
        pass

    def generate(self, invoice_data: dict, template_name: str = "default") -> bytes:
        """Generiraj PDF racun iz strukturiranih podataka.

        Args:
            invoice_data: Podaci racuna prema InvoiceData modelu
            template_name: Naziv HTML/CSS predloska

        Returns:
            PDF datoteka kao bytes
        """
        # TODO: Ucitaj HTML predlozak
        # TODO: Renderaj predlozak s podacima racuna (Jinja2)
        # TODO: Pretvori HTML u PDF (WeasyPrint)
        # TODO: Vrati PDF bajtove
        pass
