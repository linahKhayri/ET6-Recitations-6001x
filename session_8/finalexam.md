## **Final Exam Practice: OOP Principles in `USResident` Example**

### **Overview (Final Exam Practice)**
This is a **final exam practice question**. It includes an implementation of the `Person` class (which you should not modify) and requires you to complete the `USResident` class by implementing the missing methods. 

The problem is designed to test your understanding of:
- **Encapsulation**: How objects manage their data.
- **Inheritance**: Reusing code from a parent class.
- **Method Overriding**: Customizing behavior in subclasses.
- **Error Handling**: Validating input and raising exceptions.

---

## **1️⃣ Exercise: Complete `USResident` Implementation**
### **Task:**
The `USResident` class is a subclass of `Person`. Your task is to **implement the `getStatus()` method** and ensure that the `__init__()` constructor properly validates the `status` attribute.

### **Guidelines:**
- The `USResident` class should accept only three valid statuses:
  - "citizen"
  - "legal_resident"
  - "illegal_resident"
- If an invalid status is given, the constructor should raise a `ValueError`.
- Implement the `getStatus()` method to return the resident’s status.

### **Example Usage:**
```python
resident1 = USResident("Tim Beaver", "citizen")
print(resident1.getStatus())  # Output: "citizen"

resident2 = USResident("Tim Horton", "non-resident")  # Should raise ValueError
```

---

## **2️⃣ Challenge Yourself: Understanding Inheritance & Encapsulation**
### **Think About These Questions:**
🔹 **Why do we use inheritance instead of rewriting `Person` in `USResident`?**  
🔹 **What happens if we modify `Person`? How does it affect `USResident`?**  
🔹 **Why is method overriding useful in OOP?**  


---

### **Summary of Learning Goals:**
✅ **Encapsulation:** Managing data within a class.  
✅ **Inheritance:** Extending `Person` instead of duplicating code.  
✅ **Method Overriding:** Implementing `getStatus()` uniquely for `USResident`.  
✅ **Error Handling:** Raising `ValueError` for invalid statuses.  

---

**Now, complete the Python file provided and test your implementation!**
