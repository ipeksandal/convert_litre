def convert_litre_per_100km_to_mpg(litre_per_100km):
    litres_per_km = litre_per_100km / 100.0
    km_per_litre = 1 / litres_per_km

    # 1 km = 0.621371 mil
    km_per_mile = 0.621371
    miles_per_gallon = km_per_litre / km_per_mile

    return miles_per_gallon



litre_per_100km = 9.4
mpg = convert_litre_per_100km_to_mpg(litre_per_100km)
print(f"{litre_per_100km} litre/100 km, {mpg:.2f} mil/galon'a eşittir.")
