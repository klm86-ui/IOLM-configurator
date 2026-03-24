import requests
import time

start_time=0.0
elapsed_time=0.0

post_start_time=0.0
post_time=0.0
# ------------------------------------------------------
# KONFIGURACJA
# ------------------------------------------------------

API_HOST = "192.168.5.111"          # ← IP Twojego Balluffa
API_PORT = 8080                    # Port API Balluff (typowe dla XG5)
BASE_URL = f"https://{API_HOST}/api/balluff/v1"
packets_send = 0
packets_ok = 0
test_start_time=0.0
test_elapsed_time=0.0
TEST_INTERVAL=300.0
HTTP_POST_INTERVAL=1# Twój token Bearer
BEARER_TOKEN = "e71rvd8meofsso3"

# Nagłówki HTTP
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Accept": "application/json"
}

# Jeśli używasz self‑signed certificate → wyłącz weryfikację
VERIFY_SSL = False


# ------------------------------------------------------
# FUNKCJE POMOCNICZE
# ------------------------------------------------------

def api_get(endpoint):
    """Wysyła żądanie GET do Balluff REST API."""
    url = f"{BASE_URL}{endpoint}"
    global packets_ok, packets_send
    packets_send=packets_send+1
    try:
        print(url)
        response = requests.get(url, headers=HEADERS, verify=VERIFY_SSL,timeout=5
                                )
        response.raise_for_status()
        if response.status_code==200:
            packets_ok=packets_ok+1
        print(f"\n[OK] GET {endpoint}")
        return response.json()
    except Exception as e:
        print(f"\n[ERROR] GET {endpoint}: {e}")
        return None


# ------------------------------------------------------
# PRZYKŁADOWE ZAPYTANIA
# ------------------------------------------------------

def main():
    session = requests.Session()

    summary_time = 0
    print("=== Połączenie z Balluff BN00KH REST API ===")
    start_time = time.time()
    ident = api_get("/identification")
    elapsed_time = time.time() - start_time
    summary_time = elapsed_time + summary_time
    print("Response time:", elapsed_time, " IDENTYFIKACJA:", ident)
    start_time = time.time()
    net_cfg = api_get("/diagnostics")
    elapsed_time = time.time() - start_time
    summary_time = elapsed_time + summary_time
    print("Response time:", elapsed_time, "KONFIGURACJA SIECI:", net_cfg)
    start_time = time.time()
    net_status = api_get("/diagnostics/health")
    elapsed_time = time.time() - start_time
    summary_time = elapsed_time + summary_time
    print("Response time:", elapsed_time, "STATUS SIECI:", net_status)
    start_time = time.time()
    caps = api_get("/diagnostics/network")
    elapsed_time = time.time() - start_time
    summary_time = elapsed_time + summary_time
    print("Response time:", elapsed_time, "Summary time:", summary_time, "NETWORK:", caps)
    global test_start_time, test_elapsed_time,post_time,post_start_time
    test_start_time = time.time()
    print("TEST", test_elapsed_time, "___", TEST_INTERVAL)


    while test_elapsed_time < TEST_INTERVAL:
        post_time = time.time() - post_start_time
        test_elapsed_time = time.time() - test_start_time

        if post_time > HTTP_POST_INTERVAL:
            print("POST_timer:",post_time)
            post_start_time = time.time()
            post()
    print("\n=== KONIEC ===", "PAKIETY OGOLNIE:", packets_send, "Pakiety ok:", packets_ok, "Pakiety oblicozne:",
          8 * TEST_INTERVAL / HTTP_POST_INTERVAL,"Missing packets:", 8*TEST_INTERVAL/HTTP_POST_INTERVAL-packets_ok)

    session.close()
def post():
    elapsed_time = [0.0] * 10
    summary_time = 0
    start_time = time.time()
    p1 = api_get("/ports/1/processdata")
    elapsed_time[1] = time.time() - start_time
    summary_time = elapsed_time[1] + summary_time
    print("Response time:", elapsed_time[1], " PORT1:", p1)

    start_time = time.time()
    p2 = api_get("/ports/2/processdata")
    elapsed_time[2] = time.time() - start_time
    summary_time = elapsed_time[2] + summary_time
    print("Response time:", elapsed_time[2], "PORT2:", p2)

    start_time = time.time()
    p3 = api_get("/ports/3/processdata")
    elapsed_time[3] = time.time() - start_time
    summary_time = elapsed_time[3] + summary_time
    print("Response time:", elapsed_time[3], "PORT3:", p3)

    start_time = time.time()
    p4 = api_get("/ports/4/processdata")
    elapsed_time[4] = time.time() - start_time
    summary_time = elapsed_time[4] + summary_time
    print("Response time:", elapsed_time[4], "PORT4:", p4)

    start_time = time.time()
    p5 = api_get("/ports/5/processdata")
    elapsed_time[5] = time.time() - start_time
    summary_time = elapsed_time[5] + summary_time
    print("Response time:", elapsed_time[5], "PORT5:", p5)

    start_time = time.time()
    p6 = api_get("/ports/6/processdata")
    elapsed_time[6] = time.time() - start_time
    summary_time = elapsed_time[6] + summary_time
    print("Response time:", elapsed_time[6], "PORT6:", p6)

    start_time = time.time()
    p7 = api_get("/ports/7/processdata")
    elapsed_time[7] = time.time() - start_time
    summary_time = elapsed_time[7] + summary_time
    print("Response time:", elapsed_time[7], "PORT7:", p7)

    start_time = time.time()
    p8 = api_get("/ports/8/processdata")
    elapsed_time[8] = time.time() - start_time
    summary_time = elapsed_time[8] + summary_time
    print("Response time:", elapsed_time[8], "PORT8:", p8)

    print("Summary time: ", summary_time, "Elapsed time list:", elapsed_time, "PAKIETY OGOLNIE:", packets_send,
          "Pakiety ok:", packets_ok)




if __name__ == "__main__":
    main()