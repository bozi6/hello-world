"""Mapping products and reviews.
All column numbering starts from 0

#Product fields
PRODUCT_ID: Which column in the xlsx file contains the product ID?
PRODUCT_PARENT: Which column in the xlsx file contains the parent product ID?
PRODUCT_TITLE: Which column in the xlsx file contains the product title?
PRODUCT_CATEGORY: Which column in the xlsx file contains the product category?

#Review fields
REVIEW_ID: Which column in the xlsx file contains the review ID?
REVIEW_CUSTOMER: Which column in the xlsx file contains the customer ID?
REVIEW_STARS: Which column in the xlsx file contains the review stars?
REVIEW_HEADLINE: Which column in the xlsx file contains the review headline?
REVIEW_BODY: Which column in the xlsx file contains the review body text
REVIEW_DATE: Which column in the xlsx file contains the review date?

"""

#Product fields
PRODUCT_ID = 3
PRODUCT_PARENT = 4
PRODUCT_TITLE = 5
PRODUCT_CATEGORY = 6

#Review fields
REVIEW_ID = 2
REVIEW_CUSTOMER = 1
REVIEW_STARS = 7
REVIEW_HEADLINE = 12
REVIEW_BODY = 13
REVIEW_DATE = 14

#Strange fields
HELPFUL_VOTES = 8
TOTAL_VOTES = 9
VINE = 10
VERIFIED_PURCHASE = 11