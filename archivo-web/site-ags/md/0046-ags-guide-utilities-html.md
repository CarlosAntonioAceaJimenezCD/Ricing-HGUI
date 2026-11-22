---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/utilities.html"
title: "Utilities | AGS"
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

# Utilities [​](#utilities)

AGS comes with some builtin utilities for common operations.

## File functions [​](#file-functions)

### Reading files [​](#reading-files)

ts

```
import { readFile, readFileAsync } from "ags/file"

function readFile(path: string): string
function readFileAsync(path: string): Promise<string>
```

### Writing files [​](#writing-files)

ts

```
import { writeFile, writeFileAsync } from "ags/file"

function writeFile(path: string, content: string): void
function writeFileAsync(path: string, content: string): Promise<void>
```

### Monitoring files [​](#monitoring-files)

If `path` is a directory it will be recursively monitored.

ts

```
import { monitorFile } from "ags/file"

function monitorFile(
  path: string,
  callback: (file: string, event: Gio.FileMonitorEvent) => void,
): Gio.FileMonitor
```

## Timeouts and Intervals [​](#timeouts-and-intervals)

ts

```
import { interval, timeout, idle, createPoll } from "ags/time"
```

You can use JavaScript native `setTimeout` or `setInterval` functions which return a [GLib.Source](https://docs.gtk.org/glib/struct.Source.html) instance. Alternatively you can use these functions provided by AGS, which return a `Timer` instance.

ts

```
class Timer extends GObject.Object {
  declare $signals: {
    now(): void
    cancelled(): void
  }

  cancel(): void
}
```

### Interval [​](#interval)

Will immediately execute the function and every `interval` millisecond.

ts

```
function interval(interval: number, callback?: () => void): Timer
```

### Timeout [​](#timeout)

Will execute the `callback` after `timeout` millisecond.

ts

```
function timeout(timeout: number, callback?: () => void): Timer
```

### Idle [​](#idle)

Executes `callback` whenever there are no higher priority events pending.

ts

```
function idle(callback?: () => void): Timer
```

Example:

ts

```
const timer = interval(1000, () => {
  console.log("optional callback")
})

timer.connect("now", () => {
  console.log("tick")
})

timer.connect("cancelled", () => {
  console.log("cancelled")
})

timer.cancel()
```

### createPoll [​](#createpoll)

`createPoll` creates a signal that only polls when there is at least one subscriber.

ts

```
function createPoll(
  init: string,
  interval: number,
  exec: string | string[],
): Accessor<string>

function createPoll<T>(
  init: T,
  interval: number,
  exec: string | string[],
  transform: (stdout: string, prev: T) => T,
): Accessor<T>

function createPoll<T>(
  init: T,
  interval: number,
  fn: (prev: T) => T | Promise<T>,
): Accessor<T>
```

Example:

tsx

```
function Counter() {
  const counter = createPoll(0, 1000, (prev) => prev + 1)

  return <label label={counter((c) => c.toString())} />
}
```

WARNING

Under the hood when passing a command as the third argument it uses [`execAsync`](#subprocess) which runs the given programs as is. They are **not** executed in a shell environment, they do **not** expand ENV variables like `$HOME`, and they do **not** handle logical operators like `&&` and `||`.

If you want bash, run them with bash.

ts

```
createPoll("", 1000, "bash -c 'command $ENV_VAR && command'")
```

## Process functions [​](#process-functions)

Import from `ags/process`

ts

```
import { subprocess, exec, execAsync, createSubprocess } from "ags/process"
```

### Subprocess [​](#subprocess)

You can start a subprocess and run callback functions whenever it outputs to stdout or stderr. The returned `Process` instance has an `stdout` and `stderr` signal.

ts

```
class Process extends GObject.Object {
  declare $signals: {
    stdout(out: string): void
    stderr(err: string): void
    exit(code: number, signaled: boolean): void
  }

  kill(): void
  write(str: string): void
  async writeAsync(str: string): Promise<void>
}

function subprocess(args: {
  cmd: string | string[]
  out?: (stdout: string) => void
  err?: (stderr: string) => void
}): Process

function subprocess(
  cmd: string | string[],
  onOut?: (stdout: string) => void,
  onErr?: (stderr: string) => void,
): Process
```

Example:

ts

```
const proc = subprocess(
  "some-command",
  (out) => console.log(out), // optional
  (err) => console.error(err), // optional
)

// or with signals
const proc = subprocess("some-command")
proc.connect("stdout", (_, out) => console.log(out))
proc.connect("stderr", (_, err) => console.error(err))
```

### Executing external commands and scripts [​](#executing-external-commands-and-scripts)

ts

```
function exec(cmd: string | string[]): string
function execAsync(cmd: string | string[]): Promise<string>
```

WARNING

You should generally avoid `exec` and use its async variant `execAsync` as the former will block IO, meaning the whole shell will freeze and will be unresponsive until it returns.

Example:

ts

```
try {
  const out = exec("/path/to/script")
  console.log(out)
} catch (err) {
  console.error(err)
}

execAsync(["bash", "-c", "/path/to/script.sh"])
  .then((out) => console.log(out))
  .catch((err) => console.error(err))
```

WARNING

`subprocess`, `exec`, and `execAsync` executes the passed executable as is. They are **not** executed in a shell environment, they do **not** expand ENV variables like `$HOME`, and they do **not** handle logical operators like `&&` and `||`.

If you want bash, run them with bash.

ts

```
exec(["bash", "-c", "command $ENV_VAR && command"])
exec("bash -c 'command $ENV_VAR' && command")
```

### createSubprocess [​](#createsubprocess)

`createSubprocess` creates a signal that starts a subprocess when the first subscriber appears and kills the subprocess when number of subscribers drop to zero.

ts

```
export function createSubprocess(
  init: string,
  exec: string | string[],
): Accessor<string>

export function createSubprocess<T>(
  init: T,
  exec: string | string[],
  transform: (stdout: string, prev: T) => T,
): Accessor<T>
```

Example:

tsx

```
function Log() {
  const log = createSubprocess("", "journalctl -f")

  return <label label={log} />
}
```

## Http requests [​](#http-requests)

ts

```
import { fetch, URL } from "ags/fetch"

const url = new URL("https://some-site.com/api")
url.searchParams.set("hello", "world")

const res = await fetch(url, {
  method: "POST",
  body: JSON.stringify({ hello: "world" }),
  headers: {
    "Content-Type": "application/json",
  },
})

const json = await res.json()
```

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/utilities.md)

Last updated:

Pager

[Previous pageApp and CLI](/ags/guide/app-cli.html)

[Next pageResources](/ags/guide/resources.html)

Released under the GPL v3.0 License

Logo is created by VDawg
