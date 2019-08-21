#include <stdio.h>
#include <stdlib.h>

int main(){

    int piso[4] = {1,1,0,1}; //definimos condiciones iniciales de las baldozas

    int limpio = 0;
    int sucio = 1;
    int i = 0;

    int direccion; //indicamos si se va a incrementar (mover a la derecha) o si vamos a decrementar (mover a la izquierda)

    char c = 'a';

    while(1){
          
          if(piso[i] == sucio){
              printf("LIMPIAR...");
              piso[i] = limpio; // el piso que acaba de limpiar lo pone en estado = 0 (limpio) y sale del while
          }else{
              if(i == 3){
                  direccion = -1;
              }else if (i == 0){
                  direccion = 1;
              }
              i = i + direccion; //incrementa o decrementa la direccion según la posicion de la baldoza
              printf("MOVIMIENTO A %d..",i);
          }

      scanf("%c",&c);
    }
    return 0;
}