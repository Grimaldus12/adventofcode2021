import sys
import time
import numpy as np



class Image:

    def __init__(self, image, steps, enhancement_string):
        image_width = len(image[0])-1
        self.pixel_width = image_width# + 2*padding
        self.pixel_height = len(image)# + 2*padding
        self.enhancement_string = enhancement_string
        self.pixels = np.zeros((self.pixel_height, self.pixel_width),dtype=int)
        for i in range(len(image)):
            for j in range(image_width):
                self.pixels[i, j] = 1 if image[i][j] == "#" else 0
        self.pad_pixels(steps+1)



    def enhance(self, step):
        new_grid = []
        if self.enhancement_string[0] == '#':
            if step % 2 == 1:
                new_grid = np.zeros((self.pixel_height, self.pixel_width),dtype=int)
            else:
                new_grid = np.ones((self.pixel_height, self.pixel_width), dtype=int)
        for i in range(1,self.pixels.shape[0]-1):
            for j in range(1,self.pixels.shape[1]-1):
                nine_bit = self.find_neighbors(i,j,step)
                new_grid[i,j] = 0 if self.enhancement_string[int(nine_bit,2)] == "." else 1
        self.pixels = new_grid.copy()
        return np.sum(self.pixels)


    def find_neighbors(self, i, j):
        bit_string = np.concatenate((self.pixels[i - 1, j - 1:j + 2],self.pixels[i, j - 1:j + 2],self.pixels[i + 1, j - 1:j + 2]))
        return ''.join([str(num) for num in bit_string])

    def pad_pixels(self, steps):
        padded_matrix = np.zeros((self.pixels.shape[0]+(2*steps), self.pixels.shape[1]+(2*steps)), dtype=int)
        padded_matrix[steps:self.pixels.shape[0]+steps,steps:self.pixels.shape[1]+steps] = self.pixels
        self.pixel_height = padded_matrix.shape[0]
        self.pixel_width = padded_matrix.shape[1]
        self.pixels = padded_matrix.copy()


def solution(steps):
    with open(sys.argv[1]) as f:
        input = f.readlines()

    enhancement_string = input[0]
    image = Image(input[2:], steps, enhancement_string)
    lit_pixels = 0
    for i in range(steps):
        lit_pixels = image.enhance(i)
    return lit_pixels


if __name__ == "__main__":
    part1 =  solution(2)
    start = time.time()
    part2 = solution(50)
    end = time.time()
    print("Solution part one: %d" %part1)
    print("Solution part two: %d" %part2)
    print("Part 2 took %d seconds" %(end-start))
