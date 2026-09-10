import csv
def forest_analysis():
    with open("data/forest_data.csv", "r") as file:
    data = csv.DictReader(file)
    print(list(data))
    print("🌲 SylvaSense - Forest Monitoring")
    print("--------------------------------")

    area = float(input("Enter forest area in hectares: "))
    canopy = float(input("Enter tree canopy coverage (%): "))

    biomass = area * canopy * 2.5
    carbon = biomass * 0.47

    print("\n--- Forest Analysis ---")
    print(f"Forest Area: {area:.2f} hectares")
    print(f"Canopy Coverage: {canopy:.2f}%")
    print(f"Estimated Biomass: {biomass:.2f} tonnes")
    print(f"Estimated Carbon: {carbon:.2f} tonnes")

    if canopy < 30:
        print("⚠️ Warning: Low canopy coverage detected.")
    else:
        print("✅ Forest canopy condition looks healthy.")


if __name__ == "__main__":
    forest_analysis()
