import pygame
import math

x_screen = 1920
y_screen = 1080

pygame.init()

screen = pygame.display.set_mode((x_screen, y_screen))

background = pygame.image.load('abc.jpg')

sunIMG = pygame.image.load('sun_2.png')
sun_x = (x_screen/2) - 95
sun_y = (y_screen/2) - 95

mercuryIMG = pygame.image.load('mercury_2.png')
mercury_x = sun_x + 89
mercury_y = sun_y - 24
var_mercury = 0

venusIMG = pygame.image.load('venus_2.png')
venus_x = sun_x + 83
venus_y = sun_y - 48
var_venus = 0

earthIMG = pygame.image.load('worldwide_2.png')
earth_x = sun_x + 75
earth_y = sun_y - 95
var_earth = 0

marsIMG = pygame.image.load('mars_2.png')
mars_x = sun_x + 77
mars_y = sun_y - 138
var_mars = 0

jupiterIMG = pygame.image.load('jupiter_2.png')
jupiter_x = sun_x + 55
jupiter_y = sun_y - 245
var_jupiter = 0

saturnIMG = pygame.image.load('saturn.png')
saturn_x = sun_x + 63
saturn_y = sun_y - 335
var_saturn = 0

uranIMG = pygame.image.load('urano.png')
uran_x = sun_x + 79
uran_y = sun_y - 380
var_uran = 0

nenuteIMG = pygame.image.load('netuno.png')
netune_x = sun_x + 79
netune_y = sun_y - 425
var_netune = 0


def show_sun(x, y):
    screen.blit(sunIMG, (x, y))


def show_mercury(x, y):
    screen.blit(mercuryIMG, (x, y))


def show_venus(x, y):
    screen.blit(venusIMG, (x, y))


def show_earth(x, y):
    screen.blit(earthIMG, (x, y))


def show_mars(x, y):
    screen.blit(marsIMG, (x, y))


def show_jupiter(x, y):
    screen.blit(jupiterIMG, (x, y))


def show_saturn(x, y):
    screen.blit(saturnIMG, (x, y))


def show_uran(x, y):
    screen.blit(uranIMG, (x, y))


def show_netune(x, y):
    screen.blit(nenuteIMG, (x, y))


while True:
    screen.blit(background, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    show_sun(sun_x, sun_y)

    show_mercury(mercury_x, mercury_y)
    mercury_x += 0.15 * math.cos(var_mercury)
    mercury_y += 0.15 * math.sin(var_mercury)
    var_mercury += 0.0013

    show_venus(venus_x, venus_y)
    venus_x += 0.15 * math.cos(var_venus)
    venus_y += 0.15 * math.sin(var_venus)
    var_venus += 0.0011

    show_earth(earth_x, earth_y)
    earth_x += 0.15 * math.cos(var_earth)
    earth_y += 0.15 * math.sin(var_earth)
    var_earth += 0.00088

    show_mars(mars_x, mars_y)
    mars_x += 0.15 * math.cos(var_mars)
    mars_y += 0.15 * math.sin(var_mars)
    var_mars += 0.0007

    show_jupiter(jupiter_x, jupiter_y)
    jupiter_x += 0.15 * math.cos(var_jupiter)
    jupiter_y += 0.15 * math.sin(var_jupiter)
    var_jupiter += 0.0005

    show_saturn(saturn_x, saturn_y)
    saturn_x += 0.15 * math.cos(var_saturn)
    saturn_y += 0.15 * math.sin(var_saturn)
    var_saturn += 0.00038

    show_uran(uran_x, uran_y)
    uran_x += 0.15 * math.cos(var_uran)
    uran_y += 0.15 * math.sin(var_uran)
    var_uran += 0.000325

    show_netune(netune_x, netune_y)
    netune_x += 0.15 * math.cos(var_netune)
    netune_y += 0.15 * math.sin(var_netune)
    var_netune += 0.0002985

    pygame.display.update()