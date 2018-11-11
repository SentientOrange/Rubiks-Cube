import cube

# Pocket Cube
c = cube.Cube(2)

print("Starting Cube")
c.print_cube()
print()

print("Rotating Back")
c.rotate_back()
c.print_cube()
print()

print("Rotating Top")
c.rotate_top()
c.print_cube()
print()

print("Rotating Bottom")
c.rotate_bottom()
c.print_cube()
print()

print("Rotating Front")
c.rotate_front()
c.print_cube()
print()

print("Rotating Left")
c.rotate_left()
c.print_cube()
print()

print("Rotating Right")
c.rotate_right()
c.print_cube()
print()
