---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/themix-project/themix-gui/languages/it/Personalizzare il tema di icone.md"
title: "Personalizzare il tema di icone"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/themix-project/themix-gui/wiki"
---
- [Dov'è la personalizzazione del tema di icone?](#dovè-la-personalizzazione-del-tema-di-icone)
- [Suru++](#suru)
  - [Come modificare i colori delle cartelle e di tutte le icone di 16px?](#come-modificare-i-colori-delle-cartelle-e-di-tutte-le-icone-di-16px)
  - [Come abilitare le sfumature dei colori di Suru++?](#come-abilitare-le-sfumature-dei-colori-di-suru)
- [Suru++ Asprómauros](#suru-asprómauros)
  - [Come cambiare i colori di tutte le icone di 16px?](#come-cambiare-i-colori-di-tutte-le-icone-di-16px)
  - [Come abilitare le sfumature di Suru ++ Asprómauros?](#come-abilitare-le-sfumature-di-suru--asprómauros)
- [Come esportare il tema di icone?](#come-esportare-il-tema-di-icone)
- [Dove sono i temi di icone esportati?](#dove-sono-i-temi-di-icone-esportati)
- [Come importare il tema di icone non elencato sull'Oomox?](#come-importare-il-tema-di-icone-non-elencato-sulloomox)

### Dov'è la personalizzazione del tema di icone?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example1.gif" alt="Example 1 – Icons theme customization" width="80%">
</p>

### Suru++ 

#### Come modificare i colori delle cartelle e di tutte le icone di 16px?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example2.gif" alt="Example 2 – Icons colours" width="80%">
</p>

#### Come abilitare le sfumature dei colori di Suru++?

È importante osservare che le icone di `actions`, `panel` e `stato` non sono compatbili con la sfumatura.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example3.gif" alt="Example 3 – Gradient Colours" width="80%">
</p>

### Suru++ Asprómauros

#### Come cambiare i colori di tutte le icone di 16px?

È importante osservare che questo tema di icone non ha cartelle colorate. Ora le cartelle sono completamente monocromatiche e sono compatibili con la sfumatura.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example4.gif" alt="Example 4 – Suru++ Asprómauros Colours" width="80%">
</p>

#### Come abilitare le sfumature di Suru ++ Asprómauros?

Come Suru++, è importante osservare che le icone di `actions`, `panel` e `status` non sono compatibili con la sfumatura.

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example5.gif" alt="Example 5 – Suru++ Asprómauros Gradient Colours" width="80%">
</p>

### Come esportare il tema di icone?

<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/themix-project/oomox/images/examples/example6.gif" alt="Example 6 – Export icons theme" width="80%">
</p>

### Dove sono i temi di icone esportati?

* Se hai esportato Suru++ e Suru ++Asprómauros, consulta il riferimento [Come esportare il tema di icone?](#come-esportare-il-tema-di-icone), nel quale scegli il percorso che vuoi esportare.
* Se hai esportato il tema di icone non-Suru++, i temi delle icone vengono esportati nella cartella `~/.icons/`.

### Come importare il tema di icone non elencato sull'Oomox?

* Non è possibile importare sull'Oomox il tema di icone non elencato perché non hanno *plug-in* per funzionare sull'Oomox.
* Devi creare i propri *plug-in* per il tema di icone non elencato.
* Se vuoi modificare ePapirus, Papirus-Light e Papirus-Dark, puoi duplicare e modificare il *plug-in* chiamato `icons_papirus` che si trova nella cartella `oomox/plugins` o fai richiesta al [@SmartFinn](/SmartFinn). 
* Se vuoi modificare eSuru++ e Suru++ Dark, puoi duplicare e modificare il *plug-in* chiamato `icons_suruplus` che si trova nella cartella `oomox/plugins` o fai richiesta al [@gusbemacbe](/gusbemacbe). 
* Se il determinato tema di icone non è elencato sull'Oomox, devi richiedere all'autore di quel tema icone. 

**OSSERVAZIONE IMPORTANTE:** Non dimenticare di copiare il tema di icone nella `oomox/plugins/icons_NUOVO_PLUGIN/INCOLLA_TEMA_ICONE_QUI` se non vuoi aggiungere al `.gitmodules`!
