# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# •Create a method called factorial() which allows to calculate the factorial of an integer. 
# •Create a method called sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. 
# •Create a method called is_prime() allowing to test the primality of a given integer. 
# •Create a method called all_is_prime() allowing to display all prime integer numbers from 2 to n. 
# •Create a table_mult() method which creates and displays the multiplication table of a given integer (from 1 to 10). 
# •Then create an all_tables_mult() method to display all the integer multiplication tables (from 1 to 10)


class Computation:
    def __init__(self):
        ...
    
    @staticmethod
    def validation(n):
        if (not isinstance(n, int)) or n == 0:
            raise ValueError('Wrong parameter')

    def factorial(self, n):
        self.validation(n)
        f = 1
        for i in range(1, n):
            f = f * i
        return f

    def _sum(self, n):
        self.validation(n)
        s = 0
        for i in range(n + 1):
            s += i
        return s

    def is_prime(self, n):
        self.validation(n)
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 'Not a prime number'
        return 'Is a prime number'
    
    def all_is_prime(self, n):
        self.validation(n)
        prime_list = []
        for i in range(2, n):
            if i == 2:
                prime_list.append(i)
            else:
                is_prime_number = False
                for j in range(2, int(n ** 0.5) + 1):
                    if i % j == 0:
                        break
                    is_prime_number = True
                if is_prime_number == True:
                    prime_list.append(i)
        return prime_list
    
    def mult(self, n):
        self.validation(n)
        for i in range(1, 11):
            print(f'{n} * {i} == {n * i}')

    def all_tables_mult(self, n):
        self.validation(n)
        for j in range(1, 6):
            for i in range(1, 6):
                print(f'{i} * {j} == {j * i}', end='\t\t\t')
            print('')
        print('')
        for j in range(6, 11):
            for i in range(6, 11):
                print(f'{i} * {j} == {j * i}', end='\t\t\t')
            print('')

c1 = Computation()
print(c1.factorial(5))
print(c1._sum(5))
print(c1.is_prime(7))
print(c1.all_is_prime(7))
print(c1.mult(3))
print(c1.all_tables_mult(3))

