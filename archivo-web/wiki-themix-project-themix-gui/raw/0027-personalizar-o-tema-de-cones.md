- [Onde está a personalização do tema de ícones?](#onde-está-a-personalização-do-tema-de-ícones)
- [Suru++](#suru)
  - [Como alterar as cores dos directórios e de todos os ícones de 16px?](#como-alterar-as-cores-dos-directórios-e-de-todos-os-ícones-de-16px)
  - [Como habilitar os gradientes de cores de Suru++?](#como-habilitar-os-gradientes-de-cores-de-suru)
- [Suru++ Asprómauros](#suru-asprómauros)
  - [Como mudar as cores de todos os ícones de 16px?](#como-mudar-as-cores-de-todos-os-ícones-de-16px)
  - [Como habilitar os gradientes de Suru++ Asprómauros?](#como-habilitar-os-gradientes-de-suru-asprómauros)
- [Como exportar o tema dos ícones?](#como-exportar-o-tema-dos-ícones)
- [Onde são exportados os temas de ícones?](#onde-são-exportados-os-temas-de-ícones)
- [Como importar o tema de ícones não listado para Oomox?](#como-importar-o-tema-de-ícones-não-listado-para-oomox)

### Onde está a personalização do tema de ícones?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example1.gif" alt="Example 1 – Icons theme customization" width="80%">
</p>

### Suru++ 

#### Como alterar as cores dos directórios e de todos os ícones de 16px?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example2.gif" alt="Example 2 – Icons colours" width="80%">
</p>

#### Como habilitar os gradientes de cores de Suru++?

É importante observares que ícones de `actions`, `panel` e `status` não suportam gradiente de cores.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example3.gif" alt="Example 3 – Gradient Colours" width="80%">
</p>

### Suru++ Asprómauros

#### Como mudar as cores de todos os ícones de 16px?

É importante observares que este conjunto de ícones não possui directórios coloridao. Agora os directórios são totalmente monocromáticos e suportam gradientes.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example4.gif" alt="Example 4 – Suru++ Asprómauros Colours" width="80%">
</p>

#### Como habilitar os gradientes de Suru++ Asprómauros?

Como no Suru++, é importante observares que ícones de `actions`, `panel` e `status` não suportam gradiente de cores.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example5.gif" alt="Example 5 – Suru++ Asprómauros Gradient Colours" width="80%">
</p>

### Como exportar o tema dos ícones?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example6.gif" alt="Example 6 – Export icons theme" width="80%">
</p>

### Onde são exportados os temas de ícones?

* Se exportaste Suru++ e Suru++ Asprómauros, vê a referência - [Como exportar o tema dos ícones?](#como-exportar-o-tema-dos-ícones), na qual escolhes o caminho que desejas exportar.
* If you exported non-Suru++ icons theme, the icons themes are exported by default into `~/.icons/`.

### Como importar o tema de ícones não listado para Oomox?

* Não há opção de importar o tema de ícones não listado para Oomox porque eles não possuem *plugins* para funcionar no Oomox.
* Precisas criar os próprios *plugins* para o tema de ícones não listado.
* Se quiseres modificar ePapirus, Papirus-Light e Papirus-Dark, podes duplicar e modificar o *plugin* chamado `icons_papirus` que está localizado em `oomox/plugins` ou pede ao [@SmartFinn](/SmartFinn). 
* Se quiseres modificar o eSuru++ e o Suru++ Escuro, podes duplicar e modificar o *plugin* chamado `icons_suruplus` que está localizado em `oomox/plugins` ou pede ao [@gusbemacbe](/gusbemacbe). 
* Se o certo tema de ícones não estiver listado no Oomox, deverás pedir ao autor deste tema de ícones.

**OBSERVAÇÃO IMPORTANTE:** Não te esqueças de copiar o tema dos ícones para `oomox/plugins/icons_NOVO_PLUGIN/COLA_TEMA_ICONES_AQUI` se não quiseres aderir ao `.gitmodules`!
