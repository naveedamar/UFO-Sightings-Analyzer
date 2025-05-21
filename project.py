import csv
from collections import Counter
import os
import json

# Load data from CSV file into a list of dictionaries.
def load_data(filepath):
    data = []
    if not os.path.exists(filepath):
        print(f"[Error] File not found: {filepath}")
        return data

    with open(filepath, 'r', newline='', encoding='utf-8') as myfile:
        reader = csv.DictReader(myfile)
        for row in reader:
            new_row = {
                'city': row.get('Location.City', '').strip(),
                'state': row.get('Location.State', '').strip(),
                'country': row.get('Location.Country', '').strip(),
                'shape': row.get('Data.Shape', '').strip().lower(),
                'duration (seconds)': row.get('Data.Encounter duration', '').strip(),
                'datetime': f"{row.get('Dates.Sighted.Year', '')}-{row.get('Dates.Sighted.Month', '').zfill(2)}-{row.get('Date.Sighted.Day', '').zfill(2)} {row.get('Dates.Sighted.Hour', '').zfill(2)}:{row.get('Dates.Sighted.Minute', '').zfill(2)}",
                'latitude': row.get('Location.Coordinates.Latitude ', '').strip(),
                'longitude': row.get('Location.Coordinates.Longitude ', '').strip(),
                'description': row.get('Data.Description excerpt', '').strip()
            }
            data.append(new_row)
    return data

# Start of duration functions ---

# Count sightings where the duration is greater than or equal to the specified minimum duration.
def count_by_duration(data, min_duration):
    count = 0
    for row in data:
        duration_str = row.get('duration (seconds)', '')
        if duration_str:
            try:
                duration = float(duration_str)
                if duration >= min_duration:
                    count += 1
            except ValueError:
                print(f"[Warning] Could not convert duration '{duration_str}' to float for row: {row.get('datetime')}")
                continue
    return count

# Get the top N most frequent UFO sighting durations.
def get_top_durations(data, n):
    durations = []
    for row in data:
        duration_str = row.get('duration (seconds)', '')
        if duration_str:
            try:
                durations.append(float(duration_str))
            except ValueError:
                continue
    return Counter(durations).most_common(n)

# Search sightings by duration and optionally display results
def search_by_duration(data, min_duration):
    results = [row for row in data if float(row.get('duration (seconds)', 0)) >= min_duration]
    return results

# ---End of duration functions 

# Shape-related functions ---

# Get all unique UFO shapes found in the data.
def get_all_shapes(data):
    shapes = set()
    for row in data:
        shape = row.get('shape', '').strip().lower()
        if shape:
            shapes.add(shape)
    return sorted(list(shapes))

# Count sightings of a specific UFO shape (case-insensitive).
def count_by_shape(data, shape):
    return sum(1 for row in data if row.get('shape', '').strip().lower() == shape.lower())

# Get the top N most frequently sighted UFO shapes and their counts.
def get_top_shapes(data, n):
    return count_shapes(data).most_common(n)

# Search sightings by shape
def search_by_shape(data, shape):
    return [row for row in data if row.get('shape', '').strip().lower() == shape.lower()]

# Count the occurrences of each UFO shape.
def count_shapes(data):
    shapes = [row.get('shape', '').strip().lower() for row in data if row.get('shape')]
    return Counter(shapes)


# --- End of Shape-related functions 

# Region-related functions ---

# Get all unique values for a specified region type (city/state/country).
def get_region_values(data, region):
    region_data = set()
    for row in data:
        value = row.get(region, '').strip().lower()
        if value:
            region_data.add(value)
    return sorted(list(region_data))

# Count sightings in a specific region (city/state/country) with a given value (case-insensitive).
def count_by_region(data, region, value):
    return sum(1 for row in data if row.get(region, '').strip().lower() == value.lower())

# Search by region value
def search_by_region(data, region, value):
    return [row for row in data if row.get(region, '').strip().lower() == value.lower()]

# Get the top N most frequent sighting regions for a given region type.
def get_top_regions(data, n, region_type):
    regions = [row.get(region_type, '').strip().lower() for row in data if row.get(region_type)]
    return Counter(regions).most_common(n)

# --- End of Region-related functions 


# Extra Functions ---

# Count the total number of sightings in the loaded data.
def sighting_count(data):
    return len(data)

# Display a list of sighting records in a pretty JSON format.
def display_sightings(results, label=""):
    if not results:
        print(f"No sightings found for {label}.")
        return
    print(f"\n--- Sightings {label} ---")
    print(json.dumps(results, indent=4))

# --- End of Extra Functions 

# Main function to run the UFO Sightings Analyzer
def main():
    data = load_data("data/ufo_sightings.csv")

    if not data:
        print("Exiting program.")
        print("\nThanks for exploring the unknown with UFO Sightings Analyzer.")
        print("🛸 Stay curious, earthling. Goodbye!\n")
        return

    while True:
        print("\n--- UFO Sightings Analyzer ---\n")
        print("1. View Top N Durations")
        print("2. Count Sightings by Duration")
        print("3. View Top N Shapes")
        print("4. Count Sightings by Shape")
        print("5. View Top N Regions")
        print("6. Count Sightings by Region")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            # View Top N Durations: Prompts for N and displays the top N durations.
            try:
                number_of_durations = int(input("\nHow many top durations you want to see: "))
                top_durations_data = get_top_durations(data, number_of_durations)
                print(f"\nTop {number_of_durations} UFO Durations (seconds):")
                for duration, count in top_durations_data:
                    print(f"{duration}: {count} sightings")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            # Count Sightings by Duration: Prompts for a minimum duration and displays the count.
            try:
                min_duration = float(input("Enter minimum duration in seconds: "))
                count = count_by_duration(data, min_duration)
                print(f"\nFound {count} sightings longer than {min_duration} seconds.")
                if count > 0:
                    show_results = input("Do you want to see the results? (yes/no): ").strip().lower()
                    if show_results == "yes":
                        results = search_by_duration(data, min_duration)
                        display_sightings(results, f"longer than {min_duration} seconds")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            # View Top N Shapes: Prompts for N and displays the top N shapes.
            try:
                number_of_shapes = int(input("\nHow many top shapes you want to see: "))
                top_shapes_data = get_top_shapes(data, number_of_shapes)
                print(f"\nTop {number_of_shapes} UFO Shapes:")
                for shape, count in top_shapes_data:
                    print(f"{shape}: {count}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            # Count Sightings by Shape: Prompts for a shape and displays the count (with option to see results).
            print("\n--- Search by Shape ---")
            show_shapes = input("Do you want to see the list of unique shapes? (yes/no): ").strip().lower()
            if show_shapes == "yes":
                print("")
                shapes = get_all_shapes(data)
                if shapes:
                    print("Available shapes:", ", ".join(shapes))
                else:
                    print("No shapes found in the data.")
                print("")
            shape = input("Enter shape to search for: ").strip().lower()
            count = count_by_shape(data, shape)
            print(f"\nFound {count} sightings with shape '{shape}'.")
            if count > 0:
                show_results = input("Do you want to see the results? (yes/no): ").strip().lower()
                if show_results == "yes":
                    display_sightings(search_by_shape(data, shape), f"shape '{shape}'")
        elif choice == "5":
            # View Top N Regions: Prompts for region type and N, then displays the top N regions.
            region_type = input("Enter region type (city/state/country) to view top values: ").strip().lower()
            if region_type not in ["city", "state", "country"]:
                print("Invalid region type. Please enter 'city', 'state', or 'country'.")
                continue
            try:
                number_of_regions = int(input(f"\nHow many top {region_type} values you want to see: "))
                top_regions_data = get_top_regions(data, number_of_regions, region_type)
                print(f"\nTop {number_of_regions} Sighted {region_type.capitalize()}:")
                for region, count in top_regions_data:
                    print(f"{region}: {count} sightings")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            # Count Sightings by Region: Prompts for region type and value, then displays the count (with option to see results).
            print("\n--- Count Sightings by Region ---")
            region = input("Enter region type (city/state/country): ").strip().lower()
            if region not in ["city", "state", "country"]:
                print("Invalid region type. Please enter 'city', 'state', or 'country'.")
                continue
            show_regions = input(f"Do you want to see the list of unique {region} values before searching? (yes/no): ").strip().lower()
            if show_regions == "yes":
                region_values = get_region_values(data, region)
                if region_values:
                    print(f"Available {region} values:", ", ".join(region_values))
                else:
                    print(f"No {region} values found in the data.")
            value = input(f"\nEnter the {region} to search for: ").strip().lower()
            count = count_by_region(data, region, value)
            print(f"\nFound {count} sightings in {region} '{value}'.")
            if count > 0:
                show_results = input("Do you want to see the results? (yes/no): ").strip().lower()
                if show_results == "yes":
                    display_sightings(search_by_region(data, region, value), f"in {region} '{value}'")
        elif choice == "7":
            # Exit the program.
            print("\nThanks for exploring the unknown with UFO Sightings Analyzer.")
            print("🛸 Stay curious, earthling. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()