from io import BytesIO
import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy as np

def figure_to_pdf(
    pdf: FPDF, 
    picture: BytesIO,
    x_position: int, 
    y_position: int
    ) -> None:
    """
    Add a PNG image from a BytesIO object to a PDF.

    Args:
        pdf (fpdf) created fpdf
        picture (BytesIO) matplotlib figure saved to memory
        x_position (int) pdf x-axis position where figure will be displayed
        y_position (int) pdf y-axis position where figure will be displayed
    """
    pdf.add_page()
    pdf.image(picture, x=x_position, y=y_position, type='PNG')
    return pdf
    
def create_dual_array_subplot(
    first_array: np.ndarray, first_title: str,
    second_array: np.ndarray, second_title: str) -> BytesIO:
    """
    Create a subplot with two images (middle slices of two arrays) and return as PNG in BytesIO.
    """
    picture = BytesIO()
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(first_array[len(first_array) // 2])
    plt.title(first_title)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(second_array[len(second_array) // 2])
    plt.title(second_title)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(picture, format='PNG')
    picture.seek(0)
    plt.close()
    return picture

# Example usage:
pdf = FPDF()
picture = create_dual_array_subplot(
    example_array_1,
    "example_array_1",
    example_array_2,
    "example_array_2")
pdf = figure_to_pdf(pdf)