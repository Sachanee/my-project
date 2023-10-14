def sum_even_numbers(start, end):
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start > end:
    print("Invalid range: The start should be less than or equal to the end.")
else:
    result = sum_even_numbers(start, end)
    print(f"The sum of even numbers from {start} to {end} is {result}")
