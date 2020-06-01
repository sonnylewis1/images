"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    patch1 = make_recolored_patch(1.5, 0, 1.5)
    patch2 = make_recolored_patch(0, 1.5, 1.5)
    patch3 = make_recolored_patch(1.5, 1.5, 0)
    patch4 = make_recolored_patch(0, 1.5, 4.4)
    patch5 = make_recolored_patch(3, 5, 2)
    patch6 = make_recolored_patch(2.2, 3.3, 4.4)

    final_image = add_patch(0, 0, patch1, final_image)
    final_image = add_patch(0, 1, patch2, final_image)
    final_image = add_patch(0, 2, patch3, final_image)
    final_image = add_patch(1, 0, patch4, final_image)
    final_image = add_patch(1, 1, patch5, final_image)
    final_image = add_patch(1, 2, patch6, final_image)

    final_image.show()
def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    """
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

def add_patch(row, column, patch, final_image):
    width = patch.width
    height = patch.height

    for x in range(width):
        for y in range(height):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel((column * width) + x, (row * height) + y, pixel)

    return final_image

if __name__ == '__main__':
    main()