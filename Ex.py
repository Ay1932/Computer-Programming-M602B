# validating email address
import re

def is_valid_email(email):
   
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Match the email with the regex
    if re.match(email_regex, email):
        return True
    else:
        return False

# Example usage:
email_to_test = "example@example.com"
result = is_valid_email(email_to_test)
print(f"Is the email '{email_to_test}' valid? {result}")  # Output: True

# Testing with an invalid email
invalid_email = "example@.com"
result = is_valid_email(invalid_email)
print(f"Is the email '{invalid_email}' valid? {result}")  # Output: False


# Extracting phone number

def extract_phone_numbers(input_string):
    
    phone_number_regex = r'\b\d{3}-\d{3}-\d{4}\b'
    
    phone_numbers = re.findall(phone_number_regex, input_string)
    
    return phone_numbers

# Example usage:
input_text = "You can reach me at 123-456-7890 or 987-654-3210. My office number is 555-123-4567."
extracted_numbers = extract_phone_numbers(input_text)
print("Extracted phone numbers:", extracted_numbers)

# validate urls

def is_valid_url(url):
    url_regex = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(/[^\s]*)?$'
    
    if re.match(url_regex, url):
        return True
    else:
        return False

# Example usage:
urls_to_test = [
    "http://example.com",
    "https://www.example.com",
    "www.example.com",
    "example.com",
    "ftp://example.com",  # Invalid
    "http://example",      # Invalid
    "http://example.com/path/to/resource",
    "https://example.com:8080/path/to/resource?query=param#fragment"
]

for url in urls_to_test:
    result = is_valid_url(url)
    print(f"Is the URL '{url}' valid? {result}")