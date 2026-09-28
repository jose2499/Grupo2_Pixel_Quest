#include "libreria.h"

// Insertar un estudiante en la lista
void insertarEstudiante(Estudiante*& lista, string nombre, int cantidadAsignaturas, float promedioGeneral) {
    Estudiante* nuevo = new Estudiante(nombre, cantidadAsignaturas, promedioGeneral);
    if (lista == nullptr) {
        lista = nuevo;
    } else {
        Estudiante* actual = lista;
        while (actual->siguiente != nullptr) {
            actual = actual->siguiente;
        }
        actual->siguiente = nuevo;
    }
}

// Mostrar la lista de estudiantes
void mostrarEstudiantes(Estudiante* lista) {
    if (lista == nullptr) {
        cout << "No hay estudiantes registrados.\n";
        return;
    }
    Estudiante* actual = lista;
    while (actual != nullptr) {
        cout << "Nombre: " << actual->nombre
             << ", Asignaturas: " << actual->cantidadAsignaturas
             << ", Promedio: " << actual->promedioGeneral << endl;
        actual = actual->siguiente;
    }
}

// Calcular el promedio general de la clase
float calcularPromedioClase(Estudiante* lista) {
    if (lista == nullptr) return 0;

    float sumaPromedios = 0;
    int contador = 0;
    Estudiante* actual = lista;

    while (actual != nullptr) {
        sumaPromedios += actual->promedioGeneral;
        contador++;
        actual = actual->siguiente;
    }

    return (contador == 0) ? 0 : sumaPromedios / contador;
}

// Filtrar estudiantes con promedio mayor al promedio de la clase
Estudiante* filtrarEstudiantes(Estudiante* lista, float promedioClase) {
    Estudiante* nuevaLista = nullptr;

    while (lista != nullptr) {
        if (lista->promedioGeneral > promedioClase) {
            insertarEstudiante(nuevaLista, lista->nombre, lista->cantidadAsignaturas, lista->promedioGeneral);
        }
        lista = lista->siguiente;
    }

    return nuevaLista;
}

// Eliminar toda la lista
void eliminarLista(Estudiante*& lista) {
    while (lista != nullptr) {
        Estudiante* temp = lista;
        lista = lista->siguiente;
        delete temp;
    }
}
