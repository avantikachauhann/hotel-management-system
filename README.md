

# Hotels Management System

## Overview
The **Hotels Management System** is a Python-based project designed to streamline hotel operations by integrating key functionalities such as customer management, booking records, room rent calculation, restaurant billing, and generating total or old bills. The system uses **MySQL** as its database to store and retrieve customer and hotel data efficiently.

## Features
1. **Customer Management**
   - Add new customer details.
   - Search for existing customer details.

2. **Booking Management**
   - Record check-in and check-out details for customers.

3. **Room Rent Calculation**
   - Choose from multiple room categories and calculate rent based on the number of days.

4. **Restaurant Billing**
   - Choose cuisines and calculate the total restaurant bill.

5. **Billing System**
   - Generate a consolidated bill for room rent and restaurant charges.
   - Retrieve old bills for reference.

6. **Database Integration**
   - Data is securely stored and managed in a **MySQL** database.

---

## Prerequisites
1. **Python 3.x** installed on your system.
2. **MySQL Server** installed and running.
3. **MySQL Connector** for Python. Install it using:
   ```bash
   pip install mysql-connector-python
   ```

---

## Installation and Setup
1. Clone this repository or download the project files.
2. Open the project in your preferred code editor.
3. Ensure the MySQL server is running on your machine.
4. Execute the script, and provide your MySQL credentials when prompted.
5. Upon successful connection, the program will create a database (`avanti_hotels`) and necessary tables if they don't already exist.

---

## Usage Instructions
1. Run the script:
   ```bash
   python hotel_management_system.py
   ```
2. Follow the on-screen menu to navigate through the system:
   - **Enter Customer Details**: Add new customer records.
   - **Booking Record**: Enter check-in and check-out dates.
   - **Calculate Room Rent**: Choose a room type and calculate the rent based on the duration of stay.
   - **Calculate Restaurant Bill**: Place restaurant orders and generate a bill.
   - **Display Customer Details**: Search for a customer's information.
   - **Generate Total Bill Amount**: View a summary of room rent and restaurant bills.
   - **Generate Old Bill**: Retrieve past bills for customers.
   - **Exit**: Exit the system.

---

## Database Schema
### Tables:
1. **C_DETAILS**
   - `CID`: Customer ID (Primary Key)
   - `C_NAME`: Customer Name
   - `C_ADDRESS`: Address
   - `C_AGE`: Age
   - `C_COUNTRY`: Country
   - `P_NO`: Phone Number
   - `C_EMAIL`: Email Address

2. **BOOKING_RECORD**
   - `CID`: Customer ID
   - `CHECK_IN`: Check-in Date
   - `CHECK_OUT`: Check-out Date

3. **ROOM_RENT**
   - `CID`: Customer ID
   - `ROOM_CHOICE`: Room Category
   - `NO_OF_DAYS`: Number of Days
   - `ROOMNO`: Room Number
   - `ROOMRENT`: Total Room Rent

4. **RESTAURANT**
   - `CID`: Customer ID
   - `CUISINE`: Cuisine Ordered
   - `QUANTITY`: Quantity
   - `BILL`: Bill Amount

5. **TOTAL**
   - `CID`: Customer ID
   - `C_NAME`: Customer Name
   - `ROOMRENT`: Total Room Rent
   - `RESTAURANTBILL`: Total Restaurant Bill
   - `TOTALAMOUNT`: Grand Total Amount

---

## Contribution
Feel free to suggest improvements or add new features to the project. To contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed explanation of your additions.

---

## Contact
Developed and maintained by:
**Avantika Chauhan**  

For any queries or feedback, please contact: avantikachauhn@example.com.  

