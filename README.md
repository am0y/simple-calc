# Simple Calculator CLI

A simple command-line calculator application written in Python.

## Usage

```
python cli.py <operation> [arguments]
python cli.py interactive  # Starts interactive mode
```

## Operations

### Basic Operations
- `add <num1> <num2>` - Add two numbers
- `subtract <num1> <num2>` - Subtract num2 from num1
- `multiply <num1> <num2>` - Multiply two numbers
- `divide <num1> <num2>` - Divide num1 by num2
- `power <base> <exponent>` - Raise base to the power of exponent
- `sqrt <num>` - Calculate the square root of a number

### Memory Operations
- `ms <num>` - Memory store: Store a number in memory
- `mr` - Memory recall: Recall the number from memory
- `mc` - Memory clear: Clear the memory
- `m+ <num>` - Memory add: Add a number to memory

## Examples

```bash
# Basic operations
python cli.py add 5 3        # Result: 8.0
python cli.py subtract 10 4   # Result: 6.0
python cli.py multiply 3 4    # Result: 12.0
python cli.py divide 10 2     # Result: 5.0
python cli.py power 2 3       # Result: 8.0
python cli.py sqrt 9          # Result: 3.0

# Memory operations
python cli.py ms 10           # Result: 10.0 (stored in memory)
python cli.py mr              # Result: 10.0 (recalled from memory)
python cli.py m+ 5            # Result: 15.0 (adds 5 to memory)
python cli.py mc              # Result: 0.0 (clears memory)
```

## Interactive Mode

Start the calculator in interactive mode:

```bash
python cli.py interactive
```

In interactive mode, you can:
- Enter operations directly without the `python cli.py` prefix
- Use `ans` to refer to the previous result
- Type `help` to see all available commands
- Type `exit` or `quit` to exit

Example interactive session:
```
> add 5 10
Result: 15.0
> multiply ans 2
Result: 30.0
> sqrt ans
Result: 5.477225575051661
> ms ans
Result: 5.477225575051661
> mr
Result: 5.477225575051661
> exit
```

## Features

- Basic arithmetic operations
- Advanced operations (power, square root)
- Memory functions (store, recall, clear, add)
- Interactive mode with command history
- Error handling for invalid operations
- User-friendly command-line interface