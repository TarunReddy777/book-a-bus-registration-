1. Buses
 Attributes: Primary key -BusID, BusName, BusNumber, BusType, Fare, Availability, Company ID, 
RouteID
Foreign key: Company ID, DriverID, RouteID
2. Routes
 Attributes: RouteID, Source, Destination, Distance, Duration
3. Passengers
 Attributes: Name, Email, PhoneNumber
Primary Key: Email
4. Reservations
 Attributes: Primary key: ReservationNumber, Passenger_Email, BusID, RouteID, ReservationDate, 
SeatNumber, Status
Foreign Keys: Passenger_Email, BusID, RouteID
5. Tickets
 Attributes: TicketNumber, ReservationID, Price, PaymentStatus
Foreign Keys: ReservationID
7. BusCompanies
 Attributes: CompanyID, CompanyName, ContactInfo
8. Drivers
 Attributes: Primary key: DriverID, Name, LicenseNumber, PhoneNumber
Foreign key: BusID
9. Payment
 Attributes: PaymentNumber, ReservationID, Amount, PaymentDate, PaymentMethod, Status
Foreign Keys: ReservationID
10. Seats
 Attributes: BusID, SeatNumber, IsAvailable
Primary key: BusID + SeatNumber
11. Feedback
 Attributes: FeedbackID, PassengerID, Rating, Comments
Foreign Keys: Passenger_Email



Buses (BusID (PK), BusName, BusNumber, BusType, Fare, Availability, Company ID, RouteID)
Routes (RouteID, Source, Destination, Distance, Duration)
Passengers (Name, Email, PhoneNumber)
Reservations (Primary key: ReservationNumber, Passenger_Email, BusID, RouteID, ReservationDate, SeatNumber, Status)
Tickets (TicketNumber, ReservationID, Price, PaymentStatus)
BusCompanies (CompanyID, CompanyName, ContactInfo)
Drivers (Primary key: DriverID, Name, LicenseNumber, PhoneNumber, BusID)
Payment (PaymentNumber, ReservationID, Amount, PaymentDate, PaymentMethod, Status)
Seats (BusID, SeatNumber, IsAvailable)
Feedback (FeedbackID, PassengerID, Rating, Comments, Passenger_email (FK))


The relationship between each entity will be presented in the ER-diagram.
Relationships
• Bus-Company: One-to-Many (A bus belongs to one company, a company has many buses)
• Bus-Route: Many-to-Many (A bus can be assigned to multiple routes and a route can have 
multiple buses)
• Passenger-Reservation: One-to-Many (A passenger can have multiple reservations, a 
reservation belongs to one passenger)
• Reservation-Bus: Many-to-One (A reservation is for one bus, a bus can have multiple 
reservations)
• Reservation-Ticket: One-to-One (A reservation generates one ticket, a ticket is for one 
reservation)
• Reservation-Payment: One-to-One (A reservation has one payment, a payment is for one 
reservation)
• Passenger-Feedback: One-to-Many (A passenger can provide multiple feedback entries, 
feedback is for one passenger)
• Ticket-Feedback: One-to-Many (A ticket can have multiple feedback entries; feedback is for 
one ticket)
• Bus-Seat: One-to-Many (A bus has multiple seats, a seat belongs to one bus)
• Driver-Bus: Many-to-Many (A driver can be assigned to multiple buses, a bus can have 
multiple drivers)