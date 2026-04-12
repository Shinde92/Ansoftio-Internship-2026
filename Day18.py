try:
    # Take input from user
        num1 = int(input("Enter first number: "))
	    num2 = int(input("Enter second number: "))

	        # Perform division
		    result = num1 / num2

		        # Display result
			    print("Result:", result)

			    # Handle division by zero
			    except ZeroDivisionError:
			        print("Error: Cannot divide by zero!")

				# Handle invalid input
				except ValueError:
				    print("Error: Please enter valid numbers!")

				    # Handle any other unexpected error
				    except Exception as e:
				        print("Something went wrong:", e)
