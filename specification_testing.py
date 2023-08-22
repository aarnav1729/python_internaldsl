# Description: A simple testing framework that implements the Specification Testing approach

#Define the Expectation class
class Expectation:
    def __init__(self, value):
        #Initialize an instance of the Expectation with a value
        self.value = value

    def to(self, condition):
        # Check if the condition is met
        if not condition(self.value):
            # Raise an AssertionError if the condition is not met
            raise AssertionError(f"Expected {self.value} to {condition.__name__}, but it didn't.")

#Define the SpecificationTestFramework class
class SpecificationTestFramework:
    def __init__(self):

        #Initialize counters to keep track of the number of tests passed and failed
        self.passed = 0
        self.failed = 0

    def run(self, test_subject):
        # Iterate through the test cases and run them
        for name, test_case in test_subject.items():
            try:
                test_case()
                #If the test case passes, increment the passed counter
                self.passed += 1
                print(f"Test '{name}' PASSED")

            except AssertionError as e:
                #If the test case fails/raises an AssertionError, increment the failed counter
                self.failed += 1
                print(f"Test '{name}' FAILED: {e}")

        # Print the test results
        print(f"Total tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")

#Define the main function       
if __name__ == "__main__":

    # Define test cases for core data and functionality
    def test_addition():

        # Test addition of two numbers
        Expectation(2 + 2).to(lambda x: x == 4)

    def test_string_length():

        # Test length of a string
        Expectation(len("Hello, World!")).to(lambda x: x == 13)


    # Define test cases for user-defined classes, functions, and modules
    def test_user_defined_function():

        # Implement a user-defined function and test it
        def square(x):
            return x ** 2

        # Test the square function
        Expectation(square(5)).to(lambda x: x == 25)

    def test_user_defined_class():
        
        # Implement a simple user-defined class and test it
        class MyClass:

            # Define a constructor
            def __init__(self, value):
                self.value = value

            # Define a method
            def get_value(self):
                return self.value

        instance = MyClass(42)
        
        # Test the constructor
        Expectation(instance.get_value()).to(lambda x: x == 42)

    # Test control flow - if statement
    def test_if_statement():
        value = 10
        if value > 5:
            Expectation(value).to(lambda x: x > 5)

    # Test loops - for loop
    def test_for_loop():
        total = 0
        for i in range(1, 6):
            total += i
        Expectation(total).to(lambda x: x == 15)

    # Test lists - basic data structure
    def test_list_operations():
        my_list = [1, 2, 3, 4, 5]

        # Test list length
        Expectation(len(my_list)).to(lambda x: x == 5)

        # Test list element access
        Expectation(my_list[2]).to(lambda x: x == 3)

        # Test list modification
        my_list.append(6)
        Expectation(my_list[-1]).to(lambda x: x == 6)

    # Test dictionaries - another data structure
    def test_dictionary_operations():
        my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
        # Test dictionary length
        Expectation(len(my_dict)).to(lambda x: x == 3)

        # Test dictionary element access
        Expectation(my_dict['banana']).to(lambda x: x == 2)

        # Test dictionary modification
        my_dict['date'] = 1
        Expectation(my_dict['date']).to(lambda x: x == 1)

    # Test exception handling
    def test_exception_handling():
        def divide(x, y):
            try:
                result = x / y
                return result
            except ZeroDivisionError:
                return "Cannot divide by zero"
        
        Expectation(divide(10, 2)).to(lambda x: x == 5)
        Expectation(divide(5, 0)).to(lambda x: x == "Cannot divide by zero")

    # Test object-oriented concepts
    class Animal:
        def __init__(self, name):
            self.name = name

    class Dog(Animal):
        def bark(self):
            return "Woof!"

    class Cat(Animal):
        def meow(self):
            return "Meow!"

    def test_object_oriented_concepts():
        my_dog = Dog("Buddy")
        my_cat = Cat("Whiskers")

        Expectation(my_dog.name).to(lambda x: x == "Buddy")
        Expectation(my_cat.name).to(lambda x: x == "Whiskers")
        Expectation(my_dog.bark()).to(lambda x: x == "Woof!")
        Expectation(my_cat.meow()).to(lambda x: x == "Meow!")

    # Test recursion
    def test_factorial():
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        
        Expectation(factorial(5)).to(lambda x: x == 120)

    # Step 5: Develop the Testing Framework
    test_subject = {
        # Core data and functionality
        "Addition Test": test_addition,

        # User-defined classes, functions, and modules
        "String Length Test": test_string_length,
        "User-Defined Function Test": test_user_defined_function,
        "User-Defined Class Test": test_user_defined_class,

        # Control flow, loops, and data structures
        "Control Flow Test": test_if_statement,
        "For Loop Test": test_for_loop,
        "List Operations Test": test_list_operations,
        "Dictionary Operations Test": test_dictionary_operations,

        # Exception handling
        "Exception Handling Test": test_exception_handling,

        # Object-oriented concepts
        "Object-Oriented Concepts Test": test_object_oriented_concepts,

        # Recursion
        "Factorial Test": test_factorial,
    }

    # Step 6: Run the Testing Framework
    test_framework = SpecificationTestFramework()
    test_framework.run(test_subject)