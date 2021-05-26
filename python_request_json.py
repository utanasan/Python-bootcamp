import requests
from random import choice
import pyfiglet
from termcolor import colored

res = requests.get("https://news.ycombinator.com/")
print(res)
print(res.ok)
print(res.headers)
print(res.text)



url="http://www.google.com"
response = requests.get(url)
print(f"your request to {url} came back w/ status code {response.status_code}")


ur = "https://icanhazdadjoke.com/"

rsp = requests.get(ur, headers={"Accept":"application/json"})

print(rsp.text)
print(rsp.json())


header = pyfiglet.figlet_format("DAD JOKE 2021!")
header = colored(header, color="magenta")
print(header)

user_input=input("What would you like to search for? ")
u="https://icanhazdadjoke.com/search"
r=requests.get(
    u,
    headers={"Accept":"application/json"},
    params={"term":user_input}
).json()
num_jokes = r["total_jokes"]
results = r["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} about {user_input}. Here's one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}")
    print(results[0]["joke"])

else:
    print(f"Sorry, couldn't find a joke with {user_input}")




