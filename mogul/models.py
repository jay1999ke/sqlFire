from django.db import models

# Create your models here.

"""
Airport:
+	airport_id
    airport_name
	gate_cost
	total_gates
"""
class Airport(models.Model):
    airport_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    gate_cost = models.DecimalField(max_digits=14, decimal_places=2)
    total_gates = models.IntegerField()

    def __str__(self):
        return str(self.airport_id) + " | " +self.name

    class Meta:
        db_table = "airport"

"""
Airline:
+	airline_id
	name
	value
	balance
	base_airport_id
"""

class Airline(models.Model):
    airline_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    value = models.DecimalField(max_digits=14, decimal_places=2)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    airport = models.ForeignKey(Airport,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.airline_id) + " | " +self.name

    class Meta:
        db_table = "airline"


"""
Aircraft:
    aircraft_id
	company
	model
	cost
	seats
"""

class Aircraft(models.Model):
    aircraft_id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=9,decimal_places=2)
    seats = models.IntegerField()

    def __str__(self):
        return self.company + " "+self.model

    class Meta:
        db_table = "aircraft"

"""
Fleet:
+   fleet_id
    aircraft_id
+   airline_id

"""
class Fleet(models.Model):
    fleet_id = models.IntegerField(primary_key=True)
    aircraft = models.ForeignKey(Aircraft,on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fleet_id) +" | "+self.airline.name + " - "+ self.aircraft.company + " " + self.aircraft.model

    class Meta:
        unique_together = (("fleet_id", "airline"),)
        db_table = "fleet"

"""
Booked_gates:
+	airline_id
+	airport_id
	no_of_gates
"""
class BookedGate(models.Model):
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport,on_delete=models.CASCADE)
    no_of_gates = models.IntegerField()

    def __str__(self):
        return self.airline.name + " - "+self.airport.name

    class Meta:
        unique_together = (("airport", "airline"),)
        db_table ="bookedgate"


"""
Routes:
+	flight_no
+	airline_id
	destination_airport_id
	aircraft_id
	price
"""

class Route(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    dest_airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    fleet = models.ForeignKey(Fleet,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.airline.name + " | " + self.dest_airport.name

    class Meta:
        db_table = "route"

"""
Customer
+   customer_id
    first_name
    last_name
    DOB
"""

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    DOB = models.DateField()

    def __str__(self):
        return str(self.customer_id) + " | " + self.last_name + ", " + self.first_name

    class Meta:
        db_table = "customer"

"""
Passenger
+   seat_no
-   customer_id
-   flight_no
    class
"""

class Passenger(models.Model):
    seat_no = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    flight = models.ForeignKey(Route,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat_no) + " | " + self.customer.last_name + ", " + self.customer.first_name

    class Meta:
        unique_together = (("flight","seat_no"),)
        db_table = "passenger"
