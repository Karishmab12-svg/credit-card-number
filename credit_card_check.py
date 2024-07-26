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

# Main function to read input and validate credit card numbers
def main():
    try:
        n = int(input("Enter the number of credit card numbers to validate: "))
        if not 0 < n < 100:
            raise ValueError("Number of credit cards must be between 1 and 99.")
        
        credit_card_numbers = [input(f"Enter credit card number {i+1}: ").strip() for i in range(n)]

        # Validate each credit card number and print the result
        for card_number in credit_card_numbers:
            if is_valid_credit_card(card_number):
                print("Valid")
            else:
                print("Invalid")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()

# Test cases
def test_validate_credit_cards():
    assert is_valid_credit_card("4123456789123456") == True
    assert is_valid_credit_card("5123-4567-8912-3456") == True
    assert is_valid_credit_card("61234-567-8912-3456") == False
    assert is_valid_credit_card("4123356789123456") == True
    assert is_valid_credit_card("5133-3367-8912-3456") == False
    assert is_valid_credit_card("5123 - 3567 - 8912 - 3456") == False
    assert is_valid_credit_card("4444444444444444") == False
    assert is_valid_credit_card("412345678912345") == False
# Test cases
test_validate_credit_cards()
