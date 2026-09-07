"""Shell interactif pour communiquer avec une Mote RN2483 (LoRa)."""

from __future__ import annotations

import argparse
import atexit
import readline
from pathlib import Path

from serial import SerialException

from serial_connection import RN2483Connection

PROMPT = "rn2483> "

HISTORY_FILE = Path.home() / ".rn2483_history"
HISTORY_MAX_LENGTH = 1000

BUILTIN_COMMANDS = ("help", "clear", "exit", "quit")

# Complétion basique : commandes intégrées + quelques commandes AT courantes,
# utile comme point de départ avec Tab.
KNOWN_COMMANDS = BUILTIN_COMMANDS + (
    "sys get ver",
    "sys get hweui",
    "sys reset",
    "radio get sf",
    "radio get freq",
    "radio get pwr",
    "radio set sf",
    "radio set freq",
    "radio tx",
    "radio rx",
    "mac pause",
    "mac resume",
)


def print_help() -> None:
    print(
        """
Available commands:
  help               Show this help
  clear              Clear the screen
  exit, quit         Exit the shell

Navigation:
  Up / Down arrows   Recall previous commands (persisted across sessions)
  Tab                Autocomplete known commands

Any other command is sent directly to the RN2483.

Examples:
  sys get ver
  sys get hweui
  radio get sf
  radio get freq
  mac pause
  radio tx 48656C6C6F
"""
    )


def clear_screen() -> None:
    print("\033[2J\033[H", end="")


def setup_readline() -> None:
    """Configure l'historique persistant et l'auto-complétion."""

    readline.set_history_length(HISTORY_MAX_LENGTH)

    if HISTORY_FILE.exists():
        readline.read_history_file(HISTORY_FILE)

    atexit.register(save_history)

    def completer(text: str, state: int) -> str | None:
        matches = [cmd for cmd in KNOWN_COMMANDS if cmd.startswith(text)]
        return matches[state] if state < len(matches) else None

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")


def save_history() -> None:
    try:
        readline.write_history_file(HISTORY_FILE)
    except OSError as exc:
        print(f"Warning: could not save command history: {exc}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Interactive shell for the RN2483 LoRa mote.")
    parser.add_argument(
        "-p",
        "--port",
        default="/dev/ttyACM0",
        help="Serial port the mote is connected to (default: %(default)s)",
    )
    parser.add_argument(
        "-b",
        "--baudrate",
        type=int,
        default=57600,
        help="Serial baudrate (default: %(default)s)",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1.0,
        help="Serial read timeout in seconds (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    setup_readline()

    try:
        mote = RN2483Connection(args.port, baudrate=args.baudrate, timeout=args.timeout)
    except SerialException as exc:
        print(f"Could not open serial port {args.port!r}: {exc}")
        return

    print("RN2483 Interactive Shell")
    print(f"Connected to {args.port} at {args.baudrate} baud.")
    print("Type 'help' for available commands.\n")

    try:
        while True:
            try:
                command = input(PROMPT).strip()
            except EOFError:
                print()
                break

            if not command:
                continue

            if command in {"exit", "quit"}:
                break

            if command == "help":
                print_help()
                continue

            if command == "clear":
                clear_screen()
                continue

            try:
                response = mote.send_command(command)
            except SerialException as exc:
                print(f"Serial communication error: {exc}")
                continue

            print(response if response else "(no response)")

    except KeyboardInterrupt:
        print("\nInterrupted.")

    finally:
        mote.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
