class Atm:
    """A simple ATM simulation class."""
    
    def __init__(self):
        """Initialize the ATM with default pin and balance."""
        self.pin = None
        self.balance = None
        print(f"ATM instance created with ID: {id(self)}")

    def menu(self):
        """Display the main menu and handle user input."""
        while True:
            user_input = input("""
                Hi, how can I help you?
                1. Create PIN
                2. Change PIN
                3. Check Balance
                4. Withdraw
                5. Exit
                Enter your choice (1-5): 
            """).strip()
            
            match user_input:
                case '1':
                    self.create_pin()
                case '2':
                    self.change_pin()
                case '3':
                    self.check_balance()
                case '4':
                    self.withdraw()
                case '5' | _: # _ is a default case in match case statments
                    print("Thank you for using our ATM. Goodbye!")
                    return

    def create_pin(self):
        """Create a new PIN and set initial balance."""
        self.pin = input("Enter your new 4-digit PIN: ")
        while not (self.pin.isdigit() and len(self.pin) == 4):
            print("PIN must be 4 digits.")
            self.pin = input("Enter a valid 4-digit PIN: ")
            
        while True:
            try:
                self.balance = float(input("Enter initial balance: "))
                if self.balance >= 0:
                    break
                print("Balance cannot be negative.")
            except ValueError:
                print("Please enter a valid number.")
        
        print("PIN created successfully!")

    def change_pin(self):
        """Change the existing PIN after verification."""
        old_pin = input("Enter your current PIN: ")
        
        if old_pin == self.pin:
            new_pin = input("Enter new 4-digit PIN: ")
            while not (new_pin.isdigit() and len(new_pin) == 4):
                print("PIN must be 4 digits.")
                new_pin = input("Enter a valid 4-digit PIN: ")
                
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN. Access denied.")

    def check_balance(self):
        """Display the current balance after PIN verification."""
        if self.verify_pin():
            print(f"Your current balance is: ${self.balance:.2f}")

    def withdraw(self):
        """Withdraw money after PIN verification."""
        if not self.verify_pin():
            return
            
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
                
            if amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Remaining balance: ${self.balance:.2f}")
        except ValueError:
            print("Please enter a valid amount.")

    def verify_pin(self):
        """Helper method to verify PIN."""
        if not self.pin:
            print("Please create a PIN first.")
            return False
            
        pin_attempt = input("Enter your PIN: ")
        if pin_attempt == self.pin:
            return True
        print("Incorrect PIN. Access denied.")
        return False


class Fraction:
    """A class to represent fractions and perform arithmetic operations."""
    
    def __init__(self, numerator, denominator):
        """Initialize fraction with numerator and denominator."""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.num = numerator
        self.den = denominator

    def __str__(self):
        """Return string representation of the fraction."""
        return f"{self.num}/{self.den}"

    def __add__(self, other: 'Fraction') -> 'Fraction': # The quotes around 'Fraction' are only needed when the type hasn't been defined yet in the current scope. This is called a "forward reference."
        """Add two fractions."""
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den).simplify()

    def __sub__(self, other):
        """Subtract two fractions."""
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den).simplify()

    def __mul__(self, other):
        """Multiply two fractions."""
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den).simplify()

    def __truediv__(self, other):
        """Divide two fractions."""
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den).simplify()

    def simplify(self):
        """Simplify the fraction to lowest terms."""
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
            
        common_divisor = gcd(abs(self.num), abs(self.den))
        return Fraction(self.num // common_divisor, self.den // common_divisor)

    def to_decimal(self):
        """Convert fraction to decimal."""
        return self.num / self.den


# Example usage
if __name__ == "__main__":
    # ATM Demo
    atm = Atm()
    # Uncomment to test ATM functionality
    # atm.menu()
    
    # Fraction Demo
    fr1 = Fraction(3, 4)
    fr2 = Fraction(1, 2)
    
    print(f"\nFraction Operations:")
    print(f"{fr1} + {fr2} = {fr1 + fr2}")
    print(f"{fr1} - {fr2} = {fr1 - fr2}")
    print(f"{fr1} * {fr2} = {fr1 * fr2}")
    print(f"{fr1} / {fr2} = {fr1 / fr2}")
    print(f"Decimal value of {fr1}: {fr1.to_decimal():.2f}")