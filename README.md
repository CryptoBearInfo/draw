# Draw

A drawing tool for IPython notebook

## Usage
```Python
from draw import *

cv = Canvas(500, 500)
cv.add(Rect(100, 100, width=100, height=100 fill="#000"))
cv.show()
```

```Python
from draw import *
cv = Canvas()
r = Rect(100, 0, width=100, height=100 fill="#000")

def func(i):
    r.x(100*cos(i/5.))
    r.y(100*sin(i/5.))
  
cv.add(r)
cv.loop(func)
cv.show()
```

## Installation

`pip install draw`
