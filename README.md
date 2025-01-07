<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <div class="container">
        <h1>Weather Wizard 🌦️</h1>
        <p><strong>Weather Wizard</strong> is a Python-based weather application that fetches real-time weather data from the 
            <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap API</a>. It provides an interactive menu-driven interface to display detailed information about the weather in any city.</p>

  <h2>Features 🚀</h2>
        <ul>
            <li>Fetch real-time weather data for any city.</li>
            <li>View detailed weather information like:
                <ul>
                    <li>Temperature</li>
                    <li>Atmospheric Pressure</li>
                    <li>Humidity</li>
                    <li>Wind Speed</li>
                    <li>All of the above in one view</li>
                </ul>
            </li>
            <li>Handles invalid inputs gracefully.</li>
        </ul>

  <h2>How to Use 🛠️</h2>
        <ol>
            <li>Clone the repository:
                <pre>git clone https://github.com/your-username/Weather-Wizard.git
cd Weather-Wizard</pre>
            </li>
            <li>Install the required library:
                <pre>pip install requests</pre>
            </li>
            <li>Replace the placeholder <code>api_key</code> in the code with your OpenWeatherMap API key:
                <pre>api_key = "your_api_key_here"</pre>
            </li>
            <li>Run the script:
                <pre>python weather.py</pre>
            </li>
            <li>Follow the on-screen instructions to get weather details for your city.</li>
        </ol>

  <h2>Example Output 💡</h2>
        <p><strong>Input:</strong></p>
        <pre>
Enter city name: New York <br>
What Do You Want to Know:
1. Temperature
2. Pressure
3. Wind Speed
4. Humidity
5. All of the Above
6. Exit <br>
Please let us know: 5
        </pre>
        <p><strong>Output:</strong></p>
        <pre>
🌍 Weather Report for New York:
--------------------------------
🌡️ Temperature: 10°C
📏 Pressure: 1015 hPa
💧 Humidity: 70%
💨 Wind Speed: 3.5 m/s
📋 Description: Clear sky
<br>
Thank you for using Weather Wizard! Have a nice day! 😊
        </pre>

  <h2>Requirements 📦</h2>
        <ul>
            <li>Python 3.x</li>
            <li><code>requests</code> library</li>
        </ul>

  <h2>API Key 🔑</h2>
        <p>This project uses the OpenWeatherMap API. You can obtain your API key by signing up 
            <a href="https://home.openweathermap.org/users/sign_up" target="_blank">here</a>. Replace the placeholder in the code with your key.</p>

  <h2>Contribution 🤝</h2>
        <p>Feel free to fork this repository, make changes, and submit pull requests. Suggestions and feature requests are always welcome!</p>

  <h2>License 📜</h2>
        <p>This project is licensed under the MIT License.</p>

  <div class="footer">
  <h2>Author </h2>    
  <p>Developed by <strong>Raunak Jain 👨‍💻 </strong> <br>
                📧 Email: <a href="mailto:raunakjain1002@gmail.com">raunakjain1002@gmail.com</a>
            </p>
        </div>
    </div>
</body>
</html>
