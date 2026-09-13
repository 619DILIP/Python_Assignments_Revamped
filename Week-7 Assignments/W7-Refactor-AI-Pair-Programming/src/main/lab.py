import csv


def print_inventory_report():

    d = []
    with open(r"src/data/inventory.csv", encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            d.append(row)

    # figure out total value per category, the slow way
    cats = []
    for row in d:
        c = row["Category"]
        found = False
        for existing in cats:
            if existing == c:
                found = True
        if not found:
            cats.append(c)

    for c in cats:
        total = 0
        count = 0
        for row in d:
            if row["Category"] == c:
                q = row["Quantity"]
                p = row["UnitCost"]
                total = total + (int(q) * float(p))
                count = count + 1
        print(c + ": " + str(count) + " items, total value $" + str(round(total, 2)))

    # find the most expensive item, the slow way, again looping over everything
    most_expensive = None
    most_expensive_cost = 0
    for row in d:
        p = row["UnitCost"]
        if float(p) > most_expensive_cost:
            most_expensive_cost = float(p)
            most_expensive = row["ItemName"]
    print("Most expensive item: " + str(most_expensive) + " at $" + str(most_expensive_cost))

    # print low stock items (below 50 units) - no handling if Quantity is missing/blank
    print("\nLow stock items:")
    for row in d:
        if int(row["Quantity"]) < 50:
            print(row["ItemName"] + " - " + row["Quantity"] + " left")

    print("\n✅ Inventory Report Completed!")


if __name__ == "__main__":
    print_inventory_report()
