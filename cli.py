#!/usr/bin/env python3

import sys
import calculator

def print_usage():
    print("Usage: python cli.py <operation> <num1> <num2>")
    print("Operations: add, subtract, multiply, divide")
    sys.exit(1)

def main():
    if len(sys.argv) != 4:
        print_usage()
    
    operation = sys.argv[1].lower()
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Numbers must be valid numeric values")
        print_usage()
    
    if operation == "add":
        result = calculator.add(num1, num2)
    elif operation == "subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "divide":
        try:
            result = calculator.divide(num1, num2)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print(f"Error: Unknown operation '{operation}'")
        print_usage()
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()