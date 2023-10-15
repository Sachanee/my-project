def sum_even_numbers(start, end):
    if start > end:
        return "Invalid range: The start should be less than or equal to the end."
    
    even_numbers = [number for number in range(start, end + 1) if number % 2 == 0]
    total = sum(even_numbers)
    return f"The sum of even numbers from {start} to {end} is {total}"

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_even_numbers(start, end)
print(result)
