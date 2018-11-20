#%%
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from IPython.display import Latex
from IPython.display import Image
from IPython.core.display import HTML
from matplotlib import pyplot as plt
import numpy as np

#%% Latex
Latex("""The mass-energy equivalence is described by the famous equation

$$E=mc^2$$

discovered in 1905 by Albert Einstein.
In natural units ($c$ = 1), the formula expresses the identity

\\begin{equation}
E=m
\\end{equation}""")

#%% matplotlib

x = np.linspace(-np.pi, np.pi)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')

#%% Bokeh

output_notebook()

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Legend Example", tools=TOOLS)
p1.circle(x, y, legend="sin(x)")
p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend="3*sin(x)", color="green")
show(p1)

#%% Image
Image('http://jakevdp.github.com/figures/xkcd_version.png')

#%% IFrame
HTML("<iframe src='http://earth.nullschool.net' width='600' height='600'></iframe>")