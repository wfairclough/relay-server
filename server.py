from flask import Flask
from flask import request
from flask import render_template
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route("/relay/<int:relay_num>/state", methods=['GET', 'POST'])
def relay_state(relay_num):
    if request.method == 'GET':
        # Render the HTML page to show the state of the relay
        return render_template('relay.html', relay_num=relay_num)
    else:
        # Update the relay state
        relayState = 'off'
        if 'relayState' in request.form:
            relayState = request.form['relayState']

        return 'value: %s ' % relayState

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
