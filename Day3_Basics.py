# Below code is basic code for Variables and data types in Python

integer_variable = 10
float_variable = 10.5
name = "John Doe"
Boolean_variable = True

print("Integer Variable:", integer_variable)
print("Float Variable:", float_variable)    
print("String Variable:", name)
print("Boolean Variable:", Boolean_variable)

print(name +" "+ "is learning Python programming language and today is his third day of learning it and my grade is {integer_variable} and my percentage is {float_variable} and my status is {Boolean_variable}".format(integer_variable=integer_variable, float_variable=float_variable, Boolean_variable=Boolean_variable))

text = "Python Programming language"
print("The length of the text is:", len(text))
print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(text.startswith("Python"))
print(text.endswith("Nothing"))
print(text.title())