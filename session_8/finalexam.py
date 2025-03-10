## Final Exam Practice: OOP Principles in `USResident` Example
## Instructions:
# 1. Do NOT modify the `Person` class.
# 2. Complete the `USResident` class by implementing the missing method `getStatus()`.
# 3. Ensure that the `__init__()` constructor raises a ValueError if `status` is invalid.
# 4. Test your implementation by creating objects of `USResident`.

## DO NOT MODIFY THIS CLASS
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        super().__init__(name)
        if status == 'citizen' or status == 'legal_resident' or status == 'illegal_resident':
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status
resident1 = USResident("Tim Beaver", "citizen")
print(resident1.getStatus())  # Output: "citizen"
resident2 = USResident("Sophia Anderson", "legal_resident")
print(resident2.getStatus())  # Expected Output: "legal_resident"

resident2 = USResident("Tim Horton", "non-resident")
