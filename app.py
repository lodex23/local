from flask import Flask, request, jsonify, render_template
import geocoder
import pdb
import logging

app = Flask(__name__)


# Create a Logger
logger = logging.getLogger('Location_writer')

# Set the log level to Info
logger.setLevel(logging.INFO)

#Create a file handler for outputting to a file
fh = logging.FileHandler('Location.log')

fh.setLevel(logging.INFO)

#Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add the logger to the Flask app
app.logger.addHandler(fh)
fh.setFormatter(formatter)
logger.addHandler(fh)


@app.route('/')
def index():
        ip_address = request.remote_addr
        print(ip_address)

        logger.info(ip_address)

        return render_template('index.html')


@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.get_json()
    # Here you can implement the logic to determine the location using various methods
    # For simplicity, let's assume the location is provided in the request
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    logger.info(f"Latitude: {latitude}, Longitude: {longitude}")
    return None

if __name__ == '__main__':
        app.run(debug=True)