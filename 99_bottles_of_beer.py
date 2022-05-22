# bottle_count = 99

# while bottle_count > 0:
#     print(f"{bottle_count} bottles of beer on the wall")
#     print(f"{bottle_count} bottles of beer.")
#     bottle_count -= 1
#     if bottle_count == 0:
#         print("Take one down, pass it around, no more bottles of beer on the wall")
#         break
#     print(f"Take one down, pass it around, {bottle_count} bottles of beer on the wall")
#     print("**************************************")

for bottle in range(99, -1, -1):
    print(f"{bottle} bottles of beer on the wall")
    print(f"{bottle} bottles of beer.")
    bottle -= 1
    if bottle == 0:
        print("Take one down, pass it around, no more bottles of beer on the wall")
        break
    print(f"Take one down, pass it around, {bottle} bottles of beer on the wall")
    print("**************************************")