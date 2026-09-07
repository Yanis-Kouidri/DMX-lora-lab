mac reset 868
mac set deveui 0004A30B0023F200
mac set appeui 0000000000000000
mac set appkey <APPKEY_CHIRPSTACK>
mac save

mac get deveui
mac get appeui

mac join otaa

mac tx uncnf 1 D93A64
