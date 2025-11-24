"""
Simple command-line calculator with basic operations and a history feature.
"""

class Math:
    """
    Perform basic mathematical calculations such as addition,
    subtraction, multiplication, division, power, and percentage.
    """
    
    def add(self, a, b):
        """
        It adds two numbers together.
        
        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The sum of a and b.

        """
        return a + b


    def subtract(self, a, b):
        """
        It subtracts two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The result of subtracting a and b.

        """
        return a - b


    def multiply(self, a, b):
        """
        multiplies two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The result of multiplying a and b.

        """
        return a * b


    def divide(self, a, b):
        """
        It divides two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float or None
            The result of dividing a and b.

        """
        
        # Checking for division by zero to prevent the program from crashing.
        if b == 0:
            # TODO: Handle division by zero more gracefully.
            print('Division by zero is not allowed.')
        else:
            return a / b


    def power(self, a, b):
        """
        Calculates a to the power of b.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The result of calculating the number a to the power of the number b.

        """
        return a ** b


    def percent(self, a, b):
        """
        Calculates a percent of b.

        Parameters
        ----------
        a : float
            The first number as a percentage
        b : float
            The second number as the number from which the percentage should be calculated.

        Returns
        -------
        float
            The result of calculating the percentage of number b.

        """
        return (a / 100) * b

    
class History:
    """
    This class is responsible for maintaining and storing the results of computations.
    """
    def __init__(self, limit = 10):
        """
        Initialize the history with a maximum number of stored items.

        Parameters
        ----------
        limit : int
            The default is 10.

        Returns
        -------
        None.

        """
        self.limit = limit
        # TODO: Consider making this attribute private to prevent external modification.
        self.items = []
        
        
    def add(self, value):
        """
        Adds the result of the calculations to the list.

        Parameters
        ----------
        value : float
            The result of the calculations.

        Returns
        -------
        None.

        """
        self.items.append(value)
        # If the list exceeds the limit, remove the oldest item (FIFO).
        if len(self.items) > self.limit:
            self.items.pop(0)
                
    def lists(self):
        """
        Show the self.items list.

        Returns
        -------
        list
            Calculated values.

        """
        return self.items   
    
def exit_cal():
    """
    Print an exit message and return False to stop the main loop.
    """
    print("Exit. Goodbye!")
    return False
    


# ----------------------------------------------------------------------
# MAIN PROGRAM EXECUTION BLOCK
# ----------------------------------------------------------------------

math_cal = Math()
history_cal = History()
start_program = True
# Main loop
while start_program:
    # The menu
    print("\n🔢Simple calculator🔢")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Power (a ** b)")
    print("6) Percentage (a % of b)")
    print("7) Show history")
    print("8) Exit")
    
    # User menu selection
    choice_number = int(input("Select the desired number from the menu:"))
    
    # Menu routing
    if choice_number == 1:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.add(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 2:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.subtract(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 3:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.multiply(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 4:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.divide(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 5:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.power(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 6:
        first_number = int(input("Enter the first number:"))        
        second_number = int(input("Enter the second number:"))
        result = math_cal.percent(first_number, second_number)
        print(f"Result = {result} 🧮")
        history_cal.add(result)
        
    elif choice_number == 7:
        list_items = history_cal.lists()
        # Check if the history list is empty
        if not list_items:
            print("The history is empty! ❌")
        else:
            print(history_cal.lists())
        
    elif choice_number == 8:
        # Stop loop
        start_program = exit_cal()
        
    else:
        print("Invalid selection. Please enter a number between 1 and 8.")
        