# Introducción a Git 🌱

## ¿Qué es git? 🤔
git es un sistema de control de versiones usado para manetener un 
orden y un control para proyectos de programación, es una herramienta extremadamente
útil para proyectos grandes. Vease git como una galería o historial, que cada que se le da una instruccion toma una foto con descripción, fecha y autor del proyecto, hasta donde se lleve, con lo que se lleve. De esta manera podemos ir viajando en el tiempo a partes del proyecto donde necesitamos ver o corregir algo.

Por ejemplo, supongamos que lo que se realizó en un proyecto no nos gusto, simplemente nos vamos a la última foto antes de ese último cambio y es como si nada hubiese pasado.

## Instalación ⚙️
Git esta de forma nativa en Linux, sin embargo, en caso de no tenerlo basta con hacer: 

🖥️
```bash
sudo apt update && sudo apt install git -y
```
En el caso de windows usaremos lo que se conoce como git bash la cual es una interfáz para trabajar con git que usa el lenguaje bash, que es el mismo lenguaje que usa linux de forma nativa.

Por tanto, **sin importar si lo que usas windows o en linux (Ubuntu en mi caso) como ambos usan el lenguaje bash se tendrá la misma sintaxis.**
primero que nada, como esto es un control de versiones y puede hacerse en cualquier computadora hay que registrarse con nombre y correo. La forma de hacerlo es muy sencilla pero hay 3 tipos de configuraciones: 


## Establecimiento de usuario 🛠️
### Tipos de configuración

Los niveles de configuración en Git sirven para determinar el alcance y la prioridad de las preferencias del sistema, los usuarios y los proyectos. Además, acá es donde se configuran las credenciales de quien hizo los cambios en el proyecto.

Existen tres niveles: Sistema (para todos los usuarios), Global (por usuario) y Local (por proyecto), donde cada nivel anula al anterior.
[referncia](https://git-scm.com/book/es/v2/Personalizaci%C3%B3n-de-Git-Configuraci%C3%B3n-de-Git)

1. Nivel Local (--local):

- Alcance: Afecta únicamente al repositorio actual donde te encuentres.

- Uso: Es ideal si trabajas en un proyecto de código abierto o un repositorio de la empresa donde necesitas usar un correo corporativo diferente al que usas para tus proyectos personales. Se almacena en el archivo .git/config dentro de tu proyecto.

- Comando para asignar:

🖥️
```bash
 git config --local user.email "tu-correo@empresa.com"
```

2. Nivel Global (--global):

- Alcance: Afecta a todos los repositorios del usuario actual en tu computadora.

- Uso: Es el nivel más utilizado. Aquí configuras tu nombre de usuario, correo electrónico principal (por ejemplo, el de GitHub o GitLab) y tu editor de texto predeterminado. Se guarda en tu directorio de usuario en el archivo ~/.gitconfig.

- Comando para asignar:
🖥️
```bash
git config --global user.name 'tuNombreUsario'

git config --global user.email 'tu-correo@gmail.com'
```

3. Nivel de Sistema (--system)

- Alcance: Afecta a todos los usuarios y todos los repositorios de esa máquina o servidor.

- Uso: Aplica configuraciones universales para el sistema operativo, aunque rara vez se modifica directamente. Se guarda en el archivo /etc/gitconfig.

- Comando para asignar:
```bash
git config --system core.editor vim
```
[referencia](https://youtu.be/EpCaeC2vEJs?si=utmFRfMaGttZW9b3)


Además, es importante mencionar que se puede hacer un cambio de configuración. Por ejemplo, si en mi PC tengo mi configuración global pero en un directorio lo quiero hacer con la cuenta de la empresa (osea, hacerlo de manera local) simplemente hay que ingresar al repositorio, incializarlo y poner las credenciales con la configuración local

```bash
git config --local user.name "tuNombreCorporativo"
git config --local user.email "correo@empresa.com"
```

y directamente cuando se haga un commit en ese directorio se guaradará con esas credenciales.

si es el caso contrario, se elimina la variable local qu que ya no se quiere: 


```bash
git config --local --unset user.name
git config --local --unset user.email
```

y al borrar el correo lcoal git busca en el sigiuente nivel de jerarquía y aplicará.

Puedes verificar el estado actual de tus configuraciones utilizando el siguiente comando. Esto listará todas las variables activas y te mostrará el origen de cada una: 

🖥️
```bash
git config --list
```

Para saber que usuario e e-mail tienes en que configuración solamente basta agregar el nombre de la configuración

🖥️
```bash
git config --global --list
git config --local --list
```

si se configuran las credenciales de manera global significa que esas credenciales se aplicarán a todos los repositorios en la computadora, por lo que es lo recomendable si estas empezando y se esta en la computadora personal. Si siempre pues se usan los mismos datos en todos los respositorios. 

Por otro lado, usar credenciales de manera local solo se configuran para el repositorio de actual, lo que permite tener diferentes nombres de usuarios y correos para diferentes proyectos, **es el que se usa por defecto**, es muy útil si se tiene un perfil personal y uno profesional, por lo que si se usan diferentes cuentas por ejemplo en github hay que tener un credenciales para cada cuenta y mantiene las identidades separadas entre repositorios, evitando confusiones. 

## Comandos 🖥️

#### Definción preliminar: Rama(branch)
Piensese como caminos paralelos dentro de un proyecto. Si mi proyecto es un árbol, la rama main(principal) es el tronco, cuando se crea una rama, es como hacer una rama nueva al árbol, permitiendo trabajar en algo nuevo
sin afectar el tronco principal. Permite experimentar o desarrollar una nueva funcionalidad sin arriesgarnos a dañar lo que ya se tiene, que si se quiere se puede fusionar con la rama principal. Además, puede verse como 
un lugar de un trabajo temporal.

### 1. git init
🖥️
```bash 
git init
``` 
Lo que hace este comando es que en el directorio actual se crea el repositorio, permitiendo que desde ese momento sea un repositorio de git.

Desde ese momento se crea una carpeta oculta llamada `.git` donde guardara cada "foto" y configuracion del repositorio. De esta manera es el primer paso para empezar a usar nuestro control de versiones.

<span style="color:yellow">**Nota**</span>: para ver carpetas ocultas y listadas se usa:

🖥️
```bash  
    ls -la
```
A partir de este momento, cuando se entre desde el git bash a este directorio aparecerá que es la rama <span style="color:green">**master**</span> que viene a indicar que es la rama principal del repositorio, es decir, el tronco princpipal del árbol.

Lo más recomendable y por buenas practicas es cambiar la rama de nombre por <span style="color:green">**main**</span>, de la siguiente manera:

🖥️
```bash  
    git branch -m "main" 
```
    
### 2. git status
Permite conocer el estado actual del repositorio:
- Muestra la rama en la que se esta trabajando y su resúmen.
- Da a conocer si algun archivo se modificó.
- Muestra si hay algún archivo nuevo en el directorio para ingresar al repositorio.

Lo que aparezca en <span style="color:red">**rojo**</span> es porque el archivo fue modificado o creado y se necesita poner en el área de preparación. Lo que esta en <span style="color:green">**verde**</span> es porque ya está en el área de preparación pero aún no esta commiteado.

### 3. git add
Es la forma de añadir un archivo al area de preparación y se hace de la siguiente manera:

🖥️
```bash  
git add "nombreArchivo" #sube el archivo específico que tiene el nombre 'nombreArchivo'
git add .  # sube todos los archivos pendientes por montar al repositorio
```


### 4. git commit
Es la forma en que se guarda el historial, AÑADIR UNA FOTO AL REPOSITORIO o CREAR UN PUNTO EN EL ESPACIO-TIEMPO DEL PROYECTO, es decir, es la forma en que se toma una foto de todo lo que se tiene hasta ese momento. Entonces git
guarda una foto del stage. CADA COMMIT ES UN PUNTO EN EL TIEMPO al que se puede regresar si se desea y lleva un mensaje de descripcion
del autor. 

🖥️
```bash  
    git commit -m "descripcion del commit"
```

Por tanto, para hacer un commit, hay que hacer 2 pasos, siendo el primero llevar todos los archivos al área de preparación y luego hacer el commit. 

Si se quiere saltar la parte del git add para llevar los archivos al área de preparación basta con agregar el comando "-a" que representa "all" 


🖥️
```bash  
    git commit -a -m "descripcion del commit"
```

Nota:En caso que no se ponga -m, se abre un editor de texto
para escribir un mensaje detallado.

#### Otros usos con el git commit


🖥️
```bash  
    git commit  --amend -m "descripcion del commit"
```
   
Permite modificar el ultimo commit, combinando cambios actuales
con lo que ya estaba en el commit anterior. Si realizaste un commit pero olvidaste incluir uno o varios archivos, puedes añadirlos al área de preparación con git add y luego ejecutar --amend para fusionarlos en el mismo commit. Admeás, permite editar el texto de la confirmación anterior si contenía errores ortográficos o si deseas cambiar su descripción.

🖥️
```bash  
    git commit --allow-empty -m "descripcion del commit"
```

Crea un commit sin cambios en los archivos, solo con un mensaje.
Sirve para crear puntos de referencia. 

Nota: cada que se haga commit, a cada foto se le asigna un codigo único para dar a conocer que no se puede repetir en ningún momento, este codigo es un hash.

### 5. git log
Es un comando para ver el historial de commits del repositorio; 
es decir, muestra cada commit que se ha hecho dentro del repositorio mostrando la clave hash, autor, fecha, hora y mensaje. 

🖥️
```bash  
    git log
```
Otras formas para ver esta información es: 

🖥️
```bash  
    git log --oneline # Muestra sencillamente las líneas
    #del número de commit y en que rama se esta actualmente.
```

🖥️
```bash  
    git log -p # Muestra diferencias de cada commit
```

🖥️
```bash  
    git log -n # se limita a mostrar a los ultimos n commit
```
### 6. git chekout
Es un comando que se usa para cambiar entre ramas o resturar archivos y commits especificos.

🖥️
```bash  
    git chekout "nombreRama" 
```
Permite moverse entre ramas dentro del repositorio(mas adelante se estudiará esto).

🖥️
```bash  
    git chekout  -b "nombreRama" 
``` 
Crea una nueva rama con el nombre nombreRama y te cambia a esta automaticamente; es decir, paso de la rama main a la rama con el nombre nombreRama.































































## Definiciones importantes: 
**Repositorio**: es un espacio centralizado donde se almacena, organiza, mantiene y difunde información digital. [referencia](https://es.wikipedia.org/wiki/Repositorio_(contenido_digital))

**Commit**: es una "fotografía" o punto de control que guarda de forma permanente el estado de tus archivos y el código en un momento específico. Actúa como un guardado en el historial de tu proyecto, permitiéndote regresar a ese punto exacto si algo sale mal.[referencia](https://youtu.be/j9zAL52wuLg?si=xbT9Rkox1mZzytGw)

**Área de preparación**:El área de preparación (o staging area / índice) en Git es un espacio intermedio donde se agrupan los cambios antes de guardarlos definitivamente en el historial. Funciona como un borrador que te permite decidir exactamente qué modificaciones incluir en tu próxima confirmación (commit).