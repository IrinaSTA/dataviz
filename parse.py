"""Data Visualisation Project www.newcoder.io/dataviz"""
import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""
    opened_file = open(raw_file)

    csv_data = csv.reader(opened_file, delimiter=delimiter)

    parsed_data = []

    fields = csv_data.__next__()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    opened_file.close()

    return parsed_data

def main():
    """Main"""
    new_data = parse(MY_FILE, ",")

    print(new_data)

if __name__ == "__main__":
    main()
