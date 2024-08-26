from scheduler import scheduler
import numpy as np
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

# Create a 2x7 NumPy array of data strings
data = scheduler()

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Labels for rows
meal_labels = ["Lunch", "Dinner"]

# Define the PDF file name
pdf_file = 'schedule_landscape.pdf'

# Create a canvas object in landscape orientation
c = canvas.Canvas(pdf_file, pagesize=[1050,500])
height, width = pagesize=[3,400]

# Define the size of each block
block_width = 1.79 * inch
block_height = 1.7 * inch

# Define the starting position for the grid, moved down by 2 inches
x_offset = 2* inch
y_offset = 4.5 * inch  # Adjusted to fit within the landscape page

# Draw the header row with the days of the week
for j, day in enumerate(days_of_week):
    x = x_offset + j * block_width
    y = y_offset
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.lightblue)
    c.rect(x, y, block_width, block_height, fill=1)
    c.setFillColor(colors.black)
    c.drawString(x + 0.6 * inch, y + 0.5 * inch, day)

# Loop through the data and draw each block with meal labels
for i, row in enumerate(data):
    # Draw the meal label on the left side
    x_label = x_offset - block_width
    y_label = y_offset - (i + 1) * block_height
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.lightgreen)
    c.rect(x_label, y_label, block_width, block_height, fill=1)
    c.setFillColor(colors.black)
    c.drawString(x_label + 0.5 * inch, y_label + 1 * inch, meal_labels[i])

    for j, cell in enumerate(row):
        # Calculate the position of the current block
        x = x_offset + j * block_width
        y = y_offset - (i + 1) * block_height

        # Draw the rectangle for the block
        c.setStrokeColor(colors.black)
        c.setFillColor(colors.lightgrey)
        c.rect(x, y, block_width, block_height, fill=1)

        # Add the text inside the block
        c.setFillColor(colors.black)
        c.drawString(x + 0.08 * inch, y + 0.8 * inch, cell)

# Save the PDF
c.save()
