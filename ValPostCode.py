# Validating Postal Code

regex_integer_in_range = r"^[1-9][\d]{5}$"	
# This regular expression pattern ensures that the postal code consist of six digits, first digits in range 1-9 and the remaining five digits cna be any digit 0-9.

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	
# Other regular expression that validates repetitive alternating digit pair.
# Captures the first digit then looks ahead what the next digit is
# Matches a digit that is inmediately followed by the same digit




