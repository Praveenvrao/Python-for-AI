import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

print("Hello, World! - This is my first program in Python")
print("I am learning Python programming language and today is my Second day of learning it.")