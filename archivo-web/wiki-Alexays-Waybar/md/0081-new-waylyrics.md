---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/Alexays/Waybar/new-waylyrics.md"
title: "new waylyrics"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/Alexays/Waybar/wiki"
---
## waylyrics

new [waylyrics](https://github.com/switchToLinux/waylyrics) , use sdbus-cpp .

support:
- all mpris players
- custom class/id tag;
- faster and less dbus cost!


一个更高效的 [waylyrics](https://github.com/switchToLinux/waylyrics) 动态库。

优点：
- 参考了 waylyrics ，并且重新实现了大部分功能。
- 减少了对 dbus 通信请求，使用了 signal 订阅模式。
- 更新歌词更加快速（1秒）。
