# 👽 **UFO Sightings Analyzer**👽
Final project for **Harvard's CS50P** Introduction to Programming with Python, leveraging concepts from both CS50 and the University of Pennsylvania's Java and Python Specialization on Coursera.

## Video Demo: https://youtu.be/W96X9xUw3E8

## Description:

### 📁 About the Project

**UFO Sightings Analyzer** is a user-friendly Python command-line interface (CLI) designed to explore and analyze a rich dataset of over **80,000** reported UFO sightings primarily from the **National UFO Reporting Center (NUFORC)** from around the globe. Users can explore top UFO shapes, durations, and sighting locations (city, state, country), as well as search and count sightings based on these criteria. The project handles real-world CSV data, offering a user-friendly interface to investigate the mysteries of reported UFO encounters.


**Dive into decades of mysterious encounters and uncover patterns in the unknown.**

With **UFO Sightings Analyzer**, you can interactively:

- Discover the **top reported UFO shapes**.
- Investigate sightings based on the **shape** of the observed object.
- Explore sighting locations by **city, state, or country**.
- Examine detailed reports, including timestamps, geographical coordinates, and reported shapes.

### 🗂️ Dataset
The core of this project is the comprehensive dataset stored in: `data/ufo_sightings.csv`. 
### CSV Source Citing
Name of the dataset : ufo-reports \
Dataset creator's name : Sigmond Axel \
Year & Month of dataset creation : 2014, July \
URL of the dataset : https://github.com/planetsig/ufo-reports

---

## Dataset Column Descriptions

This table clarifies how the raw column headings from the `ufo_sightings.csv` file are mapped and interpreted within the UFO Sightings Analyzer project.

| Raw Column Heading                  | Mapped Name in Project          | Description                                                               |
|-------------------------------------|---------------------------------|---------------------------------------------------------------------------|
| `Location.City`                     | `city`                          | The city where the UFO was sighted                                        |
| `Location.State`                    | `state`                         | The US state of the sighting (if applicable)                              |
| `Location.Country`                  | `country`                       | The country where the sighting was reported                               |
| `Data.Shape`                        | `shape`                         | The reported shape of the observed UFO                                    |
| `Data.Encounter duration`           | `duration (seconds)`            | The duration of the sighting in seconds                                   |
| `Data.Description excerpt`          | `description`                   | A brief description or comments from the reporter                         |
| `Location.Coordinates.Latitude `    | `latitude`                      | The geographic latitude of the sighting location                          |
| `Location.Coordinates.Longitude `   | `longitude`                     | The geographic longitude of the sighting location                         |
| `Dates.Sighted.Year`                | Combined into `datetime`        | Year when the sighting occurred                                           |
| `Dates.Sighted.Month`               | Combined into `datetime`        | Month when the sighting occurred                                          |
| `Date.Sighted.Day`                  | Combined into `datetime`        | Day when the sighting occurred                                            |
| `Dates.Sighted.Hour`                | Combined into `datetime`        | Hour when the sighting occurred                                           |
| `Dates.Sighted.Minute`              | Combined into `datetime`        | Minute when the sighting occurred                                         |
| `Dates.Documented.Year`             | Not directly used               | Year the sighting was documented/posted (raw data column)                 |
| `Dates.Documented.Month`            | Not directly used               | Month the sighting was documented/posted (raw data column)                |
| `Dates.Documented.Day`              | Not directly used               | Day the sighting was documented/posted (raw data column)                  |



### 💻 How to Use
1. Clone the repository: 
     ```bash
   gh repo clone naveedamar/UFO-Sightings-Analyzer 
3. Ensure your dataset is located at data/ufo_sightings.csv.

4. Run the project.py
    
5. Explore the Menu: Follow the interactive on-screen menu to begin your analysis of the UFO sightings data!

### 🔍 Example Usage

When you run main.py, you'll be presented with a menu similar to this:

   \--- UFO Sightings Analyzer ---\
    1. View Top N Durations\
    2. Count Sightings by Duration\
    3. View Top N Shapes\
    4. Count Sightings by Shape\
    5. View Top N Regions\
    6. Count Sightings by Region\
    7. Exit 
   
   Enter your choice (1-7):

### 📌 Features:
 1. **Intuitive CLI:** A simple and user-friendly command-line interface for easy interaction.
 2. **Real-world Data Handling:** Efficiently processes a large CSV dataset.
 3. **Flexible Searches:** Conduct case-insensitive searches for shapes and regions.
 4. **Organized Code:** Implemented with modular and reusable Python functions for clarity and maintainability.
 5. **Comprehensive Analysis:** Offers functionalities to explore top trends and specific occurrences in the data.

## Functions Explanation:

1. **load_data(filepath):** This function is the entry point for your data. It takes a file path (like "data/ufo_sightings.csv") and reads the CSV file, converting each row into a Python dictionary. It then returns a list of these dictionaries, making the data easy to work with in the rest of the program. It also includes basic error handling if the file isn't found.

2. **count_by_duration(data, min_duration):** Ever wonder how many UFO sightings lasted longer than a minute? This function helps answer that. It takes your loaded data and a min_duration (in seconds), then counts and returns the total number of sightings that meet or exceed that specified duration.

3. **get_top_durations(data, n):** If you want to see the most common sighting lengths, this is your go-to. It analyzes the data to find the durations that appear most frequently. You tell it n (how many top durations you want), and it returns a list of the top N durations along with how many times each occurred.

4. **get_all_shapes(data):** This function helps you understand the variety of UFO shapes reported. It extracts every unique UFO shape mentioned in the dataset and returns them as a sorted list, so you can easily see what's available to search for.

5. **count_by_shape(data, shape):** Curious about how many "saucer"-shaped UFOs have been seen? This function takes the data and a specific shape (like "triangle" or "disk") and counts the total number of sightings reported with that exact shape, ignoring case for flexible searching.

6. **get_top_shapes(data, n):** Similar to get_top_durations, this function identifies the most frequently reported UFO shapes. You provide n to specify how many you want, and it returns a list of the top N shapes along with their respective counts.

7. **get_region_values(data, region):** This is useful for understanding the geographical spread of sightings. You specify a region type ('city', 'state', or 'country'), and it extracts and returns a sorted list of all unique values found for that region in the dataset.

8. **count_by_region(data, region, value):** If you want to know how many sightings occurred in a specific place, this function does the job. You give it a region type (e.g., 'city') and a value (e.g., 'phoenix'), and it counts and returns the total number of sightings reported in that specific region value.

9. **get_top_regions(data, n, region_type):** To see where UFOs are most frequently sighted, use this. You choose a region_type and specify n for how many you want, and it returns the top N most common region values (like cities, states, or countries) along with their counts.

10. **search_by_duration(data, min_duration), search_by_shape(data, shape), search_by_region(data, region, value):** These are your filtering tools. Each takes the data and specific criteria (a minimum duration, a shape, or a region/value pair) and returns a new list containing only the sighting records that match your search terms.

11. **display_sightings(results, label=""):** Once you've found some sightings, this function helps you see them clearly. It takes a list of results (sighting dictionaries) and an optional label, then prints each sighting in a neatly formatted, readable JSON style for easy review.

### 📁 File Structure:
    .
    ├── data/
    │   └── ufo_sightings.csv
    ├── main.py
    ├── test_project.py
    ├── README.md
    ├── requirenments.txt
