import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pathofmainfile = r'C:\Users\ksail\Documents\Python Code\School_Proj\vgchartz-2024.csv'
pathofabbriviations = r'C:\Users\ksail\Documents\Python Code\School_Proj\data_dictionary.csv'


df = pd.read_csv(pathofmainfile)
vg_df = df.ffill()
no_of_rows = len(df.index)

ab_df = pd.read_csv(pathofabbriviations)

#Creating a List of all Genres in the dataframe
genre_list = []
for i in range(no_of_rows):
    if vg_df.at[i,'Genre'] not in genre_list:
        genre_list.append(vg_df.at[i,'Genre'])

colors_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'Indigo','LightSeaGreen', 'Aqua', 'CadetBlue']

def readcsv():
    print(vg_df.head(10))

def abbriviations():
    print(ab_df)

def critic_score_sort():
    #Creating a List of avg critic scores per genres
    critic_score_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                sum =+ vg_df.at[i,'Critic_Score']
        critic_score_list.append(sum)

    plt.bar(genre_list, critic_score_list, width=0.5, color= colors_list)
    plt.show()

def sales_world():

    #Creating a List of total sales per genre
    total_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = int(vg_df.at[i,'Total_Sales'])
                sum += num
        total_sales_list.append(sum)
    
    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display Data in the form of a scatterplot')
        print('5. Display all the graphs at once')
        print('6. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,total_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, total_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            plt.show()
        elif choice == 3:        
            plt.pie(total_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            plt.show()
        elif choice == 4:
                plt.scatter(genre_list, total_sales_list, c=colors_list)
                plt.show()
        elif choice == 5:
            plt.subplot(2,2,1)
            plt.plot(genre_list,total_sales_list)
            
            plt.subplot(2,2,2)
            plt.bar(genre_list, total_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            
            plt.subplot(2,2,3)
            plt.pie(total_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            
            plt.subplot(2,2,4)
            plt.scatter(genre_list, total_sales_list, c=colors_list)
            
            plt.show()
        elif choice == 6:
            return
        else: 
            pass

def sales_NA():
    #Creating a List of sales in north america per genre
    NA_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'NA_Sales']),2)
                sum += num
        NA_sales_list.append(sum)

    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display Data in the form of a scatterplot')
        print('5. Display all the graphs at once')
        print('6. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,NA_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, NA_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            plt.show()
        elif choice == 3:        
            plt.pie(NA_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            plt.show()
        elif choice == 4:
                plt.scatter(genre_list, NA_sales_list, c=colors_list)
                plt.show()
        elif choice == 5:
            plt.subplot(2,2,1)
            plt.plot(genre_list,NA_sales_list)
            
            plt.subplot(2,2,2)
            plt.bar(genre_list, NA_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            
            plt.subplot(2,2,3)
            plt.pie(NA_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            
            plt.subplot(2,2,4)
            plt.scatter(genre_list, NA_sales_list, c=colors_list)
            
            plt.show()
        elif choice == 6:
            return
        else: 
            pass

def sales_JP():
    #Creating a List of sales in japan per genre
    JP_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'JP_Sales']),2)
                sum += num
        JP_sales_list.append(sum)

    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display Data in the form of a scatterplot')
        print('5. Display all the graphs at once')
        print('6. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,JP_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, JP_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            plt.show()
        elif choice == 3:        
            plt.pie(JP_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            plt.show()
        elif choice == 4:
                plt.scatter(genre_list, JP_sales_list, c=colors_list)
                plt.show()
        elif choice == 5:
            plt.subplot(2,2,1)
            plt.plot(genre_list,JP_sales_list)
            
            plt.subplot(2,2,2)
            plt.bar(genre_list, JP_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            
            plt.subplot(2,2,3)
            plt.pie(JP_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            
            plt.subplot(2,2,4)
            plt.scatter(genre_list, JP_sales_list, c=colors_list)
            
            plt.show()
        elif choice == 6:
            return
        else: 
            pass

def sales_PAL():
#Creating a List of sales in europe and africa per genre
    PAL_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'PAL_Sales']),2)
                sum += num
        PAL_sales_list.append(sum)

    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display Data in the form of a scatterplot')
        print('5. Display all the graphs at once')
        print('6. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,PAL_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, PAL_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            plt.show()
        elif choice == 3:        
            plt.pie(PAL_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            plt.show()
        elif choice == 4:
                plt.scatter(genre_list, PAL_sales_list, c=colors_list)
                plt.show()
        elif choice == 5:
            plt.subplot(2,2,1)
            plt.plot(genre_list,PAL_sales_list)
            
            plt.subplot(2,2,2)
            plt.bar(genre_list, PAL_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            
            plt.subplot(2,2,3)
            plt.pie(PAL_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            
            plt.subplot(2,2,4)
            plt.scatter(genre_list, PAL_sales_list, c=colors_list)
            
            plt.show()
        elif choice == 6:
            return
        else: 
            pass

def sales_other():
    #Creating a list of sales in other parts of the world per genre
    other_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'Other_Sales']),2)
                sum += num
        other_sales_list.append(sum)
    
    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display Data in the form of a scatterplot')
        print('5. Display all the graphs at once')
        print('6. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,other_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, other_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            plt.show()
        elif choice == 3:        
            plt.pie(other_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            plt.show()
        elif choice == 4:
                plt.scatter(genre_list, other_sales_list, c=colors_list)
                plt.show()
        elif choice == 5:
            plt.subplot(2,2,1)
            plt.plot(genre_list,other_sales_list)
            
            plt.subplot(2,2,2)
            plt.bar(genre_list, other_sales_list, width=0.5, label = genre_list, color=colors_list)
            plt.legend()
            
            plt.subplot(2,2,3)
            plt.pie(other_sales_list, colors=colors_list)
            plt.legend(genre_list, loc = 'upper right')
            
            plt.subplot(2,2,4)
            plt.scatter(genre_list, other_sales_list, c=colors_list)
            
            plt.show()
        elif choice == 6:
            return
        else: 
            pass

while True:
    print('=============================================================')
    print('1. show first 10 rows of dataframe')
    print('2. Show Abbriviations')
    print('=============================================================')
    print('3. Genre of games sorted by Critic Score')
    print('4. Genre of games sorted by sales world wide')
    print('5. Genre of games sorted by sales in north america')
    print('6. Genre of games sorted by sales in japan')
    print('7. Genre of games sorted by sales in europe and africa')
    print('8. Genre of games sorted by sales in other parts of the world')
    print('9. Quit the program')
    print('=============================================================')
    option = eval(input('choose option: '))
    print('=============================================================')

    if option == 1:
        readcsv()
    elif option == 2:
        abbriviations()
    elif option == 3:
        critic_score_sort()
    elif option == 4:
        sales_world()
    elif option == 5:
        sales_NA()
    elif option == 6:
        sales_JP()
    elif option == 7:
        sales_PAL()
    elif option == 8:
        sales_other()
    elif option == 9:
        quit()
    else:
        pass