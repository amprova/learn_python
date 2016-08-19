#You will need to write a format string which prints out the data using the following syntax:
## Hello John Doe. Your current balance is 53.44$.

data = ("John", "Doe", 53.44)
format_string = "Hello"
data1 = format_string + " "+ data[0] + " " + data[1]

print ("%s. Your current balance is %.2f$." %(data1, data[2]))