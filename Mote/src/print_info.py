from serial_connection import RN2483Connection


def get_info(mote: RN2483Connection, command: str) -> str:
    """Exécute une commande et retourne la réponse."""
    response = mote.send_command(command)
    return response if response else "N/A"


def main() -> None:
    mote = RN2483Connection("/dev/ttyACM0")

    try:
        print("=" * 60)
        print("RN2483 INFORMATION")
        print("=" * 60)

        print("\n[Système]")
        firmware = get_info(mote, "sys get ver")
        hweui = get_info(mote, "sys get hweui")
        vdd = get_info(mote, "sys get vdd")

        print(f"Firmware      : {firmware}")
        print(f"Hardware EUI  : {hweui}")

        if vdd.isdigit():
            print(f"Alimentation  : {int(vdd) / 1000:.3f} V")
        else:
            print(f"Alimentation  : {vdd}")

        print("\n[Radio]")
        print(f"Mode          : {get_info(mote, 'radio get mod')}")
        print(f"Fréquence     : {int(get_info(mote, 'radio get freq')) / 1_000_000:.3f} MHz")
        print(f"SF            : {get_info(mote, 'radio get sf').upper()}")
        print(f"Bandwidth     : {get_info(mote, 'radio get bw')} kHz")
        print(f"Coding Rate   : {get_info(mote, 'radio get cr')}")
        print(f"Power Index   : {get_info(mote, 'radio get pwr')}")
        print(f"CRC           : {get_info(mote, 'radio get crc')}")
        print(f"Watchdog      : {get_info(mote, 'radio get wdt')} ms")
        print(f"Sync Word     : 0x{int(get_info(mote, 'radio get sync')):02X}")
        print(f"IQ Inversion  : {get_info(mote, 'radio get iqi')}")

        print("\n[LoRaWAN]")
        print(f"Status        : {get_info(mote, 'mac get status')}")
        print(f"DevEUI        : {get_info(mote, 'mac get deveui')}")
        print(f"AppEUI        : {get_info(mote, 'mac get appeui')}")
        print(f"DevAddr       : {get_info(mote, 'mac get devaddr')}")
        print(f"ADR           : {get_info(mote, 'mac get adr')}")
        print(f"Data Rate     : DR{get_info(mote, 'mac get dr')}")
        print(f"RX Delay      : {get_info(mote, 'mac get rxdelay1')} ms")
        print(f"Auto Reply    : {get_info(mote, 'mac get ar')}")
        print(f"Retries       : {get_info(mote, 'mac get retx')}")
        print(f"Margin        : {get_info(mote, 'mac get mrgn')}")

        print("\n" + "=" * 60)

    finally:
        mote.close()


if __name__ == "__main__":
    main()
