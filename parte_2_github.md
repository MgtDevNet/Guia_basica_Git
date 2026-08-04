# GITHUB
Es una plataforma de control de versiones a nivel nube, donde todos los respositorios se guardan en una plataforma donde muchas personas desde diferentes maquinas pueden ver, editar y trabajar en conjunto. Trabaja con git, pero la diferencia es que los repositorios(galeria)
no es solo a nivel local del computador si no también que esta en la nube para que cualquier persona pueda verlo.

Github es por excelencia la red social de los desarrolladores, hay que tener un perfil presentable y se puede usar tanto para públicar proyectos como para ver proyectos de diferentes personas, siempre y cuando sean públicos o den el permiso personalmente.

En la parte de explorar(`Explore`) se pueden ver todas las públicaciones públicas hechas a nivel mundial y aparecen los repositorios de proyectos. Es un lugar bastante diferente y útil donde puedes contactar personas, entrar a proyectos open source para contribuir en ellos, entre muchas otras cosas. 

Si se tiene un proyecto importante y se quiere por ejemplo
trabajar en equipo, lo podemos subir a un servidor para que varias personas podamos ir
trabajando en el, el proyecto en githhub es una manera remota, online, es la union para trabajar
cada uno en el proyecto. SOLO HAY UN PUNTO ÚNICO DE UNION ENTRE DESARROLLADORES Y SERA 
GITHUB que sera el servidor remoto. Incluso es muy útil asi sea un trabajo personal pues en caso
que se dañe el pc o se pierda el trabajo local que se tiene si se puso el trabajo en github
no se perdera pues es un servidor remoto fuera de tu pc, incluso si se cambia de ordenador, simplemente
descargo los archivos y sigo trabajando como si no pasara nada.

Por tanto, como tenemos nuestros propios repositorios de manera local en nuestras computadoras, podemos tenerlos a nivel nube con github:

## CREA TU PRIMER RESPOSITORIO EN GITHUB
1. Entra a github y registrate: [www.github.com](https://github.com/)

2. Para crear un repositorio y tenerlo en github hay 2 formas principales: 

a). Crear un repositorio con git en nuestra propia maquina y luego subirlo con github.
b). Crear un repositorio en github y luego conectarlo con github. 

Para empezar, le damos al botón `new` para crear un nuevo repositorio  y como es la primera vez lo mejor que podemos hacer
es que le pondremos nuestro nombre. Github sabe que será el primer repo en el cual se podra crear la pagina de inicio y lo que la gente verá de primera como presentación de cada persona.

* Para todo proyecto es importante ser especifícos y pues se tiene las opciones de que los 
proyectos sean públicos(todos pueden ver) o privados(solo tú y personas con permiso podran ver) 
según la necesidad.

* Es recomendable que para todo repositorio se le añada un archivo de tipo `README.md` que es 
un documento que se coloca en la raíz de un repositorio para proporcionar información textual sobre el proyecto. 
ES LO PRIMERO QUE LOS VISITANTES VEN, por lo que se usa para explicar de que se trata, cómo usarlo y cualquier información relevante. Por convención el archivo se llama README.md con .md para markdown lo que permite formatear texto con estilos como encabezados, listas, enlaces y codigo. Contiene el titulo del proyecto, descripción, instalación, uso, contribución, licencia, Autor o mantenedores y referencias (Markdown es un lenguaje de marcado simple que convierte texto plano en formato con estilo, como encabezados, litas, enlaces y código).

* Tambien se puede añadir un .gitignore por si se necesita 

* La licencia es un documento que establece los terminos bajo los cuales otras personas pueden usar, modificar y distribuir el codigo de un repositorio, es decir, establece los derechos de autor para que nadie pueda usar lo que hiciste protegiendo al creador como a los usarios del codigo. SIN LICENCIA EL CODIGO ES PROTEGIDO AUTOMÁTICAMENTE POR DERECHOS DE AUTOR y nadie puede usarlo legalmente, una licencia da permiso para usar el código bajo ciertas condiciones. Por ello hay varios tipos de licencia.



## Unir github con git local
[documentación](https://docs.github.com/es) 
### Autenticación y coneccion SSH a github:
En general es un metodo de autenticacion de llave pública y privada para servidores remotos donde no hay necesidad de estar usando usuarios y
contraseñas, se hace mediante un archivo de clave privada en el equipo local.

primero EN LA TERMINAL comprobaremos si ya tenemos unas claves ssh con `ls -al ~/.ssh` (TODO ESTO ESTA EN LA DOCUMENTACIÓN DE GITHUB):
* Si NO se tienen llaves ssh entonces se pone `ssh-keygen -t ed25519 -C "your_email@example.com"` (notese
que ac+a se usa el algoritmo de encriptación ed25519 pero tambien puede ser el rsa y el correo debe 
ser el mismo con el que se tiene la cuenta de github) y de esta manera se crea un llave pública y una privada y hay que poner un nombre al archivo donde se guardaran. Si se quiere mas seguridad se puede poner una frase de contraseña o se puede dejar en blanco y asi se me ha crado una clave ssh; en el directorio `.ssh` apareceran 2 archivos nombre y nombre.pub que son las llaves públicas y privadas.

Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]  acá es donde se indica el nombre
de las claves. Dan unos recomendados como lo son id_rsa, id_ed25519 pero en general puede ser el que queramos. Aunque
si solo se da enter notese que se guardara automaticamente en una nueva carpeta llamada `.ssh` con el nombre id_<algorithm>

Y esto es para ingresar una contraseña adicional, en caso que no se quiera simplemente se da enter
Enter passphrase (empty for no passphrase): [Type a passphrase]

> Enter same passphrase again: [Type passphrase again]

Luego para github necesitamos el archivo de llave pública el .pub 

### AGENTE-SSH(ssh-agent)
Es un programa que se ejecuta en segundo plano y almacena tus claves privadas SSH en la memoria, de manera
que no tengas que ingresar tu frase de paso cada vez que te conectas a un servidor o interactúas con servicios
como github usando SSH. Primero se generan las claves SSH (pública y privada) y se añade la clave
privada al agente con ssh-add para que pueda ser utilizada y asi, cuando me conecte a un servidor o use
git ssh-agent proporciona automáticamente a clave privada al servidor. 

1. se ejecuta `eval "$(ssh-agent -s)"` y se iniciara el ssh-agent en segundo plano y retornara un 
`agent pid ####` que indica que el proceso esta corriendo.

4. hacer `ssh-add c:/Users/YOU/.ssh/id_ed25519` agregar la clave privada y de esta
manera se queda lista para que la clave quede guardada. 

Hasta ahora ya tenemos las claves públicas y privadas además de del agente ssh se tiene que hacer
lo siguiente:

* Nos vamos a github $\rightarrow$ settings $\rightarrow$ SSH and GPG keys (son claves importantes, en caso de que se trabaje siempre desde la misma pagina es bueno hacer esto para que se guarden estas claves y no se tenga que tener que configurar
cada que se entra.) $\rightarrow$ crear una nueva clave SSH (se le puede dar un nombre) $\rightarrow$ en la parte
de la clave se le pondra la clave pública que creamos hace un momento (es todo el código que aparece en un archivo
de tipo pubisher pero se puede abrir facilmente con el bloc de notas ) y luego se añade, en caso que se tengan
mas ordenadores o cosas por el estilo se ueden añadir mas claves.

Finalmente hay que verificar que si se haya conectado con la maquina local escribiendo `ssh -T git@github.com` en la terminal y se confirma para que esa llave se mantenga activa.

Luego de haber unido el git del pc con github, obviamente no es recomendable subir un proyecto en el primer repositorio que es la carta de presentación de cada desarrollador. Eso es solo para poner una buena introducción de lo que se verá en todo el perfil. 

Ahora al crear un repositorio nuevo se podran ver diferentes opciones desde el github 

## Comando para trabajar de git a github pronto ...