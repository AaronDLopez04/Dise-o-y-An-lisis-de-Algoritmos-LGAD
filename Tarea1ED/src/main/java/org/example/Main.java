package org.example;

public class Main {
    public static void main(String[] args) {
        // Creación de los nodos
        Nodo head = new Nodo(20);
        Nodo nodo23 = new Nodo(23);
        Nodo nodo19 = new Nodo(19);
        Nodo nodo57 = new Nodo(57);
        Nodo nodo67 = new Nodo(67);
        Nodo nodo99 = new Nodo(99);

        // Construcción de la estructura
        head.addHijo(nodo23);
        head.addHijo(nodo19);
        nodo23.addHijo(nodo57);
        nodo19.addHijo(nodo67);
        nodo67.addHijo(nodo99);

        // Encontrar y mostrar el nodo 99
        Nodo foundNode = head.findNode(99);
        if (foundNode != null) {
            System.out.println("Nodo encontrado: " + foundNode.data);
        } else {
            System.out.println("Nodo 99 no encontrado.");
        }

        // Encontrar y mostrar el nodo 57
        foundNode = head.findNode(57);
        if (foundNode != null) {
            System.out.println("Nodo encontrado: " + foundNode.data);
        } else {
            System.out.println("Nodo 57 no encontrado.");
        }
    }
}