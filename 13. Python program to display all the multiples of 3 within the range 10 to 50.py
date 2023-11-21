start = 10
end = 50

multiples_of_3 = [num for num in range(start, end + 1) if num % 3 == 0]
print(f"The multiples of 3 in the range {start} to {end} are: {multiples_of_3}")