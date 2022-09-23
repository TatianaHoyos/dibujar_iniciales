tamaño_m=int(input("ingrese tamaño de matriz, numero impar: "))
#valido que le tamaño de la matriz sea valido
while tamaño_m<3 or tamaño_m%2==0:
  print("tamaño invalido ", tamaño_m)
  tamaño_m=int(input("ingrese un número impar mayor que 1 : "))
matriz=[]
matriz=[[0 for i in range(tamaño_m)] for i in range(tamaño_m)]

#letra T
for fila in range(0,tamaño_m,1):
  for columna in range(0,tamaño_m,1):
    if fila==0:
      matriz[fila][columna]="*"
    elif columna==(tamaño_m/2-0.5):
      matriz[fila][columna]="*"
    else:
      matriz[fila][columna]=" "


dibujo=""
for fila in range(0,tamaño_m,1):
  for columna in range(0,tamaño_m,1):
     dibujo +=" " +matriz[fila][columna]+" "
  dibujo+="\n"
print(dibujo)