---
type: source
source_type: webpage
url: "https://wiki.hypr.land/configuring/extra/virtual-gpu/"
title: "Virtual GPU – Hyprland Wiki"
fetched_at: 2026-11-22T01:14:36+00:00
fetcher: "curl + markitdown"
site: "wiki.hypr.land"
---
[Skip to content](#content)

[![Logo](/favicon.svg)
![Dark Logo](/favicon-dark.svg)
Hyprland Wiki](/)[Latest git](/version-selector/)[Wiki](/)[Home](https://hypr.land/)[Showcase](https://hypr.land/hall_of_fame)[News](https://hypr.land/news)Search...
`CTRL K`
[GitHub](https://github.com/hyprwm/Hyprland "GitHub")

* [Wiki](/)

  + [Version selector ⚙️](/version-selector/)
  + [Getting Started](/getting-started/)

    - [Installation](/getting-started/installation/)
    - [Master tutorial](/getting-started/master-tutorial/)
    - [Preconfigured setups](/getting-started/preconfigured-setups/)
  + [Configuring](/configuring/)

    - [Naming conventions](/configuring/naming-conventions/)
    - [Selectors](/configuring/selectors/)
    - [Core](/configuring/core/)

      * [Monitors](/configuring/core/monitors/)
      * [Config options](/configuring/core/config-options/)
      * [Devices](/configuring/core/devices/)
      * [Dispatchers](/configuring/core/dispatchers/)
      * [Binds](/configuring/core/binds/)
      * [Rules](/configuring/core/rules/)
      * [Environment variables](/configuring/core/environment-variables/)
      * [Animations](/configuring/core/animations/)
      * [Autostart](/configuring/core/autostart/)
      * [Advanced configuration](/configuring/core/advanced-configuration/)
    - [Layouts](/configuring/layouts/)

      * [Dwindle layout](/configuring/layouts/dwindle-layout/)
      * [Scrolling layout](/configuring/layouts/scrolling-layout/)
      * [Master layout](/configuring/layouts/master-layout/)
      * [Monocle layout](/configuring/layouts/monocle-layout/)
      * [Custom layouts](/configuring/layouts/custom-layouts/)
    - [Extra](/configuring/extra/)

      * [Multi-GPU](/configuring/extra/multi-gpu/)
      * [Virtual GPU](/configuring/extra/virtual-gpu/)

        + [General](#general)
        + [Running Hyprland on vGPU](#running-hyprland-on-vgpu)
        + [Accessing the virtual display](#accessing-the-virtual-display)
      * [Performance](/configuring/extra/performance/)
      * [Tearing](/configuring/extra/tearing/)
      * [Xwayland](/configuring/extra/xwayland/)
      * [Systemd](/configuring/extra/systemd/)
    - [Lua code snippets](/configuring/code-snippets/)
  + [Hypr Ecosystem](/hypr-ecosystem/)

    - [User apps and utilities](/hypr-ecosystem/user/)

      * [hyprpaper](/hypr-ecosystem/user/hyprpaper/)
      * [hyprpicker](/hypr-ecosystem/user/hyprpicker/)
      * [hyprlauncher](/hypr-ecosystem/user/hyprlauncher/)
      * [hypridle](/hypr-ecosystem/user/hypridle/)
      * [hyprlock](/hypr-ecosystem/user/hyprlock/)
      * [xdg-desktop-portal-hyprland](/hypr-ecosystem/user/xdg-desktop-portal-hyprland/)
      * [hyprsysteminfo](/hypr-ecosystem/user/hyprsysteminfo/)
      * [hyprsunset](/hypr-ecosystem/user/hyprsunset/)
      * [hyprpolkitagent](/hypr-ecosystem/user/hyprpolkitagent/)
      * [hyprland-qt-support](/hypr-ecosystem/user/hyprland-qt-support/)
      * [hyprqt6engine](/hypr-ecosystem/user/hyprqt6engine/)
      * [hyprpwcenter](/hypr-ecosystem/user/hyprpwcenter/)
      * [hyprshutdown](/hypr-ecosystem/user/hyprshutdown/)
      * [hyprtoolkit (user docs)](/hypr-ecosystem/user/hyprtoolkit/)
      * [hyprcursor](/hypr-ecosystem/user/hyprcursor/)
    - [Developer libs and toolkits](/hypr-ecosystem/dev/)

      * [aquamarine](/hypr-ecosystem/dev/aquamarine/)
      * [hyprgraphics](/hypr-ecosystem/dev/hyprgraphics/)
      * [hyprland-guiutils](/hypr-ecosystem/dev/hyprland-guiutils/)
      * [hyprlang](/hypr-ecosystem/dev/hyprlang/)
      * [hyprtoolkit (developer docs)](/hypr-ecosystem/dev/hyprtoolkit/)
      * [hyprutils](/hypr-ecosystem/dev/hyprutils/)
      * [hyprwayland-scanner](/hypr-ecosystem/dev/hyprwayland-scanner/)
  + [Hyprland plugins](/hyprland-plugins/)

    - [Using plugins](/hyprland-plugins/using-plugins/)
    - [Development](/hyprland-plugins/development/)

      * [Getting started](/hyprland-plugins/development/getting-started/)
      * [Plugin guidelines](/hyprland-plugins/development/plugin-guidelines/)
      * [Advanced](/hyprland-plugins/development/advanced/)
  + [Useful utilities](/useful-utilities/)

    - [Must-have](/useful-utilities/must-have/)
    - [Status bars](/useful-utilities/status-bars/)
    - [Wallpapers](/useful-utilities/wallpapers/)
    - [Screen sharing](/useful-utilities/screen-sharing/)
    - [Screenshots and recording](/useful-utilities/screenshots-and-recording/)
    - [App launchers](/useful-utilities/app-launchers/)
    - [App clients](/useful-utilities/app-clients/)
    - [Phone connect](/useful-utilities/phone-connect/)
    - [Color pickers](/useful-utilities/color-pickers/)
    - [Clipboard managers](/useful-utilities/clipboard-managers/)
    - [File managers](/useful-utilities/file-managers/)
    - [Other](/useful-utilities/other/)
    - [Hypr ecosystem](/useful-utilities/hypr-ecosystem/)
    - [UWSM](/useful-utilities/uwsm/)
  + [Nix](/nix/)

    - [Hyprland on any distro using Nix](/nix/hyprland-on-any-distro-using-nix/)
    - [Hyprland on NixOS](/nix/installing-hyprland-on-nixos/)
    - [Configuring Hyprland with Hjem](/nix/configuring-hyprland-with-hjem/)
    - [Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/)
    - [Cachix](/nix/cachix/)
    - [Advanced](/nix/advanced/)
    - [Contributing and Debugging](/nix/contributing-and-debugging/)
  + [NVIDIA](/nvidia/)
  + [IPC](/ipc/)
  + [Crashes and Bugs](/crashes-and-bugs/)
  + [FAQ](/faq/)
  + [Community](/community/)
  + [Contributing and debugging](/contributing-and-debugging/)

    - [Wiki writing guidelines](/contributing-and-debugging/wiki-guidelines/)
    - [Issue guidelines](/contributing-and-debugging/issue-guidelines/)
    - [PR guidelines](/contributing-and-debugging/pr-guidelines/)
    - [Tests](/contributing-and-debugging/tests/)
    - [Translations](/contributing-and-debugging/translations/)
* [Home](https://hypr.land/)
* [Showcase](https://hypr.land/hall_of_fame)
* [News](https://hypr.land/news)

* [Version selector ⚙️](/version-selector/)
* [Getting Started](/getting-started/)

  + [Installation](/getting-started/installation/)
  + [Master tutorial](/getting-started/master-tutorial/)
  + [Preconfigured setups](/getting-started/preconfigured-setups/)
* [Configuring](/configuring/)

  + [Naming conventions](/configuring/naming-conventions/)
  + [Selectors](/configuring/selectors/)
  + [Core](/configuring/core/)

    - [Monitors](/configuring/core/monitors/)

      * [Output selection](/configuring/core/monitors/output-selection/)
      * [Positioning](/configuring/core/monitors/positioning/)
      * [Monitor modes](/configuring/core/monitors/modes/)
      * [Colors and colorspaces](/configuring/core/monitors/colors/)
    - [Config options](/configuring/core/config-options/)
    - [Devices](/configuring/core/devices/)
    - [Dispatchers](/configuring/core/dispatchers/)
    - [Binds](/configuring/core/binds/)

      * [Flags](/configuring/core/binds/flags/)
      * [Keyboard layouts](/configuring/core/binds/keyboard-layouts/)
      * [Device binds](/configuring/core/binds/devices/)
      * [Submaps](/configuring/core/binds/submaps/)
      * [Global hotkeys and binds](/configuring/core/binds/globals/)
      * [Switches](/configuring/core/binds/switches/)
      * [Gestures](/configuring/core/binds/gestures/)
    - [Rules](/configuring/core/rules/)

      * [Window Rules](/configuring/core/rules/window-rules/)
      * [Workspace Rules](/configuring/core/rules/workspace-rules/)
      * [Layer rules](/configuring/core/rules/layer-rules/)
    - [Environment variables](/configuring/core/environment-variables/)
    - [Animations](/configuring/core/animations/)
    - [Autostart](/configuring/core/autostart/)
    - [Advanced configuration](/configuring/core/advanced-configuration/)

      * [Lua events](/configuring/core/advanced-configuration/events/)
      * [Lua utilities](/configuring/core/advanced-configuration/lua-utilities/)
      * [Using hyprctl](/configuring/core/advanced-configuration/using-hyprctl/)
      * [Notifications](/configuring/core/advanced-configuration/notifications/)
      * [Permissions](/configuring/core/advanced-configuration/permissions/)
  + [Layouts](/configuring/layouts/)

    - [Dwindle layout](/configuring/layouts/dwindle-layout/)
    - [Scrolling layout](/configuring/layouts/scrolling-layout/)
    - [Master layout](/configuring/layouts/master-layout/)
    - [Monocle layout](/configuring/layouts/monocle-layout/)
    - [Custom layouts](/configuring/layouts/custom-layouts/)
  + [Extra](/configuring/extra/)

    - [Multi-GPU](/configuring/extra/multi-gpu/)
    - [Virtual GPU](/configuring/extra/virtual-gpu/)
    - [Performance](/configuring/extra/performance/)
    - [Tearing](/configuring/extra/tearing/)
    - [Xwayland](/configuring/extra/xwayland/)
    - [Systemd](/configuring/extra/systemd/)
  + [Lua code snippets](/configuring/code-snippets/)
* [Hypr Ecosystem](/hypr-ecosystem/)

  + [User apps and utilities](/hypr-ecosystem/user/)

    - [hyprpaper](/hypr-ecosystem/user/hyprpaper/)
    - [hyprpicker](/hypr-ecosystem/user/hyprpicker/)
    - [hyprlauncher](/hypr-ecosystem/user/hyprlauncher/)
    - [hypridle](/hypr-ecosystem/user/hypridle/)
    - [hyprlock](/hypr-ecosystem/user/hyprlock/)
    - [xdg-desktop-portal-hyprland](/hypr-ecosystem/user/xdg-desktop-portal-hyprland/)
    - [hyprsysteminfo](/hypr-ecosystem/user/hyprsysteminfo/)
    - [hyprsunset](/hypr-ecosystem/user/hyprsunset/)
    - [hyprpolkitagent](/hypr-ecosystem/user/hyprpolkitagent/)
    - [hyprland-qt-support](/hypr-ecosystem/user/hyprland-qt-support/)
    - [hyprqt6engine](/hypr-ecosystem/user/hyprqt6engine/)
    - [hyprpwcenter](/hypr-ecosystem/user/hyprpwcenter/)
    - [hyprshutdown](/hypr-ecosystem/user/hyprshutdown/)
    - [hyprtoolkit (user docs)](/hypr-ecosystem/user/hyprtoolkit/)
    - [hyprcursor](/hypr-ecosystem/user/hyprcursor/)
  + [Developer libs and toolkits](/hypr-ecosystem/dev/)

    - [aquamarine](/hypr-ecosystem/dev/aquamarine/)
    - [hyprgraphics](/hypr-ecosystem/dev/hyprgraphics/)
    - [hyprland-guiutils](/hypr-ecosystem/dev/hyprland-guiutils/)
    - [hyprlang](/hypr-ecosystem/dev/hyprlang/)
    - [hyprtoolkit (developer docs)](/hypr-ecosystem/dev/hyprtoolkit/)
    - [hyprutils](/hypr-ecosystem/dev/hyprutils/)
    - [hyprwayland-scanner](/hypr-ecosystem/dev/hyprwayland-scanner/)
* [Hyprland plugins](/hyprland-plugins/)

  + [Using plugins](/hyprland-plugins/using-plugins/)
  + [Development](/hyprland-plugins/development/)

    - [Getting started](/hyprland-plugins/development/getting-started/)
    - [Plugin guidelines](/hyprland-plugins/development/plugin-guidelines/)
    - [Advanced](/hyprland-plugins/development/advanced/)
* [Useful utilities](/useful-utilities/)

  + [Must-have](/useful-utilities/must-have/)
  + [Status bars](/useful-utilities/status-bars/)
  + [Wallpapers](/useful-utilities/wallpapers/)
  + [Screen sharing](/useful-utilities/screen-sharing/)
  + [Screenshots and recording](/useful-utilities/screenshots-and-recording/)
  + [App launchers](/useful-utilities/app-launchers/)
  + [App clients](/useful-utilities/app-clients/)
  + [Phone connect](/useful-utilities/phone-connect/)
  + [Color pickers](/useful-utilities/color-pickers/)
  + [Clipboard managers](/useful-utilities/clipboard-managers/)
  + [File managers](/useful-utilities/file-managers/)
  + [Other](/useful-utilities/other/)
  + [Hypr ecosystem](/useful-utilities/hypr-ecosystem/)
  + [UWSM](/useful-utilities/uwsm/)
* [Nix](/nix/)

  + [Hyprland on any distro using Nix](/nix/hyprland-on-any-distro-using-nix/)
  + [Hyprland on NixOS](/nix/installing-hyprland-on-nixos/)
  + [Configuring Hyprland with Hjem](/nix/configuring-hyprland-with-hjem/)
  + [Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/)
  + [Cachix](/nix/cachix/)
  + [Advanced](/nix/advanced/)
  + [Contributing and Debugging](/nix/contributing-and-debugging/)
* [NVIDIA](/nvidia/)
* [IPC](/ipc/)
* [Crashes and Bugs](/crashes-and-bugs/)
* [FAQ](/faq/)
* [Community](/community/)
* [Contributing and debugging](/contributing-and-debugging/)

  + [Wiki writing guidelines](/contributing-and-debugging/wiki-guidelines/)
  + [Issue guidelines](/contributing-and-debugging/issue-guidelines/)
  + [PR guidelines](/contributing-and-debugging/pr-guidelines/)
  + [Tests](/contributing-and-debugging/tests/)
  + [Translations](/contributing-and-debugging/translations/)

LightDark
System

* Light
* Dark
* System

On this page

* [General](#general)
* [Running Hyprland on vGPU](#running-hyprland-on-vgpu)
* [Usage of both a GPU and vGPU](#usage-of-both-a-gpu-and-vgpu)
* [Accessing the virtual display](#accessing-the-virtual-display)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/configuring/extra/virtual-gpu.md)

Scroll to top

[Configuring](/configuring/)

[Extra](/configuring/extra/)

Virtual GPU

# Virtual GPU

## General

If you happen to be in possession of a GPU that falls into one of these categories:

* Intel Arc Pro card
* Intel laptop integrated graphics
* NVIDIA Workstation or Server card
* NVIDIA RTX 2000 series card
* AMD Radeon Instinct card

It is very likely that your graphics card supports virtual partitioning, either through the use of mediated devices or SR-IOV.
The means of enabling this partitioning is beyond the scope of this wiki, and is very different between vendors.

As an example, once partitioning is enabled, this is what an RTX A5000 card will create:

```
# lspci -d 10de:
01:00.0 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:00.4 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:00.5 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:00.6 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:00.7 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.0 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.1 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.2 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.3 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.4 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.5 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.6 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:01.7 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.0 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.1 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.2 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.3 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.4 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.5 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.6 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:02.7 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:03.0 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:03.1 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:03.2 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
01:03.3 3D controller: NVIDIA Corporation GA102GL [RTX A5000] (rev a1)
```

You may want to pass through one of these virtual GPU partitions, also called vGPU, in a virtual machine to run Hyprland with hardware acceleration.

Note

The following procedures **do not concern paravirtualized drivers like Virtio-GPU**.

Virtio-GPU is not a virtual partition of your hardware device, but an entirely software-emulated device that forwards its duty to your host GPU.
Having been developed for this purpose, it provides an emulated screen output.
Therefore you can use Hyprland normally with it, with no extra effort required.

## Running Hyprland on vGPU

Hyprland requires by default that your graphics card has **at least one display output**.

However, for all vendors, vGPUs are render-only cards and have no emulated output on Linux.
That is because they are targeting VDI infrastructures, 3D rendering, encoding and compute use cases that are all remote.
This is also suggested by their prefix “3D controller”, instead of “VGA compatible controller”.

**To allow Hyprland to run** on a graphics card **with no output, you must enable the** `AQ_NO_KMS_REQUIREMENT` environment flag when running Hyprland:

```
hl.env("AQ_NO_KMS_REQUIREMENT", "1")
```

### Usage of both a GPU and vGPU

Warning

Users of QEMU hypervisor that are both doing a vGPU passthrough and exposing a Virtio-GPU device in their virtual machine are concerned by this section.

Most hardware and paravirtualized drivers will expose the same graphics card twice under the `/dev/dri` directory.
One node will be globally accessible and provide render capabilities, while the other will be privileged and expose one or more display outputs.

```
$ ls -lh /dev/dri/
total 0
drwxr-xr-x  2 root root         80 Apr 20 07:01 by-path/
crw-rw----+ 1 root video  226,   1 Apr 20 07:01 card1           # KMS card with outputs
crw-rw-rw-  1 root render 226, 128 Apr 20 07:01 renderD128      # DRM card, render-only
```

Hyprland will, by default, only select nodes on the system with display outputs and ignore the `render` node.
But with `AQ_NO_KMS_REQUIREMENT` lifting this need, the `render` node becomes a suitable candidate.

If you happen to be using both a virtual GPU and a hardware GPU on the same virtual machine, **you must set the `AQ_DRM_DEVICES` flag**.
This flag is described and explained in [Multi-GPU](../multi-gpu):

```
hl.env("AQ_NO_KMS_REQUIREMENT", "1")
hl.env("AQ_DRM_DEVICES", "/dev/dri/card0:/dev/dri/card1")
```

In practice, there is no guaranteed order of which node will be used as the primary renderer in a virtual machine.
It is important that you manually decide the priority.

Warning

Some hypervisors can expose PCI topologies that can be understood differently at each start.
To be sure of setting the correct node, refer to [Multi-GPU section on consistent device paths](../multi-gpu#creating-consistent-device-paths-for-specific-cards) for renaming the nodes and making your configuration consistent across reboots.

## Accessing the virtual display

When Hyprland starts without any display output, it will initialize a headless output called `HEADLESS-0` with a `1920x1080@60Hz` resolution and framerate, that you can alter in your usual `hyprland.lua` file.

You have to use a remote desktop server, supporting the wlroots capture protocol, for accessing the display and interacting with Hyprland.

The following servers are known to be supported:

* [Sunshine/Moonlight](https://app.lizardbyte.dev/Sunshine/)
* [Apollo/Artemis(Moonlight Noir)](https://github.com/ClassicOldSong/Apollo)
* [Wayvnc](https://github.com/any1/wayvnc)

Once you start Hyprland, you can start your server remotely using `hyprctl` on the guest (See [Using hyprctl](../../core/advanced-configuration/using-hyprctl))

```
hyprctl --instance 0 eval 'hl.exec_cmd("Sunshine")'
```

The remote display server should be running below the Hyprland process to inherit all its environment variables.
Otherwise it will not find your headless display.

If everything is configured and working correctly, you can set your server in your `hyprland.lua` file to be autostarted (see [Autostart](../../core/autostart)).
For example:

```
hl.on("hyprland.start", function()
    hl.exec_cmd("Sunshine")
end)
```

Congratulations on obtaining your very own virtual Hyprland desktop.

Last updated on November 20, 2026

[Multi-GPU](/configuring/extra/multi-gpu/ "Multi-GPU")[Performance](/configuring/extra/performance/ "Performance")

ESC

No results found.
