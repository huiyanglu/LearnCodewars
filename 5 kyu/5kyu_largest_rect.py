"""
Largest rectangle in background

https://www.codewars.com/kata/595db7e4c1b631ede30004c4

Imagine a photo taken to be used in an advertisement. The background on the left of the motive is whitish and you want to write some text on that background. So you scan the photo with a high resolution scanner and, for each line, count the number of pixels from the left that are sufficiently white and suitable for being written on. Your job is to find the area of the largest text box you can place on those pixels.

Example: In the figure below, the whitish background pixels of the scanned photo are represented by asterisks.

*********************************
*********
*******
******
******
******
**************
**************
**************
***************
*********************
If you count the pixels on each line from the left you get the list (or array, depending on which language you are using) [33, 9, 7, 6, 6, 6, 14, 14, 14, 15, 21]. The largest reactangle that you can place on these pixels has an area of 70, and is represented by the dots in the figure below.

*********************************
*********
*******
******
******
******
..............
..............
..............
..............*
..............*******
Write a function that, given a list of the number whitish pixels on each line in the background, returns the area of the largest rectangle that fits on that background.


"""

def largest_rect(histogram):
    histogram.append(0)
    stack = [-1] # s是h1的index的序列
    result = 0
    for i in range(0,len(histogram)):
        while histogram[i] < histogram[stack[-1]]:#s序列的最后一位对应的h1里的数
            h = histogram[stack.pop()] # []里是去掉的那个数
            w = i - stack[-1] - 1
            result = max(result, h * w)
        stack.append(i)
    histogram.pop()
    return result

print(largest_rect([3,4,5,4,3,4,5]))
