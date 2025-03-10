## Final Exam Practice: OOP Principles in `USResident` Example
## Instructions:
# 1. Do NOT modify the `Person` class.
# 2. Complete the `USResident` class by implementing the missing method `getStatus()`.
# 3. Ensure that the `__init__()` constructor raises a ValueError if `status` is invalid.
# 4. Test your implementation by creating objects of `USResident`.

## DO NOT MODIFY THIS CLASS
class Person(object):
    def __init__(self, name):
        # Create a person with name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    
    def getLastName(self):
        # Return self's last name
        return self.lastName
    
    def setAge(self, age):
        # Assumes age is an int greater than 0
        # Sets self's age to age (in years)
        self.age = age
    
    def getAge(self):
        # Returns self's current age in years
        if self.age == None:
            raise ValueError("Age not set")
        return self.age
    
    def __lt__(self, other):
        # Return True if self's name is lexicographically less than other's name
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        # Return self's name
        return self.name

## COMPLETE THIS CLASS
class USResident(Person):
    """A Person who resides in the US."""
    
    def __init__(self, name, status):
        """Initializes a USResident object.
        A USResident object inherits from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident".
        Raises a ValueError if status is not one of those 3 strings."""
        # Your code here
        pass
    
    def getStatus(self):
        """Returns the status of the resident."""
        # Your code here
        pass

## TEST CASES: Uncomment and run after implementing USResident
# resident1 = USResident("Tim Beaver", "citizen")
# print(resident1.getStatus())  # Expected Output: "citizen"

# resident2 = USResident("Sophia Anderson", "legal_resident")
# print(resident2.getStatus())  # Expected Output: "legal_resident"

# resident3 = USResident("Tim Horton", "non-resident")  # Should raise ValueError
