---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/Frequently-Asked-Questions.md"
title: "Frequently Asked Questions"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
* [Position rofi on screen](WindowPosition)
* [Custom Keymaps](Custom-Keymaps)
* [Show aliases in run menu](../issues/97)
* [xkbcommon: ERROR: couldn't find a Compose file for locale `<your locale>`](xkbcommon-FAQ#compose)
* [Using Rofi with Fish Shell](Using-Rofi-with-Fish-Shell)
* [Using rofi with compton](Using-rofi-with-compton)
* [Wayland support?](Wayland)
* [Can't tab backwards with Shift+Tab](../issues/594)
* Use **rofi** to get arbitrary user input
`bla=$(rofi -dmenu -input /dev/null -p "Enter Text > ")`
* **rofi** gives the following message: `Mode keys not enabled. Please add it to the list of enabled modi: combi,drun`

   **rofi** allows you to, at run time, switch between multiple modi (default keybinding Ctrl-Tab). With `-show` you indicate the mode you want to select when opening. If the mode is not in the list, **rofi** will complain, but still show it. To solve this warning, add your view to the `-modi` list.

* Setup keybinding for **rofi** in unity.

   Go to Control panel, keyboard then shortcuts. Then on the left select custom shortcuts. Click the `+` button and enter name + command you want to run (f.e. `rofi -show run`). Click apply. Now by double clicking disable and hitting the desired key combo you can assign a keybinding.