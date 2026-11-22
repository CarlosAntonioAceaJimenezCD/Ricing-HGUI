- [¿Dónde está la personalización del tema de íconos?](#dónde-está-la-personalización-del-tema-de-íconos)
- [Suru++](#suru)
  - [¿Cómo cambiar los colores de las carpetas y de todos los íconos de 16px?](#cómo-cambiar-los-colores-de-las-carpetas-y-de-todos-los-íconos-de-16px)
  - [¿Cómo habilitar los colores degradados de Suru++?](#cómo-habilitar-los-colores-degradados-de-suru)
- [Suru++ Asprómauros](#suru-asprómauros)
  - [¿Cómo cambiar los colores de todos los íconos de 16px?](#cómo-cambiar-los-colores-de-todos-los-íconos-de-16px)
  - [¿Cómo habilitar los degradados de Suru++ Asprómauros?](#cómo-habilitar-los-degradados-de-suru-asprómauros)
- [¿Cómo exportar el tema de iconos?](#cómo-exportar-el-tema-de-iconos)
- [¿Dónde está el tema de íconos exportado?](#dónde-está-el-tema-de-íconos-exportado)
- [¿Cómo importar un tema de íconos no listados para Oomox?](#cómo-importar-un-tema-de-íconos-no-listados-para-oomox)

### ¿Dónde está la personalización del tema de íconos?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example1.gif" alt="Example 1 – Icons theme customization" width="80%">
</p>

### Suru++ 

#### ¿Cómo cambiar los colores de las carpetas y de todos los íconos de 16px?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example2.gif" alt="Example 2 – Icons colours" width="80%">
</p>

#### ¿Cómo habilitar los colores degradados de Suru++?

Es importante observar que los íconos de `actions`, `panel` y `status` no son compatibles con el degradado. 

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example3.gif" alt="Example 3 – Gradient Colours" width="80%">
</p>

### Suru++ Asprómauros

#### ¿Cómo cambiar los colores de todos los íconos de 16px?

Es importante observar que este tema de íconos no tiene colores de las carpetas. Ahora las carpetas son llenamente monocromáticas y son compatibles con el degradado. 

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example4.gif" alt="Example 4 – Suru++ Asprómauros Colours" width="80%">
</p>

#### ¿Cómo habilitar los degradados de Suru++ Asprómauros?

Así como Suru++, es importante observar que los íconos de `actions`, `panel` y `status` no son compatibles con el degradaodo. 

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example5.gif" alt="Example 5 – Suru++ Asprómauros Gradient Colours" width="80%">
</p>

### ¿Cómo exportar el tema de iconos?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example6.gif" alt="Example 6 – Export icons theme" width="80%">
</p>

### ¿Dónde está el tema de íconos exportado?

* Si usted ha exportado Suru++ y Suru++ Asprómauros, vea la referencia [¿Cómo exportar el tema de iconos?](#cómo-exportar-el-tema-de-iconos), en cual puedes escoger el camino que quieres exportar. 
* Si usted ha exportado temas de eiconos non-Suru++, entonces los temas de íconos son exportados para `~/.icons`. 

### ¿Cómo importar un tema de íconos no listados para Oomox?

* No hay opción de importar un tema de íconos no listados para Oomox porque no tienen complementos para funcionar en el Oomox.
* Usted debe crear los propios complementos para el tema de iconos no listados.
* Si usted necesita modificar ePapirus, Papirus-Light y Papirus-Dark, usted puede duplicar y modificar el complemento llamado `icons_papirus` que se encuentra en `oomox/plugins` o solicita al [@SmartFinn](/SmartFinn).
* Si usted necesita modificar eSuru++ y Suru++ Dark, usted puede duplicar y modificar el complemento llamado `icons_suruplus` que se encuentra en `oomox/plugins` o solicita al [@gusbemacbe](/gusbemacbe).
* Si el cierto tema de íconos no está listado en el Oomox, usted debe solicitarlo al autor de ese tema de íconos.

**OBSERVACIÓN IMPORTANTE:** ¡No se olvide de copiar el tema de íconos a `oomox/plugins/icons_NUEVO_PLUGIN/PEGA_TEMA_ICONOS_AQUI` si usted no quiere agregarlo a `.gitmodules`!
