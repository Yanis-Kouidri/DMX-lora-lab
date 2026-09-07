import random
import time

from serial_connection import RN2483Connection


def generate_payload() -> tuple[str, float, int, int]:
    """Génère un payload binaire compatible avec le codec ChirpStack."""

    temperature = round(random.uniform(18.0, 25.5), 1)
    humidity = random.randint(30, 80)
    battery = random.randint(60, 100)

    temperature_encoded = int(temperature * 10)

    payload = bytes(
        [
            temperature_encoded,
            humidity,
            battery,
        ]
    ).hex().upper()

    return payload, temperature, humidity, battery


def main() -> None:
    rn2483 = RN2483Connection("/dev/ttyACM0")

    try:
        while True:
            payload, temperature, humidity, battery = generate_payload()

            print("Mesures générées")
            print(f"  Température : {temperature:.1f} °C")
            print(f"  Humidité    : {humidity} %")
            print(f"  Batterie    : {battery} %")
            print(f"  Payload     : {payload}")

            print()

            print("> mac tx uncnf 1", payload)
            print(rn2483.send_command(f"mac tx uncnf 1 {payload}"))

            # Lecture de la réponse asynchrone (mac_tx_ok)
            #print(rn2483.send_command(""))

            print("-" * 50)

            time.sleep(30)

    finally:
        rn2483.close()


if __name__ == "__main__":
    main()