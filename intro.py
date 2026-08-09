"""------------------------------------------------------------------------------------------------------



nota: recordemos que  echo "texto" sirve para poner texto en la terminal.

Comandos para trabajar de git a github, para subir nuestro codigo a github: 



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