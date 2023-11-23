import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim

def get_phone_info():
    entered_num = phone_entry.get()

    try:
        phone_num = phonenumbers.parse(entered_num, None)
        location_info = geocoder.description_for_number(phone_num, "en")
        carrier_info = carrier.name_for_number(phone_num, "en")
        time_zones = timezone.time_zones_for_number(phone_num)
        time_zones_str = ", ".join(time_zones)

        if phone_num.country_code in [1, 7]:
            geolocator = Nominatim(user_agent="phone_location")
            location = geolocator.geocode(entered_num, language="en")

            if location:
                city_info = location.address
            else:
                city_info = "City information not available."
        else:
            city_info = "City information not available for this country code."

        result_str = f"Location: {location_info}\nCarrier: {carrier_info}\nTime Zones: {time_zones_str}\nCity: {city_info}"
        result_label.config(text=result_str)
    except phonenumbers.NumberParseException as e:
        messagebox.showerror("Error", f"Invalid phone number: {e}")

# Create the main window
root = tk.Tk()
root.title("Phone Information")

# Create and place widgets
phone_label = tk.Label(root, text="Enter a phone number:")
phone_label.pack(pady=10)

phone_entry = tk.Entry(root)
phone_entry.pack(pady=10)

get_info_button = tk.Button(root, text="Get Information", command=get_phone_info)
get_info_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
