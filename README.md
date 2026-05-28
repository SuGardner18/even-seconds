# Even Seconds

In Python, a decorator is syntactic sugar for a function that returns another function.  It allows you to write re-usable functions that modify other functions.

Write a decorator called `only_even-seconds` and some other function of your choice (it can be anything). When your function is decorated with `only_even-seconds`, your function should only execute if the current time's seconds is even, otherwise it should do nothing.  So if your program is executed at 10:23:55, for example, the original function would not be executed.