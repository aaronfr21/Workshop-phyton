# exc must be exception instance or None.
raise RuntimeError from exc

# This can be useful when you are transforming exceptions
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
# output
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database

# Exception chaining happens automatically when an exception is raised inside an except or finally section
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
# output
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError