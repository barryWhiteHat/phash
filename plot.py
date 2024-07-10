import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import sys 
from phash import phash 





# Initialize empty lists for x and y
x = []
y = []

# Create figure and axis objects for both plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Function to update scatter plot
def update_plot(frame):
    ax1.clear()  # Clear previous plot
    ax1.scatter(x[:frame], y[:frame])

    ax1.scatter(x[:(frame-1)], y[:(frame-1)], color='blue', label='Previous data') 
    ax1.scatter(x[frame], y[frame], color='red', label='Last data')  
 
    ax1.set_title('Live Scatter Plot of x vs y')
    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')

# Function to update image display
def update_image(frame):

    ax2.imshow(image_1)
    ax2.set_title('Image 1')




# Example of adding data points

pics = sys.argv[1:]



for i, pic in enumerate(pics):

    image_1 = plt.imread(pic)



    val = phash(pic)

    size = int(len(val)/2)
      
    x.append(int(val[0:size],16))
    y.append(int(val[size:],16))

   
    # Update scatter plot
    update_plot(i)
    
    # Update image display every 10 frames

    update_image(i)
    
    # Pause for a moment to observe the plot
    plt.pause(0.1)

plt.show()

