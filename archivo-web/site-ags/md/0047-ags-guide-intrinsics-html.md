---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/intrinsics.html"
title: "Builtin Intrinsic Elements | AGS"
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

# Builtin Intrinsic Elements [​](#builtin-intrinsic-elements)

These are just Gtk widgets which can be used without explicitly importing. For example `<box />` and `<Gtk.Box />` are exactly the same thing.

## Gtk4 [​](#gtk4)

### box [​](#box)

[Gtk.Box](https://docs.gtk.org/gtk4/class.Box.html)

tsx

```
<box orientation={Gtk.Orientation.HORIZONTAL}>
  <Child />
  <Child />
  <Child />
</box>
```

### button [​](#button)

[Gtk.Button](https://docs.gtk.org/gtk4/class.Button.html)

tsx

```
<button onClicked={() => print("clicked")}>
  <Child />
</button>
```

### centerbox [​](#centerbox)

[Gtk.CenterBox](https://docs.gtk.org/gtk4/class.CenterBox.html)

tsx

```
<centerbox orientation={Gtk.Orientation.HORIZONTAL}>
  <Child $type="start" />
  <Child $type="center" />
  <Child $type="end" />
</centerbox>
```

### drawingarea [​](#drawingarea)

[Gtk.DrawingArea](https://docs.gtk.org/gtk4/class.DrawingArea.html)

tsx

```
<drawingarea
  $={(self) =>
    self.set_draw_func((area, cr, width, height) => {
      //
    })
  }
/>
```

### entry [​](#entry)

[Gtk.Entry](https://docs.gtk.org/gtk4/class.Entry.html)

tsx

```
<entry
  placeholderText="Start typing..."
  text=""
  onNotifyText={({ text }) => print(text)}
/>
```

### image [​](#image)

[Gtk.Image](https://docs.gtk.org/gtk4/class.Image.html)

tsx

```
<image
  file="/path/to/file.png"
  iconName="system-search-symbolic"
  pixelSize={16}
/>
```

### label [​](#label)

[Gtk.Label](https://docs.gtk.org/gtk4/class.Label.html)

tsx

```
<label
  label="<span foreground='blue'>text</span>"
  useMarkup
  wrap
  ellipsize={Pango.EllipsizeMode.END}
/>
```

### levelbar [​](#levelbar)

[Gtk.LevelBar](https://docs.gtk.org/gtk4/class.LevelBar.html)

tsx

```
<levelbar
  orientation={Gtk.Orientation.HORIZONTAL}
  widthRequest={200}
  value={0.5}
/>
```

### menubutton [​](#menubutton)

[Gtk.MenuButton](https://docs.gtk.org/gtk4/class.MenuButton.html)

tsx

```
<menubutton>
  button content
  <popover>popover content</popover>
</menubutton>
```

### overlay [​](#overlay)

[Gtk.Overlay](https://docs.gtk.org/gtk4/class.Overlay.html)

tsx

```
<overlay>
  <Child />
  <Child $type="overlay" />
  <Child $type="overlay" />
</overlay>
```

### revealer [​](#revealer)

[Gtk.Revealer](https://docs.gtk.org/gtk4/class.Revealer.html)

tsx

```
<revealer
  transitionType={Gtk.RevealerTransitionType.SLIDE_RIGHT}
  revealChild={true}
  onNotifyChildRevealed={() => print("animation finished")}
>
  <Child />
</revealer>
```

### scrolledwindow [​](#scrolledwindow)

[Gtk.ScrolledWindow](https://docs.gtk.org/gtk4/class.ScrolledWindow.html)

tsx

```
<scrolledwindow maxContentHeight={500}>
  <Child />
</scrolledwindow>
```

### slider [​](#slider)

[Astal.Slider](https://aylur.github.io/libastal/astal4/class.Slider.html)

tsx

```
<slider
  value={0.5}
  min={0}
  max={1}
  onChangeValue={({ value }) => print(value)}
/>
```

### stack [​](#stack)

[Gtk.Stack](https://docs.gtk.org/gtk4/class.Stack.html)

tsx

```
<stack visibleChildName="child2">
  <Child $type="named" name="child1" />
  <Child $type="named" name="child2" />
</stack>
```

### switch [​](#switch)

[Gtk.Switch](https://docs.gtk.org/gtk4/class.Switch.html)

tsx

```
<switch active={true} onNotifyActive={({ active }) => print(active)} />
```

### togglebutton [​](#togglebutton)

[Gtk.ToggleButton](https://docs.gtk.org/gtk4/class.ToggleButton.html)

tsx

```
<togglebutton active={true} onToggled={({ active }) => print(active)} />
```

### window [​](#window)

[Astal.Window](https://aylur.github.io/libastal/astal4/class.Window.html)

tsx

```
<window
  visible
  namespace="bar"
  class="Bar"
  monitor={0}
  exclusivity={Astal.Exclusivity.EXCLUSIVE}
  keymode={Astal.Keymode.ON_DEMAND}
  anchor={
    Astal.WindowAnchor.TOP | Astal.WindowAnchor.LEFT | Astal.WindowAnchor.RIGHT
  }
/>
```

WARNING

In Gtk4 windows are invisible by default, so don't forget to pass `visible`.

## Gtk3 [​](#gtk3)

### box [​](#box-1)

[Gtk.Box](https://docs.gtk.org/gtk3/class.Box.html)

tsx

```
<box orientation={Gtk.Orientation.HORIZONTAL}>
  <Child />
  <Child />
  <Child />
</box>
```

### button [​](#button-1)

[Gtk.Button](https://docs.gtk.org/gtk3/class.Button.html)

tsx

```
<button onClicked={() => print("clicked")}>
  <Child />
</button>
```

### centerbox [​](#centerbox-1)

[Astal.CenterBox](https://aylur.github.io/libastal/astal3/class.CenterBox.html)

tsx

```
<centerbox orientation={Gtk.Orientation.HORIZONTAL}>
  <Child $type="start" />
  <Child $type="center" />
  <Child $type="end" />
</centerbox>
```

### circularprogress [​](#circularprogress)

[Astal.CircularProgress](https://aylur.github.io/libastal/astal3/class.CircularProgress.html)

tsx

```
<circularprogress value={0.5} startAt={0.75} endAt={0.75}>
  <icon />
</circularprogress>
```

css

```
circularprogress {
  color: green;
  background-color: black;
  font-size: 6px;
  margin: 2px;
  min-width: 32px;
}
```

### drawingarea [​](#drawingarea-1)

[Gtk.DrawingArea](https://docs.gtk.org/gtk3/class.DrawingArea.html)

tsx

```
<drawingarea
  onDraw={(self, cr) => {
    //
  }}
/>
```

### entry [​](#entry-1)

[Gtk.Entry](https://docs.gtk.org/gtk3/class.Entry.html)

tsx

```
<entry
  onChanged={({ text }) => print("text changed", text)}
  onActivate={({ text }) => print("enter", text)}
/>
```

### eventbox [​](#eventbox)

[Astal.EventBox](https://aylur.github.io/libastal/astal3/class.EventBox.html)

tsx

```
<eventbox
  onClick={(_, event) => {
    print(event.modifier, event.button)
  }}
/>
```

### icon [​](#icon)

[Astal.Icon](https://aylur.github.io/libastal/astal3/class.Icon.html)

tsx

```
<icon
  // named icon or path to a file
  icon="/path/to/file.png"
  icon="missing-symbolic"
/>
```

css

```
icon {
  font-size: 16px;
}
```

### label [​](#label-1)

[Astal.Label](https://aylur.github.io/libastal/astal3/class.Label.html)

tsx

```
<label label="hello" maxWidthChars={16} wrap />
```

### levelbar [​](#levelbar-1)

[Astal.LevelBar](https://aylur.github.io/libastal/astal3/class.LevelBar.html)

tsx

```
<levelbar value={0.5} widthRequest={200} />
```

### overlay [​](#overlay-1)

[Astal.Overlay](https://aylur.github.io/libastal/astal3/class.Overlay.html)

tsx

```
<overlay>
  <Child>child</Child>
  <Child>overlay 1</Child>
</overlay>
```

### revealer [​](#revealer-1)

[Gtk.Revealer](https://docs.gtk.org/gtk3/class.Revealer.html)

tsx

```
<revealer
  transitionType={Gtk.RevealerTransitionType.SLIDE_RIGHT}
  revealChild={true}
  onNotifyChildRevealed={() => print("animation finished")}
>
  <Child />
</revealer>
```

### scrollable [​](#scrollable)

[Astal.Scrollable](https://aylur.github.io/libastal/astal3/class.Scrollable.html)

tsx

```
<scrollable heightRequest={100}>
  <Child />
</scrollable>
```

### slider [​](#slider-1)

[Astal.Slider](https://aylur.github.io/libastal/astal3/class.Slider.html)

tsx

```
<slider widthRequest={100} onDragged={({ value }) => print(value)} />
```

### stack [​](#stack-1)

[Astal.Stack](https://aylur.github.io/libastal/astal3/class.Stack.html)

tsx

```
<stack visibleChildName="child2">
  <Child name="child1" />
  <Child name="child2" />
</stack>
```

### switch [​](#switch-1)

[Gtk.Switch](https://docs.gtk.org/gtk3/class.Switch.html)

tsx

```
<switch active={true} onNotifyActive={({ active }) => print(active)} />
```

### overlay [​](#overlay-2)

[Astal.Overlay](https://aylur.github.io/libastal/astal3/class.Overlay.html)

tsx

```
<overlay>
  <Child>child</Child>
  <Child>overlay 1</Child>
  <Child>overlay 1</Child>
</overlay>
```

### togglebutton [​](#togglebutton-1)

[Gtk.ToggleButton](https://docs.gtk.org/gtk4/class.ToggleButton.html)

tsx

```
<togglebutton active={true} onToggled={({ active }) => print(active)} />
```

### window [​](#window-1)

[Astal.Window](https://aylur.github.io/libastal/astal4/class.Window.html)

tsx

```
<window
  namespace="bar"
  class="Bar"
  monitor={0}
  exclusivity={Astal.Exclusivity.EXCLUSIVE}
  keymode={Astal.Keymode.ON_DEMAND}
  anchor={
    Astal.WindowAnchor.TOP | Astal.WindowAnchor.LEFT | Astal.WindowAnchor.RIGHT
  }
/>
```

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/intrinsics.md)

Last updated:

Pager

[Previous pageResources](/ags/guide/resources.html)

[Next pageFAQ](/ags/guide/faq.html)

Released under the GPL v3.0 License

Logo is created by VDawg
