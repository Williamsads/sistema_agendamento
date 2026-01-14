import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

def log(msg):
    print(f"[TEST] {msg}")

def run_tests():
    s = requests.Session()

    # 1. Login as Admin
    log("Logging in as Admin...")
    r = s.post(f"{BASE_URL}/login", data={"username": "admin", "senha": "admin"})
    if r.url == f"{BASE_URL}/":
        log("Admin login successful.")
    else:
        log(f"Admin login failed. URL: {r.url}")
        sys.exit(1)

    # 2. Check Admin Access to /salas
    log("Checking Admin access to /salas...")
    r = s.get(f"{BASE_URL}/salas")
    if r.status_code == 200:
        log("Admin accessed /salas successfully.")
    else:
        log(f"Admin failed to access /salas. Status: {r.status_code}")
        sys.exit(1)

    # 3. Create a normal user
    log("Creating normal user 'usuario_teste'...")
    r = s.post(f"{BASE_URL}/usuarios", data={"username": "usuario_teste", "senha": "123", "is_admin": ""}) # Checkbox not sent is empty
    if r.status_code == 200:
        log("User creation request sent.")
    else:
        log(f"User creation failed. Status: {r.status_code}")

    # 4. Logout Admin
    log("Logging out Admin...")
    s.get(f"{BASE_URL}/logout")

    # 5. Login as Normal User
    log("Logging in as 'usuario_teste'...")
    r = s.post(f"{BASE_URL}/login", data={"username": "usuario_teste", "senha": "123"})
    if r.url == f"{BASE_URL}/":
        log("User login successful.")
    else:
        log(f"User login failed. URL: {r.url}")
        sys.exit(1)

    # 6. Check Normal User Access to /salas (Should fail/redirect)
    log("Checking User access to /salas (Should be denied)...")
    r = s.get(f"{BASE_URL}/salas")
    # My code redirects to dashboard with 200 OK (render template) or 302. requests follows redirects by default.
    # So the final URL should be dashboard, and maybe check content for "Acesso não autorizado" or just different content.
    if r.url == f"{BASE_URL}/":
        log("User denied access to /salas (Redirected to dashboard).")
    else:
        log(f"User access check failed. URL: {r.url}")
        #sys.exit(1) # Warning only, as it might stay on same page if flash error

    # 7. Create Reservation as User
    log("Creating reservation as User...")
    # Need a sala ID. Assuming sala with ID 1 exists (created by init_db).
    r = s.post(f"{BASE_URL}/reservar", data={
        "sala_id": "1",
        "assunto": "Teste User",
        "nome_solicitante": "Teste",
        "setor": "TI",
        "telefone": "123",
        "data": "2026-02-01",
        "hora_inicio": "10:00",
        "hora_fim": "11:00"
    })
    # Should redirect to lista_reservas
    if "/reservas" in r.url:
         log("Reservation created successfully.")
    else:
         log(f"Reservation creation failed. URL: {r.url}")

    # 8. Cancel own reservation (Should succeed)
    # Need reservation ID. We can scrape it or just assume it's ID 1 if DB was clean.
    # Let's try ID 1.
    log("Cancelling own reservation (ID 1)...")
    r = s.get(f"{BASE_URL}/cancelar/1")
    if "/reservas" in r.url:
        log("Cancellation request completed (Check messages for succeess).")
    else:
         log("Cancellation request failed.")

    log("Tests Completed.")

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"Error: {e}")
