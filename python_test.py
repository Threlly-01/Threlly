market_name = "Balogun market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False
total_daily_revenue = 25000000
average_daily_revenue = total_daily_revenue/num_traders
x = average_daily_revenue
average_daily_revenue = str(x) + " Naira"
print("Market:", market_name, ", Type:", type(market_name))
print("Traders:", num_traders, ", Type:", type(num_traders))
print("Coordinates:", location_coords, ", Type:", type(location_coords))
print("Open Sundays:", is_open_sundays, ", Type:", type(is_open_sundays))
print("Average Daily Revenue per Trader:", average_daily_revenue)

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
host_countries.append("Ivory Coast")
print(host_countries)

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
host_countries.insert(1, "Morocco")
print(host_countries)

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
host_countries.pop( 3)
print(host_countries)

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
print(len(host_countries))

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
host_countries = sorted(host_countries)
print(host_countries)

Rivers = {
    "Nile": {"length_km": 6650, "countries": 11},
 "Congo": {"length_km": 4700, "countries": 9},
 "Niger": {"length_km": 4180, "countries": 5}
}

Rivers["Zambesi"] = {"length_km": 2574, "countries": 6}
print(Rivers)

Rivers["Nile"]["countries"] = 6
print(Rivers)

for River in Rivers.keys():
    print(River)

Rivers["Congo"]["countries"]

total = 0
for River, data in Rivers.items():
    total += data["length_km"]
print(total)

for i in range(1, 11):
    print("7 x " + str(i) + "=" + str((7 * i)))

word = "AFRICA"
for i in word:
    print(i)

total = 0
for i in range(1, 51):
    if i % 2 == 0:
        total = total + i
print(total)

total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total = total + i
print(total)

i = 20
while i >= 1:
    print(i)
    i = i - 1

i = 500
while i % 3 != 0 or i % 7 != 0:
    i += 1
print(i)

def classify_rainfall (mm):
    if mm >300:
        return "Flood Risk"
    elif mm >= 200 and mm <= 300:
        return "Heavy Rain"
    elif mm >= 100 and mm <= 199:
        return "Moderate Rain"
    elif mm >= 1 and mm <= 99:
        return "Light Rain"
    else:
        return "Dry"
print("350mm: " + classify_rainfall(350))
print("250mm: " + classify_rainfall(250))
print("150mm: " + classify_rainfall(150))
print("50mm: " + classify_rainfall(50))
print("0mm: " + classify_rainfall(0))

def calculate_exchange (amount, rate):
    result = float(amount * rate)
    return result
print(calculate_exchange(100, 1580))
print("")
# This function formats a price with a currency code
# The currency parameter is optional. It defaults to "NGN"if not provided
def format_price (amount, currency = "NGN"):
    formatted = "{:,}". format(amount)
    return currency + " " + formatted
print(format_price(5000))
print(format_price(200, "GHS"))
print("")
# This function takes a list of student scores and returns the highest, lowwest and class average scores
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores)/len(scores)
    return lowest, highest, average
# Test with: [55, 72, 88, 61, 94, 47, 79]
print(analyze_scores([55, 72, 88, 61, 94, 47, 79]))