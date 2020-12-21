from urllib.request import urlopen

page = urlopen("https://hari0077.github.io/hariharansrinivasan/")

sourcecode = page.read()

print(sourcecode)

