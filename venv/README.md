TAS Library is a python library that can do many 
mathmatical problems.
***
## Included Pakage
***
|Pakage Name|For What|Call|
|----|-----|----|
|TASMath|Mathmatical problems|`from TASLibrary import TASMath`|
***
## Installation
***
`pip install taslibrary`
***
## Included Module for TASMath
***
|Module Name|Call|
|----|----|
|1. Arithmetic|`from TASLibrary.TASMath import Arithmetic`|
|2. Alzebra|`from TASLibrary.TASMath import Alzebra`|
|3. Constnt|`from TASLibrary.TASMath import Constant`|
|4. Convert|`from TASLibrary.TASMath import Convert`|
|5. ExtraFunction|`from TASLibrary.TASMath import ExtraFunction`|
|6. Geometry|`from TASLibrary.TASMath import Geometry`|
|7. Series|`from TASLibrary.TASMath import Series`|
|8. Set|`from TASLibrary.TASMath import Set`|
|9. UnitPrefix|`from TASLibrary.TASMath import UnitPrefix`|
***
### Arithmetic
***
The Arthmetic Module is for doing arthemetic problems.
***
|Function Name|Call|
|----|----|
|1. add|`Arithmetic.add()`|
|2. subtract|`Arithmetic.substract()`|
|3. devide|`Arithmetic.devide()`|
|4. multiply|`Arithmetic.multiply()`|
|5. remainder|`Arithmetic.remainder()`|
***
If you want to disply the code without calling `print()` function you can also call the functions bellow.
***
|Function Name|Call|
|----|----|
|1. add|`Arithmetic.add()`|
|2. subtract|`Arithmetic.Print.substract()`|
|3. devide|`Arithmetic.Print.devide()`|
|4. multiply|`Arithmetic.Print.multiply()`|
|5. remainder|`Arithmetic.Print.remainder()`|
***
## Alzebra
***
The Alzebra Module is for doing Alzebric problems.
***
|Function Name|Call|
|----|----|
|1. Square|`Alzebra.Square.square()`|
|2. Square_|`Alzebra.Square.square_()`|
|3. Single Square|`Alzebra.Square.singleSquare()`|
|4. Extended Square|`Alzebra.Square.Extended.square()`|
|5. Cube|`Alzebra.Cube.cube()`|
|6. Cube|`Alzebra.Cube.cube_()`|
|7. Power|`Alzebra.Power.power()`|
|8. a2substractb2|`Alzebra.ProducerFormula.a2subtractb2()`|
|9. a3addb3|`Alzebra.ProducerFormula.a2addb3()`|
***
If you want to disply the code without calling `print()` function you can also call the functions bellow.
***
|Function Name|Call|
|----|----|
|1. Square|`Alzebra.Print.Square.square()`|
|2. Square_|`Alzebra.Print.Square.square_()`|
|3. Single Square|`Alzebra.Print.Square.singleSquare()`|
|4. Extended Square|`Alzebra.Print.Square.Extended.square()`|
|5. Cube|`Alzebra.Print.Cube.cube()`|
|6. Cube|`Alzebra.Print>Cube.cube_()`|
|7. Power|`Alzebra.Print.Power.power()`|
|8. a2substractb2|`Alzebra.Print.ProducerFormula.a2subtractb2()`|
|9. a3addb3|`Alzebra.Print.ProducerFormula.a2addb3()`|
***
***
## Get Started
***
### Alzebra
***
Square two number by TASLibrary. By this you have to
use the `print()` function.
```Python
from TASLibrary.TASMath import Alzebra

# To square to number
a = Alzebra.Square.square(1, 10)
# print the variable
print(a)
```
***
If you want to print directly by one line of code
you can code like this.
```Python
from TASLibrary.TASMath import Alzebra

# Pint by one line
Alzebra.Print.Square.square(10, 20)
```
***
