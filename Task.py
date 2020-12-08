import math
import sys


def is_there_the_triangle(triangle1, triangle2):
	a1 = triangle1[0]
	b1 = triangle1[1]
	c1 = triangle1[2]
	a2 = triangle2[0]
	b2 = triangle2[1]
	c2 = triangle2[2]
	if a1 <= 0 or b1 <= 0 or c1 <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
		print("Треугольника с отрицательными сторонами не бывает)")
		return False
	if not (a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1):
		print("Треугольника со сторонами ({}, {}, {}) не существует".format(a1, b1, c1))
		return False
	if not (a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2):
		print("Треугольника со сторонами ({}, {}, {}) не существует".format(a2, b2, c2))
		return False
	return True


def similarity_check(triangle1, triangle2):
	if triangle1[0] / triangle2[0] == triangle1[1] / triangle2[1] == triangle1[2] / triangle2[2]:
		return True
	else:
		return False


def finding_the_area(triangle):
	p = (triangle[0] + triangle[1] + triangle[2]) / 2
	s = math.sqrt(p * (p - triangle[0]) * (p - triangle[1]) * (p - triangle[2]))
	return s


def finding_the_perimeter(triangle):
	return triangle[0] + triangle[1] + triangle[2]


name_file = sys.argv[1]

file = open(name_file, 'r')

n = int(file.readline())

triangles1 = [[] for i in range(n)]
triangles2 = [[] for g in range(n)]

for i in range(n):
	_ = file.readline().split()
	for j in range(3):
		triangles1[i].append(int(_[j]))
		triangles2[i].append(int(_[3 + j]))

count = 0
square = []
perimeter = []

for i in range(n):
	if not is_there_the_triangle(triangles1[i], triangles2[i]):
		continue

	if not similarity_check(triangles1[i], triangles2[i]):
		continue
	else:
		count += 1

	square.append(finding_the_area(triangles1[i]) + finding_the_area(triangles2[i]))

	perimeter.append(finding_the_perimeter(triangles1[i]) + finding_the_perimeter(triangles2[i]))

if count != 0:
	print("Количество пар подобных треугольников равно: {}".format(count))
	print("Суммарные площади каждой пары подобных треугольников равны:")
	for elem in square:
		print("{}".format(elem))
	print("Суммарные периметры каждой пары подобных треугольников равны:")
	for elem in perimeter:
		print("{}".format(elem))
else:
	print("Подобные треугольники не были найдены")
print()