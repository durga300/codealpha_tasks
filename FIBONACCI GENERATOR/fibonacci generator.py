def fibonacci_generator():
    """Generator function that yields Fibonacci numbers infinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    """Recursive function to get nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

class FibonacciIterator:
    """Iterator class for Fibonacci sequence"""
    def __init__(self, max_terms):
        self.max_terms = max_terms
        self.current_term = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_term >= self.max_terms:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current_term += 1
        return result

def main():
    while True:
        print("\nFibonacci Number Generator")
        print("1. Generate first n Fibonacci numbers")
        print("2. Generate infinite Fibonacci sequence")
        print("3. Get nth Fibonacci number")
        print("4. Use Fibonacci Iterator")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            try:
                n = int(input("Enter the number of terms to generate: "))
                if n <= 0:
                    print("Please enter a positive number!")
                    continue
                    
                sequence = fibonacci_sequence(n)
                print(f"\nFirst {n} Fibonacci numbers:")
                print(sequence)
                
                # Print in a formatted way
                print("\nIndex : Value")
                print("-" * 20)
                for i, num in enumerate(sequence):
                    print(f"{i:5d} : {num:d}")
                    
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '2':
            try:
                print("\nGenerating infinite Fibonacci sequence (Ctrl+C to stop)")
                fib = fibonacci_generator()
                count = 0
                
                print("\nIndex : Value")
                print("-" * 20)
                
                while True:
                    num = next(fib)
                    print(f"{count:5d} : {num:d}")
                    count += 1
                    
                    # Add a small delay and check if user wants to continue
                    if count % 10 == 0:
                        response = input("\nGenerate more? (y/n): ").lower()
                        if response != 'y':
                            break
                            
            except KeyboardInterrupt:
                print("\nGenerator stopped by user")
                
        elif choice == '3':
            try:
                n = int(input("Enter the position (n) to find the Fibonacci number: "))
                if n < 0:
                    print("Please enter a non-negative number!")
                    continue
                    
                result = fibonacci_recursive(n)
                print(f"\nThe Fibonacci number at position {n} is: {result}")
                
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '4':
            try:
                n = int(input("Enter the number of terms for iteration: "))
                if n <= 0:
                    print("Please enter a positive number!")
                    continue
                    
                fib_iterator = FibonacciIterator(n)
                print(f"\nFirst {n} Fibonacci numbers using iterator:")
                print("\nIndex : Value")
                print("-" * 20)
                
                for i, num in enumerate(fib_iterator):
                    print(f"{i:5d} : {num:d}")
                    
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '5':
            print("\nThank you for using the Fibonacci Generator!")
            break
            
        else:
            print("Invalid choice! Please select 1-5")

if __name__ == "__main__":
    main()