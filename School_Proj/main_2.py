import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import squarify
from collections import OrderedDict


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


#Creating a List of total sales per genre
world_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'Total_Sales'])
            sum += num
    world_sales_list.append(sum)
            
#Creating a List of sales in north america per genre
NA_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = round((vg_df.at[i,'NA_Sales']),2)
            sum += num
    NA_sales_list.append(sum)

#Creating a List of sales in japan per genre
JP_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = round((vg_df.at[i,'JP_Sales']),2)
            sum += num
    JP_sales_list.append(sum)

#Creating a List of sales in europe and africa per genre
PAL_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = round((vg_df.at[i,'PAL_Sales']),2)
            sum += num
    PAL_sales_list.append(sum)
            
#Creating a list of sales in other parts of the world per genre
other_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = round((vg_df.at[i,'Other_Sales']),2)
            sum += num
    other_sales_list.append(sum)


#List for the colors required in the graphs
colors_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'Indigo','LightSeaGreen', 'Aqua', 'CadetBlue']

#Creating functions that can be run from the options panel
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

# options to display graphs
def graphs(list_option):
    while True:
        print('=============================================================')
        print('   1. Line Graph of Total Sales by Genre')
        print('   2. Bar Graph of Total Sales by Genre')
        print('   3. Pie Chart of Total Sales by Genre')
        print('   4. Scatterplot of Total Sales by Genre')
        print('   5. Display Waterfall Chart')
        print('   6. Display Heatmap')
        print('   7. Display Bubble Chart')
        print('   8. Display Treemap')
        print('   9. Display All Charts')
        print('   10. Return to Main Menu')
        print('=============================================================')
        choice = input('Choose an option: ')
        print('=============================================================')

        if choice == '1':
            plt.plot(genre_list, list_option, marker='o')
            plt.title('Total Sales by Genre')
            plt.xlabel('Genre')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '2':
            plt.bar(genre_list, list_option, width=0.5, color=colors_list)
            plt.title('Total Sales by Genre')
            plt.xlabel('Genre')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '3':
            plt.pie(list_option, colors=colors_list, labels=genre_list, autopct='%1.1f%%')
            plt.title('Total Sales by Genre')
            plt.show()
        elif choice == '4':
            plt.scatter(genre_list, list_option, c=colors_list)
            plt.title('Total Sales by Genre')
            plt.xlabel('Genre')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45)
            plt.show()
        elif choice == '9':
            # Create a grid of subplots with specified rows and columns
            fig, axs = plt.subplots(3, 3, figsize=(18, 12))  # 3x3 grid

            # Line Graph
            axs[0, 0].plot(genre_list, list_option, marker='o')
            axs[0, 0].set_title('Line Graph')
            axs[0, 0].set_xticks(range(len(genre_list)))
            axs[0, 0].set_xticklabels(genre_list, rotation=45)

            # Bar Graph
            axs[0, 1].bar(genre_list, list_option, color='blue')
            axs[0, 1].set_title('Bar Graph')
            axs[0, 1].set_xticks(range(len(genre_list)))
            axs[0, 1].set_xticklabels(genre_list, rotation=45)

            # Pie Chart
            axs[0, 2].pie(list_option, labels=genre_list, autopct='%1.1f%%')
            axs[0, 2].set_title('Pie Chart')

            # Heatmap
            genre_sales_df = pd.DataFrame({
                'Genre': genre_list,
                'Total Sales': list_option
            }).set_index('Genre')
            
            sns.heatmap(genre_sales_df.T, annot=True, cmap='Reds', ax=axs[1, 0])
            axs[1, 0].set_title('Heatmap')

            # Scatterplot
            axs[1, 1].scatter(genre_list, list_option, color=colors_list, s=100)
            axs[1, 1].set_title('Scatterplot')
            axs[1, 1].set_xticks(range(len(genre_list)))
            axs[1, 1].set_xticklabels(genre_list, rotation=45)

            # Bubble Chart
            bubble_sizes = np.array(list_option) * 100  # Scaling bubble sizes for visibility
            axs[1, 2].scatter(genre_list, list_option, s=bubble_sizes, c=colors_list, alpha=0.5)
            axs[1, 2].set_title('Bubble Chart')
            axs[1, 2].set_xticks(range(len(genre_list)))
            axs[1, 2].set_xticklabels(genre_list, rotation=45)

            # Treemap
            squarify.plot(sizes=list_option, label=genre_list, color=colors_list, alpha=0.7, ax=axs[2, 0])
            axs[2, 0].axis('off')
            axs[2, 0].set_title('Treemap')

            # Waterfall Chart
            ordered_genre_sales = OrderedDict(sorted(zip(genre_list, list_option), key=lambda x: x[1], reverse=True))
            cumulative = np.cumsum(list(ordered_genre_sales.values()))
            waterfall_data = {
                'Genres': list(ordered_genre_sales.keys()) + ['Total'],
                'Sales': list(ordered_genre_sales.values()) + [0],
                'Cumulative': list(cumulative) + [cumulative[-1]]
            }
            waterfall_df = pd.DataFrame(waterfall_data)
            waterfall_df.loc[waterfall_df.index[-1], 'Sales'] = waterfall_df.loc[waterfall_df.index[-1], 'Cumulative']

            waterfall_df['Previous'] = waterfall_df['Cumulative'].shift(1).fillna(0)
            axs[2, 1].bar(waterfall_df['Genres'], waterfall_df['Sales'], bottom=waterfall_df['Previous'], color=colors_list[:len(ordered_genre_sales)], alpha=0.7)
            axs[2, 1].set_title('Waterfall Chart')
            axs[2, 1].set_xticks(range(len(genre_list)))
            axs[2, 1].set_xticklabels(genre_list, rotation=45)

            # Hide any unused subplot (optional)
            axs[2, 2].axis('off')  # Hides the last subplot

            # Adjust layout so everything fits without overlap
            plt.tight_layout()

            # Display the plots
            plt.show()

        elif choice == '6':  # Heatmap
            genre_sales_df = pd.DataFrame({
                'Genre': genre_list,
                'Total Sales': list_option
            }).set_index('Genre')
            
            sns.heatmap(genre_sales_df.T, annot=True, cmap='Reds')
            plt.title('Heatmap of Total Sales by Genre')
            plt.show()

        elif choice == '7':  # Bubble Chart
            bubble_sizes = np.array(list_option) * 100  # Scaling bubble sizes for visibility
            plt.scatter(genre_list, list_option, s=bubble_sizes, alpha=0.5, c=colors_list)
            plt.title('Bubble Chart of Total Sales by Genre')
            plt.xlabel('Genre')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45)
            plt.show()

        elif choice == '8':  # Treemap
            squarify.plot(sizes=list_option, label=genre_list, color=colors_list, alpha=0.7)
            plt.title('Treemap of Total Sales by Genre')
            plt.axis('off')
            plt.show()

        elif choice == '5':  # Waterfall Chart
            ordered_genre_sales = OrderedDict(sorted(zip(genre_list, list_option), key=lambda x: x[1], reverse=True))
            cumulative = np.cumsum(list(ordered_genre_sales.values()))
            waterfall_data = {
                'Genres': list(ordered_genre_sales.keys()) + ['Total'],
                'Sales': list(ordered_genre_sales.values()) + [0],
                'Cumulative': list(cumulative) + [cumulative[-1]]
            }
            waterfall_df = pd.DataFrame(waterfall_data)
            waterfall_df.loc[waterfall_df.index[-1], 'Sales'] = waterfall_df.loc[waterfall_df.index[-1], 'Cumulative']

            waterfall_df['Previous'] = waterfall_df['Cumulative'].shift(1).fillna(0)
            plt.bar(waterfall_df['Genres'], waterfall_df['Sales'], bottom=waterfall_df['Previous'], color=colors_list[:len(ordered_genre_sales)], alpha=0.7)
            plt.title('Waterfall Chart of Total Sales by Genre')
            plt.xlabel('Genre')
            plt.ylabel('Sales')
            plt.xticks(rotation=45)
            plt.show()

        elif choice == '10':
            return
        else:
            print("Invalid option, please try again.")

#main loop for the program
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
        graphs(world_sales_list)
    elif option == 5:
        graphs(NA_sales_list)
    elif option == 6:
        graphs(JP_sales_list)
    elif option == 7:
        graphs(PAL_sales_list)
    elif option == 8:
        graphs(other_sales_list)
    elif option == 9:
        quit()
    else:
        pass