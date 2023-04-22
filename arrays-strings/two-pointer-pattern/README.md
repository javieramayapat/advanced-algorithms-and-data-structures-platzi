# ****Patrón de Dos Apuntadores (⬇️ ⬇️)****


<div align="center">
<img src="https://miro.medium.com/v2/resize:fit:1400/1*XOOm3-HktTdz6keEV2-NmA.gif" width="250" height="250"/>
</div>



## ¿Qué es este patrón?

- Significa que podemos usar 2 enteros para referirnos a las posiciones de  una lista de datos y esas posiciones irlas moviendo dependiendo de ciertas condiciones

## Para que me sirve:

- Solo comparar con las cosas que yo quiero comparar y evitar redundacia, ayuda a mejorar la complejidad de los algoritmos cuando deseamos comparar de forma más inteligente.

## ¿Cómo colocar los apuntadores?

- Puedo tener 1 apuntador al inicio y un apuntador al final, esto seria una buena forma para revisar si una palabra es palindromo o no.

## ¿Qúe es el ordenamiento in place?
El ordenamiento in-place (en su traducción literal al español, "en el mismo lugar") 
es un método de ordenamiento de arreglos en el que los elementos del arreglo se reorganizan dentro del mismo arreglo sin utilizar memoria adicional.

Significa ordenando valores moviendo valores haciendo las comparaciones
sin realmente tener que aplicar un algoritmo de ordenamiento bajando de complejidad O(n log n) a una solucion lineal O(n+m)

## Ejemplos de uso para el patron de dos apuntadores
Algunos ejemplos de casos en los que se puede utilizar este patrón son:

- Para encontrar una subcadena que cumpla ciertas condiciones, puedo usar 2 apuntadores y avanzar uno mientras parece una posible subcadena, mientras que el otro indica donde inicia la subcadena.
- Para comparar elementos en dos listas puedo usar 2 punteros, cada uno de estos apuntadores tiene noción del punto actual en una de las listas.
- Para mover y ordenar los elementos “in place”, puedo tener apuntadores para tener noción de los elementos ordenados y los que no.