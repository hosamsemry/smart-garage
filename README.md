# Smart-Garage
The Smart Garage project is a web application developed using Django and Django Rest Framework (DRF) for creating RESTful APIs. The project aims to provide easy managing and reserving parking spaces in garages efficiently.

## Key Features:
- User Management: The application allows users to register, login, update their profiles, and delete their accounts securely. Passwords are hashed for enhanced security.

- Admin Panel: Admins have special privileges to register, login, manage other admin accounts, update their profiles, and delete admin accounts.

- Garage Management: Admins can add, update, and delete garage listings. Each garage listing contains essential information such as title, description, contact number, price, location (latitude and longitude), and the total number of parking slots available.

- Reservation System: Users can start and end parking reservations. They can view their current reservation status, including the start time, parking duration, and the associated garage details. Completed reservations are also stored and can be accessed for historical purposes.

- Real-time Availability: The application provides real-time updates on garage availability, indicating the number of reserved slots at any given time.

- Cost Calculation: The system automatically calculates the cost of each reservation based on the parking duration and the price per minute set by the garage owner.

- API Endpoints: All functionalities are exposed through RESTful API endpoints, enabling seamless integration with other applications or platforms.

## Technologies Used

- Django: The core web framework used for backend development.
- Django Rest Framework (DRF): Facilitates the creation of RESTful APIs for communication between the frontend and backend.
- SQLite: A lightweight and efficient relational database management system used for data storage.
- Python: The primary programming language used for backend logic implementation.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
