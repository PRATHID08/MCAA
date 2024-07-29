weather_data = [
    {'Date': '2024-07-01', 'Max Temp': 32, 'Min Temp': 22, 'Humidity': 60},
    {'Date': '2024-07-02', 'Max Temp': 30, 'Min Temp': 21, 'Humidity': 65},
    {'Date': '2024-07-03', 'Max Temp': 35, 'Min Temp': 24, 'Humidity': 70},
    {'Date': '2024-07-04', 'Max Temp': 33, 'Min Temp': 23, 'Humidity': 68},
    {'Date': '2024-07-05', 'Max Temp': 29, 'Min Temp': 20, 'Humidity': 75},
    {'Date': '2024-07-06', 'Max Temp': 31, 'Min Temp': 22, 'Humidity': 64},
    {'Date': '2024-07-07', 'Max Temp': 28, 'Min Temp': 19, 'Humidity': 80}
]


def find_highest_lowest_temperatures(data):
    max_temps = [entry['Max Temp'] for entry in data]
    min_temps = [entry['Min Temp'] for entry in data]
    
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)
    
    return highest_temp, lowest_temp

def count_days_above_30(data):
    count = sum(1 for entry in data if entry['Max Temp'] > 30)
    return count

def compute_average_humidity(data):
    humidities = [entry['Humidity'] for entry in data]
    average_humidity = sum(humidities) / len(humidities)
    return average_humidity

# Example usage
highest_temp, lowest_temp = find_highest_lowest_temperatures(weather_data)
print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature: {lowest_temp}°C")

days_above_30 = count_days_above_30(weather_data)
print(f"Number of Days Above 30°C: {days_above_30}")

average_humidity = compute_average_humidity(weather_data)
print(f"Average Humidity: {average_humidity}%")
