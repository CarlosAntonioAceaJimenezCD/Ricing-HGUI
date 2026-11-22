---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/first-widgets.html"
title: "First Widgets | AGS"
fetched_at: 2026-11-22T06:24:53+00:00
fetcher: "curl + markitdown"
site: "aylur.github.io"
---
[Skip to content](#VPContent)

[AGS](/ags/)

Search`K`

 Main Navigation [Guide](/ags/guide/quick-start.html)

References

[Gjs Guide](https://gjs.guide/)

[Gjs References](https://gjs-docs.gnome.org/)

[Astal](https://aylur.github.io/astal/)

[Gnim](https://aylur.github.io/gnim/)

[xml version="1.0" encoding="utf-8"?](https://ko-fi.com/aylur)

Appearance

[xml version="1.0" encoding="utf-8"?](https://ko-fi.com/aylur)

Menu

Return to top

 Sidebar Navigation

[Installation](/ags/guide/install.html)

[Quick Start](/ags/guide/quick-start.html)

[First Widgets](/ags/guide/first-widgets.html)

[Theming](/ags/guide/theming.html)

[App and CLI](/ags/guide/app-cli.html)

[Utilities](/ags/guide/utilities.html)

[Resources](/ags/guide/resources.html)

[Intrinsics](/ags/guide/intrinsics.html)

[FAQ](/ags/guide/faq.html)

[Examples](/ags/guide/examples.html)

[Nix](/ags/guide/nix.html)

[Migration Guide](/ags/guide/migration-guide.html)

On this page

# First Widgets [​](#first-widgets)

On this page you will learn about the JSX syntax. To learn about it more in depth you can read the [Gnim docs](https://aylur.github.io/gnim/jsx.html).

TIP

`gnim` symbols is reexported from the `ags` module.

## Entry point of applications [​](#entry-point-of-applications)

Every application's entry point is an `app.start` invocation. `app` is a singleton instance of [Gtk.Application](https://docs.gtk.org/gtk4/class.Application.html).

ts

```
import app from "ags/gtk4/app"

app.start({
  main() {
    // you will instantiate Widgets here
    // and setup anything else if you need
  },
})
```

## Root of every shell component: Window [​](#root-of-every-shell-component-window)

Desktop Shells are composed of widgets. A widget is a piece of UI that has its own logic and style. A widget can be as small as a button or an entire bar. The top level - also known as a root - widget is always a [Window](https://aylur.github.io/libastal/astal4/class.Window.html).

tsx

```
function Bar(monitor = 0) {
  return (
    <window visible class="Bar" monitor={monitor}>
      <box>Content of the widget</box>
    </window>
  )
}

app.start({
  main() {
    Bar(0)
    Bar(1) // instantiate for each monitor
  },
})
```

IMPORTANT

In Gtk4 unlike other widgets, window widgets are not visible by default. Don't forget to explicitly make it `visible`.

## Creating and nesting widgets [​](#creating-and-nesting-widgets)

Widgets are JavaScript functions which return `GObject.Object` (usually `Gtk.Widget`) instances by using JSX expressions.

MyButton.tsx

tsx

```
function MyButton() {
  return (
    <button onClicked={(self) => console.log(self, "clicked")}>
      <label label="Click me!" />
    </button>
  )
}
```

Now that you have declared `MyButton`, you can nest it into another component.

tsx

```
function MyBar() {
  return (
    <window visible>
      <box>
        Click The button
        <MyButton />
      </box>
    </window>
  )
}
```

Notice that widgets you defined start with a capital letter `<MyButton />`. Lowercase tags are builtin [intrinsic](./intrinsics.html) widgets, while capital letter is for custom widgets.

## Displaying Data [​](#displaying-data)

JSX lets you put markup into JavaScript. Curly braces let you “escape back” into JavaScript so that you can embed some variable from your code and display it.

tsx

```
function MyWidget() {
  const label = "hello"

  return <button>{label}</button>
}
```

You can also pass JavaScript to markup attributes

tsx

```
function MyWidget() {
  const label = "hello"

  return <button label={label} />
}
```

## Conditional Rendering [​](#conditional-rendering)

You can use the same techniques as you use when writing regular JavaScript code. For example, you can use an if statement to conditionally include JSX:

tsx

```
function MyWidget() {
  let content

  if (condition) {
    content = <True />
  } else {
    content = <False />
  }

  return <box>{content}</box>
}
```

You can also inline a [conditional `?`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) (ternary) expression.

tsx

```
function MyWidget() {
  return <box>{condition ? <True /> : <False />}</box>
}
```

When you don’t need the `else` branch, you can also use a shorter [logical && syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#short-circuit_evaluation):

tsx

```
function MyWidget() {
  return <box>{condition && <True />}</box>
}
```

TIP

[falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) values are not rendered.

## Rendering lists [​](#rendering-lists)

You can use [`for` loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) or [array `map()` function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

tsx

```
function MyWidget() {
  const labels = ["label1", "label2", "label3"]

  return (
    <box>
      {labels.map((label) => (
        <label label={label} />
      ))}
    </box>
  )
}
```

## Widget signal handlers [​](#widget-signal-handlers)

You can respond to events by declaring event handler functions inside your widget:

tsx

```
import Gtk from "gi://Gtk"

function MyButton() {
  function onClicked(self: Gtk.Button) {
    console.log(self, "was clicked")
  }

  return <button onClicked={onClicked} />
}
```

TIP

Using Gtk4, you can use [EventControllers](https://docs.gtk.org/gtk4/class.EventController.html) for more complex event handling.

tsx

```
<box>
  <Gtk.GestureClick
    propagationPhase={Gtk.PropagationPhase.CAPTURE}
    button={Gdk.BUTTON_PRIMARY}
    onPressed={() => print("clicked with primary button")}
  />
</box>
```

## How properties are passed [​](#how-properties-are-passed)

Using JSX, a custom widget will always have a single object as its parameter.

ts

```
type Props = {
  myprop: string
  children?: JSX.Element | Array<JSX.Element>
}

function MyWidget({ myprop, children }: Props) {
  //
}
```

TIP

`JSX.Element` is an alias to `GObject.Object`

The `children` property is a special one which is used to pass the children given in the JSX expression.

tsx

```
// `children` prop of MyWidget is the box
return (
  <MyWidget myprop="hello">
    <box />
  </MyWidget>
)
```

tsx

```
// `children` prop of MyWidget is [box, box]
return (
  <MyWidget myprop="hello">
    <box />
    <box />
  </MyWidget>
)
```

## State management [​](#state-management)

State is managed using signals which are called [`Accessor`](https://aylur.github.io/gnim/jsx#state-management).

* with `createState` you can instantiate a writable reactive value
* with `createBinding` you can hook into GObject properties.
* with `createComputed` you can derive reactive values

State exampleGObject example

tsx

```
import { createState, createComputed } from "ags"

function Counter() {
  const [count, setCount] = createState(0)

  function increment() {
    setCount((v) => v + 1)
  }

  const label = createComputed(() => count().toString())

  return (
    <box>
      <label label={label} />
      <button onClicked={increment}>Click to increment</button>
    </box>
  )
}
```

tsx

```
import GObject, { register, property } from "ags/gobject"
import { createBinding, createComputed } from "ags"

@register()
class CounterStore extends GObject.Object {
  @property(Number) count = 0
}

function Counter() {
  const counter = new CounterStore()

  function increment() {
    counter.count += 1
  }

  const count = createBinding(count, "count")
  const label = createComputed(() => count().toString())

  return (
    <box>
      <label label={label} />
      <button onClicked={increment}>Click to increment</button>
    </box>
  )
}
```

Notice how in the `createComputed` body `count` is called as a function to track it automatically as a dependency for the derived `label` property.

TIP

There is a shorthand for `createComputed`.

ts

```
// these two lines mean and do the same thing
const label = createComputed(() => count().toString())
const label = count((c) => c.toString())
```

## Integrating external programs [​](#integrating-external-programs)

Other than the aforementioned functions to manage state, AGS provides ways to integrate CLI tools you might be already familiar with: [`createPoll`](./utilities.html#createpoll) which polls a program at each given interval and [`createSubprocess`](./utilities.html#createsubprocess) which launches a given program and monitors its standard output.

As an example let's say you want to use the `date` CLI command to get a formatted date.

tsx

```
const date = createPoll("", 1000, `bash -c "date +%H:%M"`)

return <label label={date} />
```

WARNING

Running subprocesses are relatively expensive, so always prefer to use a [library](./resources.html#astal-libraries) when available.

In reality you would use [`GLib.DateTime`](https://docs.gtk.org/glib/struct.DateTime.html) or JavaScript's [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date). In newer version of GJS (1.85.2 >=) you can also use the new [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal) JavaScript builtin.

tsx

```
const date = createPoll("", 1000, () => new Date().toString())

return <label label={date} />
```

Avoid polling when possible.

Keep in mind that polling is generally considered bad practice. You should use events and signals whenever possible which will only do operations when necessary.

## Dynamic rendering [​](#dynamic-rendering)

When you want to render based on a value, you can use the `<With>` component.

tsx

```
import { With, Accessor } from "ags"

let value: Accessor<{ member: string } | null>

return (
  <box>
    <With value={value}>
      {(value) => value && <label label={value.member} />}
    </With>
  </box>
)
```

TIP

In most cases it is better to always render the component and set its `visible` property instead. Use `<With>` in cases when you need to unpack a nullable object or when you need to access nested values.

WARNING

When the value changes and the widget is re-rendered the previous one is removed from the parent component and the new one is *appended*. Order of widgets are *not* kept so make sure to wrap `<With>` in a container to avoid it. This is due to Gtk not having a generic API on containers to sort widgets.

## Dynamic list rendering [​](#dynamic-list-rendering)

The `<For>` component let's you render based on an array dynamically. Each time the array changes it is compared with its previous state. Widgets for new items are inserted while widgets associated with removed items are removed.

tsx

```
import { For, Accessor } from "ags"

let list: Accessor<Array<any>>

return (
  <box>
    <For each={list}>
      {(item, index: Accessor<number>) => (
        <label label={index((i) => `${i}. ${item}`)} />
      )}
    </For>
  </box>
)
```

WARNING

Similarly to `<With>`, when the list changes and a new item is added it is simply **appended** to the parent. Order of widgets are not kept so make sure to wrap `<For>` in a container to avoid this.

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/first-widgets.md)

Last updated:

Pager

[Previous pageQuick Start](/ags/guide/quick-start.html)

[Next pageTheming](/ags/guide/theming.html)

Released under the GPL v3.0 License

Logo is created by VDawg
