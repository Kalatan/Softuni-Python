cargo_count = int(input())
cargo_sum = 0
cargo_price = 0
bus_weight_price = 0
truck_weight_price = 0
train_weight_price = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0

for n in range(1, cargo_count + 1):
    cargo_weight = int(input())
    cargo_sum += cargo_weight
    if cargo_weight <= 3:
        bus_weight_price += cargo_weight * 200
        bus_cargo += cargo_weight
    elif 4 <= cargo_weight <= 11:
        truck_weight_price += cargo_weight * 175
        truck_cargo += cargo_weight
    elif 12 <= cargo_weight:
        train_weight_price += cargo_weight * 120
        train_cargo += cargo_weight

cargo_price = (bus_weight_price + truck_weight_price + train_weight_price) / cargo_sum
bus_cargo = (bus_cargo/cargo_sum) * 100
truck_cargo = (truck_cargo/cargo_sum) * 100
train_cargo = (train_cargo/cargo_sum) * 100

print(f"{cargo_price:.2f}")
print(f"{bus_cargo:.2f}%")
print(f"{truck_cargo:.2f}%")
print(f"{train_cargo:.2f}%")