# Introducción a Git 🌱

## ¿Qué es git? 🤔
git es un sistema de control de versiones usado para manetener un 
orden y un control para proyectos de programación, es una herramienta extremadamente
útil para proyectos grandes. Vease git como una galería o historial, que cada que se le da una instruccion toma una foto con descripción, fecha y autor del proyecto,
hasta donde se lleve, con lo que se lleve. De esta manera podemos ir viajando
en el tiempo a partes del proyecto donde necesitamos ver o corregir algo.

Por ejemplo, supongamos que lo que se realizó en un proyecto no nos gusto, simplemente nos vamos a la última foto antes de ese último cambio y es como si nada hubiese pasado.

## Instalación ⚙️
Git esta de forma nativa en Linux, sin embargo, en caso de no tenerlo basta con hacer: 

🖥️
```bash
sudo apt update && sudo apt install git -y
```
En el caso de windows usaremos lo que se conoce como git bash la cual es una interfáz para trabajar con git que usa el lenguaje bash, que es el mismo lenguaje que usa
linux de forma nativa.

Por tanto, **sin importar si lo que usas windows o en linux (Ubuntu en mi caso) como ambos usan el lenguaje bash se tendrá la misma sintaxis.**
primero que nada, como esto es un control de versiones y puede hacerse en cualquier computadora hay que registrarse con nombre y correo. La forma de hacerlo es muy sencilla pero hay 3 tipos de configuraciones: 


## Establecimiento de usuario 🛠️
### Tipos de configuración

Los niveles de configuración en Git sirven para determinar el alcance y la prioridad de las preferencias del sistema, los usuarios y los proyectos. Además, acá es donde se configuran las credenciales de quien hizo los cambios en el proyecto.

Existen tres niveles: Sistema (para todos los usuarios), Global (por usuario) y Local (por proyecto), donde cada nivel anula al anterior.
[referncia](https://git-scm.com/book/es/v2/Personalizaci%C3%B3n-de-Git-Configuraci%C3%B3n-de-Git)

1. Nivel Local (--local):

- Alcance: Afecta únicamente al repositorio actual donde te encuentres.

- Uso: Es ideal si trabajas en un proyecto de código abierto o un repositorio de la empresa donde necesitas usar un correo corporativo diferente al que usas para tus proyectos personales. Se almacena
en el archivo .git/config dentro de tu proyecto.

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
git config --global user.name 'nombreUsario'

git config --global user.name 'nombreUsario'
```

3. Nivel de Sistema (--system)

- Alcance: Afecta a todos los usuarios y todos los repositorios de esa máquina o servidor.

- Uso: Aplica configuraciones universales para el sistema operativo, aunque rara vez se modifica directamente. Se guarda en el archivo /etc/gitconfig.

- Comando para asignar:
```bash
git config --system core.editor vim
```
[referencia](https://youtu.be/EpCaeC2vEJs?si=utmFRfMaGttZW9b3)

Puedes verificar el estado actual de tus configuraciones utilizando el siguiente comando. Esto listará todas las variables activas y te mostrará el origen de cada una: 

🖥️
```bash
git config --list
```

## Definiciones importantes: 
**Repositorio**: es un espacio centralizado donde se almacena, organiza, mantiene y difunde información digital. [referencia](https://es.wikipedia.org/wiki/Repositorio_(contenido_digital))

**Commit**: es una "fotografía" o punto de control que guarda de forma permanente el estado de tus archivos y el código en un momento específico. Actúa como un guardado en el historial de tu proyecto, permitiéndote regresar a ese punto exacto si algo sale mal.[referencia](https://youtu.be/j9zAL52wuLg?si=xbT9Rkox1mZzytGw)