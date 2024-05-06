from flask import Flask, request
import geocoder
import pdb

app = Flask(__name__)

@app.route('/')
def index():
        ip_address = request.remote_addr
        pdb.set_trace()
        coordinates = get_coordinates(ip_address)

        return f'Ip address: {ip_address}<br>Coordinates: {coordinates}'

def get_coordinates(ip_address):
        g = geocoder.ip(ip_address)
        pdb.set_trace()
        if g.ok:
                return g.latlng
        else:
                return 'Failed'
if __name__ == '__main__':
        app.run(debug=True)