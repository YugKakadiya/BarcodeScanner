def lookup_table(item_id):
    lookup_data = {
        10001: ["Grocery", 0.99, "Gala Apple"],
        10002: ["Grocery", 2.49, "Whole Milk 1L"],
        10003: ["Grocery", 3.10, "Sourdough Bread"],
        10004: ["Grocery", 4.50, "Dozen Large Eggs"],
        10005: ["Grocery", 5.25, "Cheddar Cheese Block"],
        10006: ["Grocery", 8.99, "Ground Coffee 500g"],
        10007: ["Grocery", 4.20, "Green Tea Bags (50ct)"],
        10008: ["Grocery", 1.50, "Spaghetti 500g"],
        10009: ["Grocery", 2.20, "White Rice 1kg"],
        10010: ["Grocery", 7.50, "Chicken Breast 500g"],
        20001: ["Electronics", 25.00, "Wireless Mouse"],
        20002: ["Electronics", 45.00, "Mechanical Keyboard"],
        20003: ["Electronics", 150.00, "24-inch Monitor"],
        20004: ["Electronics", 8.50, "HDMI Cable 2m"],
        20005: ["Electronics", 15.00, "USB-C Fast Charger"],
        20006: ["Electronics", 60.00, "Bluetooth Headphones"],
        20007: ["Electronics", 12.00, "32GB Flash Drive"],
        20008: ["Electronics", 35.00, "1080p Webcam"],
        20009: ["Electronics", 5.00, "AA Batteries (4-pack)"],
        20010: ["Electronics", 80.00, "Wi-Fi Router"],
        30001: ["Stationery", 1.50, "Black Ballpoint Pen"],
        30002: ["Stationery", 0.50, "HB Pencil"],
        30003: ["Stationery", 3.00, "A5 Spiral Notebook"],
        30004: ["Stationery", 1.00, "Rubber Eraser"],
        30005: ["Stationery", 2.00, "30cm Plastic Ruler"],
        30006: ["Stationery", 4.50, "Highlighter Pack (4 colors)"],
        30007: ["Stationery", 6.00, "Standard Stapler"],
        30008: ["Stationery", 5.50, "A4 Printer Paper (500 sheets)"],
        30009: ["Stationery", 2.50, "Glue Stick"],
        30010: ["Stationery", 4.00, "Stainless Steel Scissors"],
        40001: ["Clothing", 15.00, "Cotton T-Shirt (White)"],
        40002: ["Clothing", 40.00, "Blue Denim Jeans"],
        40003: ["Clothing", 10.00, "Ankle Socks (3-pack)"],
        40004: ["Clothing", 12.00, "Baseball Cap"],
        40005: ["Clothing", 18.00, "Winter Knit Gloves"],
        40006: ["Clothing", 75.00, "Waterproof Jacket"],
        40007: ["Clothing", 60.00, "Running Shoes"],
        40008: ["Clothing", 25.00, "Leather Belt"],
        40009: ["Clothing", 14.00, "Wool Scarf"],
        40010: ["Clothing", 20.00, "Polarized Sunglasses"]
    }

    key = int(float(item_id))
    return lookup_data[key][2]


lookup_table()
