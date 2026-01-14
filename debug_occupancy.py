from app import app, db
from models import Reserva, Sala
from datetime import datetime

with app.app_context():
    print(f"Server Time (datetime.now()): {datetime.now()}")
    
    reservas = Reserva.query.all()
    print(f"\nTotal Reservations: {len(reservas)}")
    for r in reservas:
        print(f"ID: {r.id} | Sala: {r.sala_id} | Inicio: {r.inicio} | Fim: {r.fim}")
        
        # Test the query logic manually
        now = datetime.now()
        is_active = r.inicio <= now <= r.fim
        print(f"  -> Is Active (Python Logic)? {is_active}")

    print("\n--- Testing Database Query ---")
    salas = Sala.query.all()
    for sala in salas:
        agora = datetime.now()
        reserva_atual = Reserva.query.filter(
            Reserva.sala_id == sala.id,
            Reserva.inicio <= agora,
            Reserva.fim >= agora
        ).first()
        print(f"Sala {sala.nome}: Ocupada? {'SIM' if reserva_atual else 'NÃO'}")
