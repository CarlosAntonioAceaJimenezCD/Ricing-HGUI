---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/notifications"
title: "Notifications | AGS Wiki"
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
* [Notification](#notification)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example](#example)
* [Example Notification Popups](#example-notification-popups)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Notification](#notification)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example](#example)
* [Example Notification Popups](#example-notification-popups)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Notifications

## signals

* `dismissed`: `(id: number)` notification removed from popups
* `notified`: `(id: number)` notification added to popups and notifications
* `closed`: `(id: number)` notification removed from popups and notifications

## properties

* `popupTimeout`: `number`: milliseconds, 3000 by default
* `forceTimeout`: `boolean`: Force every notifications timeout to be `popupTimeout`. false by default.
* `cacheActions`: `boolean`: Action buttons don’t work if the sender process is no longer running. So on reboot they won’t work. false by default
* `clearDelay`: `number`: milliseconds to wait after each notification closed when calling `clear`. This is to prevent crashes when its not handled by the user.
* `dnd`: `boolean`: do no disturb, it will permit the notification to be added to Notifications.popups
* `popups`: `Notification[]`
* `notifications`: `Notification[]`

## methods

* `clear`: `() => void`: removes all notifications
* `getNotification`: `(id: number) => Notification`
* `getPopup`: `(id: number) => Notification`

## Notification

### signals

* `dismissed` notification.popup became false
* `closed`
* `invoked`: `(action: string)`

### properties

* `id`: `number`
* `app-name`: `string`
* `app-entry`: `string | null` .desktop file
* `app-icon`: `string`
* `summary`: `string` title
* `body`: `string`
* `actions`: `Array<{ id: string, label: string }>`
* `urgency`: `"low" | "normal" | "critical"`
* `time`: `number` you can `GLib.DateTime.new_from_unix_local(time)`
* `image`: `string | null` path to the image
* `popup`: `boolean` whether this should show as a popup banner
* `hints`: `Record<string, GLib.Variant>` [notification hints](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html#hints), these are not cached and this returns an empty object if loaded from cache

### methods

* `dismiss` `() => void` sets popup to false
* `close` `() => void`
* `invoke` `(actionId: string) => void` invoking an action will also close the notification

## Example

```
const notifications = await Service.import("notifications")

notifications.popupTimeout = 3000;

notifications.forceTimeout = false;

notifications.cacheActions = false;

notifications.clearDelay = 100;

Widget.Label({

label: notifications.bind("notifications").as(n =>

`there are ${n.length} notifications`

)

})
```

## [Example Notification Popups](https://github.com/Aylur/ags/tree/main/example/notification-popups)

![notifs](/ags-docs/_astro/notifs.B6UA2vlH_2srmaX.webp)

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/notifications.md)

[Previous
 Network](/ags-docs/services/network/)   [Next
 Power Profiles](/ags-docs/services/powerprofiles/)
