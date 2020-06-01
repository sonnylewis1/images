from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_sz):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_sz many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_sz: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image

    - Create a new image
    - for each in pixel (nested loop version)
        - if pixel is a border pixel
            - set it to black
        - else
            - set it to orginal image pixel
    """
    new_image_height = original_img.height + 2 * border_sz
    new_image_width = original_img.width + 2 * border_sz
    new_image = SimpleImage.blank(new_image_width, new_image_height)

    for x in range(new_image_width):
        for y in range(new_image_height):
            new_pixel = new_image.get_pixel(x, y)
            if is_border_pixel(x, y, border_sz, new_image_width, new_image_height):
                new_pixel.red = 0
                new_pixel.green = 0
                new_pixel.blue = 0
            else:
                old_x = x - border_sz
                old_y = y - border_sz
                new_pixel = original_img.get_pixel(old_x, old_y)
                new_image.set_pixel(x, y, new_pixel)

    return new_image


def is_border_pixel(x, y, border_sz, new_image_width, new_image_height):
    """
    To check for borders of the image
    :param x:
    :param y:
    :param border_sz:
    :param new_image_width:
    :param new_image_height:
    :return:
    """
    if x <= border_sz:
        return True
    if y <= border_sz:
        return True
    if new_image_width - border_sz <= x:
        return True
    if new_image_height - border_sz <= y:
        return True
    return False


if __name__ == '__main__':
    main()
