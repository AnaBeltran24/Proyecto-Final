# Proyecto Final: Algoritmos y Programación

## Videojuego Pong
###### 
Desarrollado por Ana Sofía Beltrán y
Julián Camilo Espinosa

# Introducción
¿Las mesas de Ping Pong de la universidad se encuentran ocupadas? Te traemos esta divertida alternativa virtual, donde podrás competir con tus amigos y pasar un buen rato. Para este proyecto se realizó un Pong, un videojuego basado en el tenis de mesa, que consiste en un jugador que mueve la paleta ubicada en la parte inferior de la pantalla. Una pelota se envía verticalmente a través de la pantalla y el objetivo es utilizar la paleta para devolverlo sin tocar la línea de fondo. En la parte superior hay otra paleta controlada por una máquina o por otro jugador. La pelota será devuelta en un intento de llegar a la segunda base que hace el primer contacto. De esta manera, tenemos un videojuego muy competitivo. A continuación se presentará como desarrollamos el juego y que herramientas utilizamos para este.   
  <div align="center">
    <img src="https://tierragamer.com/wp-content/uploads/2017/12/Pong-1280x720.jpg" width="650" height="300" /> </div>

# Herramientas utilizadas:

## Python:
Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador. Asimismo, es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano.

## Pygame: 
Pygame es una librería para el desarrollo de videojuegos en segunda dimensión 2D con el lenguaje de programación Python. Pygame está basada en SDL, que es una librería que nos provee acceso de bajo nivel al audio, teclado, ratón y al hardware gráfico de nuestro ordenador. Es un producto que funciona en cualquier sistema: Mac OS, Windows o Linux.

## Visual Studio Code:
Visual Studio Code es un editor de código fuente desarrollado por Microsoft que proporciona muchas facilidades para escribir, depurar y probar código. Es software libre y multiplataforma, está disponible para Windows, GNU/Linux y macOS. De igual manera, tiene una buena integración con Git, y dispone de un sinnúmero de extensiones, que básicamente te da la posibilidad de escribir y ejecutar código en cualquier lenguaje de programación.

# ¿Por qué Pong?
Tomamos la decisión de crear un Pong ya que este nos da la oportunidad de aplicar lo visto en clase, como el uso de funciones, bucles con while y for, y condicionales if, elif, else. De igual manera, queríamos desarrollar un juego multijugador, que permita la diversión entre amigos y familiares.

## ¿Cómo desarrollamos el Pong?
Para desarrollar nuestro Pong necesitamos una librería llamada pygame, la cual nos ayudó a crear nuestro juego. En primer lugar, estos son algunos elementos principales para entender qué es Pygame y la creación del programa junto a Python: 
- Función main() o clase Game(): contenedor del videojuego. 
- Control de eventos: pygame.event.get(), es decir, lista de eventos a procesar. 
- Sprites: rectángulos que representan los objetos móviles o fijos del juego. Estos pueden animarse con frames o modificarse gráficamente. También se pueden detectar colisiones entre ellos. 
- Sonidos: pygame.mixer.Sound() y play. 
- Textos: pygame.font.Font(file_path, size) y render.

Para la creación de la pantalla, primero se definió el tamaño, el cual es 750 x 500, y los colores, blanco (255,255,255) y negro (0,0,0). Después, se le asignó el título ”Juego Pong”. Después de eso creamos una clase que definimos como fondo, colocamos el texto que esta dentro de la pantalla, como lo es el nombre de los jugadores, su numero de puntos y la línea que divide la mitad del campo del juego.

Para la creación de los jugadores fue necesario asignar una clase en la cual establecimos el tamaño, el color del jugador, la posición en donde está el jugador en la pantalla que definimos anteriormente, su velocidad, la cual ayudara a que el jugador se desplace por el juego y su número de puntos inicial, el cual inicia en cero. 

Al igual que los jugadores para la pelota usamos el mismo código, a excepción de los puntos iniciales ya que a la pelota no se le define ese comando.

Una vez definido estos elementos, procedimos a desarrollar el juego con un while True y dentro de el colocamos un for que nos ayuda a cerrar la pestaña del juego. Después colocamos una serie de "if" que ayudan a la creación de los controles de los jugadores, colocandole los casos posibles para que se generen las colisiones. Luego hicimos que la pelota tuviera una dirección, por medio de una multiplicación de su velocidad por la dirección de este, y por último hicimos un algoritmo que permitiera que se sumen los puntos en los marcadores de los jugadores.

# Conclusión
Gracias a este proyecto, tuvimos la oportunidad de reforzar los temas vistos en el curso de algoritmos y programación, ya que como se menciona anteriormente, utilizamos Python, junto a sus condicionales (if) y bucles (while y for). Asimismo, aprendimos sobre Pygame y los códigos que utiliza. Por último,  logramos comprender como se lleva a cabo el proceso de programación. Es un procedimiento que requiere paciencia, delicadeza, comprensión y resolución de problemas.  Esperamos poder aplicar el conocimiento y la experiencia adquirida en este proyecto en nuestro futuro. 
# Bibliografía:
- Flores, F. (22 de julio de 2022). Qué es Visual Studio Code y qué ventajas ofrece. Obtenido de https://openwebinars.net/blog/que-es-visual-studio-code-y-que-ventajas-ofrece/
- Keepcoding, R. (9 de junio de 2022). ¿Qué es Pygame? Obtenido de https://keepcoding.io/blog/que-es-pygame/
- Universidades, S. (9 de abril de 2021). Python: qué es y por qué deberías aprender a utilizarlo. Obtenido de https://www.becas-santander.com/es/blog/python-que-es.html
- videojuegos, T. (2017). Pong. Obtenido de https://tus-videojuegos.com/pong/

