# Django Weather Detector App

Welcome to the Django Weather Detector App!

This application allows users to input a city and retrieve real-time weather data using the [OpenWeatherMap API](https://openweathermap.org/).

The app provides information such as temperature, coordinates (latitude and longitude), pressure, country code, humidity, and wind speed.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/akinyiliz/django-weather-detector.git
```

2. Navigate to the project directory:

```bash
cd django-weather-detector
```

3. Create and activate a virtual environment "myenv":

```bash
python -m venv myenv
source myenv/bin/activate # On Windows: myenv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) to access weather data.

2. Create a `.env` file in your project's root directory. Replace `your_actual_api_key` with API key obtained from [OpenWeatherMap](https://openweathermap.org/).

```plaintext
WEATHER_API_KEY=your_actual_api_key
```

## Running the App

Start the development server:

```bash
python manage.py runserver
```

Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) to access the app.

## How to Use

1. Visit the home page.

2. Enter the desired city name in the input field and press Enter key.

3. View the weather information for the specified city, including temperature, coordinates, pressure, country code, humidity, and wind speed.
