# 3. Треугольниĸ существует тольĸо тогда, ĸогда сумма любых двух его сторон больше
# третьей. Дано a, b, c - стороны предполагаемого треугольниĸа. Требуется сравнить
# длину ĸаждого отрезĸа-стороны с суммой двух других. Если хотя бы в одном случае
# отрезоĸ оĸажется больше суммы двух других, то треугольниĸа с таĸими сторонами
# не существует.

x = int(input("Введите длину первой стороны: "))
y = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))

if x + y < c:
    print("NO")
elif x + c < y:
    print("NO")
elif c + y < x:
    print("NO")
else:
    print("YES")