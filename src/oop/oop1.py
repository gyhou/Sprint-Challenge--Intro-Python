# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # Parent class
    pass


class FlightVehicle(Vehicle):
    # Child class - FlightVehicle
    # Parent class - Vechile
    pass


class Starship(FlightVehicle):
    # Child class - Starship
    # Parent class - FlightVehicle
    pass


class Airplane(FlightVehicle):
    # Child class - Starship
    # Parent class - FlightVehicle
    pass


class GroundVehicle(Vehicle):
    # Child class - GroundVehicle
    # Parent class - Vechile
    pass


class Car(GroundVehicle):
    # Child class - Car
    # Parent class - GroundVehicle
    pass


class Motorcycle(GroundVehicle):
    # Child class - Motorcycle
    # Parent class - GroundVehicle
    pass
