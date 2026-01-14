from app import create_app, db
from app.models import Sala, Reserva
from sqlalchemy import text
import os

app = create_app()

with app.app_context():
    # Detecta se é PostgreSQL ou SQLite pela URL do banco
    db_url = app.config['SQLALCHEMY_DATABASE_URI']
    is_postgres = 'postgresql' in db_url
    
    print(f"Iniciando migração para: {db_url}")
    
    # Cria as tabelas se não existirem
    db.create_all()
    print("Tabelas verificadas/criadas.")

    if is_postgres:
        print("Ambiente PostgreSQL detectado.")
        # Limpa dados existentes para evitar duplicidade (opcional, cuidado em produção real)
        # db.session.execute(text('TRUNCATE TABLE reserva, sala, usuario RESTART IDENTITY CASCADE;'))
    else:
        print("Ambiente SQLite detectado.")

    # Migração de Salas (exemplo)
    # salas_locais = ... (lógica de cópia se necessário)
    
    print("Migração concluída com sucesso!")
