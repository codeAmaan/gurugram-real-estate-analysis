import pandas as pd


def load_and_clean_data():

    df = pd.read_csv("./data/data of gurugram real Estate.csv")

    #cleaning datasets columns
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    #drop duplicates
    df = df.drop_duplicates()

    #Numeric Columns Cleaning
    df["price"] = (
        df["price"].astype(str).str.replace(",", "").astype(int)
    ) 

    df["rate_per_sqft"] = (
        df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)
    )

    #Categorical Columns Cleaning
    df["status"] = df["status"].str.strip().str.lower()
    df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
    df["flat_type"] = df["flat_type"].str.strip().str.lower()


    return df


def analyze_data(df):
        
    # Questions 1: Which is the costliest flat in the datasets?
    costliest_flat = df.loc[df["price"].idxmax()]
    # print(f'The costliest flat is a {costliest_flat['bhk_count']} BHK flat located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} crore in {costliest_flat['society']} society.')

    # Qusetion 2: Which locality has the highest average price in dataset
    highest_price_avg_locality = df.groupby("locality")["price"].mean().idxmax()
    # print(f'The locality with the highest average price is: {highest_price_avg_locality}.')

    # Question 3: which locality has the highest rate per square foot?
    highest_rate_locality = df.groupby("locality")["rate_per_sqft"].mean().idxmax()
    # print(f"The locality with the highest rate per square foot is: {highest_rate_locality}.")

    # Question 4: Do ready-to-move properties cost more than under-construction properties
    ready_to_move_avg_price = df[df["status"] == "ready to move"]["price"].mean()
    under_construction_avg_price = df[df["status"] == "under construction"]["price"].mean()

    # print("Ready to move:", ready_to_move_avg_price)
    # print("Under construction:", under_construction_avg_price)

    # if ready_to_move_avg_price > under_construction_avg_price:
    #      print("Ready-to-move properties cost more on average than under-construction properties")
    # else:
    #         print("Under-construction properties cost more on average than Ready-to-move properties")

    # Question 5: Do RERA-approved properties command a price premium?

    rera_approved_avg_price = df[df["rera_approval"] == "approved by rera"]["price"].mean()
    rera_not_approved_avg_price = df[df["rera_approval"] == "not approved by rera"]['price'].mean()

    # print("Rera-Approved_avg_price: ", rera_approved_avg_price)
    # print("Rera-Not_Approved_avg_price: ", rera_not_approved_avg_price)
    # if rera_approved_avg_price > rera_not_approved_avg_price:
    #     print("RERA-approved properties command a price premium")
    # else:
    #     print("RERA-approved properties do not command a price premium")


    # Question 7: Which BHK configuration is most expensive based on per_square_foot?
    clean_bhk_df = df[df["flat_type"] != 'plot']
    most_expensive_bhk = clean_bhk_df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
    # print(most_expensive_bhk)
    # print(f'The most expensive BHK configuration on average is :{most_expensive_bhk} BHK.')

    # Question 8: Which property type is the costliest?
    most_expensive_property_type = df.groupby("flat_type")['rate_per_sqft'].mean().idxmax()
    # print(f'The most expensive property type is: {most_expensive_property_type}.')

    # Q9: Which companies price their properties higher?

    company_stats = (
        df.groupby('company_name')['rate_per_sqft']
        .agg(['mean', 'count'])
    )

    # Only companies with at least 10 properties
    reliable_companies = company_stats[company_stats['count'] >= 10]

    # Top 5 companies by average rate per sqft
    top_5_builders = (
        reliable_companies['mean']
        .sort_values(ascending=False)
        .head(5)
    )



    return{
        "costliest_flat": costliest_flat,
        "highest_price_avg_locality": highest_price_avg_locality,
        "highest_rate_locality": highest_rate_locality,
        "ready_to_move_avg_price": ready_to_move_avg_price,
        "under_construction_avg_price": under_construction_avg_price,
        "rera_approved_avg_price": rera_approved_avg_price,
        "rera_not_approved_avg_price": rera_not_approved_avg_price,
        "most_expensive_bhk": most_expensive_bhk,
        "most_expensive_property_type": most_expensive_property_type,
        "top_5_companies": top_5_builders
    }


if __name__ == '__main__':
    df = load_and_clean_data()
    result = analyze_data(df)

    print(result['highest_price_avg_locality'])
    print(result['top_5_companies'])