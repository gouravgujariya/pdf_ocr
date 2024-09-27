# # importing required classes
# from pypdf import PdfReader
#
# # creating a pdf reader object
# reader = PdfReader('C:\\Users\\ergou\\PycharmProjects\\pythonProject\\pdf_txt_api\\pdf_data\\Application_formg.pdf', 'rb')
#
# # printing number of pages in pdf file
# print(len(reader.pages))
#
# # creating a page object
# page = reader.pages[0]
#
# # extracting text from page
# print(page.extract_text())

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Constants for dataset generation
NUM_RECORDS = 1000
REEL_IDS = [f"reel_{i}" for i in range(1, NUM_RECORDS + 1)]
PRODUCT_IDS = [f"product_{i}" for i in range(1, NUM_RECORDS + 1)]
CATEGORIES = ["Fashion", "Electronics", "Home Decor", "Beauty", "Sports"]
# HASHTAGS = ["#sale", "#trending", "#new", "#discount", "#shopnow"]
# PRICE
PRODUCT_DESCRIPTION
# PURCHASE_COUNT
# Generate synthetic data
data = {
    "Reel ID": REEL_IDS,
    "Product ID": random.choices(PRODUCT_IDS, k=NUM_RECORDS),
    "User ID": random.choices(USER_IDS, k=NUM_RECORDS),
    "Category": random.choices(CATEGORIES, k=NUM_RECORDS),
    "Hashtags": [random.sample(HASHTAGS, k=random.randint(1, 3)) for _ in range(NUM_RECORDS)],
    "Keywords": [random.sample(KEYWORDS, k=random.randint(1, 3)) for _ in range(NUM_RECORDS)],
    "Visual Features": [random.choice(VISUAL_FEATURES) for _ in range(NUM_RECORDS)],
    "Likes": np.random.randint(0, 1000, size=NUM_RECORDS),
    "Shares": np.random.randint(0, 500, size=NUM_RECORDS),
    "Comments": np.random.randint(0, 300, size=NUM_RECORDS),
    "Purchase Count": np.random.randint(0, 200, size=NUM_RECORDS)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Hashtags and Keywords lists to string format
df['Hashtags'] = df['Hashtags'].apply(lambda x: ', '.join(x))
df['Keywords'] = df['Keywords'].apply(lambda x: ', '.join(x))

# Display the first few rows of the synthetic dataset
print(df.head())

# Optionally, save to a CSV file
df.to_csv("synthetic_reel_product_data.csv", index=False)
