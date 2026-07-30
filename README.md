# Lora-lab

## WSL 2 Mote connection

To work on WSL and connect to the mote you need to do

```bash
usbipd list
```

and, with the correct busid

```bash
usbipd attach --wsl --busid 6-2
```
