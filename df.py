import pandas as pd

data = pd.read_csv('melbourne_ta_reviews.csv', sep = ',')

# -------- Search by price ------------

# /////   Cheapest price   //////////

# Order by ranking
sp_cat1_rp = data[data['priceLevel'] == '$'].sort_values(by = 'rankingPosition').head(5)
# Order by rating
sp_cat1_rt = data[data['priceLevel'] == '$'].sort_values(by = 'rating', ascending=False).head(5)
# Order by amount of reviews
sp_cat1_rv = data[data['priceLevel'] == '$'].sort_values(by = 'numberOfReviews', ascending=False).head(5)


#  //// Medium Price ///////////

# Order by ranking
sp_cat2_rp = data[data['priceLevel'] == '$$ - $$$'].sort_values(by = 'rankingPosition').head(5)
# Order by rating
sp_cat2_rt = data[data['priceLevel'] == '$$ - $$$'].sort_values(by = 'rating', ascending=False).head(5)
# Order by amount of reviews
sp_cat2_rv = data[data['priceLevel'] == '$$ - $$$'].sort_values(by = 'numberOfReviews', ascending=False).head(5)


#  ////// High Price //////////

# Order by ranking
sp_cat3_rp = data[data['priceLevel'] == '$$$$'].sort_values(by = 'rankingPosition').head(5)
# Order by rating
sp_cat3_rt = data[data['priceLevel'] == '$$$$'].sort_values(by = 'rating', ascending= False).head(5)
# Order by amount of reviews
sp_cat3_rv = data[data['priceLevel'] == '$$$$'].sort_values(by = 'numberOfReviews', ascending=False).head(5)