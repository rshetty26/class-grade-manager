def read_config_file():
    x=[]
    currentline = []
    infile = open("config.txt", 'r')
    lineNumber = 1
    for line in infile:
        currentline = []
        if lineNumber == 2:
            currentline = line.split(" ")
        else:
            currentline = line.split(",")
        x = x + [currentline]
        lineNumber = lineNumber + 1
    infile.close()
    return x

def read_data_file(filename):
    x=[]
    currentline = []
    infile = open(filename, 'r')
    for line in infile:
        currentline = []
        currentline = line.split(",")
        x = x + [currentline]
    infile.close()
    return x

def sort(listSort):
    for i in range(1, len(listSort)):
        key = listSort[i]
        j = i - 1
        while j >=0 and key < listSort[j] :
            listSort[j+1] = listSort[j]
            j = j - 1
            listSort[j+1] = key
    return listSort

def dropped_average(list1, dropNumber, pointTotal):
    dropNumber = dropNumber*-1
    sort(list1)
    list2 = []
    total = 0
    for x in range(dropNumber, len(list1)):
        list2 = list2 + [list1[x]]
    for x in list2:
        total = total + x
    return (total/len(list2))/pointTotal

def gradeCheck(grade):
    if(float(configWhole[2][0][1:3]) < grade):
        return "A"
    elif(float(configWhole[2][1][2:4]) < grade and float(configWhole[2][1][5:10]) > grade):
        return "A-"
    elif(float(configWhole[2][2][2:4]) < grade and float(configWhole[2][2][5:10]) > grade):
        return "B+"    
    elif(float(configWhole[2][3][1:3]) < grade and float(configWhole[2][3][4:9]) > grade):
        return "B"    
    elif(float(configWhole[2][4][2:4]) < grade and float(configWhole[2][4][5:10]) > grade):
        return "B-"    
    elif(float(configWhole[2][5][2:4]) < grade and float(configWhole[2][5][5:10]) > grade):
        return "C+"    
    elif(float(configWhole[2][6][1:3]) < grade and float(configWhole[2][6][4:9]) > grade):
        return "C"    
    elif(float(configWhole[2][7][2:4]) < grade and float(configWhole[2][7][5:10]) > grade):
        return "C-"    
    elif(float(configWhole[2][8][2:4]) < grade and float(configWhole[2][8][5:10]) > grade):
        return "D+"    
    elif(float(configWhole[2][9][1:3]) < grade and float(configWhole[2][9][4:9]) > grade):
        return "D"    
    elif(float(configWhole[2][10][2:4]) < grade and float(configWhole[2][10][5:10]) > grade):
        return "D-"    
    elif(float(configWhole[2][11][2:4]) > grade):
        return "F"    

configWhole = read_config_file()
dataWhole = read_data_file(configWhole[0][0])

outfile = open("Submission-1.csv", 'w')

outfile.write(" , ,")

headers = []

for x in range(1, int(configWhole[0][10])+1):
    outfile.write("A." + str(x) + ",")
    headers = headers + ["A." + str(x)]
for x in range(1, int(configWhole[0][4])+1):
    outfile.write("L." + str(x) + ",")
    headers = headers + ["L." + str(x)]
for x in range(1, int(configWhole[0][1])+1):
    outfile.write("T." + str(x) + ",")
    headers = headers + ["T." + str(x)]
for x in range(1, int(configWhole[0][7])+1):
    outfile.write("Q." + str(x) + ",")
    headers = headers + ["Q." + str(x)]
for x in range(1, int(configWhole[0][13])+1):
    outfile.write("P." + str(x) + ",")
    headers = headers + ["P." + str(x)]
for x in range(1, int(configWhole[0][16])+1):
    outfile.write("B." + str(x) + ",")
    headers = headers + ["B." + str(x)]
outfile.write("T.X Avg.,L.X Avg.,Q.X Avg.,A.X Avg.,Grade\n")

rowCount = 0
for row in dataWhole:
    temp = row[len(dataWhole[0])-1]
    temp = int(temp)
    row = row[:-1] + [str(temp)]
    for item in row:
        outfile.write(str(item)+",")

    templist = []
    for x in range(9, 9 + int(configWhole[0][1])):
        templist = templist + [int(dataWhole[rowCount][x])]
    TAvg = format(dropped_average(templist, int(configWhole[0][2]), int(configWhole[0][3])), ".2f")
    outfile.write(str(TAvg) + ",")

    templist = []
    for x in range(4, 4 + int(configWhole[0][4])):
        templist = templist + [int(dataWhole[rowCount][x])]
    AAvg = format(dropped_average(templist, int(configWhole[0][5]), int(configWhole[0][6])), ".2f")
    outfile.write(str(AAvg) + ",")
    
    templist = []
    for x in range(14, 14 + int(configWhole[0][7])):
        templist = templist + [int(dataWhole[rowCount][x])]
    LAvg = format(dropped_average(templist, int(configWhole[0][8]), int(configWhole[0][9])), ".2f")
    outfile.write(str(LAvg) + ",")
    
    templist = []
    for x in range(2, 2 + int(configWhole[0][10])):
        templist = templist + [int(dataWhole[rowCount][x])]
    QAvg = format(dropped_average(templist, int(configWhole[0][11]), int(configWhole[0][12])), ".2f")
    outfile.write(str(QAvg) + ",")

    final_grade = float(AAvg) * int(configWhole[1][0][1:]) + float(LAvg) * int(configWhole[1][1][1:]) + float(TAvg) * int(configWhole[1][2][1:]) + float(QAvg) * int(configWhole[1][3][1:]) + (float(dataWhole[rowCount][16]))/int(configWhole[0][15]) * int(configWhole[1][4][1:]) + (float(dataWhole[rowCount][17]))/int(configWhole[0][18]) * int(configWhole[1][5][1:])

    outfile.write(str(gradeCheck(final_grade))+",")
    rowCount = rowCount + 1
    outfile.write("\n")

outfile.write(" , ,")

averageslist = []

for x in range(2, len(dataWhole[0])):
    avg = 0
    for y in range(len(dataWhole)):
        avg = avg + int(dataWhole[y][x])
    avg = avg / len(dataWhole)
    averageslist = averageslist + [avg]
    avg = format(avg, ".2f")
    outfile.write(str(avg)+",")

outfile.close()

x_axis = headers
plot.bar(x_axis, averageslist, color = ('r', 'b', 'g', 'c', 'y')) 
plot.xlabel("Category")
plot.ylabel("Scores")

plot.show()
