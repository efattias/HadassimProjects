from openpyxl import load_workbook
from datetime import datetime

valid_data = []
seen_rows = set()

def time_average(path):
    wb = load_workbook(path)
    ws = wb.active
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        timestamp = str(row[0]).strip()
        value = str(row[1]).strip()

        if not is_valid_timestamp(timestamp):
            continue
        if not is_valid_value(value):
            continue
        if (timestamp, value) in seen_rows:
            continue

        seen_rows.add((timestamp, value))
        valid_data.append((datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"), float(value)))
    

def is_valid_timestamp(ts):
    try:
        datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

def is_valid_value(val):
    try:
        if val.strip().lower() in ["", "nan", "not_a_number"]:
            return False
        float(val)  
        return True
    except ValueError:
        return False

def main():
    time_average(r"PartA\time_series.xlsx")

if __name__ == "__main__":
    main()