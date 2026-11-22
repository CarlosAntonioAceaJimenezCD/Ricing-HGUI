---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/themix-project/themix-gui/languages/pt_br/Customizar o tema de ícones.md"
title: "Customizar o tema de ícones"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/themix-project/themix-gui/wiki"
---
- [Onde está a customização do tema de ícones?](#onde-está-a-customização-do-tema-de-ícones)
- [Suru++](#suru)
  - [Como alterar as cores das pastas e de todos os ícones de 16px?](#como-alterar-as-cores-das-pastas-e-de-todos-os-ícones-de-16px)
  - [Como habilitar os gradientes de cores de Suru++?](#como-habilitar-os-gradientes-de-cores-de-suru)
- [Suru++ Asprómauros](#suru-asprómauros)
  - [Como mudar as cores de todos os ícones de 16px?](#como-mudar-as-cores-de-todos-os-ícones-de-16px)
  - [Como habilitar os gradientes de Suru++ Asprómauros?](#como-habilitar-os-gradientes-de-suru-asprómauros)
- [Como exportar o tema dos ícones?](#como-exportar-o-tema-dos-ícones)
- [Onde são exportados os temas de ícones?](#onde-são-exportados-os-temas-de-ícones)
- [Como importar o tema de ícones não listado para Oomox?](#como-importar-o-tema-de-ícones-não-listado-para-oomox)

### Onde está a customização do tema de ícones?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example1.gif" alt="Example 1 – Icons theme customization" width="80%">
</p>

### Suru++ 

#### Como alterar as cores das pastas e de todos os ícones de 16px?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example2.gif" alt="Example 2 – Icons colours" width="80%">
</p>

#### Como habilitar os gradientes de cores de Suru++?

É importante observar que ícones de `actions`, `panel` e `status` não suportam gradiente de cores.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example3.gif" alt="Example 3 – Gradient Colours" width="80%">
</p>

### Suru++ Asprómauros

#### Como mudar as cores de todos os ícones de 16px?

É importante observar que este conjunto de ícones não possui pastas coloridas. Agora as pastas são totalmente monocromáticas e suportam gradientes.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example4.gif" alt="Example 4 – Suru++ Asprómauros Colours" width="80%">
</p>

#### Como habilitar os gradientes de Suru++ Asprómauros?

Como no Suru++, é importante observar que ícones de `actions`, `panel` e `status` não suportam gradiente de cores.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example5.gif" alt="Example 5 – Suru++ Asprómauros Gradient Colours" width="80%">
</p>

### Como exportar o tema dos ícones?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example6.gif" alt="Example 6 – Export icons theme" width="80%">
</p>

### Onde são exportados os temas de ícones?

* Se você exportou Suru++ e Suru++ Asprómauros, veja a referência - [Como exportar o tema dos ícones?](#como-exportar-o-tema-dos-ícones), na qual você escolhe o caminho que deseja exportar.
* If you exported non-Suru++ icons theme, the icons themes are exported by default into `~/.icons/`.

### Como importar o tema de ícones não listado para Oomox?

* Não há opção de importar o tema de ícones não listado para o Oomox porque eles não têm *plugins* para funcionar no Oomox.
* Você precisa criar os próprios *plugins* para o tema de ícones não listado.
* Se você precisa modificar ePapirus, Papirus-Light e Papirus-Dark, você pode duplicar e modificar o *plugin* chamado `icons_papirus` que está localizado em `oomox/plugins` ou peça ao [@SmartFinn](/SmartFinn). 
* Se você precisar modificar o eSuru++ e o Suru++ Escuro, você pode duplicar e modificar o *plugin* chamado `icons_suruplus` que está localizado em `oomox/plugins` ou peça ao [@gusbemacbe](/gusbemacbe). 
* Se o certo tema de ícones não estiver listado no Oomox, você deverá pedir ao autor deste tema de ícones.

**OBSERVAÇÃO IMPORTANTE:** Não se esqueça de copiar o tema dos ícones para `oomox/plugins/icons_NEW_PLUGIN/PASTE_ICONS_THEME_HERE` se você não quiser adicionar ao `.gitmodules`!
