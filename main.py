import pygame

size_place = input()
count = input()
if size_place.isdigit() == False or count.isdigit() == False:
    print("Неправильный формат ввода")

size = size_x, size_y = int(size_place), int(size_place)
pygame.init()
scr = pygame.display.set_mode(size)
pygame.display.set_caption("Прямоугольник")

scr.fill((0, 0, 0))
white = (255, 255, 255)
x_coord = 0
size_z = int(size_place) // int(count)
y_coord = 0
x = 1

if int(count) % 2 != 0:
    x_coord += size_z

for i in range(int(size_place) // size_z):
    for j in range(int(count)):
        pygame.draw.rect(scr, white, (x_coord, y_coord, size_z, size_z))
        x_coord += 2 * size_z
    y_coord += size_z
    x += 1
    if int(count) // 2 == int(count) / 2:
        if x // 2 == x / 2:
            x_coord = size_z
        else:
            x_coord = 0
    else:
        if x // 2 == x / 2:
            x_coord = 0
        else:
            x_coord = size_z

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()