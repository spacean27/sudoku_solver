def display_data(data):
    print("-------------------------")
    for i in range(0,9):
        print("|", *data[i][0:3], 
              "|", *data[i][3:6], 
              "|", *data[i][6:10],
              "|", sep=" ")
        if i in [2,5]:
            print("-------------------------")
    print("-------------------------")