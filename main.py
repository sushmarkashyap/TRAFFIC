from flask import Flask, jsonify, url_for, request, render_template
from gpiozero import LED
import time

app = Flask(__name__)

red=LED(15)
yellow=LED(17)
green=LED(18)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/redonpin', methods=['POST'])
def redonpin():
    if request.method == 'POST':
        body=request.get_json()
        # on = LED_ON(body['pin'])
        red.on()
        return jsonify({"status" : 'on.show_ledON()' })
    else:
         return jsonify({'status:cant find status'})
    
@app.route('/redoffpin', methods=['POST'])
def redoffpin():
    if request.method == 'POST':
        body=request.get_json()
        # off = LED_OFF(body['pin'])
        red.off()
        return jsonify({"status" :' off.show_ledOFF()' })
    else:
        return jsonify({'status:cant find status'})
@app.route('/yellowonpin', methods=['POST'])
def yellowonpin():
    if request.method == 'POST':
        body=request.get_json()
        # on = LED_ON(body['pin'])
        yellow.on()
        return jsonify({"status" : 'on.show_ledON()' })
    else:
         return jsonify({'status:cant find status'})
    
@app.route('/yellowoffpin', methods=['POST'])
def yellowoffpin():
    if request.method == 'POST':
        body=request.get_json()
        # off = LED_OFF(body['pin'])
        yellow.off()
        return jsonify({"status" :' off.show_ledOFF()' })
    else:
        return jsonify({'status:cant find status'})                  
    
@app.route('/greenonpin', methods=['POST'])
def greenonpin():
    if request.method == 'POST':
        body=request.get_json()
        # on = LED_ON(body['pin'])
        green.on()
        return jsonify({"status" : 'on.show_ledON()' })
    else:
         return jsonify({'status:cant find status'})
    
@app.route('/greenoffpin', methods=['POST'])
def greenoffpin():
    if request.method == 'POST':
        body=request.get_json()
        # off = LED_OFF(body['pin'])
        green.off()
        return jsonify({"status" :' off.show_ledOFF()' })
    else:
        return jsonify({'status:cant find status'})

@app.route('/trafficonpin', methods=['POST'])
def trafficonpin():
    if request.method == 'POST':
        body=request.get_json()
        r=LED(body.r)
        y=LED(body.y)
        g=LED(body.g)
        for i in range(0,5):
            r.on()
            time.sleep(2)
            r.off()
            time.sleep(0.5)
            y.on()
            time.sleep(1)
            y.off()
            time.sleep(0.5)
            g.on()
            time.sleep(2)
            g.off()
            time.sleep(0.5)
            y.on()
            time.sleep(1)
            y.off()
            time.sleep(0.5)
        return jsonify({"status" : 'on.show_ledON()' })
    else:
         return jsonify({'status:cant find status'})


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
