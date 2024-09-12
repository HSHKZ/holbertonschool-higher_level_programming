def magic_calculation(a, b)::
    result = 0  # Initialize result to 0
    for i in range(1, 3):  # Loop over the range(1, 3)
        try:
            if i > a:  # Check if i is greater than a
                raise Exception('Too far')  # Raise an exception if condition is met
            result += (a ** b) / i  # Perform the calculation and update result
        except Exception:
            result = b + a  # If an exception occurs, update result to b + a
            break  # Break the loop
    return result  # Return the final result
