Q. Read the length and width of a rectangular house block, and the length and width of a rectangular house that has been build on a block. The algorithm should then conpute and display the mowing time required to cut the grass around the house, at a rate of two square meters per minute.
```psuedocode
START
  GET Block_length, block_width,house_length,house_width
  block_area = block_length * block_width
  house_area = house_length * house_width
  mowing_area = block_area - house_area
  mowing_time = mowing_area / 2
  DISPLAY mowing_time
END
```