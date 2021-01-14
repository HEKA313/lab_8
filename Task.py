import math
import sys


def is_there_the_triangle(a1, b1, c1, a2, b2, c2):  # Проверка существования треугольника
	check = True
	if a1 <= 0 or b1 <= 0 or c1 <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
		print("Треугольника с отрицательными сторонами не бывает)")
		check = False
	if not (a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1):
		print("Треугольника со сторонами ({}, {}, {}) не существует".format(a1, b1, c1))
		check = False
	if not (a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2):
		print("Треугольника со сторонами ({}, {}, {}) не существует".format(a2, b2, c2))
		check = False
	return check


def similarity_check(triangle1, triangle2):  # Проверка подобия
	if triangle1[0] / triangle2[0] == triangle1[1] / triangle2[1] == triangle1[2] / triangle2[2]:
		check = True
	else:
		check = False
	return check


def finding_the_area(triangle):  # нахождение площади
	p = (triangle[0] + triangle[1] + triangle[2]) / 2
	s = math.sqrt(p * (p - triangle[0]) * (p - triangle[1]) * (p - triangle[2]))
	return s


def finding_the_perimeter(triangle):  # нахождение периметра
	return triangle[0] + triangle[1] + triangle[2]


name_file = sys.argv[1]  # чтение командной строки

file = open(name_file, 'r')  # открытие файла

n = int(file.readline())  # считывание количества треугольников

# инициализация массивов
triangles1 = [0] * n
triangles2 = [0] * n

for i in range(n):
	triangles1[i] = [0] * 3
	triangles2[i] = [0] * 3

for i in range(n):  # считывание массивов
	line = file.readline().split()
	for j in range(3):
		triangles1[i][j] = int(line[j])
		triangles2[i][j] = int(line[3 + j])

# инициализация переменных
count = 0
square = [0] * n
perimeter = [0] * n

for i in range(n):
	a1, b1, c1 = triangles1[i][0], triangles1[i][1], triangles1[i][2]
	a2, b2, c2 = triangles2[i][0], triangles2[i][1], triangles2[i][2]
	if is_there_the_triangle(a1, b1, c1, a2, b2, c2):  # существуют ли треугольники
		if similarity_check(triangles1[i], triangles2[i]):  # подобны ли треугольники
			# подсчет количества подобных треуг и нахождения площади и периметра
			count += 1
			square[i] = (finding_the_area(triangles1[i]) + finding_the_area(triangles2[i]))
			perimeter[i] = (finding_the_perimeter(triangles1[i]) + finding_the_perimeter(triangles2[i]))

if count != 0:  # проверка на количество подобных треугольников
	print("Количество пар подобных треугольников равно: {}".format(count))
	print("Суммарные площади каждой пары подобных треугольников равны:")
	for elem in square:  # вывод площадей
		if elem != 0:
			print("{}".format(elem))
	print("Суммарные периметры каждой пары подобных треугольников равны:")
	for elem in perimeter:  # вывод периметров
		if elem != 0:
			print("{}".format(elem))
else:
	print("Подобные треугольники не были найдены")
print()
