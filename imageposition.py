import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display the image
img = mpimg.imread("image.png")
fig, ax = plt.subplots()
ax.imshow(img)

# Function to display coordinates on hover
def on_move(event):
    if event.inaxes:
        x, y = int(event.xdata), int(event.ydata)
        

# Connect the function to the event
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
