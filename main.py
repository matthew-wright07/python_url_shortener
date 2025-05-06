import pyshorteners

url = input("Please enter a url to shorten.\n")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print(short_url)