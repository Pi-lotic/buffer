from flask import Flask
from flask import render_template
from flask import request

import RPi.GPIO as GPIO

import datetime 
import time
import sys
import Databuffer, Stringbuffer
Time = Stringbuffer.Stringbuffer('/home/pi/Data/Time.csv', 5)
Temp = Databuffer.Databuffer('/home/pi/Data/Temp.csv', 5)
Humi = Databuffer.Databuffer('/home/pi/Data/Humi.csv', 5)

#OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
#Switch_K4 = 11

# Initialize IO
GPIO.setmode(GPIO.BOARD)
#GPIO.setup (OptoIn, GPIO.IN)
#GPIO.setup (Switch_K4, GPIO.OUT)
GPIO.setup (Switch_K2, GPIO.OUT)
GPIO.setup (Switch_K1, GPIO.OUT)

# Set all Ouputs OFF
GPIO.output(Switch_K1, GPIO.HIGH)
GPIO.output(Switch_K2, GPIO.HIGH)
#GPIO.output(Switch_K4, GPIO.HIGH)


app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])


def hello(TempHum=None):
    if request.method == 'GET':
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        te = float (datetime.datetime.fromtimestamp(ts).strftime('%M'))
        hu = float (datetime.datetime.fromtimestamp(ts).strftime('%S'))
        temperature = ( te/2 ) - te/10
        humidity = hu + hu/10
        text= st + ' {0:0.1f}*C {1:0.1f}%'.format(temperature, humidity)
        Time.Set(st)
        Temp.Set(temperature)
        Humi.Set(humidity)                
        return render_template('simple.html',TempHum=text)  
    return render_template('simple.html',TempHum=text)

#app = Flask(__name__)

@app.route('/LampeAus',methods=['POST','GET'])

def LampeAus():
    if request.method == 'GET':
        GPIO.output(Switch_K1, GPIO.LOW)    # Lampe AUS
        GPIO.output(Switch_K2, GPIO.HIGH)    # Lampe AUS      
        return render_template('test.html')
    return render_template('test.html')

@app.route('/LampeEin',methods=['POST','GET'])

def LampeEin():
    GPIO.output(Switch_K1, GPIO.HIGH)    # Lampe EIN
    GPIO.output(Switch_K2, GPIO.LOW)    # Lampe AUS
    return render_template('simple.html')

@app.route('/Chart')

def Chart(chartID = 'chart_ID', chart_type = 'line', chart_height = 500,TempData=[],HumyData=[],TimeScale=[]):

    TempData = Temp.GetBuffer()
    HumyData = Humi.GetBuffer()
    TimeScale = Time.GetBuffer()
    
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Temperatur', "data":TempData }, {"name": 'Luftfeuchte', "data": HumyData}]
    title = {"text": 'Klima'}
    xAxis = {"categories": TimeScale}
    yAxis = {"title": {"text": 'Temp[*C] Humidity[%]'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)



if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, passthrough_errors=True)
    



