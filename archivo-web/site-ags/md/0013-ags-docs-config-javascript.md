---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/javascript"
title: "JavaScript | AGS Wiki"
fetched_at: 2026-11-22T06:24:53+00:00
fetcher: "curl + markitdown"
site: "aylur.github.io"
---
[Skip to content](#_top)

[AGS Wiki](/ags-docs/)

Search

Cancel

[GitHub](https://github.com/Aylur/ags) [Discord](https://discord.gg/CXQpHwDuhY)

  Select theme   DarkLightAuto

* Configuration

  + [Installation](/ags-docs/config/installation)
  + [JavaScript](/ags-docs/config/javascript)
  + [First Widgets](/ags-docs/config/first-widgets)
  + [Reactivity](/ags-docs/config/reactivity)
  + [Theming](/ags-docs/config/theming)
  + [Config Object](/ags-docs/config/config-object)
  + [Type Checking](/ags-docs/config/type-checking)
  + [CLI](/ags-docs/config/cli)
  + [Widgets](/ags-docs/config/widgets)
  + [Variables](/ags-docs/config/variables)
  + [Services](/ags-docs/config/services)
  + [Utils](/ags-docs/config/utils)
  + [App](/ags-docs/config/app)
  + [Custom Service](/ags-docs/config/custom-service)
  + [Subclassing GTK Widgets](/ags-docs/config/subclassing-gtk-widgets)
  + [Examples](/ags-docs/config/examples)
  + [Common Issues](/ags-docs/config/common-issues)
* Builtin Services

  + [Applications](/ags-docs/services/applications/)
  + [Audio](/ags-docs/services/audio/)
  + [Backlight](/ags-docs/services/backlight/)
  + [Battery](/ags-docs/services/battery/)
  + [Bluetooth](/ags-docs/services/bluetooth/)
  + [Greetd](/ags-docs/services/greetd/)
  + [Hyprland](/ags-docs/services/hyprland/)
  + [Mpris](/ags-docs/services/mpris/)
  + [Network](/ags-docs/services/network/)
  + [Notifications](/ags-docs/services/notifications/)
  + [Power Profiles](/ags-docs/services/powerprofiles/)
  + [System Tray](/ags-docs/services/systemtray/)
* Builtin Widgets

  + [Window](/ags-docs/config/widgets#window)
  + [Box](/ags-docs/config/widgets#box)
  + [Button](/ags-docs/config/widgets#button)
  + [Calendar](/ags-docs/config/widgets#calendar)
  + [CenterBox](/ags-docs/config/widgets#centerbox)
  + [CircularProgress](/ags-docs/config/widgets#circularprogress)
  + [ColorButton](/ags-docs/config/widgets#colorbutton)
  + [DrawingArea](/ags-docs/config/widgets#drawingarea)
  + [Entry](/ags-docs/config/widgets#entry)
  + [EventBox](/ags-docs/config/widgets#eventbox)
  + [FileChooserButton](/ags-docs/config/widgets#filechooserbutton)
  + [Fixed](/ags-docs/config/widgets#fixed)
  + [FlowBox](/ags-docs/config/widgets#flowbox)
  + [FontButton](/ags-docs/config/widgets#fontbutton)
  + [Icon](/ags-docs/config/widgets#icon)
  + [Label](/ags-docs/config/widgets#label)
  + [LevelBar](/ags-docs/config/widgets#levelbar)
  + [ListBox](/ags-docs/config/widgets#listbox)
  + [Menu](/ags-docs/config/widgets#menu)
  + [MenuBar](/ags-docs/config/widgets#menubar)
  + [MenuItem](/ags-docs/config/widgets#menuitem)
  + [OverLay](/ags-docs/config/widgets#overlay)
  + [ProgressBar](/ags-docs/config/widgets#progressbar)
  + [Revealer](/ags-docs/config/widgets#revealer)
  + [Scrollable](/ags-docs/config/widgets#scrollable)
  + [Separator](/ags-docs/config/widgets#separator)
  + [Slider](/ags-docs/config/widgets#slider)
  + [SpinButton](/ags-docs/config/widgets#spinbutton)
  + [Spinner](/ags-docs/config/widgets#spinner)
  + [Stack](/ags-docs/config/widgets#stack)
  + [Switch](/ags-docs/config/widgets#switch)
  + [ToggleButton](/ags-docs/config/widgets#togglebutton)

[GitHub](https://github.com/Aylur/ags) [Discord](https://discord.gg/CXQpHwDuhY)

  Select theme   DarkLightAuto

On this page

* [Overview](#_top)
* [Semicolons](#semicolons)
* [Logging, printing](#logging-printing)
* [Variables](#variables)
* [Flow control](#flow-control)
* [Functions](#functions)
* [Destructuring](#destructuring)
* [Modules](#modules)
* [String formatting](#string-formatting)

## On this page

* [Overview](#_top)
* [Semicolons](#semicolons)
* [Logging, printing](#logging-printing)
* [Variables](#variables)
* [Flow control](#flow-control)
* [Functions](#functions)
* [Destructuring](#destructuring)
* [Modules](#modules)
* [String formatting](#string-formatting)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# JavaScript

If you don’t know any JavaScript, this is a quick 5 minute course explaining most things you will need to understand.

# Docs

If you need a more in depth explanation you can look up anything on [developer.mozilla.org](https://developer.mozilla.org/en-US/), everything except for the [dom](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) will apply to gjs.

## Semicolons

Semicolons are optional, as there is [automatic semicolon insertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)

## Logging, printing

```
// in gjs and other runtimes

console.log('hello')

// in gjs

print('hello')
```

## Variables

To define a variable use the `let` or `const` keyword

```
let someString = 'some-string'

let someNumber = 69

let someBool = true

const array = ['string', 69, true]

const object = {

key: 'value',

'key-word': 'value',

}
```

## Flow control

if else

```
let i = 0

if (i < 0) {

print('its negative')

}

else if(i > 0) {

print('its more than 0')

}

else {

print('its 0')

}
```

while loop

```
let i = 0

while (i < 5) {

print(i)

i++;

}
```

for loop

```
for (let i = 0; i < 5; i++) {

print(i)

}
```

for of loop

```
const array = [0, 1, 2, 3, 4]

for (const item of array) {

print(item)

}
```

## Functions

There are multiple ways to define functions, with the `function` keyword or with [fat arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions), also know as lambda functions in other languages

named function

```
function fn(param1, param2) {

print(param1, param2)

}
```

nameless function assigned to a const variable

```
const fn = function(param1, param2) {

print(param1, param2)

}
```

fat arrow function a.k.a lambda

```
const fn = (param1, param2) => {

print(param1, param2)

}
```

invoke all of them like any other function

```
fn('hi', 'mom')
```

default parameter value

```
function fn(param1, param2 = 'hello') {

print(param1, param2)

}

fn() // undefined, hello
```

## Destructuring

arrays

```
const array = [1, 2, 3, 4, 5]

const [elem1, elem2, ...rest] = array

print(elem1, elem2, rest) // 1, 2, [3, 4, 5]
```

objects

```
const object = {one: 1, two: 2, three: 3, four: 4}

const {one, two, ...rest} = object

print(one, two, rest) // 1, 2, {three: 3, four: 4}
```

useful in function definitions

```
function fn({ one, two }) {

print(one, two)

}

fn({ one: 'hello', two: 'mom' }) // hello, mom

fn() // throws error because undefined can't be destructed
```

## Modules

exporting

```
export default 'hello'

export const string = 'mom'

export function fn(...params) {

print(...params)

}
```

importing

```
import hi, { string, fn } from './path-to-file.js'

fn(hi, string) // hello, mom
```

## String formatting

use `backticks` and `${}`

```
const string = 'mom'

const formatted = `hi ${string}`

print(formatted) // hi mom
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/javascript.md)

[Previous
 Installation](/ags-docs/config/installation)   [Next
 First Widgets](/ags-docs/config/first-widgets)
