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
Es un comando para ver el historial de commits del repositorio; es decir, muestra cada commit que se ha hecho dentro del repositorio mostrando la clave hash, autor, fecha, hora y mensaje. 

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

Nota: El identificador hash es muy importante ya que es el identificador único de los commits y entonces puede servir para movernos en momentos de tiempos diferentes del documento que tenemos. 

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

🖥️
```bash  
    git checkout -- <nombreArchivos> 
``` 
Sirve para restaurar un archivo a su última versión confirmada de commit. 

🖥️
```bash  
    git checkout <hash-del-commit> -- <nombre-del-archivo> 
``` 
Sirve para restaurar un archivo a una versión específica de un commit específico identificado con el hash. Más adelante volveremos con el uso de las ramas. 


### 7. git reset
Se usa para deshacer cambios en el repositorio. Permite mover el puntero (HEAD) de la rama actual y modificar lo que hay en el área de preparacion(staging area, que es el lugar donde git add manda los archivos) o en el área de trabajo(working directory, es donde trabajamos). 
    🖥️
```bash  
    git reset 
```

Lo que puede hacer este comando es: 

1) Cambia el puntero HEAD a un commit anterior en la historia
"olvidando" cualquier commit que haya después de ese punto.

2) Modifica el área de preparación, git reset quíta los archivos que se tengan
en el área de preparación pero aún no estan en el repositorio, por si lo que se
tenia se necesita modificar de nuevo antes de montarlo.

3) Modifica el área de trabajo.
    
dependiento de las opciones que se usen para git reset, se puede revertir el área de trabajo devolviendo TODOS los archivos a su estado en el commit especificado a diferencia de git chekout que que lo hace con un solo archivo.

#### METODOS del git reset
🖥️
```bash  
    git reset --soft HEAD~n 
```
a) --soft mueve el puntero (HEAD) sin cambiar el área
de preparacián ni el área de trabajo. Mueve el puntero HEAD
a un commit anterior, DESHACIENDO uno o mas commits. 
    
Siempre hay que indicar a que commit se quiere llevar, ya sea HEAD~n que mueve
al n-ésimo commit o al hacer HEAD^ que mueve el inmediatamente anterior o ya 
con el hash del commit

por ejemplo
🖥️
```bash  
    git reset --soft HEAD~1 
```
esto deshace el último commit, pero los cambios que se hicieron seguirán
en el área de preparación para ser re-commitiados. Es decir, si se hizo 
un `git add` porque se modificaron o crearon nuevos archivos y luego
se hizo un `commit` para estos. Pero, supongamos que no se necesitaba
ese commit pero si se desea mantener los archivos en el área de preparacion
entonces usamos el `git reset --soft`. 

<span style="color:yellow">**DESHACE COMMITS PERO MANTIENE LOS CAMBIOS DEL ÁREA DE PREPARACIÓN**</span>

🖥️
```bash  
    git reset --mixed HEAD~n
``` 
b) --mixed mueve el puntero HEAD al commit especificado y <span style="color:red">elimina</span> los archivos del área de preparación, pero mantiene los cambios en el área de trabajo, por eso ya dice que el archivo esta modificado o hay uno nuevo pero no está en el area de preparación.
 
por ejemplo
🖥️
```bash  
    git reset --mixed HEAD~1 
```

ES EL QUE SE USA POR DEFECTO SI SOLO SE PONE `git reset`
y si no se especifica un commit se va al inmediatamente anterior
por defecto.
    
deshace el ultimo commit y quita esos cambios de área de preparación
pero los cambios permanecen en el archivo.

<span style="color:yellow">**HACE COMMITS Y MUEVE LOS ARCHIVOS FUERA DEL ÁREA DE PREPARACIÓN
PERO CONSERVA LOS CAMBIOS EN EL ÁREA  DE TRABAJO**</span>
    
🖥️
```bash  
    git reset --hard <hash> 
```
c) --hard mueve el puntero(HEAD) al commit especificado, elimina el área de
preparación y el área de trabajo. Ojo, <span style="color:yellow">es irreversible para los cambios locales</span>.

<span style="color:red">DESHACE COMMITS Y ELIMINA CAMBIOS DEL ÁREA DE PREPARACIÓN Y DEL ÁREA
DE TRABAJO, DEVOLVIENDO EL REPOSITORIO A UN ESTADO ANTERIOR COMPLETAMENTE</span>

NOTA:
*Una de las formas de movernos de commits con el git reset es cambiando con el puntero
por defecto, el puntero esta en el último que es el main, ej los commits que tenemos son 
A--B--C--Main, si hago HEAD~1 se refiere al commit anterior al head, osea, C,
si hago, HEAD~2 se refiere al commit 2 posiciones atras, osea B y asi.
*HEAD^ = HEAD~1.

### 8. .gitignore

El .gitignore es un simple archivo de texto (llamado literalmente .gitignore) que le dice a Git qué archivos o carpetas debe ignorar por completo.

Sirve para que no subas accidentalmente al repositorio cosas basura o sensibles, como:

* Contraseñas o llaves de API (.env)

* Carpetas de dependencias pesadas (node_modules/, vendor/)

* Archivos generados por el sistema u compilación (.DS_Store, dist/, build/)

Se usa para evitar archivos o directorios que no se quieran tener en el repositorio y simplemente ignorarlos sin tener
complicaciones. 


1. Crear el archivo `.gitignore` en la raíz del proyecto si no se ha creado. 
🖥️
```bash  
    touch .gitignore 
```


2. Ábrelo en cualquier editor de texto como VS code, bloc de notas, vim, etc.
🖥️
```bash  
    code .gitignore 
```

3. Escribe el nombre de la carpeta con una barra al final
🖥️
```  
    <nombre-archivo>
```

4. Guardar. 

De esa manera se omitirá esa carpeta y todo lo que tenga adentro. No aparecerá en git status ni de incluirá cuando se haga un git add. 

El archivo se encuentra en la raiz del proyecto; es decir,
en el mismo directorio donde esta .git, para verlo es con la 
linea `ls -a` para archivos ocultos.

Nota: 
* El .gitignore solo funciona para archivos que nunca se han rastreado. Si ya le habías hecho git add y git commit a un archivo antes de agregarlo al .gitignore, Git lo seguirá rastreando.

* Se puede poner no solo un archivo sino una carpeta completa para que ignore la carpeta y todo su contenido. 

Puedes hacer un ejemplo para ver su funcionamiento: 

1. Para crear el archivo .gitignore.
🖥️
```bash  
    touch .gitignore  
```

2.  Crear el archivo para ignorar.
🖥️
```bash  
    touch archivo_ignorar.txt  
```

3. Ver que aparece tanto el .gitignore como el archivo_ignorar.txt.
🖥️
```bash  
    git status  
```

4. Abrir algún editor de texto.
🖥️
```bash  
    code .gitignore #Abrir en VS code  
```
🖥️
```bash  
    nano .gitignore #Abrir en el editor de linux
```

5. Agregar archivo que queremos ignorar y guardar. 
```  
    archivo_ignorar.txt  
```

6. Revisar con git status que ya no aparezca el archivo_ignorar.txt  sino solamente el archivo .gitignore.

#### Estructura de un arhivo .gitignore
Su estructura es muy sencilla, pero saber qué poner en él es fundamental para evitar subir contraseñas, no llenar tu repositorio de archivos basura y no subir archivos gigantes que bloqueen Git.

1. La Regla de Oro: ¿Qué DEBE e INDEBE ir en Git?
SÍ va a Git (Código y Recetas): Tus scripts (.py), archivos de configuración (docker-compose.yml, Dockerfile, requirements.txt), documentos explicativos (README.md).

NO va a Git (Basura y Secretos): Contraseñas, claves de bases de datos, datos personales, archivos pesados de datos (.csv, .db), archivos temporales que genera el lenguaje al ejecutar código (__pycache__).

2. Estructura estándar de un .gitignore profesional
A continuación tienes una plantilla lista para usar en proyectos de Python, Bases de Datos y Docker. Solo debes crear un archivo llamado .gitignore (con el punto al inicio) en la raíz de tu proyecto y pegar esto:
```
# ==========================================
# 1. ARCHIVOS TEMPORALES DE PYTHON
# ==========================================
# Archivos de caché que Python genera automáticamente al ejecutar código
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# ==========================================
# 2. ENTORNOS VIRTUALES LOCALES
# ==========================================
# Si creaste un venv en tu máquina local por error o costumbre
.venv/
venv/
ENV/
env/

# ==========================================
# 3. SEGURIDAD Y SECRETOS (¡MUY IMPORTANTE!)
# ==========================================
# Archivos donde guardas contraseñas y claves de acceso
.env
.env.local
*.pem
*.key

# ==========================================
# 4. ARCHIVOS DEL EDITOR DE CÓDIGO (IDE)
# ==========================================
# Configuraciones personales de tu editor que no le sirven a otros
.vscode/
.idea/
*.swp

# ==========================================
# 5. DATOS PESADOS Y BASES DE DATOS LOCALES
# ==========================================
# No subas bases de datos SQLite o datos pesados
*.sqlite3
*.db
*.csv
*.xlsx
*.parquet

# Si tienes una carpeta llamada 'data/' donde descargas datasets pesados:
data/

# ==========================================
# 6. ARCHIVOS DEL SISTEMA OPERATIVO
# ==========================================
# Archivos basura que crean Windows y macOS en silencio
.DS_Store
Thumbs.db
```
#### git rm --cached <archivo>
Si alguna vez ya habías hecho un git add de ese archivo antes de agregarlo al .gitignore, Git lo seguirá rastreando. Para sacarlo del radar sin borrarlo de tu computadora, ejecuta:

🖥️
```bash  
    git rm --cached <archivo>
```

**Consejo: Crea siempre el archivo .gitignore en el primer paso, justo antes de hacer tu primer git add . o git commit.**

### 9. git diff:
Permite ver cambios que se han hecho en ficheros antes de hacer un nuevo commit; es decir, muestra aquellas diferencias y el lugar en que estan. Estas diferencias se pueden ver si y solo si, el archivo editado no se ha montado al área de preparación (lugar que a donde `git add` lleva los archivos), es decir, se mostraran las diferencias entre lo nuevo agregado y lo que tiene guardado el último commit.

muestra las diferencias tal que: 

* + #. comandos añadidos se muestran en <span style="color:green">verde</span> y # es el numero de lineas añadidas, en caso que se hayan añadido
varias lineas dando en enter nos mostrara todas aquellas lineas que se agregaron despues del último
guardado.

* -# lineas que se eliminaron se muestran en <span style="color:red">rojo</span>. 

Es muy importanto notar que solo apareceran las líneas luego de haber dado guardar en el área de trabajo pero que aún no esta en el área de preparación. Muestra inmediatamente
todo aquello que se cambio con rojo como estaba y en verde a como esta ahora. 

### Áreas de git
* Área de trabajo(working directory): Lugar donde trabajo mis archivos, donde escribo mi codigo y hago todo lo que necesito.

* Área de preparación(Staging area): El +area de preparación es el área donde los archivos editados esperan al siguiente commit; es decir, es el lugar a donde git add manda los 
archivos.

Repositorio: Lugar donde se guarda la galería de commits.

### Desplazamientos:
Hay 2 tipos principales de desplazamientos:

#### 1. Entre ramas: 
Recordemos que para cambiar entre ramas existentes:
🖥️
```bash  
    git chekout <nombre-rama> #se pone el nombre de la rama a la que nos queremos mover
    #o
    git switch <nombre-rama>
```
Y para ver las ramas disponibles: 

🖥️
```bash  
    git branch
```

Es importante tener bien la siguiente idea: Una rama es como un espacio totalmente nuevo, con toda la información hasta el último commit del proyecto, pero hay que entender que todo lo nuevo que se haga en esta rama estará solamente en la rama y no se verá en la rama main a menos que se unan, veamos un ejemplo: 

1. Creamos una rama nueva y nos movemos a ella: 
🖥️
```bash  
    git checkout -b "rama_nueva"
```

2. Revisemos que se creó. 
🖥️
```bash  
    git branch # debería aparecer la rama main y la rama_nueva
    #además, todos los archivos del último commit. 
```

3. Creemos un archivo de texto
🖥️
```bash  
   touch archivo_texto.txt 
```
y escribir algo en el, por ejemplo: "estoy usando mi nueva rama de git"

4. guarda y has tu commit. 
🖥️
```bash  
    git add .
    git commit -m "commit en la rama nueva"
```
5. Veamos donde quedó cada rama. 
🖥️
```bash  
    git log --oneline
```
Ahora podemos ver que la rama main está en el commit anterior y la rama_nueva esta en commit superior pues tiene cambios que se hicieron después del último commit de la rama main. 

6. Cambiemos de nuevo la rama main.
🖥️
```bash  
    git checkout main
```
Ahora revisa en tus arhivos haciendo `ls` y podrás ver que el archivo llamdo `archivo_texto.txt` no existe y es porque no está en esa rama, sino en la nueva. 

**En esencia lo que tienes que entender es que tu rama main es como tu computadora personal y crear una rama es como usar una computadora diferente; la cual, le pasaste todo lo que llevabas en tu computadora personal pero sigues trabajando ahora en esta computadora diferente, de esta manera todo cambio que hagas en esta segunda computadora se quedará allí y no se verá reflejado en tu pc personal, a menos que lo unas.** 

De una manera muy resumida, la forma de combinar "la información de la computadora nueva y llevarla a tu computadora personal y que queden juntas" es directamente unir las ramas y es bastante fácil, simplemnte hay que cambiar a la rama main de nuevo. 

🖥️
```bash  
    git checkouit main
```

y hacer un git merge

🖥️
```bash  
    git merge rama_nueva
```

Eso directamente abre el `nano` que es el editor de texto por defecto de bash para escribir el nombre del commit que se tenía en la rama_nueva pero ahora en la rama main, basta con escribir lo que desees, luego `ctrl + o + enter` y luego `ctrl + x`. Más adelante volveremos con esto. 

El área de preparación es una sola rama general; es decir, si se hizo un cambio a un archivo o se creo uno nuevo y se puso en el área de preparación, luego se hizo commit en algúna rama, pero luego se decide que esos cambios deben estar en otra rama, lo que se puede hacer es devolverse entre commits con `git reset --soft` para que ya no se tengan esos commits, pero se mantengan esas ediciones en el área de preparación; luego al cambiar de rama se vuelve a hacer el commit con los archivos.


#### 2. Entre commits(viajar en el tiempo del proyecto):
Es muy similar a moverse entre ramas pero en este caso nos moveremos a un punto especifico 
del proyecto a partir de los commits.

1) Con `git log` veremos el historial de commits para ver a donde queremos movernos.
2) Debemos seleccionar la clave hash del commit al que queremos llegar y la forma de
    movernos será:
    
    🖥️
```bash  
    git chekout <hash-commit>
```

Al hacer esto entramos en un estado llamado **detached HEAD** que indica que el HEAD
que es el puntero que señala en que rama o commit estamos ahora se movera al commit
seleccionado a partir de su hash. Esto permite ver otros estados del proyecto sin afectar la parte principal. 

<span style="color: red;">Nota importante</span>: Si en el estado de **deteached HEAD** se hace un commit, como estos no estan asociados a ninguna rama entonces pueden perderse y se debe crear una rama nueva para eso.
**Si antes de moverme de commit hay cosas que que no se han guardado con un commit, pueden perderse**. 

Es visible que al cambiar de rama, cambia el nombre de la rama en el bash. Pasa lo mismo con el commit, al movernos entre commits ya no aparecerá que estamos en la rama main sino por ejemplo en (HEAD detached at 2806df5) si se cambia al commit con hash 2806df5. 

### 10. git tag
Se utiliza para marcar puntos especificos en el historial de un repositorio con etiquetas.

Son útiles para marcar versiones importantes de los proyectos; para tomar una referencia de un punto importante con un nombre.

Son las "versiones" de una aplicación.

POR BUENAS PRACTICAS EN MINÚSCULA, GUIONES BAJOS(NO ESPACIOS) o también es recomendable SINO SNAKECASE.

Hay 2 tipos de etiquetas en git, 

1.**Etiquetas ligeras(lightweight tags)**: Que son como marcadores en un commit. No tienen información adicional como mensajes o metadatos; funcionan simplemente como un puntero al commit que se esta etiquetando.

    🖥️
```bash  
    git tag <nombre-etiquieta>
```
Eso crea una etiquéta en el commit actual (HEAD)

2. **Etiquetas anotadas(annotated tags):** Son etiquétas más completas que continen un mensaje, fecha, autor y otros metadatos, se usan normalmente para lanzamientos formales de software porque almacenan información:

    🖥️
```bash  
    git tag -a <nombre-etiqueta> -m "mensaje"
```
Ejemplo
    🖥️
```bash  
    git tag -a v1.0.0 -m "Version 1.0.0: primero lanzamiento oficial"
```
Esto creará una etiquéta llamada v1.0.0 en el commit actual, junto con el mensaje descrito.

Para ver las etiquétas en orden alfabético:

🖥️
```bash  
    git tag 
```

En caso de necesitar informacion mas detallada de 
una etiquéta especifica podemos usar:

🖥️
```bash  
    git show nombre-etiqueta
```
Esto mostrará el commit etiquetado, el mensaje de la etiquéta, el autor y la fecha.

Para etiquetar un commit específico que no sea el mas reciente podemos hacerlo usando el hash del commit: 

🖥️
```bash  
    git tag <nombre-etiqueta> <commit-hash> #o pues con el HEAD~N
```   

y finalmente para eliminar una etiquéta:
🖥️
```bash  
    git tag -d <nombre-eqitqueta>
```
 
NOTA: 
* -a: Se usa para crear una etiquéta anotada en git; osea, se esta creando una etiquéta que no solo apunta a un commit sino que tambien contiene metadatos adicionales.

* -d: Se usa para eliminar una etiquéta en tu repositorio local, es útil si se comete un error  al crear una etiquéta o ya no necesita.

Luego, como tenemos commits etiquetados para movernos entre ellos (el HEAD) entonces ahora podemos usar el nombre de el tag escpecífico para ir a un commit para no tener que usar el hash:

🖥️
```bash  
    git checkout tags/<nombre-tag>
```

### 11. git reflog
Es una herramienta útil que registra todos los movimientos que ha hecho el puntero HEAD en el repositorio. A diferencia de `git log`, que solo muestra el historial de commits, `git reflog` permite ver todas las acciones importantes que se han hecho como: cambios de ramas, resets, commits y merges.

ESPECIALMENTE ÚTIL CUANDO SE NECESITAN RECUPERAR CAMBIOS O COMMITS QUE PARECEN PERDIDOS O DESHACER ACCIONES COMO UN

`git reset --hard`

Se guarda un registro de todas las veces que el puntero se mueve en el repositorio, permite ver el historial de acciones que afectan el puntero HEAD, incluso aquellas que no aparecen en 
git log.

🖥️
```bash  
    git reflog
```
Lo que retorna es una lista de la siguiente manera: 
**<hash> HEAD@{n} <descripcion>**: Donde $n$- representa el número de eventos en el historial de HEAD, donde HEAD{0} es el estado actual del puntero y luego muestra una descripción.

Por ejemplo, si se cometió algún error y se quiere volver a un estado anterior, se puede usar `git reflog` para que se muestre la lista. Identifico el commit que deseo recuperar con el HASH o HEAD@{n} y entonces para recuperar ese estado del proyecto solo ejectuco `git reset --hard`

🖥️
```bash  
    git reset --hard HEAD@{n} # y asi recupero el estado del proyecto hasta ese momento, sin importart que ya lo hubiese elminado, es la forma de recuperar todo si en algún momento hay arrepentimiento por eliminar algo. En lugar del n también se puede poner el hash del commit y listo. O simplemente poner el hash. 
```
### 12. git branch (volvamos al concepto de las ramas)
Es uno de los comandos mas importantes en git y se usa para trabajar con ramas, permitiendo desarrollar características, corregir errores o experimentar con nuevas ideas sin afectar la rama principal(se pueden crear tantas como quiera entonces se puede experimentar como se desee sin afectar el tronco del arbol del trabajo, y en caso que se quiera se puede agregar).

Hay varias funciones para este comando: 

🖥️
```bash  
    git branch 
```
Muestra todas las ramas disponibles ya creadas en el repositorio y marca con un * en la que se esta trabajando actualmente.

🖥️
```bash  
    git branch <nombre-rama> 
```
Crea una nueva rama nombre el nombre "nombre-rama". Cuidado, la nueva rama se crea a partir del ultimo commit, y se hace algún commit en esta nueva rama, no se guardará en la rama principal. Por tanto si se devuelve a la rama main, no apareceran estos commits a menos de que se fusionen, por eso es posible sin dañar la parte principal que ya funciona.

🖥️
```bash  
    git checkout <nombre-rama> 
    git switch <nombre-rama>
``` 
Para cambiar a la rama con el nombre específicado.

🖥️
```bash  
    git checkout -b <nombre-rama> 
    git switch -c <nombre-rama>
```
Crea una nueva rama con el nombre "nombre-rama" y directamente me mueve a ella.

🖥️
```bash  
   git branch -d <nombre-rama>
```
Se usa para eliminar una rama con el nombre "nombre-rama" esto siempre y cuando los cambios de esa nueva rama ya hayan sido fusionados con la rama principal; en caso que no desee fusionar esos cambios por alguna razón, se usa una $-D$ en lugar de $-d$.

Pero cuidado pues aunque se supone que se elimino la rama, se puede tener una referencia de los commits que se tuvieron y se puede viajar a ellos, pero la rama en la que estaban ya no esta, todo esto suponiendo que ya se hizo una fusión con otra rama.

🖥️
```bash  
   git branch -r
```
Muestra una lista de las ramas remotas junto del nombre de origen. 

🖥️
```bash  
   git branch -m <nombreviejo> <nombrenuevo>
```
Renombra una rama.

### 13. git merge
Es el comando para combinar dos ramas en una. Cuando se trabaja en diferentes ramas y se quieren unir cambios se aplica este comenado. 
Al aplicar esta linea Git intenta unir el historial de dos ramas, creando un nuevo commit que refleja la combinacion de los cambios realizados en ambas ramas.

Primero que nada hay que cambiarse a la rama a la que se le 
aplicaran los cambios. Por ejemplo, si hice cambios en una rama y quiero pasarlo a la rama main entonces primero hay que cambiar a esta, luego de estar en la rama main aplciamos el comando:

🖥️
```bash  
   git merge <nombre-rama>
```
Y ya con esto tendré mis ramas fucionadas. 

Hay diferentes tipos de merge con respecto a los commits que hayan: 

#### fast-forward merge
Si no hay commits adicionales en la rama main (o a la que se le fusionara otra rama) desde que se creo la rama secundaria; es decir, cuando no se hizo ningún otro cambio en la rama principal desde que se creo la otra rama. Entonces, git mueve el puntero de main hacia adelante, porque no hay ningún cambio en el main que deba combinarse, simplemente se mueve al ultimo commit de la rama secundaria, pues como se supone que no se hizo nada en el main es como si se hubiera seguido con el mismo trabajo.
    
* Antes del merge:

    A---B---C  (main)
            \
            D---E  (feature-branch)

* Después del merge (fast-forward):

    A---B---C---D---E  (main, feature-branch)

    y no hay ningun commit extra de fusión.

#### 2. Merge con commit de fusión
Sucede cuando se han hecho cambios en ambas ramas. En este caso, Git crea un commit extra llamado commit de merge, que une los cambios de ambas ramas: 

* Antes del merge:

    A---B---C  (main)
         \
          D---E  (feature-branch)

* Después del merge:

    A---B---C---M  (main)
          \    /
           D---E  (feature-branch)

M es el commit de merge, que combina los cambios de las ramas, pero notese que hay cambios de algo en general no en las mismas lineas de codigo; es decir, se agregaron funcionalidades y lineas de código al proyecto. No se editaron las que ya habían. 

#### 3. Merge con conflicto
Ocurre cuando Git no puede decidir automaticamente como combinar los cambios. Esto pasa si ambas ramas se modificaran las mismas líneas en los mismos archivos, un ejemplo: desde la rama main se hizo un cambio en la linea 10 de un archivo y en la otra  rama tambien se hizo un cambio en la linea 10 del mismo archivo, entonces hay que resolver el conflicto de manera manual y git mostrará donde estaran estos conflictos. Se dice que hay que forzar el conflicto para poder arreglarlo.

Imagínate que tú y un compañero están escribiendo juntos un libro. Los dos toman una copia del Capítulo 3 el lunes.

Tú editas el párrafo 2 para decir que el personaje vestía una chaqueta negra.

Tu compañero edita el mismo párrafo 2 para decir que el personaje vestía un suéter rojo.

El viernes se juntan para consolidar el libro. ¿Qué debe decir el párrafo 2? ¿Chaqueta o suéter? Eso es un conflicto de Git.

Cuando ocurre un conflicto durante un git merge, Git no borra nada ni rompe tu proyecto. En su lugar, modifica el archivo afectado insertando unas marcas muy características para señalar exactamente dónde está la disputa:

<<<<<<< HEAD
El personaje vestía una chaqueta negra.
=======
El personaje vestía un suéter rojo.
>>>>>>> rama-de-mi-compañero

Resolver un conflicto es simplemente tomar una decisión editorial. Tienes cuatro opciones principales:

1. Quedarte con tu cambio (borrar la versión entrante y las marcas).

2.Quedarte con el cambio de la otra rama (borrar tu versión y las marcas).

3. Combinar ambos cambios (por ejemplo: "El personaje vestía una chaqueta negra sobre un suéter rojo" y borrar las marcas).

Escribir algo completamente nuevo.

Identifica los archivos en conflicto:
Corre `git status`. Verás los archivos con conflicto resaltados bajo la categoría `Unmerged paths`.

Abre y edita el archivo:
Puedes usar tu editor preferido (como VS Code, que tiene botones dedicados para "Accept Current Change" o "Accept Incoming Change"). Asegúrate de eliminar por completo las marcas <<<<<<<, ======= y >>>>>>>.

Marca el conflicto como resuelto:
Añade el archivo al área de preparación (staging):

🖥️
```bash  
   git add archivo_resuelto.txt
```

Completa la fusión:
Crea el commit de merge para finalizar:

🖥️
```bash  
   git commit
```
(Git generará automáticamente un mensaje predeterminado indicando que se resolvió un merge).

Notas: 
* Si te entras en pánico: Puedes cancelar el proceso de fusión en cualquier momento y volver exactamente a como estabas antes de intentar el merge usando:

🖥️
```bash  
   git merge --abort
```
* Luego de fusionar las ramas, la rama secundaria no se eliminan ni desaparecen, seguira existiendo y trabajando en ella si se desea. No se borra ni se modifica por el merge pero pues en caso que ya no se necesite se puede eliminar

#### 4. El squash merge
Es una forma de fusionar ramas. Combina todos los commits de una rama en un solo commit antes de hacer la fusión con la rama principal. 

Útil para mantenre un historial limpio, eliminando
la acumulación de mútilples commits pequeños o intermedios y presentando los cambios en un único commit significativo.

Supongamos que se esta trabajando en una rama con nombre `feature` y se hacen varios commits en esta `A - B - C`, 
al realizar una fusion con squash, git combinara esos tres commit en uno solo; antes de fusionar los cambios a la rama base y el commit resultante puede tener un mensaje descriptivo que resuma los cambios. El comando es: 

🖥️
```bash  
   git merge --squash <nombre-rama> 
```
Se pedirá crear un nuevo commit para la fusión. Finalmente, esto se usa para mantener un historial mas limpio y es util cuando hay muchos commits pequeños que no son significativos individualmente.

### 14. Git stash 
Sirve para guardar temporalmente los cambios no confirmados;es decir, que no han sido commiteados si no que se 
van a una área llamada stash. Útil cuando se esta trabajando en algo, pero se necesita cambiar de rama o hacer algo
diferente sin perder los cambios actuales; lo que se ha hecho en esa rama. Guarda los archivos modificados de manera temporal y te deja con un área de trabajo limpia permitiéndote volver a los cambios más tarde cuando lo necesites.

Supongamos que se esta trabajando con una rama y se tiene algunos cambios pero no se quiere hacer commit y se necesita cambiar a la rama main para revisar algo, pero no se quiere perder el trabajo que ya se tiene en esa rama.

🖥️
```bash  
   git stash
```   
Este comando movera los cambios a una área temporal de almacenamiento llamada stash y el área de trabajo quedará limpia como si no se hubiera hecho nada.

🖥️
```bash  
   git stash list
```
Sirve para ver los stashers que se tienen guardados pues se pueden tener varios, y esto 
retornara una lista indice stash@{n}, donde n es el n-ésimo stash.  

🖥️
```bash  
   git stash apply
```   
Cuando se quieren recuperar los cambios guardados, se pueden aplicar el stash mas reciente,
el comando anterior restaura los cambios sin eliminarlo de la lista. Si se quiere eliminar
después de aplicar, se usa el comando: 

🖥️
```bash  
   git stash drop 
```
 
Para aplicar y eliminar al mismo tiempo; es decir, restaura los cambios y eliminar el stash de la lista se usa el comando: 

🖥️
```bash  
   git stash pop 
```
Para guardar un mensaje descriptivo al stash para recordar lo que se guardo:
🖥️
```bash  
   git stash save "mensaje"  
```
Luego, la forma de aplicar un stash especifico
🖥️
```bash  
   git stash apply stash@{n}  
```    
Finalmente, la forma de eliminar todos los stashes guardados.

🖥️
```bash  
   git stash clear  
```    
    
    

### 15. git rebase -i
Es una forma de ordenar y reducir commit innecesarios en una rama especifica. Permite modificar el historial
de commits de una rama de forma interactiva.

1. nos vamos a la rama que se ordenará
    
2. iniciamos el rebase interactivo: 
🖥️
```bash  
   git rebase -i HEAD~n  
``` 
Esto abre una lista con los ultimos n-commits y en un editor de texto modificable:

    pick a1b2c3d Commit A
    pick e4f5g6h Commit B
    pick i7j8k9l Commit C
    pick m1n2o3p Commit D
    pick q4r5s6t Commit E 
        
`pick` es al accion predeterminada que para que el commit se mantenga tal cual, pero lo podemos cambiar por otras acciones:
        
* squash : Combina el commit con el anterior lo que resulta en uno solo que fusiona ambos.
* reword: cambia el mensaje del commit
* drop: elimina el commit por completo

    pick a1b2c3d Commit A
    squash e4f5g6h Commit B
    squash i7j8k9l Commit C
    squash m1n2o3p Commit D
    pick q4r5s6t Commit E

se combinaron B,C y D en el commit A pero mantendrá E igual. Si  hizo un squash ha que editar el mensaje del commit resultante.

IMPORTANTE:ESTE COMANDO ES MUY PELIGROSO, PERO UNA FORMA DE SALVARSE SIN QUE SE PIERDA NADA
ES CON EL COMANDO:
🖥️
```bash  
   git rebase --abort  
```
Aborta todo lo que se estaba haciendo y vuelve todo a la normalidad.





















































## Definiciones importantes: 
**Repositorio**: es un espacio centralizado donde se almacena, organiza, mantiene y difunde información digital. [referencia](https://es.wikipedia.org/wiki/Repositorio_(contenido_digital))

**Commit**: es una "fotografía" o punto de control que guarda de forma permanente el estado de tus archivos y el código en un momento específico. Actúa como un guardado en el historial de tu proyecto, permitiéndote regresar a ese punto exacto si algo sale mal.[referencia](https://youtu.be/j9zAL52wuLg?si=xbT9Rkox1mZzytGw)

**Área de preparación**:El área de preparación (o staging area / índice) en Git es un espacio intermedio donde se agrupan los cambios antes de guardarlos definitivamente en el historial. Funciona como un borrador que te permite decidir exactamente qué modificaciones incluir en tu próxima confirmación (commit).

