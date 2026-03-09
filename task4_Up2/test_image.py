import pytest
import resize_image

def test_resize_dimensions():
    width, height = 4, 4
    data = bytes([0] * (width * height * 4))
    new_w, new_h = 2, 2
    
    result = resize_image.resize_logic(data, width, height, new_w, new_h)
    
    assert len(result) == new_w * new_h * 4
    assert isinstance(result, (bytes, bytearray))

def test_resize_logic():
    red_pixel = bytes([255, 0, 0, 255])
    empty_pixel = bytes([0, 0, 0, 0])
    data = red_pixel + empty_pixel * 3
    
    result = resize_image.resize_logic(data, 2, 2, 4, 4)
    
    assert result[0:4] == red_pixel

def test_invalid_input():
    result = resize_image.resize_logic(bytes([]), 10, 10, 5, 5)
    assert len(result) == 0

@pytest.mark.parametrize("size", [(10, 10), (100, 50), (1, 1)])
def test_various_sizes(size):
    nw, nh = size
    data = bytes([255] * (20 * 20 * 4))
    result = resize_image.resize_logic(data, 20, 20, nw, nh)
    assert len(result) == nw * nh * 4