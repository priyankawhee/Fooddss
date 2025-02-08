import pandas as pd
import json

# Load the CSV data
df = pd.read_csv('cleaned_reviews_recipes.csv')

# Use only relevant columns present in the dataset
relevant_columns = ['Rating', 'RecipeCategory', 'AuthorName_x', 'Name']
df = df[relevant_columns]

# Generate JSON data for visualizations
rating_counts = df['Rating'].value_counts().to_dict()
top_categories = df['RecipeCategory'].value_counts().nlargest(10).to_dict()
top_authors = df['AuthorName_x'].value_counts().nlargest(10).to_dict()

# Create the dashboard data dictionary
dashboard_data = {
    "rating_counts": rating_counts,
    "top_categories": top_categories,
    "top_authors": top_authors
}

# Write the dashboard data to JSON file
with open('dashboard_data.json', 'w') as json_file:
    json.dump(dashboard_data, json_file)

print("dashboard_data.json has been updated successfully!")
