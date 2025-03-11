#!/usr/bin/env python3

import sys
import re
import calculator

def print_usage():
    print("\nSimple Calculator CLI")
    print("\nUsage:")
    print("  python cli.py <operation> [arguments]")
    print("  python cli.py interactive  (starts interactive mode)")
    print("\nAvailable Operations:")
    print("  add <num1> <num2>         - Add two numbers")
    print("  subtract <num1> <num2>    - Subtract num2 from num1")
    print("  multiply <num1> <num2>    - Multiply two numbers")
    print("  divide <num1> <num2>      - Divide num1 by num2")
    print("  power <base> <exponent>   - Raise base to the power of exponent")
    print("  sqrt <num>                - Calculate the square root of a number")
    print("\nMemory Operations:")
    print("  ms <num>       - Memory store: Store a number in memory")
    print("  mr             - Memory recall: Recall the number from memory")
    print("  mc             - Memory clear: Clear the memory")
    print("  m+ <num>       - Memory add: Add a number to memory")
    sys.exit(1)

def handle_operation(operation, args):
    try:
        if operation == "add":
            if len(args) != 2:
                raise ValueError("Add operation requires exactly 2 numbers")
            return calculator.add(float(args[0]), float(args[1]))
        
        elif operation == "subtract":
            if len(args) != 2:
                raise ValueError("Subtract operation requires exactly 2 numbers")
            return calculator.subtract(float(args[0]), float(args[1]))
        
        elif operation == "multiply":
            if len(args) != 2:
                raise ValueError("Multiply operation requires exactly 2 numbers")
            return calculator.multiply(float(args[0]), float(args[1]))
        
        elif operation == "divide":
            if len(args) != 2:
                raise ValueError("Divide operation requires exactly 2 numbers")
            return calculator.divide(float(args[0]), float(args[1]))
        
        elif operation == "power":
            if len(args) != 2:
                raise ValueError("Power operation requires exactly 2 numbers")
            return calculator.power(float(args[0]), float(args[1]))
        
        elif operation == "sqrt":
            if len(args) != 1:
                raise ValueError("Square root operation requires exactly 1 number")
            return calculator.square_root(float(args[0]))
        
        elif operation == "ms":
            if len(args) != 1:
                raise ValueError("Memory store operation requires exactly 1 number")
            return calculator.memory_store(float(args[0]))
        
        elif operation == "mr":
            if len(args) != 0:
                raise ValueError("Memory recall operation doesn't take any arguments")
            return calculator.memory_recall()
        
        elif operation == "mc":
            if len(args) != 0:
                raise ValueError("Memory clear operation doesn't take any arguments")
            return calculator.memory_clear()
        
        elif operation == "m+":
            if len(args) != 1:
                raise ValueError("Memory add operation requires exactly 1 number")
            return calculator.memory_add(float(args[0]))
        
        else:
            raise ValueError(f"Unknown operation '{operation}'")
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

def interactive_mode():
    print("Interactive Calculator Mode (type 'help' for commands, 'exit' to quit)")
    last_result = 0
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                break
            
            if user_input.lower() == 'help':
                print_usage()
                continue
            
            # Replace 'ans' with the last result
            user_input = user_input.replace('ans', str(last_result))
            
            # Parse the input
            tokens = re.findall(r'[\w.+-]+', user_input)
            if not tokens:
                continue
            
            operation = tokens[0].lower()
            args = tokens[1:]
            
            result = handle_operation(operation, args)
            if result is not None:
                print(f"Result: {result}")
                last_result = result
        
        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print_usage()
    
    operation = sys.argv[1].lower()
    
    if operation == "help":
        print_usage()
    
    if operation == "interactive":
        interactive_mode()
        return
    
    result = handle_operation(operation, sys.argv[2:])
    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()