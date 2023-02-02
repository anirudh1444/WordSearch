answer = [] 

def word_search(grid, words):

    """
    Traverses through 2D letters array looking for all the words given by user 
    @param row: index of current row
    @param col: index of current column
    @param curr_words: remaining words which are left to find and also contain the same letters as current 
    @param direction: the direction in which the word is being spelt (ie. horizontally, vertically)
    @param current: the letters being memoized
    """
    def traverse(row, col, curr_words, direction, current):

        # Checks that the column and row parameters inputted are valid 
        if row >= len(grid) or col >= len(grid[0]) or row < 0:
            return False 
        
        # Memoizes the word 
        current += grid[row][col]
        copy1 = []

        for word in curr_words:

            # Checks if either the first or last part of word matches current 
            if word[:len(current)] == current or word[::-1][:len(current)] == current:
                # If word is found, it will be added to the answer key and removed from remaining words list
                if word == current:
                    answer.append((word, i + 1, j + 1, direction))
                    if word in words:
                        words.remove(word)
                
                # Does the same thing as previously, but for words found in the reverse direction (avoids searching in 8 directions at any given point)
                elif word == current[::-1]:
                    answer.append((word, row + 1, col + 1, "Reverse " + direction))
                    if word in words:
                        words.remove(word)
                else:
                    copy1.append(word)
        
        # Continues traversal if there are some words which still match the current pattern
        if copy1:
            if direction == "D":
                traverse(row + 1, col, copy1[:], "D", current)
            elif direction == "R":
                traverse(row, col + 1, copy1[:], "R", current)
            elif direction == "RD":
                traverse(row + 1, col + 1, copy1[:], "RD", current)
            elif direction == "LD":
                traverse(row + 1, col - 1, copy1[:], "LD", current)
    
    # Initiates traversal at every point 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            copy = []
            for word in words:
                if word[0] == grid[i][j] or word[-1] == grid[i][j]:
                    if len(word) == 1:
                        answer.append(word)
                    else:
                        copy.append(word)
            if copy:
                traverse(i + 1, j, copy, "D", grid[i][j])
                traverse(i, j + 1, copy, "R", grid[i][j])
                traverse(i + 1, j + 1, copy, "RD", grid[i][j])
                traverse(i + 1, j - 1, copy, "LD", grid[i][j])

    return answer




if __name__ == '__main__':

    # Obtains number of rows, columns, and all the letters
    rows = int(input("How many rows does the matrix contain? \n"))
    cols = int(input("How many columns does the matrix contain? \n"))
    letters = input("Input all capital letters without any spaces. \n")
    grid = []
    row = []

    # Places all the letters into a 2D Array
    for i, let in enumerate(letters):
        row.append(let)
        if (i + 1) % cols == 0:
            grid.append(row)
            row = []
    
    # User inputs words to be found

    input_words = input("Input all the words to be found with commas and spaces in between. \n")
    words = input_words.split(", ")
    print(word_search(grid, words))

"""
Test example:
Rows: 11
Columns: 9
Letters: EANHMDSHDHLGAMNPYSEEANYEGMDWGJESRUWBYNRODBDNEMAJWRWEIJMELISSAGISHARONSROSNRJBRIADARUALELUBGBRJJABOG
Words: ANGELA, MELISSA, RYAN, EDWARD, LISA, LAURA, SHARON, JOSEPH, BRIAN, CARLOS
"""