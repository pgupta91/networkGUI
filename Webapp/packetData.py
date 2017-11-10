class packetDataClass:
    command = []
    deviceType = []
    errorCodes = []
    gpioTable = []
    DAC1 = []
    radioControl = []
    localTime = []
    LED1 = []
    LED2 = []
    LED3 = []
    LED4 = []
    buzzer = []
    itemCount = 0

    def setData(self, dataList):
        self.itemCount = len(dataList)
        for item in dataList:
            data = str(item)
            cellData = data.split(",")
            self.command.append(cellData[0])
            self.deviceType.append(cellData[1])
            self.errorCodes.append(cellData[2])
            self.gpioTable.append(cellData[3])
            self.DAC1.append(cellData[4])
            self.radioControl.append(cellData[5])
            self.localTime.append(cellData[6])
            self.LED1.append(cellData[7])
            self.LED2.append(cellData[8])
            self.LED3.append(cellData[9])
            self.LED4.append(cellData[10])
            self.buzzer.append(cellData[11])




