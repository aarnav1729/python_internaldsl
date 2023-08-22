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
    
    def test_addition():
        # Test addition of two numbers
        Expectation(2 + 2).to(lambda x: x == 4)

    def test_subtraction():
        # Test subtraction of two numbers
        Expectation(5 - 3).to(lambda x: x == 2)

    def test_multiplication():
        # Test multiplication of two numbers
        Expectation(2 * 3).to(lambda x: x == 6)

    def test_division():
        # Test division of two numbers
        Expectation(6 / 3).to(lambda x: x == 2)

    def test_modulo():
        # Test modulo of two numbers
        Expectation(5 % 2).to(lambda x: x == 1)

    def test_exponentiation():
        # Test exponentiation of two numbers
        Expectation(2 ** 3).to(lambda x: x == 8)

    def test_float_addition():
        # Test addition of two floating-point numbers
        Expectation(2.5 + 3.7).to(lambda x: x == 6.2)

    def test_float_subtraction():
        # Test subtraction of two floating-point numbers
        Expectation(5.5 - 3.3).to(lambda x: x == 2.2)

    def test_float_multiplication():
        # Test multiplication of two floating-point numbers
        Expectation(2.5 * 3.7).to(lambda x: x == 9.25)

    def test_float_division():
        # Test division of two floating-point numbers
        Expectation(6.2 / 3.1).to(lambda x: x == 2.0)

    def test_float_modulo():
        # Test modulo of two floating-point numbers
        Expectation(5.5 % 2.5).to(lambda x: x == 0.5)

    def test_float_exponentiation():
        # Test exponentiation of two floating-point numbers
        Expectation(2.0 ** 0.5).to(lambda x: x == 1.4142135623730951)

    def test_string_length():
        # Test length of a string
        Expectation(len("Hello, World!")).to(lambda x: x == 13)

    def test_list_concatenation():
        # Test list concatenation
        Expectation([1, 2] + [3, 4]).to(lambda x: x == [1, 2, 3, 4])

    def test_string_concatenation():
        s1 = "Hello"
        s2 = "World"
        # Test string concatenation
        Expectation(s1 + ", " + s2).to(lambda x: x == "Hello, World")

    def test_list_comprehension():
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = [x**2 for x in numbers]
        Expectation(squared_numbers).to(lambda x: x == [1, 4, 9, 16, 25])

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
            # Test if the value is greater than 5
            Expectation(value).to(lambda x: x > 5)

    # Test loops - for loop
    def test_for_loop():
        total = 0
        for i in range(1, 6):
            total += i
            # Test the total
        Expectation(total).to(lambda x: x == 15)

    # Test lists
    def test_list_operations():
        my_list = [1, 2, 3, 4, 5]

        # Test list length
        Expectation(len(my_list)).to(lambda x: x == 5)

        # Test list element access
        Expectation(my_list[2]).to(lambda x: x == 3)

        my_list.append(6)
        # Test list modification
        Expectation(my_list[-1]).to(lambda x: x == 6)

    # Test dictionaries
    def test_dictionary_operations():
        my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
        # Test dictionary length
        Expectation(len(my_dict)).to(lambda x: x == 3)

        # Test dictionary element access
        Expectation(my_dict['banana']).to(lambda x: x == 2)

        my_dict['date'] = 1
        # Test dictionary modification
        Expectation(my_dict['date']).to(lambda x: x == 1)

    def test_dictionary_merging():
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        # Test dictionary merging
        Expectation({**dict1, **dict2}).to(lambda x: x == {'a': 1, 'b': 3, 'c': 4})

    def test_tuple_unpacking():
        a, b = (1, 2)
        # Test tuple unpacking
        Expectation((a, b)).to(lambda x: x == (1, 2))

    def test_bool():
        # Test a boolean value
        Expectation(True).to(lambda x: x is True)

    def test_boolean_operations():
        a = True
        b = False

        # Test logical AND operation
        Expectation(a and b).to(lambda x: x is False)

        # Test logical OR operation
        Expectation(a or b).to(lambda x: x is True)

        # Test logical NOT operation
        Expectation(not b).to(lambda x: x is True)


    def test_exception_handling():
        def divide(x, y):
            try:
                result = x / y
                return result
            except ZeroDivisionError:
                return "Cannot divide by zero"
        # Test exception handling
        Expectation(divide(10, 2)).to(lambda x: x == 5)
        Expectation(divide(5, 0)).to(lambda x: x == "Cannot divide by zero")

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

        # Test object-oriented concepts
        Expectation(my_dog.name).to(lambda x: x == "Buddy")
        Expectation(my_cat.name).to(lambda x: x == "Whiskers")
        Expectation(my_dog.bark()).to(lambda x: x == "Woof!")
        Expectation(my_cat.meow()).to(lambda x: x == "Meow!")

    def test_factorial():
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        # Test factorial (recursion)      
        Expectation(factorial(5)).to(lambda x: x == 120)

    # Develop the Testing Framework
    test_subject = {
        "Addition Test": test_addition,
        "Subtraction Test": test_subtraction,
        "Multiplication Test": test_multiplication,
        "Division Test": test_division,
        "Modulo Test": test_modulo,
        "Exponentiation Test": test_exponentiation,
        "Float Addition Test": test_float_addition,
        "Float Subtraction Test": test_float_subtraction,
        "Float Multiplication Test": test_float_multiplication,
        "Float Division Test": test_float_division,
        "Float Modulo Test": test_float_modulo,
        "Float Exponentiation Test": test_float_exponentiation,
        "List Concatenation Test": test_list_concatenation,
        "List Comprehension Test": test_list_comprehension,
        "String Concatenation Test": test_string_concatenation,
        "String Length Test": test_string_length,
        "User-Defined Function Test": test_user_defined_function,
        "User-Defined Class Test": test_user_defined_class,
        "Control Flow Test": test_if_statement,
        "For Loop Test": test_for_loop,
        "List Operations Test": test_list_operations,
        "Dictionary Operations Test": test_dictionary_operations,
        "Dictionary Merging Test": test_dictionary_merging,
        "Tuple Unpacking Test": test_tuple_unpacking,
        "Exception Handling Test": test_exception_handling,
        "Object-Oriented Concepts Test": test_object_oriented_concepts,
        "Factorial Test": test_factorial,
        "Boolean Test": test_bool,
        "Boolean Operations Test": test_boolean_operations,
    }

    import test_module

    def test_user_defined_module():
        # Test a function or class from the imported module
        result = test_module.my_function()
        Expectation(result).to(lambda x: x == "Testing my_function!")

    # Add the user-defined module test to the test_subject
    test_subject["User-Defined Module Test"] = test_user_defined_module

    # Run the Testing Framework
    test_framework = SpecificationTestFramework()
    test_framework.run(test_subject)