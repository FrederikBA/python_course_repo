import pandas as pd

df = pd.read_csv("Highest Holywood Grossing Movies.csv")

# 1. Find the top 10 highest grossing Disney movies measured by world sales
def highest_grossing_disney_movies():
    disney_movies = df[
        df["Distributor"].str.contains("Walt Disney Studios Motion Pictures") == True
    ]

    new_index_data = disney_movies.set_index("Title")

    disney_movies_by_world_sales = pd.Series(new_index_data["World Sales (in $)"])

    return disney_movies_by_world_sales.nlargest(10)


# 2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)
def license_distribution():
    distribution_dict = df["License"].value_counts().to_dict()

    licensed_movies_count = sum(distribution_dict.values())

    total_movies = df.shape[0]

    unlicensed_movies = total_movies - licensed_movies_count

    distribution_dict["Not available"] = unlicensed_movies

    return distribution_dict


# 3. Get the percentage of PG rated movies between 2001 and 2015
def percentage_of_pg_rated_movies():

    # Year range
    year_range = [
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]

    # Find occurences of PG-rated movies by year.
    data = df[df["License"].str.contains("PG") == True]

    pg_rated_movies = data[data["License"].str.contains("PG-13") == False]

    pg_rated_movies["Release Date"] = (
        pg_rated_movies["Release Date"].str.split(",").str.get(-1).str.strip()
    )

    certain_years_pg = pg_rated_movies[pg_rated_movies["Release Date"].isin(year_range)]

    occurences_of_pg_rated = certain_years_pg.groupby("Release Date").size().to_dict()

    # Find occurences of all licensed movies
    all_licenses = df

    all_licenses["Release Date"] = (
        all_licenses["Release Date"].str.split(",").str.get(-1).str.strip()
    )

    certain_years_all = all_licenses[all_licenses["Release Date"].isin(year_range)]

    occurences_of_all = certain_years_all.groupby("Release Date").size().to_dict()

    # Calculate percentage of PG movies for each value in dict
    percentage_dict = {}
    for (k, v), (k2, v2) in zip(
        occurences_of_pg_rated.items(), occurences_of_all.items()
    ):
        percentage = v / v2 * 100
        percentage_dict[k] = percentage

    return percentage_dict


# 4. Calculate the average of world sales for each genre and visualize the data with a bar chart.


print(df)
