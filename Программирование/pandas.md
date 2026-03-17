Содержит Dataframe и Series. Series это одномерный массив данных с индексами. DataFrame представляет из себя двумерную матрицу из нескольких series. Каждый столбец DataFrame может отличаться от другого по типу данных.

Создание серии происходит из списка
к примеру 
$num = [1,2,3,4]$
$ser = pd.Series(num)$
![Pasted image 20260314191716.png](Pasted image 20260314191716.png.md)
![Pasted image 20260314191844.png](Pasted image 20260314191844.png.md)
как и в [numpy](numpy.md) мы модем явно задать тип данных (да да в коде инт а у меня плавающая точка. Спасибо большое сборщику мусора за переполнение).

Так же можно передавать с помощью списка новые индексы в Series
![Pasted image 20260314192313.png](Pasted image 20260314192313.png.md)
![Pasted image 20260314192325.png](Pasted image 20260314192325.png.md)

Так же, как и в словарях можно обращаться по ключу
![Pasted image 20260314192530.png](Pasted image 20260314192530.png.md)
![Pasted image 20260314192543.png](Pasted image 20260314192543.png.md)


изменение тоже происходит по ключам

![Pasted image 20260314192745.png](Pasted image 20260314192745.png.md)
![Pasted image 20260314192755.png](Pasted image 20260314192755.png.md)

Так же можно создавать DataFrame из словаря
![Pasted image 20260314193509.png](Pasted image 20260314193509.png.md)
![Pasted image 20260314193523.png](Pasted image 20260314193523.png.md)

метод Merge 
