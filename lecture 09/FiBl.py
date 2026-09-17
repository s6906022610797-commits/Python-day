try:
    numerator = float("Enter the numerator: ")
    denominator = float("Enter the denominator")

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError :
    print("Error: You cannot divide by zero.")

except ValueError :
    print("Error: Invalid input. Please enter numeric values.")

finally:
    print("Exception completed, whether an exception occurred or not.")

print("End of program")