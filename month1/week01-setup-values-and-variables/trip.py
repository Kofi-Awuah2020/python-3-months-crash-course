def trip_cost(distance_km, litres_per_100km, price_per_litre):
    litres = distance_km * litres_per_100km / 100
    return round(litres * price_per_litre, 2)

if __name__ == "__main__":
    print(f"Trip: 250 km | Cost: {trip_cost(250, 6, 1.85)}")