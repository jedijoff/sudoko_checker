Currently this script takes 9 user inputs of 9 numbers that are the numbers in their suduko puzzle rows.

It currently checks each row, each box of 9 numbers and the diagonals to ensure the numbers 1-9 only appear once. Each row is then checked against the checker list, that has the numbers 1-9 in it, as strings.

For the boxes I broke the puzzle down into 3 blocks of 3 rows and then fed the first 3 numbers from the first block of three rows to sq_1, middle three numbers from the 3 rows are assigned to sq_2, and the last three numbers from each block of 3 are fed into sq_3, each sq is sorted, then checked to make sure these match the checker list, the block of three rows are assigned a boolean value True if all sqs match the check_list and False if any of the squares is incorrect. 

It is nearly complete, I just have to write the column checker now, and then add a final check of the results list to see if the puzzle is correct - phew.
