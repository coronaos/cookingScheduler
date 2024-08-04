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
c = canvas.Canvas(pdf_file, pagesize=landscape(letter))
width, height = landscape(letter)

# Define the size of each block
block_width = 1.2 * inch
block_height = 1.2 * inch

# Define the starting position for the grid, moved down by 2 inches
x_offset = 1.3 * inch
y_offset = height - 2 * inch  # Adjusted to fit within the landscape page

# Draw the header row with the days of the week
for j, day in enumerate(days_of_week):
    x = x_offset + j * block_width
    y = y_offset
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.lightblue)
    c.rect(x, y, block_width, block_height, fill=1)
    c.setFillColor(colors.black)
    c.drawString(x + 0.2 * inch, y + 0.4 * inch, day)

# Loop through the data and draw each block with meal labels
for i, row in enumerate(data):
    # Draw the meal label on the left side
    x_label = x_offset - block_width
    y_label = y_offset - (i + 1) * block_height
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.lightgreen)
    c.rect(x_label, y_label, block_width, block_height, fill=1)
    c.setFillColor(colors.black)
    c.drawString(x_label + 0.2 * inch, y_label + 0.4 * inch, meal_labels[i])

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
        c.drawString(x + 0.2 * inch, y + 0.4 * inch, cell)

# Save the PDF
c.save()
