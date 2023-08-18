#def convert(input_grid):
    #pass

NUMS = {
        '     |  |   ':'1',
        ' _  _||_    ':'2',
        ' _  _| _|   ':'3',
        '   |_|  |   ':'4',
        ' _ |_  _|   ':'5',
        ' _ |_ |_|   ':'6',
        ' _   |  |   ':'7',
        ' _ |_||_|   ':'8',
        ' _ |_| _|   ':'9',
        ' _ | ||_|   ':'0'
       }

def convert(input_grid):
    if (len(input_grid))%4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    else:
        if all((len(name))%3 != 0 for name in input_grid):
            raise ValueError("Number of input columns is not a multiple of three")
        else:
            result = []
            for r in range(0, len(input_grid), 4):
                row = ''
                for c in range(0, len(input_grid[r]), 3):
                    num = ''
                    for i in range(0, 4):
                        num += input_grid[r+i][c : c+3]
                    row += NUMS[num] if num in NUMS else '?'
                result.append(row)
            return ','.join(result)