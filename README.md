# py-pratice_poo

**KATA I:** Evaluacion de Alumnos
 Vamos a desarrollar un programa donde nos facilite la evaluación de los alumnos. Para ello vamos a usar un POO.

Alumno:
    Propiedades:
    - Nombre
    - Apellidos
    - DNI
    - Edad
    - Nota

    Metodos:
    - Saludar
    - Añadir nota (0-10)
    - Cumplir años (+1 a la edad)

**KATA II:** Asignatura
 Usando la Kata anterior, vamos a crear una clase llamada Asignatura, para modularizar nuestro programa.

Asignatura:
    Propiedades:
    - Nombre
    - Nota

    Metodos
    - Añadir nota

Alumno(modificación):
    Propiedades:
    - Asignaturas

    Metodos:
    - Añadir Asignaturas
    - Eliminar Asignaturas

**KATA III**: Clase
 Usando la Kata anterior, camos a crear una clase llamada "Clase" donde crearemos la estructura de una clase con su profesor, alumnos y asignaturas con las mejores practicas posibles.

Clase:
    Propiedades:
    - Profesor
    - Alumnos
    - Asignaturas

    Metodos:
    - Añadir/Borrar Alumnos
    - Aádir/Borrar Asignatura

**KATA IV**: Encapsulando
Usando la Jata anterior, vamos a poner en privado los siguientes metodos y propiedades

Clase:
    - id(solo getter)

Asignatura:
    - id(solo getter)
    - nota(getter/setter)

Alumno:
    - dni(solo getter)

**KATA V**: Usuario/Profesor
Usando la Kata anterior, genera la clase Ususario y usa la herencia para que desde Usuario se cree Alumno y Profesor, reutilizando todo lo que veas oportuno