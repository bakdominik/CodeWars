from CodeWarsTests import * 

# NOT SOLVED YET

class Image:
    
  def __init__(self, data, w, h): 
    self.pixels = data
    self.width = w
    self.height = h

class Central_Pixels_Finder(Image):

  def central_pixels(self, colour):
  # your code goes here
    pass


Test.describe("central_pixels tests")

Test.it("Example_Tests")

image = Central_Pixels_Finder( [1,1,4,4,4,4,2,2,2,2,
                                1,1,1,1,2,2,2,2,2,2,
                                1,1,1,1,2,2,2,2,2,2,
                                1,1,1,1,1,3,2,2,2,2,
                                1,1,1,1,1,3,3,3,2,2,
                                1,1,1,1,1,1,3,3,3,3], 10, 6 );

# Only one red pixel has the maximum depth of 3:
red_ctr = [ 32 ];
Test.assert_equals(image.central_pixels(1), red_ctr, "" )

# Multiple blue pixels have the maximum depth of 2:
blue_ctr = [ 16,17,18,26,27,28,38 ];
Test.assert_equals(sorted(image.central_pixels(2)), blue_ctr, "" )

# All the green pixels have depth 1, so they are all "central":
green_ctr = [ 35,45,46,47,56,57,58,59 ];
Test.assert_equals(sorted(image.central_pixels(3)), green_ctr, "" )

# Similarly, all the purple pixels have depth 1:
purple_ctr = [ 2,3,4,5 ];
Test.assert_equals(sorted(image.central_pixels(4)), purple_ctr, "" )

# There are no pixels with colour 5:
non_existent_ctr = [ ];
Test.assert_equals(image.central_pixels(5), non_existent_ctr, "" )
