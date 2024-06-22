from openai import OpenAI
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

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

    return forecast_list

@app.route('/chat', methods=['POST'])
def chat_with_model():
    weather_forecast = get_weather_forecast()
    user_input = request.json['user_input']

    # Construct prompt with user input and weather forecast
    prompt = f"Hi, You are a farmers assistant. We provide you with weather details and you need to help farmers answering their questions. Here is the latest weather forecast:\n{weather_forecast}\n\nUser Question: {user_input}\n\nAnswer:"

    # Initialize OpenAI client
    client = OpenAI(api_key ="")

    # Generate completion
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    # print(completion)
    print(completion.choices[0].message.content)
    return {"message": completion.choices[0].message.content}
    # return jsonify({'response': completion.choices[0].message})

if __name__ == '__main__':
    app.run(debug=True)
