---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/Alexays/Waybar/Module:-Umbriel.md"
title: "umbriel/layout"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/Alexays/Waybar/wiki"
---
> [!NOTE]
> This page is **auto-generated from [`man/waybar-umbriel-layout.5.scd`](https://github.com/Alexays/Waybar/blob/master/man/waybar-umbriel-layout.5.scd), [`man/waybar-umbriel-window.5.scd`](https://github.com/Alexays/Waybar/blob/master/man/waybar-umbriel-window.5.scd), [`man/waybar-umbriel-workspaces.5.scd`](https://github.com/Alexays/Waybar/blob/master/man/waybar-umbriel-workspaces.5.scd)** on the `master` branch.
> Do not edit it here — changes will be overwritten on the next sync.
> To update it, edit the man page(s) and open a PR.

# umbriel/layout

## DESCRIPTION

The **layout** module displays the layout of the active workspace on the bar's output.

Umbriel reports one of **scrolling**, **dwindle**, **master**, or **stacking** for each workspace. The module hides itself while the output has no active workspace.

## CONFIGURATION

Addressed by **umbriel/layout**

| **Option** | **Typeof** | **Default** | **Description** |
|:--:|:--:|:--:|:--:|
| **format** | string | {} | The default format, how the layout should be displayed. The positional **{}** (the default) and **{layout}** are both replaced by the current layout name. |
| **format-\<layout\>** | string | **none** | The custom format to use when a specific layout is active (for example, **format-scrolling**, **format-dwindle**, **format-master**, or **format-stacking**). Keys use Umbriel's lowercase layout names and are case-sensitive. If no match is found, it falls back to **format**. |
| **expand** | bool | false | Enables the module to consume all leftover space. |

## FORMAT REPLACEMENTS

**{layout}**: The active workspace's layout: **scrolling**, **dwindle**, **master**, or **stacking**.

## STYLE

The current layout name is added as a dynamic CSS class.

- **\#layout**

- **\#layout.scrolling**

- **\#layout.dwindle**

- **\#layout.master**

- **\#layout.stacking**

## EXAMPLES

    "umbriel/layout": {
        "format": "{layout}",
        "format-scrolling": "Scrolling",
        "format-dwindle": "Dwindle",
        "format-master": "Master",
        "format-stacking": "Stacking"
    }

### CSS Example

    #layout {
        color: #ffffff;
        padding: 0 5px;
    }

    #layout.scrolling {
        color: #a6e3a1;
    }

    #layout.dwindle {
        color: #89b4fa;
    }

    #layout.master {
        color: #f9e2af;
    }

    #layout.stacking {
        color: #f38ba8;
    }

# umbriel/window

## DESCRIPTION

The **window** module displays the title of the currently focused window in Umbriel.

## CONFIGURATION

Addressed by **umbriel/window**

| **Option** | **Typeof** | **Default** | **Description** |
|:--:|:--:|:--:|:--:|
| **format** | string | {title} | The format, how information should be displayed. See **FORMAT REPLACEMENTS**. |
| **rewrite** | object |  | Rules to rewrite the window title. See **REWRITE RULES**. |
| **separate-outputs** | bool | false | Show the last focused window of the bar's output instead of the globally focused window. |
| **icon** | bool | false | Show the application icon. |
| **icon-size** | integer | 24 | Size of the application icon. |
| **expand** | bool | false | Enables this module to consume all left over space dynamically. |
| **max-length** | integer |  | The maximum length in characters the module should display. |
| **show-empty** | bool | false | When no window is focused (empty workspace or all windows closed), keep the module visible and render **format** with empty replacements and **{column}**, **{row}** and **{max_col}** set to -1. When false, the module is hidden while no window is focused. |

## FORMAT REPLACEMENTS

**{title}**: The current title of the focused window.

**{app_id}**: The current app ID of the focused window.

**{id}**: The stable ID of the focused window.

**{workspace}**: The name of the workspace containing the focused window.

**{workspace_id}**: The stable ID of the workspace containing the focused window.

**{layout}**: The layout of the workspace containing the focused window.

**{output}**: The output containing the focused window.

**{column}**: The window's column in the scrolling layout, or -1 when it is floating or the layout has no columns.

**{row}**: The window's row in the scrolling layout, or -1 when it is floating or the layout has no columns.

**{max_col}**: The highest column index among the windows on the same workspace.

## REWRITE RULES

**rewrite** is an object where keys are regular expressions and values are rewrite rules if the expression matches. Rules may contain references to captures of the expression.

Regular expression and replacement follow ECMA-script rules.

If no expression matches, the title is left unchanged.

Invalid expressions (e.g., mismatched parentheses) are skipped.

## EXAMPLES

    "umbriel/window": {
    	"format": "{}",
    	"rewrite": {
    		"(.*) - Mozilla Firefox": "🌎 $1",
    		"(.*) - zsh": "> [$1]"
    	},
    	"icon": true,
    	"icon-size": 20
    }

## STYLE

- **\#window**

- **window#waybar.empty \#window** When no windows are on the workspace

The following classes are applied to the entire Waybar rather than just the window widget:

- **window#waybar.empty** When no windows are in the workspace

- **window#waybar.solo** When only one window is on the workspace

- **window#waybar.\<app-id\>** Where **app-id** is the app ID of the only window on the workspace

# umbriel/workspaces

## DESCRIPTION

The **workspaces** module displays the workspaces of the Umbriel compositor.

## CONFIGURATION

Addressed by **umbriel/workspaces**

| **Option** | **Typeof** | **Default** | **Description** |
|:--:|:--:|:--:|:--:|
| **all-outputs** | bool | false | If set to false, workspaces will only be shown on the output they are on. If set to true all workspaces will be shown on every output. |
| **sort-by-name** | bool | false | Sort workspaces by name (numeric sort when all names are numbers). Unnamed workspaces fall back to their index on the output. |
| **sort-by-id** | bool | false | Sort workspaces by their stable id. Takes precedence over **sort-by-name**. |

If no sorting option is enabled, workspaces are sorted by output and index.

| **Option** | **Typeof** | **Default** | **Description** |
|:--:|:--:|:--:|:--:|
| **format** | string | {value} | The format, how information should be displayed. |
| **format-icons** | object |  | Based on the workspace name, index and state, the corresponding icon gets selected. See **ICONS**. |
| **disable-click** | bool | false | If set to false, you can click to change workspace. If set to true this behaviour is disabled. |
| **enable-bar-scroll** | bool | false | If set to false, you can't scroll to cycle through workspaces from the entire bar. If set to true this behaviour is enabled. |
| **reverse-scroll** | bool | false | If set to false, scrolling up/left switches to the previous workspace and scrolling down/right switches to the next workspace. If set to true, the behavior is reversed. |
| **disable-markup** | bool | false | If set to true, button label will escape pango markup. |
| **current-only** | bool | false | If set to true, only the active or focused workspace will be shown. |
| **display-condition** | string | "show-all" | oneof: "show-all", "keep-named", "only-populated" Specifies the conditions for showing workspace widgets. **show-all**: displays widgets for all workspaces. **keep-named**: always displays named workspaces, irrespective of whether they contain windows or not. **only-populated**: only displays widgets for workspaces that have windows. |
| **hide-empty** | bool | false | If set to true, empty workspaces will not be shown. |
| **ignore-workspaces** | array | \[\] | Regexes to match against workspace names. If there is a match, the workspace will not be shown. |
| **on-update** | string |  | Command to execute when the module is updated. |
| **expand** | bool | false | Enables this module to consume all left over space dynamically. |
| **workspace-taskbar** | object |  | Contains settings for the workspace taskbar, which displays app icons within each workspace. |
| **enable** | bool | false | Enables the workspace taskbar mode. |
| **icon-size** | int | 16 | Size of the icons in the workspace taskbar. |
| **format-window-separator** | string | " " | Separator used between window representations generated by **window-rewrite**. |
| **window-rewrite** | object | {} | Rules to map window app_id and/or title to a specific string representation (e.g., an icon). Keys are regular expressions matching \`app_id\<regex\>\` and/or \`title\<regex\>\`. Values are the replacement strings, which can contain \`{app_id}\` and \`{title}\` placeholders. |
| **window-rewrite-default** | string | "?" | The default representation for windows that don't match any rule in **window-rewrite**. |

## FORMAT REPLACEMENTS

**{value}**: Name of the workspace.

**{name}**: Name of the workspace.

**{icon}**: Icon, as defined in **format-icons**.

**{index}**: 1-based index of the workspace on its output.

**{output}**: Output where the workspace is located.

**{total}**: The total number of workspaces.

**{layout}**: The workspace layout: **scrolling**, **dwindle**, **master**, or **stacking**.

**{windows}**: Concatenated representation of windows in the workspace, using **window-rewrite** rules and **format-window-separator**.

## ICONS

Additional to workspace name matching, the following **format-icons** can be set.

- **default**: Will be shown, when no string matches are found.

- **focused**: Will be shown, when the workspace is focused.

- **active**: Will be shown, when the workspace is active on its output.

- **urgent**: Will be shown, when the workspace has urgent windows.

- **empty**: Will be shown, when the workspace is empty.

## CLICK ACTIONS

Left click switches to the workspace. Middle clicking a window in the workspace taskbar closes it. Scrolling the bar switches to the next or previous workspace on the focused output when **enable-bar-scroll** is enabled.

## EXAMPLES

    "umbriel/workspaces": {
        "format": "{icon} {windows}",
        "format-window-separator": "|",
        "window-rewrite-default": "?",
        "window-rewrite": {
            "app_id<firefox>": "🌐",
            "app_id<foot>": ">_",
            "app_id<org.gnome.Nautilus> title<.*Downloads.*>": "⬇"
        },
        "format-icons": {
            "browser": "🌐",
            "discord": "💬",
            "active": "●",
            "default": "○"
        }
    }

    "umbriel/workspaces": {
        "format": "{icon}",
        "workspace-taskbar": {
            "enable": true,
            "icon-size": 18
        }
    }

## STYLE

- **\#workspaces button**

- **\#workspaces button.focused**: The focused workspace.

- **\#workspaces button.active**: The workspace is active (visible) on its output.

- **\#workspaces button.urgent**: The workspace has one or more urgent windows.

- **\#workspaces button.empty**: The workspace is empty.

- **\#workspaces button.current_output**: The workspace is from the same output as the bar that it is displayed on.

- **\#workspaces button#umbriel-workspace-\<name\>**: Workspaces named this, or the index for unnamed workspaces.

- **\#workspaces button.umbriel-workspace**: The main container for the workspace.

- **\#workspaces button.umbriel-taskbar-btn**: The icon buttons within the taskbar.

- **\#workspaces button.umbriel-taskbar-btn.focused**: The taskbar icon button of the focused window.
