class EngUnit(object):
    """Generic class for engineering unit objects containing a float value and string unit."""
    
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

    def __pow__(self, other):
        new_value = self.value ** other
        return self.__class__(new_value, self.unit)


class Temperature(EngUnit):
    """Creates a temperature object that can store a temperature value and
    convert between units of temperature."""
    
    class Unit():
        K = 'K'
        C = 'C'
        R = 'R'
        F = 'F'

    # conversions { } is not used to convert the Temperature() class because 
    # temperature is not converted with a scalar.  See the convert() function below.
    conversions = {
        'K' : 1.0,
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

    def __add__(self, other):
        self_original_unit = self.unit

        self.changeUnit('K')

        if other.unit in ('K', 'C'):
            new_value = self.value + other.value
        else:
            new_value = self.value + (other.value * 5.0 / 9.0)            

        new_unit = self.__class__(new_value, 'K')
        new_unit.changeUnit(self_original_unit)
        return new_unit

    def __sub__(self, other):
            self_original_unit = self.unit

            self.changeUnit('K')

            if other.unit in ('K', 'C'):
                new_value = self.value - other.value
            else:
                new_value = self.value - (other.value * 5.0 / 9.0)            

            new_unit = self.__class__(new_value, 'K')
            new_unit.changeUnit(self_original_unit)
            return new_unit


class Length(EngUnit):
    """Creates a length object that can store a length value and 
    convert between units of length."""
    
    class Unit():
        fm = 'fm' 
        pm = 'pm' 
        nm = 'nm' 
        um = 'um' 
        mm = 'mm' 
        cm = 'cm'
        m = 'm'
        dam = 'dam'
        hm = 'hm' 
        km = 'km'
        Mm = 'Mm' 
        Gm = 'Gm'
        Tm = 'Tm'
        Pm = 'Pm'

        inch = 'inch'
        ft = 'ft'
        yd = 'yd'
        mi = 'mi'

        nautMi = 'nautMi'
        lightYear = 'lightYear'

    conversions = {
        'fm' : 1000000000000000,
        'pm' : 1000000000000,
        'nm' : 1000000000,
        'um' : 1000000,
        'mm' : 1000,
        'cm' : 100,
        'm' : 1.0,
        'dam' : 0.1,
        'hm' : 0.01,
        'km' : 0.001,
        'Mm' : 0.000001,
        'Gm' : 0.000000001,
        'Tm' : 0.000000000001,
        'Pm' : 0.000000000000001,

        'inch' : 39.3701,
        'ft' : 3.28084,
        'yd' : 1.09361,
        'mi' : 0.000621371,

        'nautMi' : 1.0 / 1852.0,
        'lightYear' : 1.0 / (9.4607304725808 * (10**15))
    }


class Current(EngUnit):
    """Creates a current (amperage) object that can store a current (amperage) value and 
    convert between units of current (amperage)."""
    
    class Unit():
        A = 'A'
        mA = 'mA'
        kA = 'kA'
    
    conversions = {
        'A' : 1,
        'mA' : 1000,
        'kA' : 0.001
    }


class EngTime(EngUnit):
    """Creates a time object that can store a time value and 
    convert between units of time."""
    
    class Unit():
        ms = 'ms'
        s = 's'
        minute = 'minute'
        hr = 'hr'
        day = 'day'
    
    conversions = {
        'ms' : 1000.0,
        's' : 1.0,
        'minute' : 1.0 / 60.0,
        'hr' : 1.0 / 60.0 / 60.0,
        'day' : 1.0 / 60.0 / 60.0 / 24.0
    }


class Pressure(EngUnit):
    """Creates a pressure object that can store a pressure value and 
    convert between units of pressure."""
    
    class Unit():
        bar = 'bar' 
        mbar = 'mbar' 
        ubar = 'ubar' 
        Pa = 'Pa' 
        hPa = 'hPa' 
        kPa = 'kPa' 
        MPa = 'MPa' 
        kgcm2 = 'kgcm2' 
        atm = 'atm' 
        mmHg = 'mmHg' 
        mmH2O = 'mmH2O' 
        mH2O = 'mH2O' 
        psi = 'psi' 
        ftH2O = 'ftH2O' 
        inH2O = 'inH2O' 
        inHg = 'inHg' 
    
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


class Mass(EngUnit):
    """Creates a mass object that can store a mass value and 
    convert between units of mass."""
    
    class Unit():
        kg = 'kg'
        g = 'g'
        mg = 'mg'
        metricTon = 'metricTon'
        lb = 'lb'
        oz = 'oz'
        grain = 'grain'
        shortTon = 'shortTon'
        longTon = 'longTon'
        slug = 'slug'
    
    conversions = {
        'kg' : 1.0,
        'g' : 1000.0,
        'mg' : 1000000.0,
        'metricTon' : 1.0 / 1000.0,
        'lb' : 2.2046226218,
        'oz' : 35.274,
        'grain' : 2.2046226218 * 7000.0,
        'shortTon' : 1.0 / 907.185,
        'longTon' : 1.0 / 1016.047,
        'slug' : 1.0 / 14.5939029
    }


class Force(EngUnit):
    """Creates a force object that can store a force value and 
    convert between units of force."""

    class Unit():
        N = 'N'
        kN = 'kN'
        MN = 'MN'
        GN = 'GN'
        gf = 'gf'
        kgf = 'kgf'
        dyn = 'dyn'
        Jm = 'J/m'
        Jcm = 'J/cm'
        shortTonF = 'shortTonF'
        longTonF = 'longTonF'
        kipf = 'kipf'
        lbf = 'lbf'
        ozf = 'ozf'
        pdl = 'pdl'

    conversions = {
        'N' : 1.0,
        'kN' : 1.0 / 1000.0,
        'MN' : 1.0 / 1000000.0,
        'GN' : 1.0 / 1000000000.0,
        'gf' : 1.019716213e+2,
        'kgf' : 1.019716213e-1,
        'dyn' : 1e+5,
        'J/m' : 1.0,
        'J/cm' : 100.0,
        'shortTonF' : 1.124045e-4,
        'longTonF' : 1.003611e-4,
        'kipf' : 2.248089e-4,
        'lbf' : 2.248089431e-1,
        'ozf' : 3.5969430896,
        'pdf' : 7.2330138512
    }


class Power(EngUnit):
    """Creates a power object that can store a power value and 
    convert between units of power."""

    class Unit():
        kW = 'kW'
        BTU_hr = 'BTU/hr'
        BTU_min = 'BTU/min'
        BTU_sec = 'BTU/sec'
        cal_sec = 'cal/sec'
        cal_min = 'cal/min'
        cal_hr = 'cal/hr'
        erg_sec = 'erg/sec'
        erg_min = 'erg/min'
        erg_hr = 'erg/hr'
        ftlb_sec = 'ftlb/sec'
        GW = 'GW'
        MW = 'MW'
        kCal_sec = 'kCal/sec'
        kCal_min = 'kCal/min'
        kCal_hr = 'kCal/hr'
        mW = 'mW'
        W = 'W'
        VA = 'VA'
        hp_mech = 'hp_mech'
        hp_ele = 'hp_ele'
        hp_metric = 'hp_metric'
        metric_ton_ref = 'metric_ton_ref'
        US_ton_ref = 'US_ton_ref'
        J_sec = 'J/sec'
        J_min = 'J/min'
        J_hr = 'J/hr'
        kgfm_sec = 'kgf-m/sec'

    conversions = {
        'kW' : 1.0,
        'BTU/hr' : 3412.14,
        'BTU/min' : 56.869,
        'BTU/sec' : 0.94781666666,
        'cal/sec' : 238.85,
        'cal/min' : 238.85 * 60,
        'cal/hr' : 238.85 * 60 * 60,
        'erg/sec' : 10e9,
        'erg/min' : 10e9 * 60,
        'erg/hr' : 10e9 * 60 * 60,
        'ftlb/sec' : 737.56,
        'GW' : 1e-6,
        'MW' : 1e-3,
        'kCal/sec' : 0.24,
        'kCal/min' : 0.24 * 60,
        'kCal/hr' : 0.24 * 60 * 60,
        'mW' : 1e6,
        'W' : 1e3,
        'VA' : 1e3,
        'hp_mech' : 1.3410220888,
        'hp_ele' : 1.3404825737,
        'hp_metric' : 1.359621617304,
        'metric_ton_ref' : 0.259,
        'US_ton_ref' : 0.2843451361,
        'J/sec' : 1000.0,
        'J/min' : 1000.0 * 60,
        'J/hr' : 1000.0 * 60 * 60,
        'kgf-m/sec' : 101.97162129779
    }

class Flow(EngUnit):
    """Creates a flow object that can store a flow value and 
    convert between units of flow."""

    class Unit():
        BBL_hr = 'BBL/hr'
        BBL_min = 'BBL/min'
        BBL_sec = 'BBL/sec'
        GAL_hr = 'GAL/hr'
        GAL_min = 'GAL/min'
        GAL_sec = 'GAL/sec'

    conversions = {
        'BBL/hr' : 3600.0,
        'BBL/min' : 60.0,
        'BBL/sec' : 1.0,
        'GAL/hr' : 151200.0,
        'GAL/min' : 2520.0,
        'GAL/sec' : 42.0,
    }