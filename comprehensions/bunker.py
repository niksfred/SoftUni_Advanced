categories = {x:[] for x in input().split(", ")}

lines = int(input())
for _ in range(lines):
    category, item, item_desc = input().split(" - ")
    quantity_pair, quality_pair = item_desc.split(";")
    quality = quality_pair.split(":")
    quantity = quantity_pair.split(":")
    package = {item:{"quantity":int(quantity[1]), "quality":int(quality[1])}}

    categories[category].append(package)

items_count = 0
quality_sum = 0
for key in categories:
    for items in categories[key]:
        for key in items:
            items_count += items[key]["quantity"]

for key in categories:
    for items in categories[key]:
        for key in items:
            quality_sum += items[key]["quality"]

average_quality = quality_sum / len(categories)

print(f"Count of items: {items_count}")
print(f"Average quality: {average_quality:.2f}")
for category in categories:
    items_in_category = [names for dict in categories[category] for names in dict]
    print(category,"->",", ".join(items_in_category))

print(categories)
