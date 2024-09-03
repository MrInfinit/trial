import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify  # For Treemap
from collections import OrderedDict

# File paths
path_of_main_file = r'C:\Users\ksail\Documents\Python Code\School_Proj\vgchartz-2024.csv'
path_of_abbreviations = r'C:\Users\ksail\Documents\Python Code\School_Proj\data_dictionary.csv'

# Reading the data
vg_df = pd.read_csv(path_of_main_file).ffill()  # Fill missing values
ab_df = pd.read_csv(path_of_abbreviations)
no_of_rows = len(vg_df.index)

# Creating a list of all genres in the dataframe
genre_list = vg_df['Genre'].unique().tolist()

# Function to display the main dataframe
def display_main_df():
    print(vg_df)

# Function to display the abbreviations
def display_abbreviations():
    print(ab_df)

# Function to sort and display genres by average critic score
def sort_by_critic_score():
    critic_score_list = []
    for genre in genre_list:
        genre_scores = vg_df[vg_df['Genre'] == genre]['Critic_Score'].sum()
        critic_score_list.append(genre_scores)

    plt.bar(genre_list, critic_score_list, width=0.5)
    plt.title('Average Critic Score by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Critic Score')
    plt.xticks(rotation=45)
    plt.show()

# Function to display sales data in various formats
def display_sales_worldwide():
    total_sales_list = []
    for genre in genre_list:
        genre_sales = vg_df[vg_df['Genre'] == genre]['Total_Sales'].sum()
        total_sales_list.append(genre_sales)

    colors_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 
                   'Indigo', 'LightSeaGreen', 'Aqua', 'CadetBlue']

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

# Function to display sales data for North America
def display_sales_NA():
    NA_sales_list = []
    for genre in genre_list:
        genre_sales = vg_df[vg_df['Genre'] == genre]['NA_Sales'].sum()
        NA_sales_list.append(genre_sales)

    plt.bar(genre_list, NA_sales_list, width=0.5)
    plt.title('Sales in North America by Genre')
    plt.xlabel('Genre')
    plt.ylabel('NA Sales')
    plt.xticks(rotation=45)
    plt.show()

# Function to display sales data for Europe
def display_sales_EU():
    EU_sales_list = []
    for genre in genre_list:
        genre_sales = vg_df[vg_df['Genre'] == genre]['EU_Sales'].sum()
        EU_sales_list.append(genre_sales)

    plt.bar(genre_list, EU_sales_list, width=0.5)
    plt.title('Sales in Europe by Genre')
    plt.xlabel('Genre')
    plt.ylabel('EU Sales')
    plt.xticks(rotation=45)
    plt.show()

# Main function to execute the program
def main():
    while True:
        print('=============================================================')
        print('   1. Display Main DataFrame')
        print('   2. Display Data Abbreviations')
        print('   3. Display Sales Data Worldwide')
        print('   4. Display Sales Data for North America')
        print('   5. Display Sales Data for Europe')
        print('   6. Display Top Genres by Average Critic Score')
        print('   7. Exit')
        print('=============================================================')
        choice = input('Choose an option: ')
        print('=============================================================')

        if choice == '1':
            display_main_df()
        elif choice == '2':
            display_abbreviations()
        elif choice == '3':
            display_sales_worldwide()
        elif choice == '4':
            display_sales_NA()
        elif choice == '5':
            display_sales_EU()
        elif choice == '6':
            sort_by_critic_score()
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print("Invalid option, please try again.")

# Run the main function
main()