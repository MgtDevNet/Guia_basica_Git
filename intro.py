"INTRODUCCION A GIT"

"""
Ya sabemos que git es un sistema de control de versiones usado para manetener un 
orden y un control para proyectos de programación, es una herramienta extremadamente
util para proyectos grandes. Vease git como una galeria o historial, que cada que se le
da una instruccion toma una foto con descripcion, fecha, y autor del proyecto
hasta donde se lleve con lo que se lleve, de esta manera podemos ir viajando
en el tiempo a partes del proyecto donde necesitamos ver algo, o corregir algo, o directamente
supongamos que lo que hicimos no nos gusto, simplemente nos vamos a la ultima foto o
a la que necesitemos para poder seguir con nuestro proyecto.

Para esto necesitamos instalar git, y en windows usaremos lo que se conoce como 
git bash la cual es interfaz para trabajar con git, primero que nada, como esto
es un control de versiones y puede hacerse en cualquier computadora hay que registrarse
con nombre y correo la forma de hacerlo es muy sencilla es 

    git config --global user.name "nombreUsario"
    git config --global user.email "correUsuario"

que es para ingresar a lo que conocemos como repositorio(es la galeria que hablamos)

Para revisar esta informacion se hace con git config --global --list y aparece
la credencial que se tiene, es decir, la cuenta actual. Esta cuenta puede abrirse
en un tiempo determinado usando credential.helper tal que:

    git --congif --global credential.helper <opcion>

    ej git --congif --global credential.helper cache 
    almacena credenciales por un tiempo determinado, 15 min 
    por defecto, por lo que si se vuelve a entrar a git en ese tiempo
    no hay necesidad de volver a poner las credenciales

    ej git --congif --global credential.helper store
    Almacena credenciales en un archivo de texto plano en el sistema.

    ej git --congif --global credential.helper wincred
    usa el administrador de credenciales del sistema operativo
    para almacenar de una manera segura

    etc.

Poner config en el comando es para configurar opciones dentro del sistema 
Git. Permite establecer configuraciones y preferencias que afectaran el comportamiento
de git. 

Poner --global dice que aplica la configuracion del usuario a nivel global,
es decir,  afectando todos los repositorios que se usen en la maquina local.

Poner --local Aplica la configuracion solo al repositorio en el que se esta trabajando
actualmenete, Es el nivel predeterminado si no se escoge una opcion especifica

Poner --system Aplica la configuracion a nivel del sistema, afectando a todos
los usuarios de la maquina

Si se esta usando git credential manager, git almacena las credenciales en caché para que no
tengas que agregarlas cada vez. Notese que si se configuran las credenciales de manera global
significa que esas credenciales se aplicarán a todos los repositorios en la computadora. Si siempre
se usa el mismo nombre de usuario y correo para todos los proyectos y repositorios es mejor usar este,
es util cuanod se esta trabajando desde la computadora personal donde yo trabajo y uso los mismos
datos en todos los respositorios. Por otro lado, usar credenciales de manera local solo se configuran 
para el repositorio de actual, lo que permite tener diferentes nombres de usuarios y correos para diferentes
proyectos, es el que se usa por defecto, git config user.name "nombre" git config user.email "email" que es 
util sse trabaja en diferentes proyectos con diferentes identidades, como cuando se tiene un perfil personal
y uno profesional, por lo que si se usan diferentes cuentas por ejemplo en github hay que tener un credenciales
diferentes para cada cuenta y mantiene las identidades separadas entre repositorios, evitando confusiones. Es 
muy recomendado cuando  se trabaja con proyectos personales y/o empresariales o si se trabaja en una 
computadora publica o compartida.
Si ya tengo las credenciales glocales en mi pc pero deseo establecer credenciales locales para un
proyecto particular, primero desde el git bash, nos vamos al directorio donde inicaremos el 
repositorio y alli mismo genero el nombre y correo que se quieren usar localmente en ese repositorio.
Entonces cada vez que se haga un commit en ese proyecto, Git usara las credenciales locales que se configuraron
para ese repositorio y sus credenciales no se ven afectadas y asi puede usarse ese para otra cuenta de github

nota: para cambiar las credenciales locales simplemente se vuelve a poner git config user.name "nuevo nombre" y
git config user.email "nuevo email" o si se quieren eliminar y volver a las globales es con 
git config --unset user.name y git config --unset user.email y eso hará que git vueltva a las credenciales
globales para ese repositorio.

Esto se hace en cualquier momento despues de haber creado o clonado el repositorio. Es recomendable
configurar las credenciales antes de hacer el primer commit

----------------------------------------------------------------------------------

INTRODUCCION A COMANDOS BASICOS DE GIT

preliminar
RAMAS EN GIT: Piensese como caminos paralelos dentro de un proyecto. 
si mi proyecto es un arbol, la rama main es el tronco, cuando se crea una rama, 
es como hacer una rama nueva al arbol, permitiendo trabajar en algo nuevo
sin afectar el tronco principal. Permite experimentar o desarrollar
una nueva funcionalidad sin arriesgarnos a dañar lo que ya se tiene que luego
si se quiere se puede fusionar con la rama principal. Tambien puede verse como 
un lugar de un trabajo temporal

nota: poner "pwd" muestra el directorio del pc en el que se esta trabajando
actualmente

1. git init: lo que hace este comando es que en el directorio
que se este, crea el repositorio perimitiendo que desde ese momento
se pueda mantener todo ese directorio como un repositorio de git. Desde
ese momento se crea una carpeta oculta llamada .git donde guardara
cada "foto" y configuracion del repositorio. De esta manera es el primer
paso para empezar a usar git.

    nota: para ver carpetas ocultas se usa "ls -a"

A partir de este momento, cuando se entre desde el git bash a este directorio
aparecera que es la rama MASTER que viene a indicar que es la rama
principal del repositorio, lo mas recomendable por buenas practicas
es cambiar la rama de nombre por MAIN tal que 

    git branch -m "main" codigo para renombrar una rama en git

2. git status: Permite conocer el estado actual del repositorio, primero
muestra la rama en la que se esta trabajando y su resumen. Da a concer
si algun archivo se modifico, si hay algun archivo nuevo el directorio para
ingresar al repositorio, etc.
    -lo que aparezca en rojo es porque fue modificado o creado y 
    se necesita poner en el area de preparacion.
    -lo que esta en verde es porque ya esta en el area de preparacion
    pero aun no esta commiteado

3. git add: Es la forma de añadir un archivo al area de preparación, tal que
    git add "nombre" sube el archivo con nombre "nombre"
    git add . , sube todos los archivos pendientes por montar al repositorio

4. git commit: Es la forma en que se guarda el historial(AÑADIR UNA FOTO AL REPOSITORIO),
(CREAR UN PUNTO EN EL ESPACIO TIEMPO DEL PROYECTO), es decir, es la forma en que
se toma una foto de todo lo que se tiene hasta ese momento, entonces git
guarda una foto del stage. CADA COMMIT ES UN PUNTO EN EL TIEMPO
al que se puede regresar si se desea y lleva un mensaje de descripcion
del autor. 
    git commit -m "descripcion del commit"
En caso que el cambio haya sido de varios archivos y se quiere
hacer un commit de todos se usa el "-a"
    git commit -a -m "descripcion del commit"

    -a: añade todos los archivos modificados

En caso que no se ponga -m, se abre un editor de texto
para escribir un mensaje detallado.

    git commit  --amend -m "descripcion del commit"
Permite modificar el ultimo commit, combinando cambios actuales
con lo que ya estaba en el commit anterior.

    git commit --allow-empty -m "descripcion del commit"
Crea un commit sin cambios en los archivos, solo con un mensaje

nota: cada que se haga commit, a cada foto se le asigna un codigo unico
para dar a conocer que no se puede repetir en ningun momento, este codigo
es un hash.

5. git log: Es un comando para ver el historial de commits del repositorio. 
Es decir, muestra cada commit que se ha hecho dentro del repositorio
y da la clave hash, autor, fecha, hora y mensaje. 
    git log
hay formas de que me resuma el mensaje como 
    git log --oneline y muestra todo mas corto

    git log -p muestra diferencias de cada commit

    git log -n # se limita a mostrar a los ultimos # commits

    etc
    PARA SALIR DE ESTE HAY QUE DARLE A LA Q, pues me lleva a un paginador
    pager que es un lugar en el cual se pueden ver grandes cantidades
    de texto de una manera controlada

    en caso de no querer usar este paginador lo que se puede hacer
    es usar el comando: 
        git --no-pager log 
    y se retorna todo el historial de commits sin necesidad de usar
    el paginador.

6. git chekout: se usa para cambiar entre ramas o resturar archivos y commits
especificos.

    a) git chekout nombre-rama y cambia de una rama
    a otra lo cual permite moverse entre ramas diferentes
    dentro del repositorio(mas adelante se vera esto)

        git chekout  -b nueva-rama crea una nueva rama
    con el nombre nueva-rama  te cambia a esta automaticamente.

    b) Restaurar archivos archivo.ext Es para restaurar un archivo
    o un conjunto de archivos a un estado anterior a como estaban en un 
    commit especifico o en una rama. Se hace con: 
        git chekout archivo.ext 
    y entonces el archivo se llevara a la forma DEL ULTIMO COMMIT que se tenia.

    Mas adelante se mostrara una forma para recuperar lo que ha sido eliminado
    suponiendo el caso hipotetico de que se elimino algo que no se queria.

   TENGASE EN CUENTA QUE EN ALGUNAS ULTIMAS VERSIONES DE GIT SE TIENEN
   NUEVOS METODOS PARA CAMBIAR DE RAMA O RESTAURAR UN ARCHIVO 

7. git reset: se usa para deshacer cambios en el repositorio.
permite mover el puntero (HEAD) de la rama actual y modificar lo que hay
en el area de preparacion(staging area, que es el lugar donde git add manda los archivos)
o en el area de trabajo(working directory, es donde trabajamos). 
Dependiendo de las opciones puede afectar el historial de commits, hay 3 modos
principales

    1) git reset cambia el puntero HEAD a un commit anterior en la historia
    "olvidando" cualquier commit que haya despues de ese punto

    2) Modifica el area de preparacion, git reset quita los archivos que se tengan
    en el area de preparacion pero aun no estan en el repositorio por si lo que se
    tenia se necesita modificar de nuevo antes de montarlo el repositorio

    3) Modifica el area de trabajo, dependiento de las opciones
    que se usen para git reset, se puede revertir el area de trabajo
    devolviendo TODOS los archivos a su estado en el commit especificado
    a diferncia de git chekout que que lo hace con un solo archivo.

    METODOS 
    a) --soft mueve el puntero (HEAD) sin cambiar el area
    de preparacion ni el area de trabajo. Mueve el puntero HEAD
    a un commit anterior, deshaciendo uno o mas commits
    
        git reset --soft HEAD~1 
        Siempre hay que indicar a que commit se quiere llevar, ya sea HEAD~n que mueve
        al n-ésimo commit o al hacer HEAD^ que mueve el inmediatamente anterior o ya 
        con el hash del commit
    
    esto deshace el ultimo commit pero los cambios que se hicieron seguiran
    en el area de preparacin para ser re-commitiados. Es decir, si se hizo 
    un git add porque se modificaron o crearon nuevos archivos y luego
    se hizo un commit para estos pero ahora supongamos que no se necesitaba
    ese commit pero si se desea mantener los archivos en el area de preparacion
    entonces usamos el git reset --soft 

        DESHACE COMMITS PERO MANTIENE LOS CAMBIOS DEL ÁREA DE PREPARACIÓN

    b) --mixed mueve el puntero HEAD al commit especificado y elimina los archivos
    del area de preparación, pero mantiene los cambios en el area de trabajo, por eso
    ya dice que el archivo esta modificado o hay uno nuevo pero no esta en el area de preparación.
 
        git reset --mixed HEAD~1

        ES EL QUE SE USA POR DEFECTO SI SOLO SE PONE git reset
        y si no se especifica un commit se va al inmediatamente anterior
        por defecto
    
    deshace el ultimo commit y quita esos camios de area de preparacion
    pero los cambios permanecen en el archivo

        DESHACE COMMITS Y MUEVE LOS ARCHIVOS FUERA DEL AREA DE PREPARACION
        PEO CONSERVA LOS CAMBIOS EN EL AREA  DE TRABAJO
    
    c) --hard mueve el puntero(HEAD) al commit especificado, elimina el area de
    preparacion y el area de trabajo. ojo, es irreversible
    para los cambios locales.

        DESHACE COMMITS Y ELIMINA CAMBIOS DEL AREA DE PREPARACION Y DEL AREA
        DE TRABAJO, DEVOLVIENDO EL REPOSITORIO A UN ESTADO ANTERIOR COMPLETAMENTE

notese que git reset es para el historial de commits pero git chekout
para restaurar es archivos.

NOTA: una de las formas de movernos de commits con el git reset es cambiando con el puntero
por defecto, el puntero esta en el ultimo que es el main, ej los commits que tenemos son 
A--B--C--Main, si hago HEAD~1 se refiere al commit anterior al head, osea, C,
si hago, HEAD~2 se refiere al commit 2 posiciones atras, osea B y asi.
y HEAD^ = HEAD~1

la otra forma de cambiar el puntero de commit, es directamente usando el hash
del commit tal que 
    git reset --hard <hash>
   
8. git ignore: Se usa para evitar archivos o directorios que no se quieran tener
en el repositorio y simplemente pasarlos por la galleta sin tener
complicaciones. 
1. se crea un archivo vacio .gitignore tal que 

    touch .gitignore y alli ponemos los archivos
    o directorios que queremos que no se guarden.

    (touch crea un archivo vacio )

el archivo se encuentra en la raiz del proyecto, es decir,
en el mismo directorio donde esta .git, para verlo con la 
linea "ls -a" para archivos ocultos y se abre con cualquier editor de texto.
Esto se hace uno por cada repositorio.

nota: touch archivo.txt sirve para crear archivos vacios
   
9. git diff: Permite ver cambios que se han hecho en ficheros antes de hacer
    un nuevo commit, es decir, muestra aquellas diferencias y el lugar en que estan.
    Estas diferencias se pueden ver si y solo si el archivo editado no se ha montado
    al area de preparacion (lugar que a donde git add lleva los archivos), es decir,
    si no se ha montado el archivo editado al area de preparacion, se mostraran las diferencias
    entre lo nuevo agregado y lo que tiene guardado el ultimo commit.

        git diff 
    muestra las diferencias tal que: 
        + #. comandos añadidos, y # es el numero de lineas añadidas, en caso que se hayan añadido
        varias lineas dando en enter nos mostrara todas aquellas lineas que se agregaron despues del ultimo
        guardado.

        -# lineas que se eliminaron

    Es muy importanto notar que solo apareceran las lineas luego de haber dado guardar en el 
    area de trabajo pero que aun no esta en el area de preparación. Y muestra inmediatamente
    todo aquello que se cambio con rojo como estaba y en verde a como esta ahora

Nota: Areas de git

Area de trabajo(working directory): lugar donde trabajo mis archivos, donde escribo 
mi codigo y hago todo lo que necesito como vs code o neatbeans.

Area de preparacion(Staging area): El area de preparación es el area donde los archivos
editados esperan al siguiente commit, es decir, es el lugar a donde git add manda los 
archivos.

Repositorio: lugar donde se guarda la galeria de commits.

-----------------------------------------------------------------------------------------------
Desplazamientos: hay 2 tipos principales de desplazamientos entre ramas y entre commits.

    1. Entre ramas: 
    se hace usando git chekout o git switch para cambiar a una rama ya existente.
        git branch, es la forma de ver las ramas disponibles a las cuales se puede 
        viajar

        git chekout rama2 o git switch rama2 es para movernos a la rama2 actualizando el area
        de trabajo y cambios.

        para crear una rama nueva usamos el comando "git chekout -b nuevarama" o "git switch -c nuevarama"

        y para devolverse a la rama anterior es con el -, "git chekout -" o "git switch -"
        y si se quiere devolver directamete al main se puede usar "git checkout main" o pues en si
        el nombre de la rama principal. 

    2. Entre commits(viajar en el tiempo del proyecto):
    es muy similar a moverse entre ramas pero en este caso nos moveremos a un punto especifico 
    del proyecto a partir de los commits.
        a) con git log veremos el historial de commits para ver a donde queremos movernos
        b) debemos seleccionar la clave hash del commit al que queremos llegar y la forma de
        movernos sera con el "git chekout <hashcommit>"

    Al hacer esto entonces entramos en un estado llamado "detached HEAD" que indica que el HEAD
    que es el puntero que señala en que rama o commit estamos ahora se movera al commit
    al que he seleccionado a partir de su hash. Esto permite ver otros estados del proyecto
    sin afectar la parte principal. 

    Ojo: Si en el estado de "deteached HEAD" se hace un commit como estos no estan asociados
    a ninguna rama entonces pueden perderse y entonces debo crear una rama nueva para eso.
    si antes de moverme de commit hay cosas que he hecho commit, es decir, que no he guardado
    pueden perderse 

    IMPORTANTE: Es muy importante tener en cuenta que los commits que se hacen en una rama diferente
    de la MAIN no apareceran ahi a menos que se fusionen, es decir, los commits o las fotos perteneceran
    a esa rama en especifico(las fotos pertenecen a otra subcarpeta) a menos que se fusionenen con el merge.
    De esta manera se muestra el como funcionan las ramas, pues pude hacer muchas ediciones del mismo archivo
    pero en el archivo de la rama MAIN es que como si no hubiera pasado nada.
    Otra situacion a tener en cuenta es que el area de preparacion es una sola rama general, es decir, si se hizo
    un cambio a un archivo o se creo uno nuevo y se puso en el área de preparación y se hizo un commit en algúna rama
    pero luego quiero que este en otra rama, lo que puedo hacer es devolverme entre commits con git reset --soft para que 
    ya no se tengan esos commits pero se mantengan esas ediciones y luego al cambiar de rama puedo volver a hacer el commit
    con los archivos que se mantiene en el area de preparacion

    git reset --soft HEAD~3 (me devuelvo al 3er commit anterior pero los archivos se mantienen en el área de preparación)
    git switch main
    git add .
    git commit -m"commit organizado "
-------------------------------------------------------
10.git tag: 
Se utiliza para marcar puntos especificos en el historial de un repositorio como etiquetas.
Son útiles para marcar versiones importantes de tu proyecto, para tomar una referencia de un punto importante un nombre.
son las "versiones" de una aplicación. POR BUENAS PRACTICAS EN MINUSCULA Y SI MUCHO PONERLE
GUIONES BAJOS, NO ESPACIOS, SINO SNAKECASE
Hay 2 tipos de etiquetas en git, 

    1.etiquetas ligeras(lightweight tags) que son como marcadores
    en un commit. No tienen informacion adicional como mensajes o metadatos.
    funcionan simplemente como un puntero al commit que se esta etiquetando

        git tag <nombreEtiquieta> eso crea una etiqueta en el commit actual (HEAD)

    2. etiquetas anotadas(annotated tags) son etiquetas mas completas que continen un mensaje,
    fecha, autor y otros metadatos, se usan normalmente para lanzamientos formales de software porque 
    almacenan informacion

        git tag <nombreEtiqueta> -m "mensaje"
        git tag -a v1.0.0 -m "Version 1.0.0: primero lanzamiento oficial"

    esto creara una etiqueta llamada v1.0.0 en el commit actual, junto con el mensaje descrito.

    NOTEMOS que para listar todas las etiquetas que hay se usa el comando "git tag" y nos retorna una lisa de todas
las etiquetas en orden alfabético. en caso de necesitar informacion mas detallada de 
una etiqueta especifica podemos usar "git show nombre-etiqueta" esto mostrara el commit etiquetado, el mensaje
de la etiqueta, el autor y la fecha.

Para etiquetar un commit especifico que no sea el mas reciente podemos hacerlo usando el
hash del commit: 
    git tag <nombreEtiqueta> <commitHash> o pues con el HEAD~N

y finalmente para eliminar una etiqueta localmente usamos git tag -d <nombre>

NOTA: 
-a: se usa para crear una etiqueta anotada en git, osea, se esta creando
una etiqueta que o solo apunta a un commit sino que tambien contiene metadatos adicionales

-d: se usa para eliminar una etiqueta en tu repositorio local, es util si se comete un error
al crear una etiqueta o ya no necesita una etiqueta especifica.

para moverme (el HEAD) entre commits entonces ahora podemos usar el nombre de el tag escpecifico para ir
a un commit para no tener que usar el hash, tal que 
    git checkout tags/<nombreTag> 

al poner "git tag" me aparecera todos los tags que tengo hasta ese momento, en caso de necesitarlo.

    
11. git reflog: es una herramienta util que registra
todos los movimientos del puntero HEAD en el repositorio. A diferencia
de git log, que solo muestra el historial de commits, git reflog permite ver
todas las acciones importantes que se han hecho, como cambios de ramas,
resets, commits y merges. ESPECIALMENTE UTIL CUANDO SE NECESITAN
RECUPERAR CAMBIOS O COMMITS QUE PARECEN PERDIDOS O DESHACER
ACCIONES COMO UN git reset --hard.
se guarda un registro de todas las veces que el puntero
se mueve en el repositorio, permite ver el historial de acciones
que afectan el puntero HEAD, incluso aquellas que no aparecen en 
git log.

    git reflog

muestra una lista con los movimientos del puntero HEAD, incluyendo commits,
ramas, resets, etc. y aparece como

    <hash> HEAD@{n} <descripcion> donde n representa el numero de eventos
    en el historial de HEAD. donde HEAD{0} es el estado actual del HEAD
    y luego muestra una descripcion

Si se cometio algun error y se quiere volver a un estado anterior, se puede
usar git reflog, se usa git reflog para que se muestre la lista, identifico
el commit que deseo recuperar con el HASH o HEAD@{n}, entonces para recuperar
se hace con el mismo git reset --hard y el commit al que me voy es el que 
recupere con el git reflog

    git reset --hard HEAD@{n} y asi recupero lo mio (DAME LO QUE ME PERTENECE)

12. GIT BRANCH: Es uno de los comandos mas importantes en git y se usa para trabajar
con ramas, permitiendo desarrollar caratcterísticas, corregir errores o 
experimentar con nuevas ideas sin afectar la rama principal(se pueden crear tantas como quiera
entonces se puede experimentar como se desee sin afectar el tronco del arbol del trabajo, y en caso
que se quiera se puede agregar).
Hay varias funciones para este comando: 

    1. git branch , muestra todas las ramas disponibles
    ya creadas en el repositorio y marca con un * en la que se
    esta trabajando actualmente

    2. git branch <nombre>, crea una nueva rama nombre el nombre "nombre"
    pero ojo, la nueva rama se crea a partir del ultimo commit, y si hago
    algun commit en esta nueva rama, no se guarda en la rama principal si no que
    se deriva en esta nueva rama, por lo que si se devuelve al rama main no apareceran
    estos commits a menos de que se fusionen, de esto se basa, poder experimentar sin 
    dañar la parte principal que ya funciona
    
    3. git checkout <rama> o git switch <rama> para cambiar de rama

    4. git checkout -b <nombre> o git switch -c <nombre>, crea una nueva rama
    con el nombre "nombre" y directamente me mueve a ella.

    5. git branch -d <nombre>: se usa para eliminar una rama 
    con el nombre "nombre" esto siempre y cuando los cambios de esa
    nueva rama ya hayan sido fusionados con la rama principal, en caso
    que no desee fusionar esos cambios porque tal vez no quedo bien
    lo que se hizo se usa una -D en lugar de -d. Pero ojo pues aunque 
    se supone que se elimino la rama podemos tener una referencia de los commits
    que se tuvieron y se puede viajar a ellos, pero la rama en la que estaban ya no 
    esta, todo esto suponiendo que ya se hizo una fusion con otra rama.

    6. git branch -r, muestra una lista de las ramas remotas junto 
    del nombre de origen 

    7. git branch -m <nombreviejo> <nombrenuevo>, renombra una rama

13.git merge:
Es el comando para combinar dos ramas en una. Cuando se trabaja en diferentes
ramas y se quieren unir cambios se aplica el git merge. Al aplicar esta linea
Git intenta unir el historial de dos ramas, creando un nuevo commit que refleja
la combinacion de los cambios realizados en ambas ramas.

    Primero que nada hay que cambiarse a la rama a la que se le 
    aplicaran los cambios. se tiene una rama y se quiere unir con 
    la rama main entonces primero haey que cambiar a la rama main y
    ahi luego de estar en la rama main aplciamos la funcion

        git merge <nombre-rama> y esto fusionara la nueva rama con la 
        rama main
    
    Hay diferentes tipos de merge con respecto a los commits que hayan: 

    1. fast-forward merge: si no hay commits adicionales en la rama main(o a la que se le fusionara otra rama)
    desde que se creo la rama secundaria,es decir, cuando no se hizo ningun otro cambio
    desde la rama principal desde que se creo la otra rama. Entonces, git mueve
    el puntero de main hacia adelante, porque no hay ningun cambio en el main que deba combinarse, simplemente
    se mueve al ultimo commit de la rama secundaria, pues como se supone que no se hizo nada en el main
    es como si se hubiera seguido con el mismo trabajo.
    
        Antes del merge:

    A---B---C  (main)
            \
            D---E  (feature-branch)

    Después del merge (fast-forward):

    A---B---C---D---E  (main, feature-branch)

    y no hay ningun commit extra de fusión.

    2. Merge con commit de fusión: 
    Sucede cuando se han hecho cambios en ambas ramas. En este caso, Git
    crea un commit extra llamado commit de merge, que une los cambios de ambas ramas
    Antes del merge:

    A---B---C  (main)
           \
            D---E  (feature-branch)

    Después del merge:

    A---B---C---M  (main)
          \    /
           D---E  (feature-branch)

    M es el commit de merge, que combina los cambios de las ramas, pero notese que hay cambios
    de algo en general no en las mismas lineas de codigo, en ese caso pasa lo siguiente

    3. Merge con conflicto: 
    Ocurre cuando Git no puede decidir automaticamente como combinar los cambios.
    Esto pasa si ambos modificaran las mismas líneas en los mismos archivos, un ejemplo
    es que desde la rama main se hizo un cambio en la linea 10 de un archivo y en la otra 
    rama tambien se hizo un cambio en la linea 10 del mismo archivo y entonces hay que 
    resolver el conflicto de manera manual y git mostrara donde estaran estos conflictos. Entonces
    hay que forzar el conflicto para poder arreglarlo.

    NOTA: Luego de fusionar las ramas, la rama secundaria no se eliminar ni desaparece, seguira existiendo
    y trabajando en ella y se desea, no se borra ni se modifica por el merge pero pues en caso
    que ya no se necesite se puede eliminar

    4. El squash merge en git es una forma de fusionar ramas que combina todos los commits de una rama en un solo 
    commit antes de hacre la fusión con la rama principal. Útil para mantenre un historial limpio, eliminando
    la acumulación de mútilples commits pequeños o intermedios y presentando los cambios en un único commit significativo.
    Supongamos que se esta trabajando en una rama con nombre feature y se hacen varios commits en esta A - B - C, 
    al realizar una fusion con squash git combinara esos tres commit en uno solo, 
    antes de fusionar los cambios a la rama base y el commit resultante puede tener un mensaje descriptivo que resuma
    los cambios. y se hace tal que

        git merge --squash feature 

    y git pedira crear un nuevo commit para la fusión. finalmente, esto se usa para mantener un historial mas limpio
    y es util cuando hay muchos commits pequeños que no son significativos individualmente


14. Git stash 
Sirve para guardar temporalmente los cambios no confirmados, es decir, que no han sido commiteados si no que se 
van a un area llamada stash. Útil cuando se esta trabajando en algo, pero se necesita cambiar de rama o hacer algo
diferente sin perder los cambios actuales, lo que se ha hecho en esa rama. Guarda los archivos modificados de manera temporal y te deja con un área
de trabajo limpia permitiédnote volver a los cambios más tarde cuando lo necesites. Supongamos que estamos
trabajando con una rama y se tiene algunos cambios pero no se quiere hacer commit y se necesita cambiar a la rama main
para revisar algo, pero no se quiere perder el trabajo que ya se tiene en esa rama.
    
    git stash, movera los cambios a una area temporal de almacenamiento
    llamada stash y el área de trabajo quedará limpia como si no se hubiera hecho nada
    
    git stash list, sirve para ver los stashers que se tienen guardados pues se pueden tener varios, y esto 
    retornara una lista d eso con un indice stash@{n} es el n-ésimo stash.  
    
    git stash apply, cuando se quieren recuperar los cambios guardados, se pueden aplicar el stash mas reciente
    esto restaura los cambios del stash mas reciente sin eliminarlo de la lista. Si se quiere eliminar
    despues de aplicar se puede usar git stash drop o simlemente usar git stash pop
    para aplicar y eliminar al mismo tiempo, esto restaura los cambios y elimina el stash de la lista
    
    git stash save "mensaje" sirve para guardar un mensaje descriptivo al stash para recordar lo que se guardo
    y se puede ver en la lista
    
    git stash apply stash@{n} es la forma de aplicar un stash especifico cuando se tiene 
    una lista de varios
    
    git stash clear es la forma de eliminar todos los stashes guardados.
    
    
15. git rebase -i: Es una forma de ordenar y reducir commit innecesarios en una rama especifica para  tener
commits que no sirven indivudualmente que se hace con git rebase -i que permite modificar el historial
de commits de una rama de forma interactiva.

    1. nos vamos a la rama que se ordenara
    
    2. iniciamos el rebase interactivo: git rebase -i HEAD~# y esto abre una lista con los ultimos
    # commits y en un editor de texto y este se podra modificar 
        pick a1b2c3d Commit A
        pick e4f5g6h Commit B
        pick i7j8k9l Commit C
        pick m1n2o3p Commit D
        pick q4r5s6t Commit E 
        
    pick es al accion predeterminada que es para que el commit se mantenga tal cual pero este lo podemos cambiar por otras acciones
        squash : combina el commit con el anterior lo que resulta en uno solo que fusiona ambos
        reword: cambia el mensaje del commit
        drop: elimina el commit por completo

        pick a1b2c3d Commit A
        squash e4f5g6h Commit B
        squash i7j8k9l Commit C
        squash m1n2o3p Commit D
        pick q4r5s6t Commit E

        se combinaron BCD en el commit A pero mantendra E igual. Si  hizo un squash ha que editar el mensaje
        del commit resultante.

        CUIDADO PUES ESTE COMANDO ES MUY PELIGROSO PERO UNA FORMA DE SALVARSE SIN QUE SE PIERDA NADA
        ES CON EL CODIGO git rebase --abort y aborta todo lo que se estaba haciendo y vuelve todo a la normalidad

        """

#---------------------------------------------------------------------------------------------------------
#GITHUB
"""
Es una plataforma de control de versiones a nivel nube, donde todos los respositorios se 
guardan en una plataforma donde muchas personas desde diferentes maquinas pueden ver, editar
y trabajar en conjunto. Trabaja con git desde abajo pero la diferencia es que los repositorios(galeria)
no es solo a nivel local del computador si no también que esta en la nube para que cualquier persona 
pueda verlo.
Git hub es por excelencia la red social de los desarrolladores, hay que tener un perfil presentable
y se puede usar tanto para publicar proyectos como para ver proyectos de diferentes personas
siempre y cuando sean publicos o den el permiso personalmente. En la parte de explore se pueden 
ver todas las publicaciones publicas hechas a nivel mundial y aparecen los repositorios de proyectos
grandes e importantes que son de codigo abierto.
Cada proyecto tiene su propia URL.

CREANDO MI PRIMER RESPOSITORIO EN GITHUB
Como ya sabemos es el lugar donde se va a crear con git y hay 2 formas principales
de hacerlo: 
    1. Crear un proyecto con git en la maquina y luego subirlo con github.
    2. Crear en github un proyecto directamente que trabaje con git

esto dependera del trabajo o el respectivo proyecto. Para empezar,
le damos new para crear un nuevo repositorio  y como es la primera vez lo mejor que podemos hacer
es que al repositorio le pondremos nuestro nombre pues github sabe que sera el primero 
en el cual se podra crear la pagina de inicio y lo que la gente vera de primera
como presentación de cada persona.

-Para todo proyecto es importante ser especificos y pues se tiene las opciones de que los 
proyectos sean públicos(todos pueden ver) o privados(solo tu y personas con permiso podran ver) 
según la necesidad.

-NOTA: Es recomendable que para todo repositorio se le añada un archivo de tipo "README.md" que es 
un documento que se coloca en la raíz de un repositorio para proporcionar información sobre el proyecto. 
ES LO PRIMERO QUE LOS VISITANTES VEN, por lo que se usa para explicar de que se trata el proyecto, cómo usarlo
y cualquier información relevante. Por convención el archivo se llama README.md con .md para markdown lo que permite
formatear texto con estilos como encabezados, listas, enlaces y codigo. Contiene el titulo del proyecto, descripción,
instalación, uso, contribución, licencia, Autor o mantenedores y referencias (Markdown es un lenguaje
de marcado simple que convierte texto plano en formato con estilo, como encabezados, litas,
enlaces y código).

-Tambien se puede añadir un .gitignore por si se necesita 

-La licencia es un documento que establece los terminos bajo los cuales
otras personas pueden usar, modificar y distribuir el codigo de un repositorio, es decir, 
establece los derechos de autor para que nadie pueda usar lo que hiciste protegiendo al creador
como a los usarios del codigo. SIN LICENCIA EL CODIGO ES PROTEGIDO AUTOMÁTICAMENTE POR DERECHOS DE AUTOR y
nadie puede usarlo legalmente, una licencia da permiso para usar el código bajo ciertas condiciones. Por 
ello hay varios tipos de licencia.

-> DE GIT A GITHUB: Si se tiene un proyecto importante y se quiere por ejemplo
trabajar en equipo, lo podemos subir a un servidor para que varias personas podamos ir
trabajando en el, el proyecto en git hub es una manera remota, online, es la union para trabajar
cada uno en el proyecto. SOLO HAY UN PUNTO ÚNICO DE UNION ENTRE DESARROLLADORES Y SERA 
GITHUB que sera el servidor remoto. Incluso es muy útil asi sea un trabajo personal pues en caso
que se dañe el pc o se pierda el trabajo local que se tiene si se puso el trabajo en github
no se perdera pues es un servidor remoto fuera de tu pc, incluso si se cambia de ordenador, simplemente
descargo los archivos y sigo trabajando como si no pasara nada.

AUTENTICACIÓN SSH ---------------------------------------------------------------------------------------
(hay que leer la documentación) sección de autenticación. DESDE LA TERMINAL NO EL GITBASH
Autenticación y coneccion SSH a github: Primero lo veremos a grandes rasgos, es mi tarea
revisar esto con detenimiento a partir la documentación. En general es un metodo de autenticacion
de llave publica y privada para servidores remotos donde no hay necesidad de estar usando usuarios y
contraseñas, se hace mediante un archivo de clave privada en el equipo local. primero EN LA TERMINAL comprobaremos
si ya tenemos unas claves ssh con ls -al ~/.ssh TODO ESTO ESTA EN LA DOCUMENTACIÓN DE GIT, si no
se tienen llaves ssh entonces se pone ssh-keygen -t ed25519 -C "your_email@example.com" (notese
que aca se usa el algoritmo de encriptación ed25519 pero tambien puede ser el rsa y el correo debe 
ser el mismo con el que se tiene la cuenta de github) y de esta
manera se crea un llave pública y una privada y hay que poner un nombre al archivo donde se guardaran
estas cosas. y si se quiere mas seguridad se puede poner una frase de contraseña o se puede dejar en blanco
y asi se me ha crado una clave ssh y en el directorio .ssh apareceran 2 archivos nombre y nombre.pub 
que son las llaves publicas y privadas.

Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]  aca es donde se indica el nombre
de las claves. Dan unos recomendados como lo son id_rsa, id_ed25519 pero en general puede ser el que queramos. aunque
si solo se da enter notese que se guardara automaticamente en una nueva carpeta llamada .ssh con el nombre id_algorithm

Y esto es para ingresar una contraseña adicional, en caso que no se quiera simplemente se da enter
Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]

luego para github necesitamos el archivo de llave publica el .pub 

AGENTE-SSH(ssh-agent)
Es un programa que se ejecuta en segundo plano y almacena tus claves privadas SSH en la memoria, de manera
que no tengas que ingresar tu frase de paso cada vez que te conectas a un servidor o interactúas con servicios
como github usando SSH. Primero se generan las claves SSH (pública y privada) y se añade la clave
privada al agente con ssh-add para que pueda ser utilizada y asi, cuando me conecte a un servidor o use
git ssh-agent proporciona automáticamente a clave privada al servidor. 

1. se ejecuta eval "$(ssh-agent -s)" y se iniciara el ssh-agent en segundo plano y retornara un 
agent pid #### que indica que el proceso esta corriendo.

4. hacer ssh-add c:/Users/YOU/.ssh/id_ed25519 agregar la clave privada y de esta
manera se queda lista para que la clave quede guardada. 


RECOREMOS QUE TODO ESTO ESTA EN LA DOCUMENTACION DE GITHUB GRATIS EN LA WEB 

AHORA LUEGO DE TENER las claves publicas y privadas ademas de del agente ssh se tiene que hacer
lo siguiente, nos vamos a github y a la parte de settings y luego a SSH and GPG keys 
que son claves importantes, en caso de que se trabaje siempre desde la misma pagina
es bueno hacer esto para que se guarden estas claves y no se tenga que tener que configurar
cada que se entra. le damos para crear una nueva clave SSH y se le puede dar un nombre y en la parte
de la clave se le pondra la clave publica que creamos hace un momento (es todo el codigo que aparece en un archivo
de tipo pubisher pero se puede abrir facilmente con el bloc de notas ) y luego se añade, en caso que se tengan
mas ordenadores o cosas por el estilo se ueden añadir mas claves. 
Finalmente hay que verificar que si se haya conectado con la maquina local escribiendo ssh -T git@github.com en el git bash 
y se confirma con yes para que esa llave se mantenga activa.
------------------------------------------------------------------------------------------------------

Ahora luego de haber unido el git del pc con github, obviamente no es recomendable subir un 
proyecto en el primer repositorio que es la carta de presentación de cada desarrollador. Eso 
es solo para poner una buena introducción de lo que se vera en todo el perfil y eso. 
Ahora al crear un repositorio nuevo se podran ver diferentes opcines desde el github 

nota: recordemos que  echo "texto" sirve para poner texto en la terminal.

Comandos para trabajar de git a github, para subir nuestro codigo a github: 

1. git remote: Es un comando que permite gestionar los respototios remotos asociados
con mi repositorio local (el repositorio remoto es una version de mi proyecto en un servidor)
por ello para poder unir un repositorio local a un servidor, como dice en el principio cuando se crea
el repostorio en github, hay que usar el comando 

    git remote add origin https://github.com/usuario/nombre_repositorio_online.git 

donde origin es el nombre que se le da al repositorio remoto y lo otro es la URL del repositorio 
remoto de github. y luego de darle enter entonces se supone que uni mi repositorio local.

    git remote -v: muestra los repositorios configurados
    con el repositorio local. 

    git remote remove nombre: elimina el remoto llamado nombre. Luego 
    el repositorio local no estara vinculado con el remoto.

    git remote rename origin nuevo-nombre: renombrael remoto origin a nuevo-nombre

    git remote set-url nombre nueva-url: Sirve para actualizar la url del repositorio

    git remote show origin: Muestra detalles sobre el remoto llamado origin

2. git push: Es el comando en git que se usa para subir mis cambios locales (commits) al respositorio
remoto como github. Es como actualizar la version online del proyecto con las modificaciones
que has he hecho con mi maquina local. y entonces para empezar a mover las cosas hacemos

    git push -u origin main
    -u: establece una referencia de seguimiento para la rama local vinculandola con la rama remota 
    de tal manera que no hay que poner todo eso otra vez para subir los commits. 
    origin: nombre del repositorio remoto por defecto
    main: nombre de la rama remota donde quieres enviar tus cambios
    Esa es la manera de ralacionar la rama main con la rama principal remota. Tal vez
    pida autenticar la contraseña de github pero nada mas. Es muy complejo entender
    todas la seguridad que esto pueda tener. Ahora se refresa la pagina de github y 
    ya se pueden ver los arhivos que teniamos en local, incluido el gitignore y todo en una
    rama que se llama main .   

    luego simplemente hago git push y ya estaria. 

Es importante mencionar que desde el mismo github podemos hacer commits y gestionar
varias cosas que se hacen desde git. y que cada respositorio remoto puede tener y deberia tener un 
archivo de tipo README.md para la descripcion del proyecto para las pesonas que estaran interesadas
en trabajar con el, al hacerlo ser hara un commit con el archivo readme. Notese que en el 
repositorio remoto en la esquina superior derecha se pueden ver todos los commits


IMPORTANTE: Cuando nosotros seguimos trabajando en nuestro proyecto de manera local y luego hacemos un commit
de este. No se guardara en github automaticamente, es decir, se guardara en el repositorio local que nostoros
tenemos pero no se guardara en el remoto para ello hay que hacer algo mas, es decir, nuestro git push. y de esa manera
nuestro repositorio local estara a la par con el repositorio remoto. incluso 
haciendo git log, aparecera DONDE ESTA EL ORIGIN que es el nombre del repositorio remoto. 

3.git fetch: Este comando descarga todos los cambios del repositorio remoto al repositorio local, pero sin aplicar
esos cambios a la rama actual. Es decir, permite ver en que ha cambiado el remoto antes de decidir si deseas incorporar 
esos cambios. Es como ver una vista previa sin afectar el trabajo actual. Por ejemplo, si se esta trabajando
en una rama main pero un compañero ha hecho cambios en el repositorio remoto que aun no tenemos en el local, para 
ver los cambios en el remoto es
    git fetch origin 

Esto descargara todos los cambios del repositorio remoto origin 
pero sin fusionarlos en la rama actual. Para ver los cambios sin aplicarlos aun
se puede ver la nueva informacion en el remoto y comparar

    git log origin/main

y esto muestra el historial del remoto para ver los commit que se han agregado
desde la ultima vez que sincronizaste. En caso de que se decida incorporar
los cambios despues de verlos, se puede hacer con un git merge  o un GIT PULL

    git merge origin/main que fusiona los cambios descargados en la rama main.

finalmente, git fetch descarga los cambios que tiene el repositorio remoto antes de
aplicarlos a la rama main para ver las actualizaciones antes de fusionarlas al trabajo.
Es el que usamos luego de hacer el git push -u origin main, o sirve cuando se intenta
hacer un git push pero hay un problema pues querra decir que se esta intentando subir o actulizar
desde el local al remoto pero alguien hizo algun cambio primero y hay conflicto por lo que primero
hay que revisar estos conflictos y tener nuestra rama main local acutalizada a la del remoto 
y ahi ya no habran conflictos. 

4. git pull:Es una combinación de git fetch y git merge. Es decir, descarga
los cambios del remoto y automáticamente los fusiona con la rama actual en un solo paso. 
Este se usa cuando se esté seguro de que se quiere traer y fusionar automáticamente los 
cambios del remoto a la rama local

    git pull origin main: trae los cambios del remoto
    y los fusiona. En caso de que hayan conflictos git avisara
    y pedir que se resuelvan

luego de que se unan, todos los nuevos archivos y codigos estaran en mi
repositorio local. Es importante que si llegamos a tener problemas con esto
revisemos videos o la respectiva documentacion para solucionarlos. 

5. git clone:Es el comando que se usa para copiar un repositorio remoto completo 
a tu computadora. Basicamente descarga todos los archivos, el historial de cambios y las ramas
del repositorio, creando una copia completa en el sistema local. 
De esta manera al copiar todos los archivos y el historial nos permite ver y editar
todo el proyecto en la máquina. También configura el remoto llado origin, lo que permite
que conecte y sincronize con el repositorio original. 

    git clone https://github.com/usuario/proyecto.git
              ssh...

Crea una carpeta llamada proyecto en el sistema local, con los archivos, 
commits y ramas del repositorio y entonces se puede trabajar en el proyecto en
la computadora como si fuera el original.Aunque esto tambien se puede hacer a mano
obviamente es mejor pues simplemente trabajar con el control de versiones. Es recomendable
clonarlo por medio del ssh pues al inicio ya lo configuramos. Finalmente se crea una carpeta
con todo lo de este repositorio. Puede que algunas veces exista algun problema al hacer
las conecciónes con ssh pero es porque muchas veces las redes corporativas restringen
el puerto 22 que usa ssh en este caso se puede intentar usar https en lugar de ssh.
Notese que en una red privada no hay ningún problema a la hora de clonar un repo. 

6. fork: Hacer un fork en git es como sacar una copia completa de un proyecto que está
en un repositorio de alguien más, pero esta copia queda en tu propia cuenta sin afectar el 
original que es de alguien mas. Da una versión propia del proyecto donde
se pueden hacer cambios y experimentos y no se necesita ningún permiso especial. Supongamos
que hay un proyecto muy increible en el cual se quiere trabajar y experimentar, entonces
se clona en el respositorio local con el git clone, excelente y se editan muchas cosas, ahora bien,
a la hora se montar al respositorio remoto habrá un error pues se esta intentando editar un repo
de otra persona lo cual si no se tiene un permiso especial no se podra. Aca entra el FORK. Ese repositorio
del proyecto increible de otra persona le puedo dar al botón FORK en github y de esta manera se crea una 
copia de este repositorio en mi propio repositorio local para yo poder hacer
todo lo que se me de la gana sin afectar en nada al dueño original, luego de tener esta copia en 
mi repositorio remoto lo que puedo hacer es clonar este en mi maquina local para ahora si poder
subir los cambios al repositorio remoto pero obviamente al remoto que esta en mi cuenta.  
"""
'''
Ese error:

```
fatal: refusing to merge unrelated histories
```

ocurre en Git cuando estás intentando hacer un `pull`, `merge` o `push` entre dos repositorios (o ramas) que no tienen un historial en común. Suele pasar cuando:

- Iniciaste un repositorio local con `git init` y luego lo conectaste a un repositorio remoto que ya tenía contenido (como un `README.md`, por ejemplo).
- O estás tratando de fusionar ramas completamente independientes.

---

### ✅ 🔧 **Solución rápida (cuando estás seguro de lo que haces):**

Usa el flag `--allow-unrelated-histories`:

```bash
git pull origin main --allow-unrelated-histories
```

Este comando le dice a Git: "Sí, ya sé que no tienen relación, pero fusiónalos de todos modos".

🔁 Cambia `main` por `master` o la rama que estés usando, si es el caso.

---

### 🧠 ¿Y después qué pasa?

Git intentará fusionar ambos historiales. Si hay conflictos, te los mostrará y tú deberás resolverlos manualmente. Una vez hecho esto:

```bash
git add .
git commit -m "Merge unrelated histories"
git push origin main
```

---

### 🗂️ 💡 ¿Cómo organizar bien tu repo para que no vuelva a pasar?

1. **Clona primero el repositorio remoto si ya existe:**

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

2. **Y luego agrega tu proyecto local (archivos, notebooks, etc.) dentro de esa carpeta clonada.**

3. Finalmente:

```bash
git add .
git commit -m "Añadir archivos del proyecto"
git push origin main
```

---

¿Quieres que te ayude a reorganizar tu estructura de proyecto y subirlo desde cero bien organizado? Te puedo dar los pasos desde local a remoto con orden.
'''
#con git push --force actualiza el github a como esta el git normal. 