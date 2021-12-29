page_count = int(input())
pages_per_hour = int(input())
days = int(input())

needed_hours = page_count / pages_per_hour
needed_days = needed_hours / days

print(needed_days)