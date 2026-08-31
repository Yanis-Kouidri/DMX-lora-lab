# Lora-lab

## Hardware

### Mote (sensor)

This project targets the **Microchip RN2483 LoRa Technology Mote**, an evaluation board for experimenting with **LoRa** and **LoRaWAN** networks.

**LoRa modem:** Microchip RN2483A (868 MHz, EU868)

### Gateway

- Model: MikroTik wAP LoRa8
- Version: MikroTik RouterOS 7.24

## WSL 2 Mote connection

To work on WSL and connect to the mote you need to run on Windows PowerShell:

```bash
usbipd list
```

and, with the correct busid

```bash
usbipd attach --wsl --busid 6-2
```

Or better

```bash
usbipd attach --hardware-id 04d8:000a --wsl
```
