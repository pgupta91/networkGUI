class packetStructureClass:
    commandDict = {
                   "New Config Strng": 0x01,
                   "Edit Config Strng": 0x02,
                   "Payload is Config String": 0x03,
                   "Payload is Data String from Address in the data string": 0x04,
                   "Clear local data string": 0x05,
                   "Reset local config String to default and remove from network": 0x06,
                   "Reset device": 0x07,
                   "Payload data is Table 1": 0x08,
                   "Payload data is Table 2": 0x09
                   }
    deviceTypeDict = {"Standard Node": 0x01}

    errorCodesDict = {"Battery ok": 0x00, "Battery low": 0x01}

    gpioTableDict = {"ON": 0x00, "OFF": 0x01}

    DAC1Dict = {"default": 0x00}

    radioControlDict = {"default": 0x00}

    localTimeDict = {"default": 0x00}

    ledDict = {"Off, set externally": 0x00,
           "Blink every 5 sec, set externally": 0x01,
           "Blink every 1 sec, set externally": 0x02,
           "Off, set by node": 0x00,
           "Blink every 5 sec, set by node": 0x11,
           "Blink every 1 sec, set by node": 0x12}

    buzzerDict = {"default": 0x00}






