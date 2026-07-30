from serial import Serial


class RN2483Connection:
    """Gestion de la connexion série avec le RN2483."""

    def __init__(
        self,
        port: str,
        baudrate: int = 57600,
        timeout: float = 1.0,
    ) -> None:
        self._serial = Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout,
        )

    def send_command(self, command: str) -> str:
        """Envoie une commande AT et retourne la réponse."""

        self._serial.reset_input_buffer()

        self._serial.write(f"{command}\r\n".encode())

        response = self._serial.readline()

        return response.decode().strip()

    def close(self) -> None:
        """Ferme le port série."""

        self._serial.close()