# repeating_timer

Run a function over and over in a thread.

## Why?

A package from [Q-continuum](http://hg.q-continuum.net) (with the same name) claims to provide this functionality. However, it no longer works in python 3. This project is a complete rewrite that works with Python 3, and aims to have more features.

## Usage.

```python
from repeating_timer import RepeatingTimer

t = RepeatingTimer(1.0, print, "Hi.")
t.start()
```

This will print "Hi." every second.
