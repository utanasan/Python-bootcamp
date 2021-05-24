"""Given the provided dictionary of donations:
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
Use a loop to calculate the total value of the donations.  Save the result to a variable called total_donations"""

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donation=0
for value in donations.values():
	total_donation+=value
print(total_donation)

#total_donations = sum(value for value in donations.values())

#total_donations = sum(donations.values())
