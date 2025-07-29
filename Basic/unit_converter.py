def km_to_miles(km):
    print(f"{km} km is equal to {km * 0.621371} miles")

def miles_to_km(miles):
    print(f"{miles} miles is equal to {miles / 0.621371} km")

def celsius_to_fahrenheit(celsius):
    print(f"{celsius} °C is equal to {(celsius * 9/5) + 32} °F")

def fahrenheit_to_celsius(fahrenheit):
    print(f"{fahrenheit} °F is equal to {(fahrenheit - 32) * 5/9} °C")

def kg_to_pounds(kg):
    print(f"{kg} kg is equal to {kg * 2.20462} pounds")

def pound_to_kg(pounds):
    print(f"{pounds} pounds is equal to {pounds / 2.20462} kg")

def liters_to_gallons(liters):
    print(f"{liters} liters is equal to {liters * 0.264172} gallons")

def gallons_to_liters(gallons):
    print(f"{gallons} gallons is equal to {gallons / 0.264172} liters")

def minutes_to_seconds(minutes):
    print(f"{minutes} minutes is equal to {minutes * 60} seconds")

def seconds_to_minutes(seconds):
    print(f"{seconds} seconds is equal to {seconds / 60} minutes")

def sq_meters_to_sq_feet(sqm):
    print(f"{sqm} sq meters is equal to {sqm * 10.7639} sq feet")

def sq_feet_to_sq_meters(sqft):
    print(f"{sqft} sq feet is equal to {sqft / 10.7639} sq meters")

def main():
    while True:
        try:
            a = float(input("Enter value: "))
            print('''
            LIST OF UNIT THAT CONVERT :
            - km
            - miles
            - kg
            - pound
            - liters
            - gallons
            -celsius
            - fahrenheit
            - seconds
            - minutes
            - sq feet
            - sq meters
            ''')
            unit = input("Choose unit to convert to : ").lower().strip()

            if unit == "miles":
                km_to_miles(a)
            elif unit == "km":
                miles_to_km(a)
            elif unit == "fahrenheit":
                celsius_to_fahrenheit(a)
            elif unit == "celsius":
                fahrenheit_to_celsius(a)
            elif unit == "pounds":
                kg_to_pounds(a)
            elif unit == "kg":
                pound_to_kg(a)
            elif unit == "gallons":
                liters_to_gallons(a)
            elif unit == "liters":
                gallons_to_liters(a)
            elif unit == "seconds":
                minutes_to_seconds(a)
            elif unit == "minutes":
                seconds_to_minutes(a)
            elif unit == "sq feet":
                sq_meters_to_sq_feet(a)
            elif unit == "sq meters":
                sq_feet_to_sq_meters(a)
            
            else:
                print("Invalid unit.")
        except ValueError:
            print("Please enter a valid number.")

        choice = input("Do you want to calculate again? (y/n): ").lower()
        if choice == 'n':
            print("Goodbye! 👋")
            break  # exit the loop


main()
