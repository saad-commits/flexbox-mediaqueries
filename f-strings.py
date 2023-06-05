#after python 3.6 versions available 
# use for string formatting 
country="India"
name="Saad"
letter="Hey my name is {0} and i am from {1}"
print(letter.format(name,country))
print(letter.format(country,name))

#f-strings
print(f"Hey my name is {name} and i am from {country}")


txt="For only {price:.2f} dollars!"
print(txt.format(price=49.000005555))

# ab ye hi chhez f string se 
price=500
txt =f"For only {price:.2f} rupess you will get the service "
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

# agar literalyy ye hi print karna hai to 
print(f"Hey my name is {{name}} and i am from {{country}}")


