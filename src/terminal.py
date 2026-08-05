from serial_connection import RN2483Connection


PROMPT = "rn2483> "


def print_help() -> None:
    print(
        """
Available commands:
  help               Show this help
  clear              Clear the screen
  exit, quit         Exit the shell

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


def main() -> None:
    mote = RN2483Connection("/dev/ttyACM0")

    print("RN2483 Interactive Shell")
    print("Type 'help' for available commands.\n")

    try:
        while True:
            command = input(PROMPT).strip()

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

            response = mote.send_command(command)

            if response:
                print(response)
            else:
                print("(no response)")

    except KeyboardInterrupt:
        print("\nInterrupted.")

    finally:
        mote.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()