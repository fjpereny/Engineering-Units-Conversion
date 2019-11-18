class Unit(object):
    """Temperature object containing a float temperature value and string unit."""
    
    conversions = dict()
    def __init__(self, value, unit):
        super().__init__()
        self.value = value
        self.unit = unit
        self.baseUnit = dict(zip(self.conversions.values(), self.conversions.keys()))[1]

    def convert(self, to_unit):
        """Converts the object from one unit to another."""
        from_unit = self.unit
        to_unit = to_unit
        return float(self.value) / float(self.conversions[from_unit]) * float(self.conversions[to_unit])
        
    def changeUnit(self, unit):
        """Converts the current value of the object to a new unit.  Returns a float of the new value."""
        self.value = self.convert(unit)
        self.unit = unit
        return float(self.value)

    def setValue(self, value, unit):
        """Sets the value and unit of the object"""
        self.value = value
        self.unit = unit

    def getValue(self):
        """Returns a list of the float value and unit of the object."""
        return [float(self.value), self.unit]

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __add__(self, other):
        new_value = self.value + other.changeUnit(self.unit)
        return self.__class__(new_value, self.unit)

    def __sub__(self, other):
        new_value = self.value - other.changeUnit(self.unit)
        return Unit(new_value, self.unit)

    def __mul__(self, other):
        new_value = self.value * other
        return Unit(new_value, self.unit)

    def __rmul__(self, other):
        new_value = self.value * other
        return Unit(new_value, self.unit)

    def __truediv__(self, other):
        new_value = self.value / other
        return Unit(new_value, self.unit)

    def __floordiv__(self, other):
        new_value = self.value // other
        return Unit(new_value, self.unit)

class Temperature(Unit):
    conversions = {
        'K' : 1,
    }

    def convert(self, to_unit):
        """
        Converts a temperature value from one unit of measure to another.
        Returns a float value of the temperature in requested units. 
        Returns None for incorrect value.

        Units of Measure
        ---------------
        Units of measure entered as a string.
        'K' - Degree Kelvin\n
        'F' - Degree Farenheit\n
        'R' - Degree Rankine\n
        'C' - Degree Celcius

        Parameters
        ---------------
        value : float
            Value of the temperature measurement.\n
        from_unit : str
            Unit of measurement to convert from.\n
        to_unit : str
            Unit of measurement to convert to.
        """
    
        temperature_kelvin = 0
        if self.unit.upper() == 'K':
            temperature_kelvin = self.value
        elif self.unit == 'R':
            temperature_kelvin = self.value * 5.0 / 9.0
        elif self.unit == 'C':
            temperature_kelvin = self.value + 273.15
        elif self.unit == 'F':
            temperature_kelvin = (self.value + 459.67) / 9.0 * 5.0
        else:
            return None
        
        # Return Value in Required Unit
        if to_unit == 'K':
            return float(temperature_kelvin)
        elif to_unit == 'R':
            return temperature_kelvin * 9.0 / 5.0
        elif to_unit == 'C':
            return temperature_kelvin - 273.15
        elif to_unit == 'F':
            return temperature_kelvin * 9.0 / 5.0 - 459.67
        else:
            return None    

class Length(Unit):
    conversions = {
        'fm' : 1000000000000000,
        'pm' : 1000000000000,
        'nm' : 1000000000,
        'um' : 1000000,
        'mm' : 1000,
        'cm' : 100,
        'm' : 1,
        'dam' : 0.1,
        'hm' : 0.01,
        'km' : 0.001,
        'Mm' : 0.000001,
        'Gm' : 0.000000001,
        'Tm' : 0.000000000001,
        'Pm' : 0.000000000000001,

        'in' : 39.3701,
        'ft' : 3.28084,
        'yd' : 1.09361,
        'mi' : 0.000621371
    }

