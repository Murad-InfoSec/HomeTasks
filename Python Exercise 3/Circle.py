from decimal import Decimal
import math


# Circle class
class Cyrcle:
   
   # Calculate circle area
   #Decimal for scientific and financial presicion
    @staticmethod    
    def area(radius:Decimal):
        return math.pi * radius ** 2

   # Calculate circle circumference
   #Decimal for scientific and financial presicion
    @staticmethod
    def circumference (radius:Decimal):
        return 2 * math.pi * radius


# Test calculations
print(Cyrcle.area(5))
print(Cyrcle.circumference(5))
