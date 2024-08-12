package org.example;
import java.util.ArrayList;
import java.util.List;

class Nodo {
    int data;
    List<Nodo> hijos;

    Nodo(int data) {
        this.data = data;
        this.hijos = new ArrayList<>();
    }
    void addHijo(Nodo hijo) {
        hijos.add(hijo);
    }

    Nodo findNode(int value) {
        if (this.data == value) {
            return this;
        }
        for (Nodo hijo : hijos) {
            Nodo result = hijo.findNode(value);
            if (result != null) {
                return result;
            }
        }
        return null;
    }
}
