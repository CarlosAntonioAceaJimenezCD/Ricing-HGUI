---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/mpris"
title: "Mpris | AGS Wiki"
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
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Player](#player)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widget](#example-widget)
* [Example Media Widget](#example-media-widget)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Player](#player)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widget](#example-widget)
* [Example Media Widget](#example-media-widget)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Mpris

Note

dependency: `gvfs` for cover art caching
NixOS: `services.gvfs`

Note

Not every media player supports `position`, `volume` and other functionality. Support varies from player to player.

## signals

* `changed`: emits on any state change except position change
* `player-changed`: `(busName: string)`
* `player-closed`: `(busName: string)`
* `player-added`: `(busName: string)`

## properties

* `players`: `Player[]` see below
* `cacheCoverArt`: `boolean` wether to cache `track-cover-url`, default: `true`

## methods

* `getPlayer`: `(string) => Player` returns Player that has given string in its busName

## Player

### signals

* `position`: `(position: number)` this is signaled when the position is set explicitly
* `closed`

### properties

* `bus-name`: `string` the dbus name that starts with `org.mpris.MediaPlayer2`
* `name`: `string` stripped from busName like `spotify` or `firefox`
* `identity`: `string` name of the player like `Spotify` or `Mozilla Firefox`
* `entry`: `string` .desktop entry without the extension
* `trackid`: `string`
* `track-artists`: `string[]` list of artists
* `track-title`: `string`
* `track-album`: `string`
* `track-cover-url`: `string` url to the cover art
* `cover-path`: `string` path to the cached cover art
* `metadata`: `{ [key: string]: unknown }` metadata object, see [freedesktop.org](https://www.freedesktop.org/wiki/Specifications/mpris-spec/metadata/) for known keys
* `play-back-status`: `"Playing" | "Paused" | "Stopped"`
* `can-go-next`: `boolean`
* `can-go-prev`: `boolean`
* `can-play`: `boolean`
* `shuffle-status`: `boolean | null` null if unsupported by the player
* `loop-status`: `"None" | "Track" | "Playlist" | null` null if unsupported by the player
* `volume`: `number` -1 if unsupported by the player
* `length`: `number` -1 if unsupported by the player
* `position`: `number` -1 if unsupported by the player

### methods

* `playPause`: `() => void`
* `play`: `() => void`
* `stop`: `() => void`
* `next`: `() => void`
* `previous`: `() => void`
* `shuffle`: `() => void`
* `loop`: `() => void`

## Example Widget

```
const mpris = await Service.import('mpris')

/** @param {import('types/service/mpris').MprisPlayer} player */

const Player = player => Widget.Button({

onClicked: () => player.playPause(),

child: Widget.Label().hook(player, label => {

const { track_artists, track_title } = player;

label.label = `${track_artists.join(', ')} - ${track_title}`;

}),

})

const players = Widget.Box({

children: mpris.bind('players').as(p => p.map(Player))

})
```

## [Example Media Widget](https://github.com/Aylur/ags/tree/main/example/media-widget)

![media-widget](/ags-docs/_astro/mpris.Zo6ZrunH_2q85t7.webp)

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/mpris.md)

[Previous
 Hyprland](/ags-docs/services/hyprland/)   [Next
 Network](/ags-docs/services/network/)
