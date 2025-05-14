# database/insert_data.py

import mysql.connector
import pandas as pd
import os

def insert_data_for_area(db_name, area_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dimitris19961996!",
        database=db_name
    )
    cursor = conn.cursor()

    # Define paths for CSV files for each table (Adjust your folder paths accordingly)
    base_folder = f"data/{area_name}"  # Folder for the area (e.g., "athens" or "thessaloniki")
    
    # Define the full paths for each CSV file
    listings_csv = os.path.join(base_folder, "check.csv")
    calendar_csv = os.path.join(base_folder, "calendar.csv")
    reviews_csv = os.path.join(base_folder, "reviews.csv")

    # Check if the CSV files exist before proceeding
    if not os.path.exists(listings_csv) or not os.path.exists(calendar_csv) or not os.path.exists(reviews_csv):
        print(f"Error: One or more CSV files are missing in {base_folder}")
        return

    df_listings = pd.read_csv(
    listings_csv,
     encoding='utf-8',        # Use 'utf-8-sig' if BOM errors happen
)

    #df_listings = df_listings.where(pd.notnull(df_listings), None)  # Handle NaN values

    listings_insert_query = """
        INSERT INTO listings (
            listing_id, listing_url, scrape_id, last_scraped, source, name,
            description, neighborhood_overview, picture_url, host_id,
            host_url, host_name, host_since, host_location, host_about,
            host_response_time, host_response_rate, host_acceptance_rate,
            host_is_superhost, host_thumbnail_url, host_picture_url,
            host_neighbourhood, host_listings_count, host_total_listings_count,
            host_verifications, host_has_profile_pic, host_identity_verified,
            neighbourhood, neighbourhood_cleansed, neighbourhood_group_cleansed,
            latitude, longitude, property_type, room_type, accommodates,
            bathrooms, bathrooms_text, bedrooms, beds, amenities, price,
            minimum_nights, maximum_nights, minimum_minimum_nights,
            maximum_minimum_nights, minimum_maximum_nights,
            maximum_maximum_nights, minimum_nights_avg_ntm,
            maximum_nights_avg_ntm, calendar_updated, has_availability,
            availability_30, availability_60, availability_90, availability_365,
            calendar_last_scraped, number_of_reviews, number_of_reviews_ltm,
            number_of_reviews_l30d, first_review, last_review,
            review_scores_rating, review_scores_accuracy, review_scores_cleanliness,
            review_scores_checkin, review_scores_communication, review_scores_location,
            review_scores_value, license, instant_bookable,
            calculated_host_listings_count, calculated_host_listings_count_entire_homes,
            calculated_host_listings_count_private_rooms, calculated_host_listings_count_shared_rooms,
            reviews_per_month
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s)
    """

    for row in df_listings.itertuples(index=False, name=None):
        try:
            print(row)
            cursor.execute(listings_insert_query, row)
        except mysql.connector.Error as e:
            print(f"Error inserting listing row: {e}")

    conn.commit()

    # Insert data into the 'calendar' table
    df_calendar = pd.read_csv(calendar_csv)
    for col in ['price', 'adjusted_price']:
        df_calendar[col] = df_calendar[col].replace(r'[\$,]', '', regex=True).astype(float)

    df_calendar['adjusted_price']='None'
    print(df_calendar.head().to_string)
    calendar_insert_query = """
        INSERT INTO calendar (
            listing_id, date, available, price, adjusted_price, minimum_nights, maximum_nights
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for row in df_calendar.itertuples(index=False, name=None):
        try:
            cursor.execute(calendar_insert_query, row)
        except mysql.connector.Error as e:
            print(f"Error inserting calendar row: {e}")

    conn.commit()

    # Insert data into the 'reviews' table
    df_reviews = pd.read_csv(reviews_csv)
    df_reviews = df_reviews.where(pd.notnull(df_reviews), None)  # Handle NaN values

    reviews_insert_query = """
        INSERT INTO reviews (
            listing_id, id, date, reviewer_id, reviewer_name, comments
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in df_reviews.itertuples(index=False, name=None):
        try:
            cursor.execute(reviews_insert_query, row)
        except mysql.connector.Error as e:
            print(f"Error inserting review row: {e}")

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Data insertion for {area_name} completed successfully.")


# Call the function for both Athens and Thessaloniki
def main():
    insert_data_for_area("airbnb_athens", "athens(airbnb)")
    insert_data_for_area("airbnb_thessaloniki", "thessaloniki(airbnb)")

if __name__ == "__main__":
    main()
