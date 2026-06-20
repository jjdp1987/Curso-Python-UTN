#Compartir eje

import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 500)
s1 = np.sin(t)
s2 = np.cos(t)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 5),
layout='constrained')
ax1.plot(t, s1, label="sin(t)")
ax1.set_ylabel("Amplitud")
ax1.legend()
ax2.plot(t, s2, color="orange", label="cos(t)")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Amplitud")
ax2.legend()
fig.suptitle("Subplots compartiendo eje X")
plt.show()


#Compartir eje Y

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(9, 4),
layout='constrained')
ax1.plot(x, np.exp(x))
ax1.set_title("exp(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2.plot(x, np.exp(0.5 * x))
ax2.set_title("exp(0.5x)")
ax2.set_xlabel("x")
fig.suptitle("Subplots compartiendo eje Y")
plt.show()