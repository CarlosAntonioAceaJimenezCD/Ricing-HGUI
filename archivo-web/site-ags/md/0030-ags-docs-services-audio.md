---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/audio"
title: "Audio | AGS Wiki"
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
  + [Stream](#stream)
* [Example Widgets](#example-widgets)
  + [Volume Slider](#volume-slider)
  + [Indicator Icon](#indicator-icon)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
  + [Stream](#stream)
* [Example Widgets](#example-widgets)
  + [Volume Slider](#volume-slider)
  + [Indicator Icon](#indicator-icon)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Audio

Note

Gvc, the backend used for audio uses pulseaudio, so make sure `pipewire-pulse` is installed if using pipewire

## signals

* `speaker-changed` default speaker’s state changed
* `microphone-changed` default microphone’ state changed
* `stream-added`: `(id: number)` new stream appeared
* `stream-removed`: `(id: number)` stream disappeared

## properties

* `control`: [Gvc.MixerControl](https://gjs-docs.gnome.org/gvc10~1.0/gvc.mixercontrol)
* `speaker`: `Stream` writable
* `microphone`: `Stream` writable
* `apps`: `Stream[]` list of streams filtered by sink inputs
* `recorders`: `Stream[]` list of streams filtered by source outputs
* `speakers`: `Stream[]` list of streams filtered by sinks
* `microphones`: `Stream[]` list of streams filtered by sources

## methods

* `getStream`: `(id: number) => Stream`

### Stream

* `stream` [Gvc.MixerStream](https://gjs-docs.gnome.org/gvc10~1.0/gvc.mixerstream) the wrapped stream object
* `name`: `string`
* `application_id`: `string|null`
* `description`: `string|null`
* `icon-name`: `string`
* `id`: `number`
* `is-muted`: `boolean` this returns if volume is 0, setting this to true sets volume to 0. If you want the actual `is-muted`, you can use `Stream.stream.isMuted`
* `volume`: `number`: writable, between 0 and 1

## Example Widgets

### Volume Slider

```
const audio = await Service.import('audio')

/** @param {'speaker' | 'microphone'} type */

const VolumeSlider = (type = 'speaker') => Widget.Slider({

hexpand: true,

drawValue: false,

onChange: ({ value }) => audio[type].volume = value,

value: audio[type].bind('volume'),

})

const speakerSlider = VolumeSlider('speaker')

const micSlider = VolumeSlider('microphone')
```

### Indicator Icon

```
const audio = await Service.import('audio')

const volumeIndicator = Widget.Button({

on_clicked: () => audio.speaker.is_muted = !audio.speaker.is_muted,

child: Widget.Icon().hook(audio.speaker, self => {

const vol = audio.speaker.volume * 100;

const icon = [

[101, 'overamplified'],

[67, 'high'],

[34, 'medium'],

[1, 'low'],

[0, 'muted'],

].find(([threshold]) => threshold <= vol)?.[1];

self.icon = `audio-volume-${icon}-symbolic`;

self.tooltip_text = `Volume ${Math.floor(vol)}%`;

}),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/audio.md)

[Previous
 Applications](/ags-docs/services/applications/)   [Next
 Backlight](/ags-docs/services/backlight/)
