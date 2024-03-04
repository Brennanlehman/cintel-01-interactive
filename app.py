# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Set page options for PyShiny App
ui.page_opts(title="PyShiny App with Plot", fillable=True)

# Create a sidebar with an input slider for the number of bins
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Define a plot function for rendering a histogram
@render.plot(alt="A histogram")
def histogram():
    # Set a random seed for reproducibility
    np.random.seed(3)
    
    # Generate random data for the histogram
    x = 100 + 15 * np.random.randn(437)
    
    # Plot the histogram using the specified number of bins
    plt.hist(x, input.selected_number_of_bins(), density=True)
