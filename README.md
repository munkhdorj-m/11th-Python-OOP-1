# Object Oriented Programming 1

OOP PDF:

https://drive.google.com/file/d/1Dfu8jYSOsRFwReeNXO6nA0ffTYqtH2BT/view?usp=sharing

---

## Exercise 1

**Problem:**
 
**Student Grades (Encapsulation):**  
Create a Student class where the grade is private and safe from incorrect modification.  

Requirements:   
-Private attribute: `__grade`  
-Public methods:   
&nbsp;&nbsp;&nbsp;&nbsp;`set_grade(val)` - Must be 0–100  
&nbsp;&nbsp;&nbsp;&nbsp;`get_grade()`      
-Public attribute: `name`   

Example:

    Input:
       s = Student("Bob")
       s.set_grade(85)
       print(s.get_grade())

    Output:
       85
  
---

## Exercise 2

**Problem:**
 
**Student Grades (Encapsulation):**  
Create a BankAccount class that safely manages deposits and withdrawals using encapsulation.

Requirements:   
Private attribute: 
* `__balance` (starts at 0)
Public methods:   
* `deposit(amount)`
⋅⋅⋅⋅* Add amount to balance.
⋅⋅⋅⋅* Ignore invalid (negative or zero) amounts  
* `get_grade()` 
⋅⋅⋅⋅* Subtract amount from balance
⋅⋅⋅⋅* Only allow if balance is enough
⋅⋅⋅⋅* If not enough → do nothing
* `get_balance()`
....* Return current balance
-Public attribute: `name`   

Example:

    Input:
       s = Student("Bob")
       s.set_grade(85)
       print(s.get_grade())

    Output:
       85
  
---

