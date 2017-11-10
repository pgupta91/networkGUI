from packetData import packetDataClass
from packetStructure import packetStructureClass
from flask import Flask, render_template, request
from blinkyscript import myComm
app = Flask(__name__)


@app.route('/')
def homeScreen():
    return render_template("home.html", selected = 'Home')
@app.route('/register')
def mainScreen():
    dataList = []
    with open("E:/test1.txt", "rb") as fp:
        for line in fp:
            dataList.append(line)
    packetObject = packetDataClass()
    packetObject.setData(dataList)

    return render_template("mainScreen.html",
                           selected='register',
                           command = packetObject.command,
                           deviceType = packetObject.deviceType,
                           errorCodes = packetObject.errorCodes,
                           gpioTable = packetObject.gpioTable,
                           DAC1 = packetObject.DAC1,
                           radioControl = packetObject.radioControl,
                           localTime = packetObject.localTime,
                           LED1 = packetObject.LED1,
                           LED2 = packetObject.LED2,
                           LED3 = packetObject.LED3,
                           LED4 = packetObject.LED4,
                           buzzer = packetObject.buzzer,
                           itemCount = packetObject.itemCount)

@app.route('/editNode.html', methods = ['POST'])
def editNodes():
    packetStructObject = packetStructureClass()
    return render_template('editNode.html',
                           commandDict = packetStructObject.commandDict,
                           deviceTypeDict = packetStructObject.deviceTypeDict,
                           errorCodesDict = packetStructObject.errorCodesDict,
                           gpioTableDict = packetStructObject.gpioTableDict,
                           DAC1Dict = packetStructObject.DAC1Dict,
                           radioControlDict = packetStructObject.radioControlDict,
                           localTimeDict = packetStructObject.localTimeDict,
                           ledDict = packetStructObject.ledDict,
                           buzzerDict = packetStructObject.buzzerDict)


@app.route('/editNode', methods = ['POST'])
def editedNodes():
    if request.method == 'POST':
        packetStructObject = packetStructureClass()
        payloadString = str(packetStructObject.commandDict[request.form['command']])+ ','
        payloadString += str(packetStructObject.deviceTypeDict[request.form['deviceType']]) + ','
        payloadString += str(packetStructObject.errorCodesDict[request.form['errorCode']]) + ','
        payloadString += str(packetStructObject.gpioTableDict[request.form['gpioTable']]) + ','
        payloadString += str(packetStructObject.DAC1Dict[request.form['dac1']]) + ','
        payloadString += str(packetStructObject.radioControlDict[request.form['radioControl']]) + ','
        payloadString += str(packetStructObject.localTimeDict[request.form['localTime']]) + ','
        payloadString += str(packetStructObject.ledDict[request.form['LED1']]) + ','
        payloadString += str(packetStructObject.ledDict[request.form['LED2']]) + ','
        payloadString += str(packetStructObject.ledDict[request.form['LED3']]) + ','
        payloadString += str(packetStructObject.ledDict[request.form['LED4']]) + ','
        payloadString += str(packetStructObject.buzzerDict[request.form['buzzer']])
        with open("E:/test1.txt", "wb") as fo:
            fo.write(payloadString)
        return render_template('mainScreen.html')

@app.route('/sendAction.html',methods=['POST'])
def sendData():
    inputValue = request.form['sendData']
    with open("E:/test.txt", "wb") as fo:
        if inputValue == "1":
            fo.write(b'\x01')
        elif inputValue == "0":
            fo.write(b'\x01')
    myComm(inputValue)
    return render_template('sendAction.html',sendDataValue = inputValue)

@app.route('/receiveAction.html',methods=['POST'])
def getData():
    with open("E:/test.txt", "rb") as fo:
        getValue = fo.read()
    return render_template('receiveAction.html',getDataValue = getValue)

if __name__ == '__main__':
    #setupSerial()
    app.run(debug=True)

