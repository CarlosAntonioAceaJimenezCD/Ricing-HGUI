- [Où est la personnalisation du thème des icônes ?](#où-est-la-personnalisation-du-thème-des-icônes-)
- [Suru++](#suru)
  - [Comment changer les couleurs des dossiers et de toutes les icônes de 16px ?](#comment-changer-les-couleurs-des-dossiers-et-de-toutes-les-icônes-de-16px-)
  - [Comment activer les dégradés de couleurs de Suru++ ?](#comment-activer-les-dégradés-de-couleurs-de-suru-)
- [Suru++ Asprómauros](#suru-asprómauros)
  - [Comment changer les couleurs de toutes les icônes de 16px ?](#comment-changer-les-couleurs-de-toutes-les-icônes-de-16px-)
  - [Comment activer les dégradés de couleurs de Suru++ Asprómauros ?](#comment-activer-les-dégradés-de-couleurs-de-suru-asprómauros-)
- [Comment exporter le thème des icônes ?](#comment-exporter-le-thème-des-icônes-)
- [Où est le thème d'icônes exporté ?](#où-est-le-thème-dicônes-exporté-)
- [Comment importer le thème des icônes non listés dans Oomox ?](#comment-importer-le-thème-des-icônes-non-listés-dans-oomox-)

### Où est la personnalisation du thème des icônes ?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example1.gif" alt="Example 1 – Icons theme customization" width="80%">
</p>

### Suru++ 

#### Comment changer les couleurs des dossiers et de toutes les icônes de 16px ?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example2.gif" alt="Example 2 – Icons colours" width="80%">
</p>

#### Comment activer les dégradés de couleurs de Suru++ ?

Il est important de noter que les icônes de `actions`, `panel` et `status` ne sont pas compatibles avec le dégradé.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example3.gif" alt="Example 3 – Gradient Colours" width="80%">
</p>

### Suru++ Asprómauros

#### Comment changer les couleurs de toutes les icônes de 16px ?

Il est important de noter que ce thème d’icônes n’a pas de dossiers colorés. Maintenant, les dossiers sont entièrement monochromatiques et sont compatibles avec le dégradé.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example4.gif" alt="Example 4 – Suru++ Asprómauros Colours" width="80%">
</p>

#### Comment activer les dégradés de couleurs de Suru++ Asprómauros ?

Comme Suru++, il est important de noter que les icônes de `actions`, `panel` et `status` ne sont pas compatibles avec le dégradé.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example5.gif" alt="Example 5 – Suru++ Asprómauros Gradient Colours" width="80%">
</p>

### Comment exporter le thème des icônes ?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example6.gif" alt="Example 6 – Export icons theme" width="80%">
</p>

### Où est le thème d'icônes exporté ?

* Si vous avez exporté Suru++ et Suru++ Asprómauros, voyez la référence [Comment exporter le thème des icônes ?](#comment-exporter-le-thème-des-icônes-), dans laquelle vous choissisez le chemin vous voulez exporter. 
* Si vous avez exporté le thème d'icônes non-Suru++, donc les thèmes d'icônes sont exportés sur `~.icons`. 

### Comment importer le thème des icônes non listés dans Oomox ?

* Il n’y a pas aucune option d’importer le thème des icônes non listé dans Oomox, parce qu’ils ne ont pas de plug-ins pour fonctionner avec l’Oomox.
* Vous devez créer vos propres plug-ins pour le thème des icônes non listé.
* Si vous voulez modifier ePapirus, Papirus-Light et Papirus-Dark, vous pouvez dupliquer et modifier le plug-in appelé `icons_papirus` qui se trouve dans `oomox/plugins` ou demandez au [@SmartFinn](/SmartFinn). 
* Si vous voulez modifier eSuru++ and Suru++ Dark, vous pouvez dupliquer et modifier le plug-in appelé `icons_suruplus` qui se trouve dans `oomox/plugins` ou demandez au [@gusbemacbe](/gusbemacbe). 
* Si le certain thème d’icônes n’est pas listé sur l’Oomox, vous devez demander à l’auteur de ce thème-là. 

**ATTENTION IMPORTANTE :** Ne oubliez pas de copier le thème d’icônes dans `oomox/plugins/icons_NOUVEAU_PLUGIN/COLLEZ_THEME_ICONES_ICI` si vous ne voulez pas ajouter au `.gitmodules` !
