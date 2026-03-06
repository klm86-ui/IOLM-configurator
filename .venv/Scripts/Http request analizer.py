import requests
import time

# Konfiguracja początkowa
URL = "http://127.0.0.1:5000/api"   # podaj adres IP i endpoint
PAYLOAD = {
    "key1": "value1",
    "key2": "value2"
}

BlobSeq1={"Port1ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/iolinkdevice/iolreadacyclic","data": {"index":49,"subindex": 0}}}
BlobSeq2={"Port1ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/iolinkdevice/iolreadacyclic","data": {"index":49,"subindex": 0}}}
BlobSeq3={"Port1ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/iolinkdevice/iolreadacyclic","data": {"index":49,"subindex": 0}}}
HEADERS = {    "Content-Type": "application/json"
}

# Liczniki i dane
sent_requests = 0
received_responses = 0
response_times = []

def send_post_request():
    global sent_requests, received_responses, response_times
    sent_requests += 1
    start_time = time.time()
    try:
        response = requests.post(URL, json=PAYLOAD, headers=HEADERS)
        elapsed_time = time.time() - start_time
        response_times.append(elapsed_time)

        if response.status_code == 200:
            received_responses += 1
            print(f"[OK] Kod odpowiedzi: {response.status_code}, czas: {elapsed_time:.4f} s")
        else:
            print(f"[BŁĄD] Kod odpowiedzi: {response.status_code}, czas: {elapsed_time:.4f} s")

    except requests.exceptions.RequestException as e:
        elapsed_time = time.time() - start_time
        response_times.append(elapsed_time)
        print(f"[WYJĄTEK] {e}, czas: {elapsed_time:.4f} s")

    print(f"Zapytania wysłane: {sent_requests}, Odpowiedzi poprawne: {received_responses}")

def show_summary():
    print("\n--- PODSUMOWANIE ---")
    print(f"Łączna liczba zapytań: {sent_requests}")
    print(f"Liczba odpowiedzi 200: {received_responses}")
    if response_times:
        avg_time = sum(response_times) / len(response_times)
        print(f"Średni czas odpowiedzi: {avg_time:.4f} s")
        print(f"Minimalny czas odpowiedzi: {min(response_times):.4f} s")
        print(f"Maksymalny czas odpowiedzi: {max(response_times):.4f} s")
    else:
        print("Brak danych o czasie odpowiedzi.")

if __name__ == "__main__":
    for i in range(5):  # liczba prób
        send_post_request()
        time.sleep(1)   # odstęp między zapytaniami

    show_summary()