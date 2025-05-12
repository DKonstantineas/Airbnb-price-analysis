import mysql.connector
from mysql.connector import errorcode


def setup_airbnb_databases():
    # MySQL connection settings
    config = {
        "host": "localhost",
        "user": "root",
        "password": "Dimitris19961996!"  # your actual password
    }

    # Database names
    databases = ["airbnb_athens", "airbnb_thessaloniki"]

    # Table definitions
    tables = {
        "listings": """
        CREATE TABLE listings (
            listing_id INT AUTO_INCREMENT PRIMARY KEY,
            id INT,
            listing_url VARCHAR(255),
            scrape_id BIGINT,
            last_scraped DATE,
            source VARCHAR(50),
            name VARCHAR(255),
            description TEXT,
            neighborhood_overview TEXT,
            picture_url VARCHAR(255),
            host_id INT,
            host_url VARCHAR(255),
            host_name VARCHAR(100),
            host_since DATE,
            host_location VARCHAR(100),
            host_about TEXT,
            host_response_time VARCHAR(50),
            host_response_rate VARCHAR(20),
            host_acceptance_rate VARCHAR(20),
            host_is_superhost BOOLEAN,
            host_thumbnail_url VARCHAR(255),
            host_picture_url VARCHAR(255),
            host_neighbourhood VARCHAR(100),
            host_listings_count INT,
            host_total_listings_count INT,
            host_verifications TEXT,
            host_has_profile_pic BOOLEAN,
            host_identity_verified BOOLEAN,
            neighbourhood VARCHAR(100),
            neighbourhood_cleansed VARCHAR(100),
            neighbourhood_group_cleansed VARCHAR(100),
            latitude DECIMAL(10, 8),
            longitude DECIMAL(11, 8),
            property_type VARCHAR(100),
            room_type VARCHAR(50),
            accommodates INT,
            bathrooms FLOAT,
            bathrooms_text VARCHAR(50),
            bedrooms INT,
            beds INT,
            amenities TEXT,
            price DECIMAL(10, 2),
            minimum_nights INT,
            maximum_nights INT,
            minimum_minimum_nights INT,
            maximum_minimum_nights INT,
            minimum_maximum_nights INT,
            maximum_maximum_nights INT,
            minimum_nights_avg_ntm FLOAT,
            maximum_nights_avg_ntm FLOAT,
            calendar_updated VARCHAR(100),
            has_availability BOOLEAN,
            availability_30 INT,
            availability_60 INT,
            availability_90 INT,
            availability_365 INT,
            calendar_last_scraped DATE,
            number_of_reviews INT,
            number_of_reviews_ltm INT,
            number_of_reviews_l30d INT,
            first_review DATE,
            last_review DATE,
            review_scores_rating FLOAT,
            review_scores_accuracy FLOAT,
            review_scores_cleanliness FLOAT,
            review_scores_checkin FLOAT,
            review_scores_communication FLOAT,
            review_scores_location FLOAT,
            review_scores_value FLOAT,
            license VARCHAR(50),
            instant_bookable BOOLEAN,
            calculated_host_listings_count INT,
            calculated_host_listings_count_entire_homes INT,
            calculated_host_listings_count_private_rooms INT,
            calculated_host_listings_count_shared_rooms INT,
            reviews_per_month FLOAT
        )
        """,
        "calendar": """
            CREATE TABLE IF NOT EXISTS calendar (
                calendar_id  INT AUTO_INCREMENT PRIMARY KEY,
                listing_id BIGINT,
                date DATE,
                available VARCHAR(250),
                price DECIMAL,
                adjusted_price VARCHAR(250),
                minimum_nights INT,
                maximum_nights INT
            )
        """,
        "reviews": """
            CREATE TABLE IF NOT EXISTS reviews (
                reviews_id INT AUTO_INCREMENT PRIMARY KEY,
                listing_id INT,
                id INT,
                date DATE,
                reviewer_id INT,
                reviewer_name VARCHAR(255),
                comments TEXT
            )
        """
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        for db in databases:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
            print(f"Database created or exists: {db}")

            cursor.execute(f"USE {db}")

            # Create all tables from the 'tables' dictionary
            for table_name, table_creation_query in tables.items():
                cursor.execute(table_creation_query)
                print(f"'{table_name}' table created or exists in {db}")

        cursor.close()
        conn.close()
        print("All databases and tables set up successfully.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied. Check your MySQL username or password.")
        else:
            print(f"MySQL error: {err}")
