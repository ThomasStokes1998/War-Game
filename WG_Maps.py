import numpy as np


def water(tiles=1):
    return [-1] * tiles


def land(tiles=1):
    return [0] * tiles


def cities(tiles=1):
    return [2] * tiles


def mountain(tiles=1):
    return [-2] * tiles


def town(tiles=1):
    return [1] * tiles


# Europe Map
europe_row0 = water(35)
europe_row1 = water(17) + land(5) + water(13)
europe_row2 = water(12) + land(2) + water(2) + land(3) + mountain() + water(15)
europe_row3 = water(12) + land() + water(3) + land() + mountain() + land() + water(16)
europe_row4 = water(11) + land() + water(3) + land() + mountain(2) + land() + water() + land(4) + water(11)
europe_row5 = water(13) + land() + water() + land() + mountain() + land(6) + water(12)
europe_row6 = water(14) + land(3) + mountain(2) + land(4) + water(12)
europe_row7 = water(14) + land() + mountain(6) + land() + water(13)
europe_row8 = water(13) + land() + mountain(5) + land(3) + water(13)
europe_row9 = water(13) + land() + water() + land() + mountain(2) + land(3) + water(14)
europe_row10 = water(14) + land(6) + water(15)
europe_row11 = water(15) + land(2) + town() + land(2) + cities() + land() + water(13)
europe_row12 = water(16) + land(7) + water(12)
europe_row13 = water(16) + land(7) + water(12)
europe_row14 = water(8) + land(5) + water(3) + land(7) + water(12)
europe_row15 = water(7) + land(6) + water(3) + land(3) + water() + land() + mountain() + land(2) + water(11)
europe_row16 = water(8) + land(5) + town() + water(5) + land() + mountain() + land() + mountain() + land() + water(11)
europe_row17 = water(4) + land() + water() + land(7) + water(6) + mountain() + land() + mountain() + land(3) + water(9)
europe_row18 = water(3) + land(10) + water(3) + land() + water(4) + land() + mountain() + land(4) + water(8)
europe_row19 = water(4) + land(8) + water(9) + land(2) + town() + land(3) + water(8)
europe_row20 = water(3) + land() + water() + land(8) + water(7) + land(7) + water(8)
europe_row21 = water(4) + land(8) + cities() + water(4) + land() + water(2) + cities() + town() + land(6) + water(7)
europe_row22 = water(4) + land(8) + mountain() + water(4) + land() + mountain() + land(9) + water(7)
europe_row23 = water(4) + land(3) + mountain() + land(3) + mountain() + land() + water(5) + land() + mountain() + land(
    12) + water(3)
europe_row24 = water(3) + land(9) + water(6) + land(7) + town() + land(6) + water(3)
europe_row25 = water(3) + land(4) + mountain() + land(4) + water(6) + land(2) + mountain() + land(2) + cities() + land(
    8) + water(3)
europe_row26 = water(2) + land(7) + water(8) + land(2) + mountain() + land(11) + water(4)
europe_row27 = water(3) + land(3) + town() + water(8) + land(16) + water(4)
europe_row28 = water(4) + land() + water(13) + land() + town() + land(8) + town() + cities() + land() + water(4)
europe_row29 = water(20) + town() + land(8) + town() + land(3) + water(2)
europe_row30 = water(17) + land(15) + water(2) + land()
europe_row31 = water(16) + land(9) + cities() + land(2) + water() + land() + water(3) + land(2)
europe_row32 = water(16) + land(4) + water(2) + land() + town() + water() + land() + water(7) + land(2)
europe_row33 = water(15) + land(4) + water(14) + land(2)
europe_row34 = water(14) + land() + water(18) + land(2)
europe_row35 = water(31) + land(4)


def uk_map():
    map = np.array([europe_row0, europe_row1, europe_row2, europe_row3, europe_row4, europe_row5,
                   europe_row6, europe_row7, europe_row8, europe_row9, europe_row10, europe_row11,
                   europe_row12, europe_row13, europe_row14, europe_row15, europe_row16, europe_row17,
                   europe_row18, europe_row19, europe_row20, europe_row21, europe_row22, europe_row23,
                   europe_row24, europe_row25, europe_row26, europe_row27, europe_row28, europe_row29,
                   europe_row30, europe_row31, europe_row32, europe_row33, europe_row34, europe_row35], dtype='object')
    return map

map = uk_map()
print(map[35][34])

print(np.max([[1,2,3,4]]))