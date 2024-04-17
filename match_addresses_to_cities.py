import pandas as pd

# Read the Excel file containing the addresses
df = pd.read_excel("address_list.xlsx")

# List of cities
cities = [
    "Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga",
    "Dunedin", "Palmerston North", "Napier", "Hastings", "New Plymouth",
    "Rotorua", "Nelson", "Whangarei", "Invercargill", "Whanganui",
    "Gisborne", "Blenheim", "Timaru", "Taupo", "Masterton",
    "Levin", "Tokoroa", "Ashburton", "Whakatane", "Cambridge",
    "Gore", "Oamaru", "Greymouth", "Queenstown", "Waiuku",
    "Motueka", "Kerikeri", "Thames", "Kawerau", "Huntly",
    "Opotiki", "Paeroa", "Dannevirke", "Wairoa", "Stratford",
    "Te Kuiti", "Dargaville", "Picton", "Waipukurau", "Reefton",
    "Feilding", "Marton", "Temuka", "Foxton", "Balclutha",
    "Matamata", "Kaikohe", "Westport", "Warkworth", "Pukekohe",
    "Kerikeri", "Kaikoura", "Hokitika", "Alexandra", "Wanaka",
    "Amberley", "Turangi", "Morrinsville", "Waipawa", "Ohakune",
    "Opunake", "Otorohanga", "Waitara", "Eltham", "Murchison",
    "Norsewood", "Gore", "Kaitaia", "Otaki", "Te Awamutu",
    "Woodville", "Edgecumbe", "Greytown", "Putaruru", "Havelock",
    "Snells Beach", "Takaka", "Methven", "Kawakawa", "Waihi",
    "Te Aroha", "Lincoln", "Milton", "Owaka", "Darfield",
    "Winton", "Manapouri", "Waipawa", "Picton", "Owaka",
    "Moerewa", "Kaitangata", "Taumarunui", "Opua", "Collingwood"
]

# Function to match address with cities
def match_city(address):
    if pd.isna(address):  # Check if the address is NaN
        return None
    for city in cities:
        if city.lower() in address.lower():
            return city
    return None

# Apply the function to match city for each address in column 'Address Title'
df['City'] = df['Address Title'].apply(match_city)

# Save the DataFrame with "Address Title" and "City" columns to a new Excel file
df[['Address Title', 'City']].to_excel("city_list_matched.xlsx", index=False, na_rep='')

