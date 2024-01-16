uløstSudoku = [[0,5,0, 0,0,0, 0,3,0],
               [0,0,4, 9,7,0, 8,0,0],
               [0,0,0, 0,6,3, 4,2,0],

               [5,8,0, 3,2,0, 0,0,0],
               [0,0,0, 0,0,9, 7,0,0],
               [9,0,3, 0,0,0, 0,8,0],

               [4,7,5, 0,3,8, 0,1,9],
               [0,2,0, 0,0,0, 0,7,6],
               [3,0,6, 7,1,2, 0,4,8]]

notering = [[0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],

            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],

            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0]]

løstSudoku = [[0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],

              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],

              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0]]

telleliste = []

# while True:
#     for y in uløstSudoku:
#         for x in y:
#             print(notering[uløstSudoku.index(y)][y.index(x)])
    
# for y in uløstSudoku:
#     for x in y:
#         print(x)
#         print(notering[uløstSudoku.index(y)][y.index(x)])

def xline(y,x,z):
    telleliste = []
    # if y < 3 and x < 3:
    #     for i in range(0,3):
    #         for j in range(0,3):
    #             telleliste.append(uløstSudoku[i][j])
    # if y >= 3 and x >= 3:
    #     if y < 6 and x < 6:    
    #         for i in range(0,3):
    #             for j in range(0,3):
    #                 telleliste.append(uløstSudoku[i][j])
    #     else:    
    #         for i in range(0,3):
    #             for j in range(0,3):
    #                 telleliste.append(uløstSudoku[i][j])
    
    # if y < 3 and x < 3:
    #     for i in range(0,3):
    #         for j in range(0,3):
    #             telleliste.append(uløstSudoku[i][j])
    # if y >= 3 and x < 3:
    #     if y < 6 and x < 6:    
    #         for i in range(0,3):
    #             for j in range(0,3):
    #                 telleliste.append(uløstSudoku[i][j])
    #     else:    
    #         for i in range(0,3):
    #             for j in range(0,3):
    #                 telleliste.append(uløstSudoku[i][j])
    
    if y < 3:
        if x < 3:
            for i in range(0,3):
                for j in range(0,3):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 3 and x < 6:
            for i in range(0,3):
                for j in range(3,6):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 6:
            for i in range(0,3):
                for j in range(6,9):
                    telleliste.append(uløstSudoku[i][j])

    elif y < 6 and y >= 3:
        if x < 3:
            for i in range(3,6):
                for j in range(0,3):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 3 and x < 6:
            for i in range(3,6):
                for j in range(3,6):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 6:
            for i in range(3,6):
                for j in range(6,9):
                    telleliste.append(uløstSudoku[i][j])
    
    elif y >= 6:
        if x < 3:
            for i in range(6,9):
                for j in range(0,3):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 3 and x < 6:
            for i in range(6,9):
                for j in range(3,6):
                    telleliste.append(uløstSudoku[i][j])
        elif x >= 6:
            for i in range(6,9):
                for j in range(6,9):
                    telleliste.append(uløstSudoku[i][j])
    
    if telleliste.count(z) == 0:
        telleliste = []
        for i in range(0,9):
            telleliste.append(uløstSudoku[i][x])
        #print(telleliste)
        if telleliste.count(z) == 0:
            return True

                

while True:
    for y in range(0,9):
        for x in range(0,9):
            if uløstSudoku[y][x] == 0:
                for z in range(1,10):
                    if uløstSudoku[y].count(z) == 0:
                        if xline(y,x,z) == True:
                            #print(xline(y,x,z))
                            uløstSudoku[y][x] = z
                            print(uløstSudoku)
                            print("")
                        
                        



        

        
            
