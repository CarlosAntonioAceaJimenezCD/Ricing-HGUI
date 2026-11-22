---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/nix.html"
title: "Usage on NixOS | AGS"
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

# Usage on NixOS [​](#usage-on-nixos)

Initialize a directory using the template.

sh

```
nix flake init --template github:aylur/ags
```

TIP

If you are new to NixOS and are not yet familiar with flakes, derivations or development shells the recommended way to use AGS is the [home-manager](#using-home-manager) module.

## Bundle and DevShell [​](#bundle-and-devshell)

To build a derivation you can use the `ags bundle` command.

flake.nix

nix

```
{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

    astal = {
      url = "github:aylur/astal";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    ags = {
      url = "github:aylur/ags";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.astal.follows = "astal";
    };
  };

  outputs = { self, nixpkgs, ags, astal }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    packages.${system}.default = pkgs.stdenv.mkDerivation {
      pname = "my-shell";

      src = ./.;

      nativeBuildInputs = with pkgs; [
        wrapGAppsHook3
        gobject-introspection
        ags.packages.${system}.default
      ];

      buildInputs = [
        pkgs.glib
        pkgs.gjs
        astal.io
        astal.astal4
        # packages like astal.battery or pkgs.libsoup_4
      ];

      installPhase = ''
        ags bundle app.ts $out/bin/my-shell
      '';

      preFixup = ''
        gappsWrapperArgs+=(
          --prefix PATH : ${pkgs.lib.makeBinPath ([
            # runtime executables
          ])}
        )
      '';
    };
  };
}
```

While working on the project, it would make sense to use the `ags` cli instead of building it everytime with `nix`.

You could enter a shell with `agsFull` package which exposes AGS + every [Astal library](https://aylur.github.io/astal/guide/libraries/references#astal-libraries).

sh

```
nix shell github:aylur/ags#agsFull
```

Or define a `devShell` and cherry pick packages.

flake.nix

nix

```
{
  outputs = { self, nixpkgs, ags }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = [
        (ags.packages.${system}.default.override {
          extraPackages = [
            # cherry pick packages
          ];
        })
      ];
    };
  };
}
```

## Using home-manager [​](#using-home-manager)

If you prefer the workflow of "configuring a program" instead of "using a library", you can use the home-manager module.

Example content of `flake.nix`

flake.nix

nix

```
{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    astal.url = "github:aylur/astal";

    ags.url = "github:aylur/ags";
  };

  outputs = { home-manager, nixpkgs, ... }@inputs:
  let
    system = "x86_64-linux";
  in
  {
    homeConfigurations."${username}" = home-manager.lib.homeManagerConfiguration {
      pkgs = import nixpkgs { inherit system; };

      # pass inputs as specialArgs #
      extraSpecialArgs = { inherit inputs; };

      # import your home.nix #
      modules = [ ./home-manager/home.nix ];
    };
  };
}
```

Example content of `home.nix` file

home.nix

nix

```
{ inputs, pkgs, ... }:
{
  # add the home manager module
  imports = [ inputs.ags.homeManagerModules.default ];

  programs.ags = {
    enable = true;

    # symlink to ~/.config/ags
    configDir = ../ags;

    # additional packages and executables to add to gjs's runtime
    extraPackages = with pkgs; [
      inputs.astal.packages.${pkgs.system}.battery
      fzf
    ];
  };
}
```

The module only includes the core `astal3`, `astal4` and `astal-io` libraries. If you want to include any other [library](https://aylur.github.io/astal/guide/libraries/references#astal-libraries) you have to add them to `extraPackages`. You can also add binaries which will be added to the gjs runtime.

WARNING

The `configDir` option symlinks the given path to `~/.config/ags`. If you already have your source code there leave it as `null`.

## Using Astal CLI tools [​](#using-astal-cli-tools)

The home-manager module does not expose Astal CLIs to the home environment, you have to do that yourself if you want:

home.nix sh

nix

```
home.packages = [ inputs.astal.packages.${pkgs.system}.notifd ];
```

sh

```
astal-notifd --help
```

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/nix.md)

Last updated:

Pager

[Previous pageExamples](/ags/guide/examples.html)

[Next pageMigration Guide](/ags/guide/migration-guide.html)

Released under the GPL v3.0 License

Logo is created by VDawg
