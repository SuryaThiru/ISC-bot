import pygame

pygame.init()

pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()

print(j.get_init())

print(j.get_id())
print(j.get_name())
print(j.get_numaxes())

buttons = j.get_numbuttons()
for i in range(buttons):
	button = j.get_button( i )

	print(button, ' : ', i)

while True:
	for event in pygame.event.get():
		print(event.__dict__)
		if event.type == pygame.JOYBUTTONDOWN:
			print('keydown')
		elif event.type == pygame.JOYBUTTONUP:
			print('keyup')
