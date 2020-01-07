# Instruction for using Latex in Matplotlib #

* Install MIKTex

* Activate Latex usage with:

```
import matplolib.pyplot as plt
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text', usetex=True)
plt.rc('font', family='times new roman', size=16)
```
