Car Rental Agency Management System

- Project Description

This project is a car rental agency management system with a graphical user interface (GUI) developed using PyQt5 in Python.

The system allows users to manage cars, clients, and rental transactions efficiently. Data is stored in text files and can be saved to CSV and Excel files.

- Features
  
Graphical Interface: Developed using PyQt5 and QtDesigner.

Data Management: Uses text files (clients.txt, voitures.txt, locations.txt) as a database.

Menu Options:

Gestion des Voitures: Manage car records.

Gestion des Clients: Manage client records.

Gestion des Locations: Manage rental transactions.

Enregistrement: Save data to text, CSV, and Excel files.

- Installation
  
Ensure Python is installed on your system.

Install PyQt5 module: pip install PyQt5

Clone this repository and navigate to the project directory.

- Running the Project

To start the application, run the file "menu principal.py"

- Usage

- Gestion des Voitures (cars management):

Add a New Car: Enter details (matricule, marque, couleur, état, date d'achat, prix de location). Data validation ensures correct input.

Matricule: 3 numbers followed by "tu" and 4 numbers (e.g., 128tu4777).

Delete a Car: By matricule or marque.

Delete Cars Older than 10 Years: Automatically deletes cars older than 10 years based on the current date and date d'achat.

Modify Car Details: Modify price, état, or couleur by matricule.

View All Cars: Displays a list of all cars.

Search Cars: By marque, couleur, or matricule.

View Rented Cars: Displays cars with état = louée.

View Available Cars: Displays cars with état = disponible.

- Gestion des Clients (clients management) :

Add a New Client: Enter details (CIN, nom, prénom, age, adresse, mail, téléphone). Data validation ensures correct input.

CIN: 8 numbers starting with 0, 1, or 2 (e.g., 11112222).

Nom & Prénom: Alphabetical characters only, starting with a capital letter.

Age: Greater than 18 and less than 100.

Adresse: Alphabetical characters only, starting with a capital letter.

Mail: Valid email format (e.g., example@gmail.com).

Téléphone: 8 numbers starting with 2, 5, or 9.

Delete a Client: By CIN.

Modify Client Details: Modify mail, telephone, or address by CIN.

View All Clients: Displays a list of all clients.

Search Client: By CIN.

- Gestion des Locations (rental transactions management) :

Add a New Rental: Enter details (CIN, matricule, date, durée par jour). Data validation ensures correct input.

CIN: Must be of a client that already exists in the clients database.

Matricule: Must be of a car that already exists and is available (état = disponible).

Delete a Rental: By CIN, matricule, and date.

Modify Rental Details: Modify date or durée by CIN, matricule, and date.

View All Rentals: Displays a list of all rentals (CIN, matricule, date, durée, montant).

Montant: Automatically calculated as prix (from car) * durée.

Search Rentals: By CIN, matricule, date, or durée.

![image](https://github.com/aya-zid/Car_Rental_Agency_Management/assets/71102523/bcb93afe-4998-4be1-823e-f72b98cac882)


