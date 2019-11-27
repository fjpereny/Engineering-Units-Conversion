# Engineering-Units-Conversion
## Description
Python Engineering Unit Conversion Library is a current work in progress.  The aim of the library is 
to provide users with easy management of engineering units and to avoid mistakes when working with 
and converting between different units of measurement.

### Supported Units 
* Temperature
* Pressure
* Mass
* Power
* Time
* Force
* Electric Current
* Length
  
Custom units can be added by copying and pasting one of the generic
classes and changing the data. This library will continue to be updated to include
additional engineering units.

## Installation & Dependencies
This library is compatible with Python 3 and does not use
any external dependencies.

## Usage
### Adding EngUnitConversion to your project:
```python
import EngUnitConversion
```
or
```python
import EngUnitConversion as EUC
```
or
```python
from EngUnitConversion import *
```

### Creating an EngUnit Object
All EngUnit objects are instantiated using a float value and a initial unit of measurement.
The following code creates a Temperature with a value of 100 and unit of degree Fahrenheit.
```python
t1 = Temperature(100, Temperature.Unit.F)
```

### Units of Measurement
All available unit conversions are stored in the EngUnit.Unit sub-class or can be called 
directly using the associated string.
```python
f1 = Force(10.5, Force.Unit.kN)
```
is equivalent to
```python
f1 = Force(10.5, 'kN')
```

### Getting Value & Unit
```python
f1 = Force(10.5, Force.Unit.kN)
print(f1.value)
print(f1.unit)
```
yields the following console output:
```txt
10.5
kN
```


### Changing Units of Measurement
The objects unit of measure can be changed by calling the changeUnit function.  This returns
the new value and stores the new value and engineering unit in the object.
```python
t1 = Temperature(100, Temperature.Unit.F)
print(t1)
print(t1.changeUnit('C'))
print(t1)
```
yields the following output:
```txt
100 F
37.77777777777783
37.77777777777783 C
```
Notice how the function changeUnit() both returns the value as a float changes the current
instance of the object the new value unit.

### Working with Units
When using EngUnit objects to perform operations, a new EngUnit object will be returned with 
the first object's unit by default.

#### Addition & Subtraction
```python 
p1 = Power(100, Power.Unit.kW)
print(Power)

p2 = Power(15000, Power.Unit.BTU_min)
print(p2)

p1 += p2
print(p1)
```
yields the following output:

```txt
100 kW
15000 BTU/min
363.764089398442 kW
```

#### Multiplication & Division
```python 
t1 = Temperature(400, 'K')
print(t1)

t2 = 1.5 * t1
print(t2)

t3 = t2.changeUnit('F')
print(t3)

t4 = t3 / 2
print(t4)
```
output:

```txt
400 K
600.0 K
620.3299999999999
310.16499999999996
```
Note: Reverse Division is not defined.  The following example will yield 
an error:
```python
t4 = 2 / t3
```
If reverse division is required EngUnit.value should be used.  For example:
```python
x = 2 / t3.value
t4 = Temperature(x, 'F')
```

## License
    Copyright (C) 2019  Frank Pereny

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see https://www.gnu.org/licenses.
