import pyshorteners

url = input("Please enter a url to shorten.\n")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print(f"Here is your shortened url: {short_url}")