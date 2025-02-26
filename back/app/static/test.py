import csv
import random

# Define the prioritized locations
locations = [
    #china
    ("Beijing", "China"), ("Shanghai", "China"), ("Guangzhou", "China"),
    ("Shenzhen", "China"), ("Chengdu", "China"), ("Wuhan", "China"),
    ("Hangzhou", "China"), ("Chongqing", "China"), ("Nanjing", "China"),
    ("Tianjin", "China"), ("Xi'an", "China"), ("Suzhou", "China"),
    ("Qingdao", "China"), ("Dalian", "China"), ("Shenyang", "China"),
    ("Changchun", "China"), ("Harbin", "China"), ("Changsha", "China"),
    ("Nanchang", "China"), ("Fuzhou", "China"), ("Xiamen", "China"),
    ("Ningbo", "China"), ("Wenzhou", "China"), ("Zhengzhou", "China"),
    ("Jinan", "China"), ("Taiyuan", "China"), ("Hohhot", "China"),
    ("Hefei", "China"), ("Huangshan", "China"), ("Wuhan", "China"),
    ("Changsha", "China"), ("Nanchang", "China"), ("Fuzhou", "China"),
    ("Xiamen", "China"), ("Ningbo", "China"), ("Wenzhou", "China"),
    ("Zhengzhou", "China"), ("Jinan", "China"), ("Taiyuan", "China"),
    ("Hohhot", "China"), ("Hefei", "China"), ("Huangshan", "China"),
    ("Wuhan", "China"), ("Changsha", "China"), ("Nanchang", "China"),
    ("Fuzhou", "China"), ("Xiamen", "China"),("Ningbo", "China"),
    #another cities from china
    ("Changzhou", "China"), ("Zhenjiang", "China"), ("Yangzhou", "China"),
    ("Taizhou", "China"), ("Nantong", "China"), ("Suqian", "China"),
    ("Lianyungang", "China"), ("Huaian", "China"), ("Yancheng", "China"),
    ("Xuzhou", "China"), ("Huai'an", "China"), ("Lianyungang", "China"),
    ("Huaian", "China"), ("Yancheng", "China"), ("Xuzhou", "China"),
    ("Huai'an", "China"), ("Lianyungang", "China"), ("Huaian", "China"),
    ("Yancheng", "China"), ("Xuzhou", "China"), ("Huai'an", "China"),
    ("Lianyungang", "China"), ("Huaian", "China"), ("Yancheng", "China"),
    ("Xuzhou", "China"), ("Huai'an", "China"), ("Lianyungang", "China"),
    ("Huaian", "China"), ("Yancheng", "China"), ("Xuzhou", "China"),
    ("Huai'an", "China"), ("Lianyungang", "China"), ("Huaian", "China"),
    ("Yancheng", "China"), ("Xuzhou", "China"), ("Huai'an", "China"),
    ("Lianyungang", "China"), ("Huaian", "China"), ("Yancheng", "China"),
    ("Xuzhou", "China"), ("Huai'an", "China"), ("Lianyungang", "China"),
    ("Huaian", "China"), ("Yancheng", "China"), ("Xuzhou", "China"),
    ("Huai'an", "China"), ("Lianyungang", "China"), ("Huaian", "China"),
    ("Yancheng", "China"), ("Xuzhou", "China"), ("Huai'an", "China"),
    ("Lianyungang", "China"), ("Huaian", "China"), ("Yancheng", "China"),
    ("Xuzhou", "China"), ("Huai'an", "China"), ("Lianyungang", "China"),
    #india
    ("Kolkata", "India"), ("Surat", "India"), ("Pune", "India"),
    ("Jaipur", "India"), ("Lucknow", "India"), ("Kanpur", "India"),
    ("Nagpur", "India"), ("Indore", "India"), ("Thane", "India"),
    ("Bhopal", "India"), ("Visakhapatnam", "India"), ("Pimpri-Chinchwad", "India"),
    ("Patna", "India"), ("Vadodara", "India"), ("Ghaziabad", "India"),
    ("Ludhiana", "India"), ("Agra", "India"), ("Nashik", "India"),
    ("Faridabad", "India"), ("Meerut", "India"), ("Rajkot", "India"),
    ("Kalyan-Dombivli", "India"), ("Vasai-Virar", "India"), ("Varanasi", "India"),
    ("Srinagar", "India"), ("Aurangabad", "India"), ("Dhanbad", "India"),
    ("Amritsar", "India"), ("Navi Mumbai", "India"), ("Allahabad", "India"),
    ("Ranchi", "India"), ("Haora", "India"), ("Coimbatore", "India"),
    ("Jabalpur", "India"), ("Gwalior", "India"), ("Vijayawada", "India"),
    ("Jodhpur", "India"), ("Madurai", "India"), ("Raipur", "India"),
    ("Kota", "India"), ("Guwahati", "India"), ("Chandigarh", "India"),
    ("Solapur", "India"), ("Hubli-Dharwad", "India"), ("Bareilly", "India"),
    ("Moradabad", "India"), ("Mysore", "India"), ("Gurgaon", "India"),
    ("Aligarh", "India"), ("Jalandhar", "India"), ("Tiruchirappalli", "India"),
    ("Bhubaneswar", "India"), ("Salem", "India"), ("Mira-Bhayandar", "India"),
    ("Thiruvananthapuram", "India"), ("Bhiwandi", "India"), ("Saharanpur", "India"),
    ("Gorakhpur", "India"), ("Guntur", "India"),
    
    #another cities from india
    ("Bikaner", "India"), ("Ajmer", "India"), ("Udaipur", "India"),
    ("Bhilwara", "India"), ("Alwar", "India"), ("Bharatpur", "India"),
    ("Sikar", "India"), ("Pali", "India"), ("Sri Ganganagar", "India"),
    ("Kota", "India"), ("Bundi", "India"), ("Bhilwara", "India"),
    ("Chittorgarh", "India"), ("Dungarpur", "India"), ("Jaipur", "India"),
    ("Jaisalmer", "India"), ("Jhalawar", "India"), ("Jhunjhunu", "India"),
    ("Jodhpur", "India"), ("Karauli", "India"), ("Kota", "India"),
    ("Nagaur", "India"), ("Pali", "India"), ("Pratapgarh", "India"),
    ("Rajsamand", "India"), ("Sawai Madhopur", "India"), ("Sikar", "India"),
    ("Sirohi", "India"), ("Sri Ganganagar", "India"), ("Tonk", "India"),
    ("Udaipur", "India"), ("Bharatpur", "India"), ("Bikaner", "India"),
    ("Bundi", "India"), ("Churu", "India"), ("Dausa", "India"),
    ("Dholpur", "India"), ("Dungarpur", "India"), ("Hanumangarh", "India"),
    ("Jaisalmer", "India"), ("Jalore", "India"), ("Jhalawar", "India"),
    ("Jhunjhunu", "India"), ("Karauli", "India"), ("Nagaur", "India"),
    ("Pali", "India"), ("Pratapgarh", "India"), ("Rajsamand", "India"),
    ("Sawai Madhopur", "India"), ("Sikar", "India"), ("Sirohi", "India"),
    ("Sri Ganganagar", "India"), ("Tonk", "India"), ("Udaipur", "India"),
    #russia
    ("Moscow", "Russia"), ("Saint Petersburg", "Russia"), ("Novosibirsk", "Russia"),
    ("Yekaterinburg", "Russia"), ("Nizhny Novgorod", "Russia"), ("Samara", "Russia"),
    ("Omsk", "Russia"), ("Kazan", "Russia"), ("Chelyabinsk", "Russia"),
    ("Rostov-on-Don", "Russia"), ("Ufa", "Russia"), ("Volgograd", "Russia"),
    ("Perm", "Russia"), ("Krasnoyarsk", "Russia"), ("Voronezh", "Russia"),
    ("Saratov", "Russia"), ("Krasnodar", "Russia"), ("Tolyatti", "Russia"),
    #USa
    ("New York", "USA"), ("Los Angeles", "USA"), ("Chicago", "USA"),
    ("Houston", "USA"), ("Phoenix", "USA"), ("Philadelphia", "USA"),
    ("San Antonio", "USA"), ("San Diego", "USA"), ("Dallas", "USA"),
    ("San Jose", "USA"), ("Austin", "USA"), ("Jacksonville", "USA"),
    ("San Francisco", "USA"), ("Indianapolis", "USA"), ("Columbus", "USA"),
    ("Fort Worth", "USA"), ("Charlotte", "USA"), ("Seattle", "USA"),
    ("Denver", "USA"), ("El Paso", "USA"), ("Detroit", "USA"),  
    ("Washington", "USA"), ("Boston", "USA"), ("Memphis", "USA"),
    
    ("New York", "USA"), ("London", "UK"), ("Berlin", "Germany"),
    ("Sydney", "Australia"), ("Tokyo", "Japan"), ("Paris", "France"),
    ("Moscow", "Russia"), ("Cairo", "Egypt"), ("Dubai", "UAE"),
    ("Rome", "Italy"), ("Toronto", "Canada"), ("Seoul", "South Korea"),
    ("Singapore", "Singapore"), ("Bangkok", "Thailand"), ("Kuala Lumpur", "Malaysia"),
    ("Jakarta", "Indonesia"), ("Cape Town", "South Africa"), ("Rio de Janeiro", "Brazil"),
    ("Buenos Aires", "Argentina"), ("Mexico City", "Mexico"), ("Lagos", "Nigeria"),
    ("Nairobi", "Kenya"), ("Mumbai", "India"), ("Delhi", "India"),
    #south america
    ("Sao Paulo", "Brazil"), ("Buenos Aires", "Argentina"), ("Lima", "Peru"),
    ("Bogota", "Colombia"), ("Rio de Janeiro", "Brazil"), ("Caracas", "Venezuela"),
    ("Santiago", "Chile"), ("Guayaquil", "Ecuador"), ("La Paz", "Bolivia"),
    ("San Salvador", "El Salvador"), ("Asuncion", "Paraguay"), ("Montevideo", "Uruguay"),
    ("Georgetown", "Guyana"), ("Paramaribo", "Suriname"), ("Cayenne", "French Guiana"),
    ("Quito", "Ecuador"), ("Bridgetown", "USA"), ("Port of Spain", "Trinidad and Tobago"),
    ("Kingston", "Jamaica"), ("Havana", "Cuba"), ("Nassau", "Bahamas"),
    ("Santo Domingo", "Dominican Republic"), ("Port-au-Prince", "Haiti"),
    ("Saint John's", "Antigua and Barbuda"), ("Basseterre", "Saint Kitts and Nevis"),
    ("Roseau", "Dominica"), ("Castries", "Saint Lucia"), ("St. George's", "Grenada"),
    ("Kingstown", "Saint Vincent and the Grenadines"), ("Port of Spain", "Trinidad and Tobago"),
    ("Bridgetown", "USA"), ("St. John's", "Antigua and Barbuda"), ("Basseterre", "Saint Kitts and Nevis"),
    ("Roseau", "Dominica"), ("Castries", "Saint Lucia"), ("St. George's", "Grenada"),
    ("Kingstown", "Saint Vincent and the Grenadines"), ("Port of Spain", "Trinidad and Tobago"),
    ("Bridgetown", "USA"), ("St. John's", "Antigua and Barbuda"), ("Basseterre", "Saint Kitts and Nevis"),
    ("Roseau", "Dominica"), ("Castries", "Saint Lucia"), ("St. George's", "Grenada"),
    ("Kingstown", "Saint Vincent and the Grenadines"), ("Port of Spain", "Trinidad and Tobago"),
    ("Bridgetown", "USA"),
    #europe
    ("London", "UK"), ("Paris", "France"), ("Berlin", "Germany"),
    ("Madrid", "Spain"), ("Rome", "Italy"), ("Amsterdam", "Netherlands"),
    ("Vienna", "Austria"), ("Prague", "Czech Republic"), ("Warsaw", "Poland"),
    ("Budapest", "Hungary"), ("Stockholm", "Sweden"), ("Oslo", "Norway"),
    ("Helsinki", "Finland"), ("Copenhagen", "Denmark"), ("Dublin", "Ireland"),
    ("Brussels", "Belgium"), ("Lisbon", "Portugal"), ("Athens", "Greece"),
    ("Zurich", "Switzerland"), ("Geneva", "Switzerland"), ("Luxembourg", "Luxembourg"),
    ("Monaco", "Monaco"), ("Andorra la Vella", "Andorra"), ("San Marino", "San Marino"),
    ("Vatican City", "Vatican City"), ("Reykjavik", "Iceland"), ("Valletta", "Malta"),
    ("Tirana", "Albania"), ("Sarajevo", "Bosnia and Herzegovina"), ("Skopje", "North Macedonia"),
    ("Podgorica", "Montenegro"), ("Pristina", "Kosovo"), ("Belgrade", "Serbia"),
    ("Ljubljana", "Slovenia"), ("Zagreb", "Croatia"), ("Sofia", "Bulgaria"),
    ("Bucharest", "Romania"), ("Chisinau", "Moldova"), ("Tbilisi", "Georgia"),
    
]

# Increase the probability of China and India being selected
weighted_locations = locations * 5  # Adjust the weight multiplier as needed

def get_random_location():
    return random.choice(weighted_locations)

# Process the CSV data
def anonymize_geo_location(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        for row in reader:
            city, country = get_random_location()
            row['Geo-location Data'] = f"{city}, {country}"
            writer.writerow(row)

# Provide the input and output CSV file paths
input_csv = '/Users/javierrangel/Documents/DB_Project/back/app/static/cybersecurity_attacksold.csv'
output_csv = '/Users/javierrangel/Documents/DB_Project/back/app/static/cybersecurity_attacks.csv'

# Run the anonymization function
anonymize_geo_location(input_csv, output_csv)


import pandas as pd
import random
from datetime import datetime

def weighted_random_date_generator(month_weights, year):
    # Select a month based on the defined weights
    month = random.choices(list(month_weights.keys()), weights=list(month_weights.values()), k=1)[0]
    # Randomly generate a day for the selected month (assuming 28-31 days)
    day = random.randint(1, 28 if month == 2 else (30 if month in [4, 6, 9, 11] else 31))
    # Randomly generate a time
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    # Construct the datetime object and format it
    return datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S')

def modify_csv_dates(file_path, output_path):
    df = pd.read_csv(file_path)

    # Define the month weights based on the requirements
    month_weights = {
        1: 10, 2: 20, 3: 10, 4: 10, 5: 15, 6: 10,
        7: 15, 8: 10, 9: 20, 10: 20, 11: 20, 12: 15
    }

    # Update the timestamps
    df['Timestamp'] = df['Timestamp'].apply(lambda x: weighted_random_date_generator(month_weights, pd.to_datetime(x).year))

    # Save the modified CSV
    df.to_csv(output_path, index=False)

# Example usage
#modify_csv_dates(input_csv, output_csv)
