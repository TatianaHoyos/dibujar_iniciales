tamaño_m=int(input("ingrese tamaño de matriz, numero impar mayor a 3: "))
#valido que le tamaño de la matriz sea valido
while tamaño_m<5 or tamaño_m%2==0:
  print("tamaño invalido ", tamaño_m)
  tamaño_m=int(input("ingrese un número impar mayor que 3: "))
matriz=[]
matriz=[[0 for i in range(tamaño_m)] for i in range(tamaño_m)]

#letra T
for fila in range(0,tamaño_m,1):
  for columna in range(0,tamaño_m,1):
    if columna==1 or columna==tamaño_m-2:
        matriz[fila][columna]="*"
    elif fila==(tamaño_m/2-0.5) and columna>1 and columna<tamaño_m-2:
        matriz[fila][columna]="*"
    else:
        matriz[fila][columna]=" "


dibujo=""
for fila in range(0,tamaño_m,1):
  for columna in range(0,tamaño_m,1):
     dibujo +=" " +matriz[fila][columna]+" "
  dibujo+="\n"
print(dibujo)