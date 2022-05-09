import csv, sys

def fetch_data():
    # Returning some example data - hit a JSON API or something here
    return [{
        "name": "Name 1",
        "age": 32,
        "description": "Look, we can use commas and\ttabs & stuff in here!",
    }, {
        "name": "Name 2",
        "age": 28,
        "description": "More of the same...",
    }]

def make_csv_rows(dicts, keys):
    rows = []
    rows.append(keys)
    for item in dicts:
        rows.append([item[key] for key in keys])
    return rows
 
if __name__ == '__main__':
    dicts = fetch_data()
    rows = make_csv_rows(dicts, ('name', 'age', 'description'))
    # output csv to stdout
    w = csv.writer(sys.stdout, csv.excel_tab)
    w.writerows(rows)