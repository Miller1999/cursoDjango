Djanfo esta pensado para la reutilizacion utiliza el modelo MD

### Arquitectura - Clase 2

- M -> Model -> Estos son los datos y todo lo referente a ellos
- V -> View -> Conector puede ver los datos e interactuar sobre ellos, flujo, etc
- T -> Template -> La parte grafica, HTML y CSS

Se conectan mediante un contexto.

**Recomendacion**
No conectar directamente el template y el Model, siempre pasar por el View ya que esta contiene herramientas para poder trabajar con los datos

### ORM

El orm nos permite relacionar nuestros modelos en el back con tablas en la base de datos esto noes permite construir las bases de datos usando solo codigo python sin ncesisdad de hacer sentencias en SQL, estos ORM tambien ayudan a que no dependamos del motor de base de datos
