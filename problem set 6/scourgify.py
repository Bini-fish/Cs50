import sys
import csv

def main():
    scourgify()

def scourgify():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        pass
    
    path = sys.argv[1]
    path2 = sys.argv[2]
    if ".csv" not in path:
        sys.exit("Not a CSV file")
    
    try:
        input = open(path, "r") 
        output = open(path2, "w")       
    except FileNotFoundError:
        sys.exit(f"Could not read {path}")

    column_data = csv.DictReader(input, delimiter=",")
    writer = csv.DictWriter(output, ["first", "last", "house"])

    writer.writeheader()
    for row in column_data:
        last, first = row["name"].split(",")
        writer.writerow({
            "first": first.strip(), 
            "last": last, 
            "house": row["house"]
        })
if __name__ == "__main__":
    main()