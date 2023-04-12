

raw_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

rd_sum, rd_count, rd_max, rd_min = sum(raw_data), len(raw_data), max(raw_data), min(raw_data)
rd_any7, rd_all7 = any(i%7 == 0 for i in raw_data), all(i%7 == 0 for i in raw_data)
rd_avg = rd_sum / rd_count

print(f'{rd_sum=}\n{rd_count=}\n{rd_avg=}\n{rd_max=}\n{rd_min=}\n{rd_any7=}\n{rd_all7=}')
