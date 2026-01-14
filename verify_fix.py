import requests
import datetime

BASE_URL = "http://127.0.0.1:5000"

def run():
    s = requests.Session()
    # Login
    s.post(f"{BASE_URL}/login", data={"username": "admin", "senha": "admin"})
    
    # Book crossing midnight
    # 23:00 to 01:00
    r = s.post(f"{BASE_URL}/reservar", data={
        "sala_id": "1",
        "assunto": "Teste Madrugada",
        "nome_solicitante": "Tester",
        "setor": "QA",
        "telefone": "999",
        "data": datetime.date.today().strftime("%Y-%m-%d"),
        "hora_inicio": "23:00",
        "hora_fim": "01:00"
    })
    
    if "Reserva realizada com sucesso" in r.text or r.url.endswith("/reservas"):
        print("Success: Reservation accepted.")
    else:
        print("Failed: Reservation rejected (or other error).")
        # print(r.text)

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)
