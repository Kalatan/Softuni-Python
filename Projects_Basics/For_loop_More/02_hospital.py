days = int(input())
doctors = 7
treated = 0
untreated = 0

for n in range(1, days + 1):
    if n % 3 == 0 and n > 1 and untreated > treated:
        doctors += 1
    patients = int(input())
    if patients > doctors:
        untreated += patients - doctors
        treated += doctors
    else:
        treated += patients

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")

