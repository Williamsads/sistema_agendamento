import sqlite3
import os

def migrate():
    db_path = os.path.join("instance", "reservas.db")
    
    if not os.path.exists(db_path):
        # Fallback to current directory
        if os.path.exists("reservas.db"):
            db_path = "reservas.db"
        else:
            print(f"Banco de dados não encontrado em {db_path} ou reservas.db")
            return
            
    print(f"Migrando banco de dados: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sala'")
        if not cursor.fetchone():
            print("Tabela 'sala' não encontrada.")
            return

        # Check if column exists
        cursor.execute("PRAGMA table_info(sala)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if "ordem" not in columns:
            cursor.execute("ALTER TABLE sala ADD COLUMN ordem INTEGER DEFAULT 0")
            conn.commit()
            print("Coluna 'ordem' adicionada com sucesso.")
        else:
            print("Coluna 'ordem' já existe.")
        
        conn.close()
    except Exception as e:
        print(f"Erro ao migrar: {e}")

if __name__ == "__main__":
    migrate()
