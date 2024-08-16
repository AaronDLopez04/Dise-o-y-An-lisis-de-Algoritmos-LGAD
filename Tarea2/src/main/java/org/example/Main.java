package org.example;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        int[] arreglo = {1, 2, 3, 4};
        List<String> combinaciones = new ArrayList<>();
        // T(n)=1

        System.out.println("Entrada: " + Arrays.toString(arreglo));
        generarCombinaciones(arreglo, combinaciones);
        //T(n)=n^2

        // Imprimir las combinaciones
        for (String combinacion : combinaciones) {
            System.out.println(combinacion);
        }
        //T(n)=n^2

        // Imprimir la cantidad total de combinaciones
        System.out.println("Final: " + combinaciones.size());
        //T(n)=1
    }

    private static void generarCombinaciones(int[] arreglo, List<String> combinaciones) {
        // Recorrer cada par posible de elementos en el arreglo
        for (int k : arreglo) { //T(n)=n
            for (int i : arreglo) { //T(n)=n
                // Formar la combinación y agregarla a la lista
                combinaciones.add(k + " " + i); //T(n)=1
            }
        }
        //T(n)= n*n = n^2
    }
}
//S(n)= 1 + n^2 + n^2 + 1 = 2n^2 + 2