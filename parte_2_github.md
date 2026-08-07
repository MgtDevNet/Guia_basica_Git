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

## Comando para trabajar con git y github

### 1. git remote
Es un comando que permite gestionar los repositorios remotos asociados con mi repositorio local (el repositorio remoto es una versión de mi proyecto en un servidor)
;por ello; para poder unir un repositorio local a uno remoto en github creamos por separado cada reposotorio y luego los unimos con el comando:  

🖥️
```bash  
    git remote add origin https://github.com/usuario/nombre-repositorio.git #unión por https  
    git remote add origin git@github.com:usuario/nombre-repositorio.git # unión por ssh
```
    
Donde `origin` es el nombre que se le da a la rama princiapl del repositorio remoto las url ya sea por https o ssh es el identificador con el repositorio remoto en la web, luego de darle enter entonces se une con el repo local.

🖥️
```bash  
    git remote -v # muestra todos los repositorios remotos configurados
    #por tanto, es una forma de verificar si ya se tiene un repo remoto configurado a mi repo local
```

🖥️
```bash  
    git remote remove <nombre-repositorio> # para remover y desvincular un repositorio remoto con uno local
```

🖥️
```bash  
    git remote rename origin <nombre-nuevo> # cambia el nombre del repositorio remoto de origin al nombre indicado
```

🖥️
```bash  
    git remote set-url nombre nueva-url # sirve para actualizar la url del repositorio
```

🖥️
```bash  
    git remote show origin # muestra detalles sobre el remoto llamado origin
```  

### 2. git push
Es el comando en git que se usa para subir mis cambios locales (commits) al respositorio remoto como github. Es como actualizar la version online del proyecto con las modificaciones que has he hecho con la maquina local. 

**Primer git push que debe hacerse para establecer el vínculo entre ramas**
🖥️
```bash
    git push -u origin main  
``` 
* -u: establece una referencia de seguimiento para la rama local vinculandola con la rama remota de tal manera que no hay que poner todo eso otra vez para subir los commits. 
* origin: nombre del repositorio remoto por defecto.
* main: nombre de la rama remota donde quieres enviar tus cambios.

Esa es la manera de relacionar la rama main con la rama principal remota origin. Tal vez pida autenticar la contraseña de github pero nada más. Ahora, se refresa la pagina de github y ya se pueden ver los arhivos que teniamos en local, incluido el gitignore y todo en una rama que se llama main.   

> De ahora en adelante, basta con hacer un `git push` para enviar los cambios de local a remoto.  

Notese que en el repositorio remoto en la esquina superior derecha se pueden ver todos los commits

IMPORTANTE: Cuando nosotros seguimos trabajando en nuestro proyecto de manera local y luego hacemos un commit de este. No se guardara en github automaticamente; es decir, se guardará en el repositorio local que nostoros tenemos pero no se guardará en el remoto; para ello, hay que hacer  nuestro git push. Al hacerlo, nuestro repositorio local estará a la par con el repositorio remoto. 

Haciendo `git log`, aparecerá el head de ORIGIN que es el nombre del repositorio remoto y también donde está el head de MAIN. Recordemos que el head es el indicador de donde nos encontramos en el proyecto. 

### 3.git fetch
Este comando descarga todos los cambios del repositorio remoto al repositorio local, pero sin aplicar esos cambios a la rama actual. Es decir, permite ver en que ha cambiado el repo remoto antes de decidir si deseas incorporar esos cambios. Es como ver una vista previa sin afectar el trabajo actual. Por ejemplo, si se esta trabajando en una rama main pero un compañero ha hecho cambios en el repositorio remoto que aún no tenemos en el local, para ver los cambios en el remoto es

🖥️
```bash
    git fetch origin  
``` 
     
Esto descargara todos los cambios del repositorio remoto origin pero sin fusionarlos en la rama actual.

Para ver los cambios sin aplicarlos aún se puede ver la nueva informacion en el remoto y comparar

🖥️
```bash
    git log origin/main
```     
Esto muestra el historial del remoto para ver los commit que se han agregado desde la última vez que sincronizaste. En caso de que se decida incorporar los cambios despues de verlos, se puede hacer con un git merge o un GIT PULL

🖥️
```bash
    git merge origin/main # que fusiona los cambios descargados en la rama main.
```
Finalmente, git fetch descarga los cambios que tiene el repositorio remoto antes de
aplicarlos a la rama main para ver las actualizaciones antes de fusionarlas al trabajo.

Es el comando que se usa luego de hacer el `git push -u origin main`, sirve cuando se intenta hacer un git push pero hay un problema pues querrá decir que se esta intentando subir o actulizar desde el local al remoto, pero alguien hizo algun cambio primero y hay conflicto por lo que primero
hay que revisar estos conflictos y tener nuestra rama main local acutalizada a la del remoto y ahi ya no habran conflictos. 
