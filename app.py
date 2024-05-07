from flask import Flask, request, jsonify, render_template
import geocoder
import pdb

app = Flask(__name__)

@app.route('/')
def index():
        ip_address = request.remote_addr
        print(ip_address)


        return render_template('index.html')


@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.get_json()
    # Here you can implement the logic to determine the location using various methods
    # For simplicity, let's assume the location is provided in the request
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    return jsonify({'latitude': latitude, 'longitude': longitude})

if __name__ == '__main__':
        app.run(debug=True)