import re
# Function to validate a single credit card number
def is_valid_credit_card(card_number):
    # Regex pattern to match the credit card number requirements
    pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    # Check if the card number matches the basic pattern
    if not re.match(pattern, card_number):
        return False
    # Remove hyphens for further validation
    card_number = card_number.replace('-', '')
    # Check if the card number has 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_number):
        return False
    return True

# Read input
n = int(input())
credit_card_numbers = [input().strip() for _ in range(n)]
# Validate each credit card number and print the result
for card_number in credit_card_numbers: # For each input validate the number
    if is_valid_credit_card(card_number):
        print("Valid")
    else:
        print("Invalid")
