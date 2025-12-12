
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import base64
import time
from contextlib import suppress

try:
    import websocket  # pip install websocket-client
except ImportError as e:
    raise SystemExit("Zainstaluj proszę pakiet: pip install websocket-client") from e


def open_ws(ip, port=80, path="/websocket", user=None, password=None, timeout=3):
    url = f"ws://{ip}:{port}{path}"
    headers = []
    if user and password:
        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        headers.append(f"Authorization: Basic {token}")

    ws = websocket.create_connection(url, timeout=timeout, header=headers)
    return ws  # zwracamy obiekt połączenia; trzymamy je otwarte


def main():
    ap = argparse.ArgumentParser(description="Sprawdź ile dostępnych połączeń WebSocket ma jeszcze ifm AL1402 (IoT Core).")
    ap.add_argument("--ip",default="192.168.5.131",  help="Adres IP AL1402 (np. 192.168.0.55)")
    ap.add_argument("--port", type=int, default=80, help="Port HTTP (domyślnie 80)")
    ap.add_argument("--path", default="/getidentity", help="Ścieżka WebSocket (domyślnie /websocket)")
    ap.add_argument("--max", type=int, default=8, help="Górny limit prób (dla IoT Core typowo 8)")
    ap.add_argument("--user", help="Użytkownik (Basic Auth w IoT Core, jeśli włączony)")
    ap.add_argument("--password", help="Hasło (Basic Auth)")
    ap.add_argument("--hold", type=float, default=2.0, help="Ile sekund utrzymać połączenia zanim zamkniemy (domyślnie 2s)")
    args = ap.parse_args()

    sockets = []
    success = 0
    for i in range(args.max):
        try:
            ws = open_ws(args.ip, args.port, args.path, args.user, args.password)
            sockets.append(ws)
            success += 1
            # Nie wysyłamy nic — wystarczy utrzymać handshake 101 i otwarty kanał
        except Exception as ex:
            print(f"Połączenie nr {i+1} nieudane: {ex}")
            break

    print(f"\nDostępnych połączeń WebSocket (w momencie testu): {success}")
    if success == args.max:
        print("Uwaga: osiągnięto limit prób. Możliwe, że dostępnych jest więcej (zwiększ --max),")
        print("albo osiągnąłeś realny limit urządzenia/firmware.")

    # Trzymamy chwilę, by potwierdzić stabilność, potem zamykamy
    time.sleep(max(0, args.hold))
    for ws in sockets:
        with suppress(Exception):
            ws.close()


if __name__ == "__main__":
    main()