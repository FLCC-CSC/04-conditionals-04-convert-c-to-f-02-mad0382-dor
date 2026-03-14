# FILE NAME - convert_C_to_F_02.py

# NAME: Melvin Dorta
# DATE: March 14th 2026
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====\n")
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius\n")

# Ask the user for the conversion choice
choice = input("Please choose from the above menu: ")

# Celsius to Fahrenheit conversion
if choice == "1":
    temp_c = float(input("Enter a temperature to convert: "))
    temp_f = temp_c * 9/5 + 32
    print(f"\n{temp_c} degrees Celsius is {temp_f} degrees Fahrenheit.")

# Fahrenheit to Celsius conversion
elif choice == "2":
    temp_f = float(input("Enter a temperature to convert: "))
    temp_c = (temp_f - 32) * 5/9
    print(f"\n{temp_f} degrees Fahrenheit is {temp_c} degrees Celsius.")

# Handle invalid choices
else:
    print("\nInvalid choice. Please run the program again and select 1 or 2.")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?







'''
