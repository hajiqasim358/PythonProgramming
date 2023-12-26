print("Welcome To Python Programming.")
print("Hello Everyone", "I am Qasim") # this will replace the comma with a white sapace, to
                                     # print something instead of comma use the "sep" attribute
                                     # example below explains the separator
print("Hello Everyone","I am Qasim", sep="# ") # the string in double quotation will replace
                                                # the comma in output of the program.

# As we know that the above statements will be printed on separate lines because
# python by default addds \n to the end. to avoid this we can use the "end" attribute to
# change the default value as shown below.
print("Hello", end="")
print("Welcome")

# to add some white space or something else add anythng you want to display it
print("Weccome to",end=" ")
print("Programming.")