
class AIExtractor:
    """Izvlaci strukturirane podatke s racuna koristeci Claude Vision."""

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        # TODO: Inicijaliziraj  klijent
        # TODO: Spremi odabir modela
        pass

    def extract_from_image(self, image_bytes: bytes, mime_type: str) -> dict:
        """Prepoznaj podatke s racuna iz slike koristeci Claude Vision API.

        Args:
            image_bytes: Sirovi bajtovi slike
            mime_type: MIME tip slike (image/png, image/jpeg, itd.)

        Returns:
            Prepoznati podaci racuna kao dict
        """
        # TODO: Napravi prompt za strukturiranu ekstrakciju podataka s racuna
        # TODO: Posalji sliku 
        # TODO: Parsiraj odgovor u strukturirani format 
        # TODO: Validiraj prepoznate podatke prema InvoiceData modelu
        # TODO: Obradi greske / nisku pouzdanost prepoznavanja
        pass

    def extract_from_pdf(self, pdf_bytes: bytes) -> dict:
        """Prepoznaj podatke s racuna iz PDF dokumenta.

        Args:
            pdf_bytes: Sirovi bajtovi PDF-a

        Returns:
            Prepoznati podaci racuna kao dict
        """
        # TODO: Pretvori PDF stranice u slike 
        # TODO: Posalji svaku stranicu kroz extract_from_image
        # TODO: Spoji rezultate s vise stranica
        pass

    def _build_extraction_prompt(self) -> str:
        """Napravi sistemski prompt za prepoznavanje racuna."""
        # TODO: Definiraj ocekivanu JSON shemu za izlaz
        # TODO: Ukljuci upute za ekstrakciju 
        pass
