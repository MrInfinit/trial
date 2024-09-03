import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import squarify
import streamlit as st
from collections import OrderedDict

# Load data
pathofmainfile = r'C:\Users\ksail\Documents\Python Code\School_Proj\vgchartz-2024.csv'
pathofabbriviations = r'C:\Users\ksail\Documents\Python Code\School_Proj\data_dictionary.csv'

df = pd.read_csv(pathofmainfile)
vg_df = df.ffill()
ab_df = pd.read_csv(pathofabbriviations)

no_of_rows = len(df.index)

# Creating genre and sales lists
genre_list = vg_df['Genre'].unique().tolist()

world_sales_list = vg_df.groupby('Genre')['Total_Sales'].sum().tolist()
NA_sales_list = vg_df.groupby('Genre')['NA_Sales'].sum().tolist()
JP_sales_list = vg_df.groupby('Genre')['JP_Sales'].sum().tolist()
PAL_sales_list = vg_df.groupby('Genre')['PAL_Sales'].sum().tolist()
other_sales_list = vg_df.groupby('Genre')['Other_Sales'].sum().tolist()

# Colors for the charts
colors_list = sns.color_palette("Set3", len(genre_list))

# Extract game titles for analysis
game_list = vg_df['Title'].unique().tolist()

# Streamlit App
st.set_page_config(page_title="Video Game Sales Analysis", layout="wide")

# Create tabs
tab1, tab2 = st.tabs(["Data Analysis", "Data Exploration"])

# Data Exploration Tab
with tab2:
    st.title("Data Exploration")
    
    option = st.radio("Select an option", ["Show First 10 Rows", "Show Abbreviations"],
    horizontal=True
    )

    if option == "Show First 10 Rows":
        st.write(vg_df.head(10))

    elif option == "Show Abbreviations":
        st.write(ab_df)

# Data Analysis Tab
with tab1:
    st.title("Data Analysis")

    analysis_option = st.radio(
        "Choose Analysis Type",
        ["Genre Analysis", "Game Analysis"],
        horizontal=True
    )
    
    sales_option = st.radio(
        "Choose Sales Type",
        ["World Sales", "North America Sales", "Japan Sales", "Europe and Africa Sales", "Other Sales"],
        horizontal=True
    )
    
    # Initialize variables
    game_data = []
    list_option = []

    # Mapping sales option names to DataFrame column names
    sales_option_mapping = {
        "World Sales": "Total_Sales",
        "North America Sales": "NA_Sales",
        "Japan Sales": "JP_Sales",
        "Europe and Africa Sales": "PAL_Sales",
        "Other Sales": "Other_Sales"
    }

    if analysis_option == "Game Analysis":
        # Select games for analysis
        selected_games = st.multiselect(
            "Select up to 10 games for analysis",
            options=game_list,
            max_selections=10
        )

        if selected_games:
            vg_df_filtered = vg_df[vg_df['Title'].isin(selected_games)]
            if vg_df_filtered.empty:
                st.warning("Selected games have no data.")
            else:
                list_option = vg_df_filtered.groupby('Title')[sales_option_mapping[sales_option]].sum().tolist()
                game_data = selected_games
        else:
            st.warning("Please select at least one game.")
    
    else:  # Genre Analysis
        list_option = {
            "World Sales": world_sales_list,
            "North America Sales": NA_sales_list,
            "Japan Sales": JP_sales_list,
            "Europe and Africa Sales": PAL_sales_list,
            "Other Sales": other_sales_list
        }[sales_option]
        game_data = genre_list

    chart_option = st.radio(
        "Select Chart Type",
        ["Line Graph", "Bar Graph", "Pie Chart", "Scatterplot", "Treemap", "Heatmap", "Bubble Chart", "Waterfall Chart", "Show All"],
        horizontal=True
    )

    if analysis_option == "Genre Analysis" or analysis_option == "Game Analysis":
        if not game_data or not list_option:
            st.warning("No data to display. Please select games and sales type.")
        else:
            try:
                if chart_option == "Line Graph":
                    plt.figure(figsize=(10, 6))
                    plt.plot(game_data, list_option, marker='o')
                    plt.title(f'{sales_option} by Game')
                    plt.xlabel('Game')
                    plt.ylabel(sales_option)
                    plt.xticks(rotation=45)
                    st.pyplot(plt)
                
                elif chart_option == "Bar Graph":
                    plt.figure(figsize=(10, 6))
                    plt.bar(game_data, list_option, color=colors_list[:len(game_data)])
                    plt.title(f'{sales_option} by Game')
                    plt.xlabel('Game')
                    plt.ylabel(sales_option)
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

                elif chart_option == "Pie Chart":
                    plt.figure(figsize=(8, 8))
                    plt.pie(list_option, colors=colors_list[:len(game_data)], labels=game_data, autopct='%1.1f%%')
                    plt.title(f'{sales_option} by Game')
                    st.pyplot(plt)

                elif chart_option == "Scatterplot":
                    plt.figure(figsize=(10, 6))
                    plt.scatter(game_data, list_option, c=colors_list[:len(game_data)], s=100)
                    plt.title(f'{sales_option} by Game')
                    plt.xlabel('Game')
                    plt.ylabel(sales_option)
                    plt.xticks(rotation=45)
                    st.pyplot(plt)
                    
                elif chart_option == "Treemap":
                    plt.figure(figsize=(10, 6))
                    squarify.plot(sizes=list_option, label=game_data, color=colors_list[:len(game_data)], alpha=0.7)
                    plt.title(f'Treemap of {sales_option} by Game')
                    plt.axis('off')
                    st.pyplot(plt)
                    
                elif chart_option == "Heatmap":
                    game_sales_df = pd.DataFrame({
                        'Game': game_data,
                        'Total Sales': list_option
                    }).set_index('Game')
                    plt.figure(figsize=(10, 6))
                    sns.heatmap(game_sales_df.T, annot=True, cmap='Reds')
                    plt.title(f'Heatmap of {sales_option} by Game')
                    st.pyplot(plt)
                
                elif chart_option == "Bubble Chart":
                    plt.figure(figsize=(10, 6))
                    bubble_sizes = np.array(list_option) * 100  # Scaling bubble sizes for visibility
                    plt.scatter(game_data, list_option, s=bubble_sizes, alpha=0.5, c=colors_list[:len(game_data)])
                    plt.title(f'Bubble Chart of {sales_option} by Game')
                    plt.xlabel('Game')
                    plt.ylabel(sales_option)
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

                elif chart_option == "Waterfall Chart":
                    ordered_game_sales = OrderedDict(sorted(zip(game_data, list_option), key=lambda x: x[1], reverse=True))
                    cumulative = np.cumsum(list(ordered_game_sales.values()))
                    waterfall_data = {
                        'Games': list(ordered_game_sales.keys()) + ['Total'],
                        'Sales': list(ordered_game_sales.values()) + [0],
                        'Cumulative': list(cumulative) + [cumulative[-1]]
                    }
                    waterfall_df = pd.DataFrame(waterfall_data)
                    waterfall_df.loc[waterfall_df.index[-1], 'Sales'] = waterfall_df.loc[waterfall_df.index[-1], 'Cumulative']
                    waterfall_df['Previous'] = waterfall_df['Cumulative'].shift(1).fillna(0)
                    plt.figure(figsize=(10, 6))
                    plt.bar(waterfall_df['Games'], waterfall_df['Sales'], bottom=waterfall_df['Previous'], color=colors_list[:len(ordered_game_sales)], alpha=0.7)
                    plt.title(f'Waterfall Chart of {sales_option} by Game')
                    plt.xlabel('Game')
                    plt.ylabel('Sales')
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

                elif chart_option == "Show All":
                    fig, axs = plt.subplots(3, 3, figsize=(18, 12))

                    axs[0, 0].plot(game_data, list_option, marker='o')
                    axs[0, 0].set_title('Line Graph')
                    axs[0, 0].set_xticks(range(len(game_data)))
                    axs[0, 0].set_xticklabels(game_data, rotation=45)

                    axs[0, 1].bar(game_data, list_option, color=colors_list[:len(game_data)])
                    axs[0, 1].set_title('Bar Graph')
                    axs[0, 1].set_xticks(range(len(game_data)))
                    axs[0, 1].set_xticklabels(game_data, rotation=45)

                    axs[0, 2].pie(list_option, labels=game_data, autopct='%1.1f%%')
                    axs[0, 2].set_title('Pie Chart')

                    game_sales_df = pd.DataFrame({
                        'Title': game_data,
                        'Total Sales': list_option
                    }).set_index('Title')
                    
                    sns.heatmap(game_sales_df.T, annot=True, cmap='Reds', ax=axs[1, 0])
                    axs[1, 0].set_title('Heatmap')

                    axs[1, 1].scatter(game_data, list_option, color=colors_list[:len(game_data)], s=100)
                    axs[1, 1].set_title('Scatterplot')
                    axs[1, 1].set_xticks(range(len(game_data)))
                    axs[1, 1].set_xticklabels(game_data, rotation=45)

                    squarify.plot(sizes=list_option, label=game_data, color=colors_list[:len(game_data)], alpha=0.7, ax=axs[1, 2])
                    axs[1, 2].set_title('Treemap')
                    axs[1, 2].axis('off')

                    bubble_sizes = np.array(list_option) * 100
                    axs[2, 0].scatter(game_data, list_option, s=bubble_sizes, alpha=0.5, color=colors_list[:len(game_data)])
                    axs[2, 0].set_title('Bubble Chart')
                    axs[2, 0].set_xticks(range(len(game_data)))
                    axs[2, 0].set_xticklabels(game_data, rotation=45)

                    ordered_game_sales = OrderedDict(sorted(zip(game_data, list_option), key=lambda x: x[1], reverse=True))
                    cumulative = np.cumsum(list(ordered_game_sales.values()))
                    waterfall_data = {
                        'Games': list(ordered_game_sales.keys()) + ['Total'],
                        'Sales': list(ordered_game_sales.values()) + [0],
                        'Cumulative': list(cumulative) + [cumulative[-1]]
                    }
                    waterfall_df = pd.DataFrame(waterfall_data)
                    waterfall_df.loc[waterfall_df.index[-1], 'Sales'] = waterfall_df.loc[waterfall_df.index[-1], 'Cumulative']
                    waterfall_df['Previous'] = waterfall_df['Cumulative'].shift(1).fillna(0)
                    axs[2, 1].bar(waterfall_df['Games'], waterfall_df['Sales'], bottom=waterfall_df['Previous'], color=colors_list[:len(ordered_game_sales)], alpha=0.7)
                    axs[2, 1].set_title('Waterfall Chart')
                    axs[2, 1].set_xticks(range(len(waterfall_df['Games'])))
                    axs[2, 1].set_xticklabels(waterfall_df['Games'], rotation=45)

                    for ax in axs.flat:
                        ax.label_outer()

                    plt.tight_layout()
                    st.pyplot(fig)
                
            except Exception as e:
                st.error(f"An error occurred while plotting: {e}")

