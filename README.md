# Lora-lab

## Hardware

This project targets the **Microchip RN2483 LoRa Technology Mote**, an evaluation board for experimenting with **LoRa** and **LoRaWAN** networks.

**LoRa modem:** Microchip RN2483A (868 MHz, EU868)

## WSL 2 Mote connection

To work on WSL and connect to the mote you need to do

```bash
usbipd list
```

and, with the correct busid

```bash
usbipd attach --wsl --busid 6-2
```
