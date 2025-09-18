aqi_values = [50, 65, 55, 80, 70, 65, 90, 100]  
average_aqi = sum(aqi_values) / len(aqi_values)
unique_aqi = set(aqi_values)
aqi_count = {
    50: aqi_values.count(50),
    65: aqi_values.count(65),
    55: aqi_values.count(55),
    80: aqi_values.count(80),
    70: aqi_values.count(70),
    90: aqi_values.count(90),
    100: aqi_values.count(100)
}

print("AQI Values (List):", aqi_values)
print("Average AQI:", average_aqi)
print("Unique AQI Values (Set):", unique_aqi)
print("AQI Frequency (Dictionary):", aqi_count)
