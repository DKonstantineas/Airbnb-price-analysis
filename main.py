# main.py

from database.database_connection import setup_airbnb_databases
from database.insert_data import insert_data_for_area

def main():
    # Step 1: Setup the databases and tables
    print("Starting Airbnb project setup...")
    setup_airbnb_databases()  # This will create the databases and tables
    print("Setup complete.")
    
    # Step 2: Insert data for Athens
    print("Inserting data for Athens...")
    insert_data_for_area("airbnb_athens", "Athens(airbnb)")  # This will insert data into the Athens database
    print("Data for Athens inserted successfully.")
    
    # # Step 3: Insert data for Thessaloniki
    # print("Inserting data for Thessaloniki...")
    # insert_data_for_area("airbnb_thessaloniki", "Thessaloniki(airbnb)")  # This will insert data into the Thessaloniki database
    # print("Data for Thessaloniki inserted successfully.")

if __name__ == "__main__":
    main()
