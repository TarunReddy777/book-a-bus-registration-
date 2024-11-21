CREATE DATABASE Bus_Reservation_System;

USE DATABASE Bus_Reservation_System;

-- Create BusCompany table
CREATE TABLE BusCompany (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

-- Create Route table
CREATE TABLE Route (
    RouteID INT PRIMARY KEY AUTO_INCREMENT,
    Source VARCHAR(100) NOT NULL,
    Destination VARCHAR(100) NOT NULL,
    Distance FLOAT NOT NULL,
    Duration VARCHAR(100) NOT NULL
);

-- Create Bus table
CREATE TABLE Bus (
    BusID INT PRIMARY KEY AUTO_INCREMENT,
    BusName VARCHAR(100) NOT NULL,
    BusNumber VARCHAR(20) NOT NULL UNIQUE,
    Capacity INT NOT NULL,
    BusType VARCHAR(50) NOT NULL,
    Fare DECIMAL(10, 2) NOT NULL,
    CompanyID INT NOT NULL,
    RouteID INT NOT NULL,
    FOREIGN KEY (CompanyID) REFERENCES BusCompany(CompanyID),
    FOREIGN KEY (RouteID) REFERENCES Route(RouteID)
);

-- Create Passenger table
CREATE TABLE Passenger (
    Email VARCHAR(100) PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL
);

-- Create Reservation table
CREATE TABLE Reservation (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,
    ReservationDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(20) CHECK (Status IN ('Booked', 'Cancelled')),
    BusID INT NOT NULL,
    PassengerEmail VARCHAR(100) NOT NULL,
    RouteID INT NOT NULL,
    SeatNumber VARCHAR(5) NOT NULL,
    FOREIGN KEY (BusID) REFERENCES Bus(BusID),
    FOREIGN KEY (PassengerEmail) REFERENCES Passenger(Email),
    FOREIGN KEY (RouteID) REFERENCES Route(RouteID)
);

-- Create Ticket table
CREATE TABLE Tickets (
    TicketNumber VARCHAR(20) PRIMARY KEY,
    Price DECIMAL(10, 2) NOT NULL,
    PaymentStatus VARCHAR(20) CHECK (PaymentStatus IN ('Paid', 'Pending')),
    ReservationID INT NOT NULL,
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID)
);

-- Create BusCompanies table
CREATE TABLE BusCompanies (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

-- Create Driver table
CREATE TABLE Drivers (
    DriverID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    LicenseNumber VARCHAR(20) NOT NULL,
    DateOfBirth DATE NOT NULL
);

-- Create Payment table
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod VARCHAR(50) NOT NULL,
    Status VARCHAR(20) CHECK (Status IN ('Paid', 'Pending')),
    ReservationID INT NOT NULL,
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID)
);

-- Create Seat table
CREATE TABLE Seats (
    BusID INT NOT NULL,
    SeatNumber VARCHAR(5) NOT NULL,
    IsAvailable BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (BusID, SeatNumber),
    FOREIGN KEY (BusID) REFERENCES Bus(BusID)
);

-- Create Feedback table
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Comments TEXT,
    PassengerEmail VARCHAR(100) NOT NULL,
    FOREIGN KEY (PassengerEmail) REFERENCES Passenger(Email)
);

-- Create Bus_Driver_Mapping table
CREATE TABLE Bus_Driver_Mapping (
    BusID INT NOT NULL,
    DriverID INT NOT NULL,
    PRIMARY KEY (BusID, DriverID),
    FOREIGN KEY (BusID) REFERENCES Bus(BusID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

-- Create Driver_PhoneNumber table
CREATE TABLE Driver_PhoneNumber (
    DriverID INT NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    PRIMARY KEY (DriverID, PhoneNumber),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

-- Insert mock data

-- Inserting mock data for BusCompany
INSERT INTO BusCompany (CompanyName, Email) 
VALUES 
('ABC Travels', 'abc@travels.com'),
('XYZ Bus Services', 'xyz@services.com');

-- Inserting mock data for Route
INSERT INTO Route (Source, Destination, Distance, Duration)
VALUES 
('New York', 'Los Angeles', 2800, '5 hours 30 minutes'),
('Chicago', 'San Francisco', 2500, '4 hours 50 minutes');

-- Inserting mock data for Bus
INSERT INTO Bus (BusName, BusNumber, Capacity, BusType, Fare, CompanyID, RouteID)
VALUES 
('Luxury Express', 'LX100', 50, 'Luxury', 120.50, 1, 1),
('City Shuttle', 'CS200', 40, 'Economy', 60.00, 2, 2);

-- Inserting mock data for Passenger
INSERT INTO Passenger (Email, FirstName, LastName, PhoneNumber)
VALUES 
('john.doe@example.com', 'John', 'Doe', '123-456-7890'),
('jane.smith@example.com', 'Jane', 'Smith', '987-654-3210');

-- Inserting mock data for Reservation
INSERT INTO Reservation (ReservationDate, Status, BusID, PassengerEmail, RouteID, SeatNumber)
VALUES 
('2024-11-20 10:00:00', 'Booked', 1, 'john.doe@example.com', 1, 'A1'),
('2024-11-20 11:00:00', 'Cancelled', 2, 'jane.smith@example.com', 2, 'B2');

-- Inserting mock data for Tickets
INSERT INTO Tickets (TicketNumber, Price, PaymentStatus, ReservationID)
VALUES 
('T1001', 120.50, 'Paid', 1),
('T1002', 60.00, 'Pending', 2);

-- Inserting mock data for Driver
INSERT INTO Drivers (FirstName, LastName, LicenseNumber, DateOfBirth)
VALUES 
('Alice', 'Johnson', 'DL123456', '1985-05-10'),
('Bob', 'Williams', 'DL654321', '1990-08-20');

-- Inserting mock data for Payment
INSERT INTO Payment (Amount, PaymentDate, PaymentMethod, Status, ReservationID)
VALUES 
(120.50, '2024-11-20 09:30:00', 'Credit Card', 'Paid', 1);

-- Inserting mock data for Seat
INSERT INTO Seats (BusID, SeatNumber, IsAvailable)
VALUES 
(1, 'A1', TRUE),
(1, 'A2', FALSE),
(2, 'B1', TRUE);

-- Inserting mock data for Feedback
INSERT INTO Feedback (Rating, Comments, PassengerEmail)
VALUES 
(5, 'Great experience!', 'john.doe@example.com'),
(3, 'The trip was okay.', 'jane.smith@example.com');

-- Inserting mock data for Bus_Driver_Mapping
INSERT INTO Bus_Driver_Mapping (BusID, DriverID)
VALUES 
(1, 1),
(2, 2);

-- Inserting mock data for Driver_PhoneNumber
INSERT INTO Driver_PhoneNumber (DriverID, PhoneNumber)
VALUES 
(1, '555-123-4567'),
(2, '555-987-6543');