#include "libreria.h"

int main() {
    Estudiante* listaEstudiantes = nullptr;
    int opcion;

    do {
        cout << "\nMenu:\n";
        cout << "1. Registrar estudiante\n";
        cout << "2. Mostrar estudiantes\n";
        cout << "3. Mostrar promedio general de la clase\n";
        cout << "4. Filtrar estudiantes con promedio mayor al promedio de la clase\n";
        cout << "5. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1: {
                string nombre;
                int cantidadAsignaturas;
                float promedioGeneral;

                cout << "Ingrese el nombre del estudiante: ";
                cin >> nombre;
                cout << "Ingrese la cantidad de asignaturas: ";
                cin >> cantidadAsignaturas;

                if (cantidadAsignaturas <= 0) {
                    cout << "La cantidad de asignaturas debe ser mayor a 0.\n";
                    break;
                }

                float sumaNotas = 0, nota;
                for (int i = 1; i <= cantidadAsignaturas; i++) {
                    do {
                        cout << "Ingrese la nota de la asignatura " << i << " (0-20): ";
                        cin >> nota;
                        if (nota < 0 || nota > 20) {
                            cout << "Nota invalida. Ingrese una nota entre 0 y 20.\n";
                        }
                    } while (nota < 0 || nota > 20);
                    sumaNotas += nota;
                }

                promedioGeneral = sumaNotas / cantidadAsignaturas;
                insertarEstudiante(listaEstudiantes, nombre, cantidadAsignaturas, promedioGeneral);
                break;
            }

            case 2:
                mostrarEstudiantes(listaEstudiantes);
                break;

            case 3: {
                float promedioClase = calcularPromedioClase(listaEstudiantes);
                cout << "Promedio general de la clase: " << promedioClase << endl;
                break;
            }

            case 4: {
                float promedioClase = calcularPromedioClase(listaEstudiantes);
                Estudiante* listaFiltrada = filtrarEstudiantes(listaEstudiantes, promedioClase);
                cout << "Estudiantes con promedio mayor al promedio de la clase:\n";
                mostrarEstudiantes(listaFiltrada);
                eliminarLista(listaFiltrada); // Limpiar la lista filtrada
                break;
            }

            case 5:
                cout << "Saliendo...\n";
                eliminarLista(listaEstudiantes); // Limpiar la lista original
                break;

            default:
                cout << "Opcion invalida.\n";
        }
    } while (opcion != 5);

    return 0;
}
