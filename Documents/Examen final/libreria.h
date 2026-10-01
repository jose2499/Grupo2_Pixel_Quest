#pragma once
#include <iostream>
#include <string>
using namespace std;

// Estructura para representar un estudiante
struct Estudiante {
    string nombre;
    int cantidadAsignaturas;
    float promedioGeneral;
    Estudiante* siguiente;

    Estudiante(string n, int ca, float pg) : nombre(n), cantidadAsignaturas(ca), promedioGeneral(pg), siguiente(nullptr) {}
};

// Funciones para manejar la lista de estudiantes
void insertarEstudiante(Estudiante*& lista, string nombre, int cantidadAsignaturas, float promedioGeneral);
void mostrarEstudiantes(Estudiante* lista);
float calcularPromedioClase(Estudiante* lista);
Estudiante* filtrarEstudiantes(Estudiante* lista, float promedioClase);
void eliminarLista(Estudiante*& lista);
