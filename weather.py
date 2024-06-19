from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather_forecast():
    url = "https://api.weather.gov/gridpoints/MPX/107,69/forecast"
    headers = {
        'User-Agent': 'WeatherBot/1.0 (your-email@example.com)',
        'Accept': 'application/ld+json'
    }
    response = requests.get(url, headers=headers).json()
    periods = response['periods']
    
    forecast_list = []
    for period in periods:
        forecast_list.append({
            'name': period['name'],
            'startTime': period['startTime'],
            'endTime': period['endTime'],
            'isDaytime': period['isDaytime'],
            'temperature': period['temperature'],
            'temperatureUnit': period['temperatureUnit'],
            'windSpeed': period['windSpeed'],
            'windDirection': period['windDirection'],
            'shortForecast': period['shortForecast'],
            'detailedForecast': period['detailedForecast']
        })

    return jsonify({'forecasts': forecast_list})

if __name__ == '__main__':
    app.run(debug=True)
