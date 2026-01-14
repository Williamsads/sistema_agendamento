from datetime import datetime
import pytz

def get_now_br():
    """Retorna o datetime atual no fuso horário de Brasília/Recife (com info de fuso)."""
    return datetime.now(pytz.timezone('America/Recife'))

def get_now_br_naive():
    """Retorna o datetime atual no fuso horário de Brasília/Recife (apenas wall-clock)."""
    return get_now_br().replace(tzinfo=None)
