# Advanced Multiple Choice Questions

## Problem 1
You have the following class hierarchy:
```python
class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')
```
Which of the following is correct?

- [ ] When `a = A()` we say that `a` is an instance of `A`.
- [ ] When `b = B()` we say that `b` is a subclass of `A`.
- [ ] Both of the above.
- [ ] Neither of the above.

<details>
  <summary>Show Answer</summary>
  ✅ When `a = A()` we say that `a` is an instance of `A`.
</details>

---

## Problem 2
Consider the function `f` below. What is its Big O complexity?
```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)
```

- [ ] O(n²)
- [ ] O(n log n)
- [ ] O(n)
- [ ] O(1)

<details>
  <summary>Show Answer</summary>
  ✅ O(n)
</details>

---

## Problem 3
The complexity of `1^n + n^4 + 4n + 4` is:

- [ ] Constant
- [ ] Logarithmic
- [ ] Linear
- [ ] Polynomial
- [ ] Exponential

<details>
  <summary>Show Answer</summary>
  ✅ Polynomial
</details>
