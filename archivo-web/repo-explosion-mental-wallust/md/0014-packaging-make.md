---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/packaging-make.md"
title: "Makefile"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Makefile
Using `make` is _optional_ if you know your way into cargo and **can** accept
the job to **manually install man pages, completions and the binary**.

I've only added a `Makefile` to simplify _installing_ these assets, as well as
the binary. By default  `make` uses native compilation, you can define your
wished target like this:

**Building**
```
$ TARGET=x86_64-pc-windows-gnu make install CARGOFLAGS="--release --target=$TARGET"
```

**Installing**
```
# TARGET=x86_64-pc-windows-gnu make CARGOFLAGS="--release --target=$TARGET" RELEASE="target/$TARGET/release"
```

Don't forget that `make` by itself runs `cargo` in order to built the binary.
It's common on projects that use make to split building in two steps, given
that `make install` requires permissions to write on `$DESTDIR$PREFIX`.
