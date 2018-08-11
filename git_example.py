```
This python file si a goood starting pouint.
Activation Funstions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  return  (1/(1+np.exp(-x)))
  
def relu(x):
  # entr code below
  return  np.max(0,x)
