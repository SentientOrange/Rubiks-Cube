# Import testing

import pytest
import cube

def test_cube_size():
   c = cube.Cube()
   assert c.get_size() == 3