class Unit(object):
    """Unit object containing a float value and string unit."""
    
    numerator = []
    denominator = []
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
        return self.__class__(new_value, self.unit)

    def __mul__(self, other):
        new_value = self.value * other
        return self.__class__(new_value, self.unit)

    def __rmul__(self, other):
        new_value = self.value * other
        return self.__class__(new_value, self.unit)

    def __truediv__(self, other):
        new_value = self.value / other
        return self.__class__(new_value, self.unit)

    def __floordiv__(self, other):
        new_value = self.value // other
        return self.__class__(new_value, self.unit)

class TempUnit(Unit):
    K = 'K'
    C = 'C'
    R = 'R'
    F = 'F'

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

class LengthUnit(Unit):

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

class CurrentUnit(Unit):
    amp = 'A'
    mAmp = 'mA'
    kAmp = 'kA'
    conversions = {
        'A' : 1,
        'mA' : 1000,
        'kA' : 0.001
    }

class TimeUnit(Unit):
    ms = 'ms'
    sec = 's'
    minute = 'min'
    hr = 'hr'
    day = 'day'
    
    conversions = {
        'ms' : 1000,
        's' : 1,
        'min' : 1.0 / 60.0,
        'hr' : 1.0 / 60.0 / 60.0,
        'day' : 1.0 / 60.0 / 60.0 / 24.0
    }

class PressureUnit(Unit):
    bar = 'bar'
    mbar = 'mbar'
    ubar = 'ubar'
    atm = 'atm'
    Pa = 'Pa'
    hPa = 'hPa'
    kPa = 'kPa'
    MPa = 'MPa'
    mmHg = 'mmHg'
    Torr = 'mmHg'
    mmH2O = 'mmH2O'
    mH2O = 'mH2O'
    psi = 'psi'
    ftH2O = 'ftH2O'
    inH2O = 'inH2O'
    inHg = 'inHg'
    kgcm2 = 'kgcm2'

    conversions = {
        'bar' : 1.0,
        'mbar' : 1000.0,
        'ubar' : 1000000.0,
        'Pa' : 100000.0,
        'hPa' : 1000.0,
        'kPa' : 100.0,
        'MPa' : 0.1,
        'kgcm2' : 1.01972,
        'atm' : 0.986923,
        'mmHg' : 750.062,
        'mmH2O' : 10197.162129779,
        'mH2O' : 10.197162129779,
        'psi' : 14.5038,
        'ftH2O' : 33.455256555148,
        'inH2O' : 401.865,
        'inHg' : 29.53
    }

class MassUnit(Unit):
    g = 'g'
    mg = 'mg'
    kg = 'kg'
    metricTon = 'metricTon'
    
    lb = 'lb'
    slug = 'slug'
    oz = 'oz'
    gr = 'gr'
    ton = 'ton'

    conversions = {
        'kg' : 1.0,
        'g' : 1000.0,
        'mg' : 1000000.0,
        'metricTon' : 1.0 / 1000.0,
        'lb' : 2.2046226218,
        'oz' : 35.274,
        'gr' : 2.2046226218 * 7000.0,
        'ton' : 2.2046226218 / 2000.0
    }
