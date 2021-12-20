import sys
import time
from itertools import chain

import numpy as np



class Image:

    def __init__(self, image, enhancement_string):
        image_width = len(image[0])-1
        self.pixel_width = image_width
        self.pixel_height = len(image)
        self.enhancement_string = enhancement_string
        self.mapping = {'#':1, '.':0}
        self.pixels = np.zeros((self.pixel_height, self.pixel_width),dtype=int)
        for i in range(len(image)):
            for j in range(image_width):
                self.pixels[i, j] = 1 if image[i][j] == "#" else 0
        self.pad_pixels(False)


    def enhance(self, step, first_last):
        if first_last == 0 and step % 2 == 1:
            self.pad_pixels(True)
            new_grid = np.zeros((self.pixel_height, self.pixel_width),dtype=int)
        elif first_last == 0:
            self.pad_pixels(False)
            new_grid = np.ones((self.pixel_height, self.pixel_width), dtype=int)
        elif first_last == 1:
            self.pad_pixels(True)
            new_grid = np.ones((self.pixel_height, self.pixel_width),dtype=int)
        else:
            self.pad_pixels(False)
            new_grid = np.zeros((self.pixel_height, self.pixel_width), dtype=int)

        for i in range(1,self.pixels.shape[0]-1):
            for j in range(1,self.pixels.shape[1]-1):
                nine_bit = self.find_neighbors(i,j)
                new_grid[i,j] = self.mapping[self.enhancement_string[int(nine_bit,2)]]
        self.pixels = new_grid
        return np.sum(self.pixels)


    def find_neighbors(self, i, j):
        bit_string = list(chain.from_iterable(self.pixels[i - 1:i+2, j - 1:j + 2].tolist()))
        return ''.join([str(num) for num in bit_string])

    def pad_pixels(self, ones):
        self.pixels = np.pad(self.pixels,((1,1),(1,1)), constant_values=0) if not ones else np.pad(self.pixels,((1,1),(1,1)), constant_values=1)
        self.pixel_height, self.pixel_width = self.pixels.shape[0], self.pixels.shape[1]


def find_first_last_comb(enhancement_string):
    if enhancement_string[0] == '#' and enhancement_string[-1] == '.': return 0
    elif enhancement_string[0] == '#' and enhancement_string[-1] == '#': return 0
    else: return 2


def solution(steps):
    with open(sys.argv[1]) as f:
        input = f.readlines()

    enhancement_string = input[0].strip()
    image = Image(input[2:], enhancement_string)
    lit_pixels = 0
    first_last = find_first_last_comb(enhancement_string)
    for i in range(steps):
        lit_pixels = image.enhance(i, first_last)
    return lit_pixels


if __name__ == "__main__":
    part1 =  solution(2)
    start = time.time()
    part2 = solution(50)
    end = time.time()
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
    print("Part 2 took %d seconds" %(end-start))
