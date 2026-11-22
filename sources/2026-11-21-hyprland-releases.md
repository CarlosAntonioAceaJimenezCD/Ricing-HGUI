---
type: source
source_type: report
url: "https://github.com/hyprwm/Hyprland/releases"
title: "Hyprland · GitHub Releases (v0.56.1 – v0.57.2)"
fetched_at: 2026-11-22T00:51:12+00:00
fetcher: curl + jq
author: "hyprwm"
---

# Hyprland releases (datos crudos de la API de GitHub)

## v0.57.2 · 2026-11-09T11:14:08Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.57.2

Another round of patches backported from main on top of 0.57.1.

This fixes various regressions, as well as some crashes under heavy load from RT scheduling.

## Fixes Backported
 - config/lua: fix accessing an expired window ref from a lua object (#16853) by @vaxerski
 - core/fullscreen: fix client_requested_fs_uses_layout_handler being handled incorrectly for some programs (#16870) by @erstarr
 - helpers/cm: fix small typo in calculating brightness saturation (#16897) by @fxzzi
 - keybinds: fix modifier resolution when remapped (#16820) by @vaxerski
 - overlay: fix double counting when present early exited. (#16834) by @ItsOhen
 - protocols/subcompositor: fix nested ancestor traversal
 - render: fix invalidation artifacts with two floating overlapped windows (#16888) by @fxzzi
 - scrolling/fullscreen: fix only internal un-FS not restoring prev col width (#16896) by @erstarr
 - seat: fix grab check (#16900) by @vaxerski
 - algo/scroll: remove redundant cleanup of FS lists when compositor shutdown requested (#16792) by @erstarr
 - config/values: adjust limits again (#16898) by @vaxerski
 - core/layers: allow bottom layers and background layers under fs (#16740) by @fxzzi
 - core: enable prctl(2) only on Linux (#16839) by @tagattie
 - desktop/layerSurface: use refocusPointer instead of simulate on map (#16902) by @vaxerski
 - init: stop acquiring realtime scheduling
 - layout/floating: preserve parent-relative window placement
 - protocols/activation: send urgent-only tokens if serial is missing (#16827) by @vaxerski
 - protocols/subcompositor: handle expired ancestry during teardown
 - start: handle and report signal-terminated children
 - window: allow unpinning window onto special workspace (#16854) by @rgalhos


## Special thanks

Big thank you to the Omacom Foundation for being Hyprland's Exclusive sponsor!

Additionally, big thank you to the individuals who donated to help keep the project alive!

#### Top Supporters:

gaserre, MadCatX, d, Bonsai, RaymondLC92, eynix, Theory_Lukas, soy_3l.beantser, miget.com, 3RM, iain, Tonao Paneguini, Kay, gfunnymoney, yamauchihiroshi, Hunter Wesson, alexmanman5, --, TyrHeimdal, Ammar Hossain, alukortti, Jonas Bové, ExBhal, Vaidas Damosevicius, ari-cake, Jas Singh, lzieniew, Seishin, Xoores, Balázs Püspök-Kiss, taigrr, DHH, Brandon Wang, Cehovski

#### New Monthly Supporters:

lazy_sleepers, TheGreatMcPain, jar0, EddieTheHead14, Clayton S, cendert, Alex Reuman, NanoMercury, 13enny13oy, bug-coder, Howard Shane, babble, BEJ, Victoriano, javif89, Martin, arximboldi, Juan Felipe Uribe Cardona, Eric W. Bates, Alferann, sgt.moon, Maw, west0nw, _, Tyler, carpet.lover, Stam Kapetanakis, judas_, Mark Fingerhuth, Frapol, Spark, chinesecatfood, Luuumine, JMH, Jeff Aaron, Vandav, mfed

#### One-time Donators:

Theis, Alexandre, Alba&Héctor, juboba, ZmagoD, pizza_lover, chocman, Here you go, Yoway Buorn, Zeal, Federico, Jamjam, Stefan, Jacques Fernandes, Ar, macnedav, StefanH, chapgx, Karol, Viktor, Seraphim of Boise, ysksn, Anton Herzog, deruma, Deleted User, hei, toxa237, PyArch, Noboriki, Clement Pont, Clippy, Romano Kleinwächter, Krob, Inscolosus, Marco, rony539, Thierry C., curbol, Alex, marsch, Jelte, Darwin Vilpando, Michka, aussiedini, Carlos Segura, Hercules, Magkid, BIGGASSS, Nick, Roman Korver, Deano, RammFire, Oyarsa, Jeff L, Fdonnet, bernarduh, sacrebleu, Reinhardt - Beavis, Jannek, Santiago Perez, ProfessorNova, DickyB , houdinihacker, Micah Stevens, Sunday, Dylan, Leo, romulus, Daniel, kessmahat, sudoalex, tuding, Abdi, Bartosz, NightVision, X3N0N, Josh, Erick, btmxh, Mex, In. Cognito, Banclaevius, Hougan, prtzl, luan, amaka, Erik van Velzen, CoolMcGrrr, Abhinav, JM, geddon_jt, tomkersten, Carl, Blackcat, bbq, gmase, w32deadcodea, Benoit Servais, BonkusCheemus, Frisbee, Astralyd, Kevin Hill, nomminommi23, thoastbrot, Dorin, Nolliv22, MicMun, Jkob, Wouter Bos, Wenz, Hello, bob, Yuza, Kuba Wójcik, imashhi, Snake, Altoine, Gabriel Henrique, Z, Da

## v0.57.1 · 2026-11-03T09:47:31Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.57.1

As usual, a small update with a few fixes backported from main onto 0.57.0.

This fixes some keybind issues, black screens on nvidia, and other minor regressions.

## Fixes backported
 - config/lua: fix validator for custom accel profiles (#16730) by @vaxerski
 - keybinds: fix _consuming exceptions for chord resolving (#16806) by @vaxerski
 - protocols/session-lock: fix removed output causing a protocol error (#16784) by @vaxerski
 - state/workspace: fix underflow in r parsing resulting in a bad return (#16786) by @vaxerski
 - config/values: adjust limits for tablet values (#16782) by @vaxerski
 - config: restore opt-in KMS dmabuf filtering
 - decoration/groupbar: round boxes in device space to match damage (#16687) by @andresilva
 - keybinds: do not shadow mouse event inputs (#16788) by @vaxerski
 - monitor: set max_bpc based on configured bitdepth (#16708) by @fxzzi
 - protocols/dmabuf: refresh format feedback after config updates
 - protocols/dmabuf: use replacement table for feedback updates
 - renderer: draw small surfaces at their logical size (#16711) by @hitori-chan
 - window: preserve fullscreen on client maximize requests
 
 
## Special thanks

Big thank you to the Omacom Foundation for being Hyprland's Exclusive sponsor!

Additionally, big thank you to the individuals who donated to help keep the project alive!

#### Top Supporters:

gaserre, MadCatX, d, Bonsai, RaymondLC92, eynix, Theory_Lukas, soy_3l.beantser, miget.com, 3RM, iain, Tonao Paneguini, Kay, gfunnymoney, yamauchihiroshi, Hunter Wesson, alexmanman5, --, TyrHeimdal, Ammar Hossain, alukortti, Jonas Bové, ExBhal, Vaidas Damosevicius, ari-cake, Jas Singh, lzieniew, Seishin, Xoores, Balázs Püspök-Kiss, taigrr, DHH, Brandon Wang, Cehovski

#### New Monthly Supporters:

lazy_sleepers, TheGreatMcPain, jar0, EddieTheHead14, Clayton S, cendert, Alex Reuman, NanoMercury, 13enny13oy, bug-coder, Howard Shane, babble, BEJ, Victoriano, javif89, Martin, arximboldi, Juan Felipe Uribe Cardona, Eric W. Bates, Alferann, sgt.moon, Maw, west0nw, _, Tyler, carpet.lover, Stam Kapetanakis, judas_, Mark Fingerhuth, Frapol, Spark, chinesecatfood, Luuumine, JMH, Jeff Aaron, Vandav, mfed

#### One-time Donators:

Theis, Alexandre, Alba&Héctor, juboba, ZmagoD, pizza_lover, chocman, Here you go, Yoway Buorn, Zeal, Federico, Jamjam, Stefan, Jacques Fernandes, Ar, macnedav, StefanH, chapgx, Karol, Viktor, Seraphim of Boise, ysksn, Anton Herzog, deruma, Deleted User, hei, toxa237, PyArch, Noboriki, Clement Pont, Clippy, Romano Kleinwächter, Krob, Inscolosus, Marco, rony539, Thierry C., curbol, Alex, marsch, Jelte, Darwin Vilpando, Michka, aussiedini, Carlos Segura, Hercules, Magkid, BIGGASSS, Nick, Roman Korver, Deano, RammFire, Oyarsa, Jeff L, Fdonnet, bernarduh, sacrebleu, Reinhardt - Beavis, Jannek, Santiago Perez, ProfessorNova, DickyB , houdinihacker, Micah Stevens, Sunday, Dylan, Leo, romulus, Daniel, kessmahat, sudoalex, tuding, Abdi, Bartosz, NightVision, X3N0N, Josh, Erick, btmxh, Mex, In. Cognito, Banclaevius, Hougan, prtzl, luan, amaka, Erik van Velzen, CoolMcGrrr, Abhinav, JM, geddon_jt, tomkersten, Carl, Blackcat, bbq, gmase, w32deadcodea, Benoit Servais, BonkusCheemus, Frisbee, Astralyd, Kevin Hill, nomminommi23, thoastbrot, Dorin, Nolliv22, MicMun, Jkob, Wouter Bos, Wenz, Hello, bob, Yuza, Kuba Wójcik, imashhi, Snake, Altoine, Gabriel Henrique, Z, Dan, Azide, Adam Curry, Viviaes, azalea, derp, NuclearToast, Rishu Raj, Malkovic, Sean, atarit0, dirk, finquilizer, Élder Bernardi, Windwarg, OldPastaFace, Miggi, Joy, Mr Smith, Roberto, sonicbhoc, Antoni, Stefan Dahinden, Daniel Li, MajesticOrtix, Roy, poor_man, Ger O'M, Greyed Out, Avram S., SK, Laurier Roy, King, Supporter, anonymous hypruser, aidnm, kl_Haribo, xnmp, Morata, Jonny Sierra, Chris Arias, auregosu, Mohamed Bouallegue, jo, David, Ladislav Böhm, nug, Skrazzo, Cam C., rafal Burdzy, Ripal Barot, N/A, Nassiel Alaunaery, totyko, Gal, Hi, Fizlo, opensource, fhmj, DJVger, Hijinx, Thank

## v0.57.0 · 2026-10-28T10:42:35Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.57.0

A big update, bringing a bunch of neat features, and tons of fixes, from A to Z.

Special thanks to my grandma for making this release possible in the first place!

## New features:
 - config/events: add config.unload event (#16005) by @Dregu
 - config/lua: add `reload_config()` api (#16108) by @LRitzdorf
 - config/lua: add hl.get_devices() (#16429) by @vaxerski
 - config/lua: add minimize event (#16071) by @vaxerski
 - config/lua: add window.update_state (#16527) by @vaxerski
 - config: Add `cursor:warp_on_monitor_change` (#15844) by @kolayne
 - config: add `layers` config category, move 2 config options from `misc` to there. (#16617) by @erstarr
 - config: add deprecation notices (#15669) by @vaxerski
 - desktop/rule: add no_xdg_drags window rule (#15573) by @vaxerski
 - desktop/windowRule: add active_border and inactive_border rules (#15581) by @RommelRivera
 - desktop/windowRule: add no_glow window rule (#15863) by @Aqa-Ib
 - desktop/windowRule: add no_wobble window rule and workspace rule (#15735) by @Aqa-Ib
 - feat: add missing lua stub (#15579) by @nath1416
 - groupbar: re-add groupbar positional dragging (#15615) by @MightyPlaza
 - input/tablet: add `input:tablet:enabled` (#16380) by @Undeadamien
 - input: add swallowing focus click (#16250) by @pedromiguelvc
 - layout/drag: add binds:drag_center_window (#15563) by @LegendaryBanana37
 - pointer: add pointer transforms (#16143) by @vaxerski
 - render: add scene composition (#16340) by @vaxerski
 - renderer: implement window wobble (#14920) by @vaxerski
 - renderer/gl: implement swappable blur variants (#15661) by @vaxerski
 - renderer/shaders: add decoration:blur:proportional (#16643) by @darkwater
 - renderer/workspace: add workspace presentable for passing workspace data to window rendering (#16440) by @vaxerski
 - renderer: ensure only one buffer reference is added (#15584) by @gulafaran
 - session: add disable-able systemd session target (#15776) by @LRitzdorf
 - tests: add fallback focus test for pinned windows on special workspaces (#15826) by @Meehir5907
 - workspace: add changeworkspaceid to socket2 (#15571) by @vaxerski

## Fixes:
 - CI: fix codeownersplus status comment spam (#15597) by @kolayne
 - algo/master: fix some master layout window-drag bugs (#15956) by @LRitzdorf
 - algo/scrolling: fix unFSing window sticking to the left corner instead of respecting `focus_fit_method` (#15716) by @erstarr
 - ci/vouch: fix template file
 - config/actions: fix center not saving the new pos of a floating window (#15810) by @erstarr
 - config/lua: `created` to `created_early`, new `created` after setup is done; fix `on_created_empty` rule (#16221) by @LRitzdorf
 - config/lua: fix empty object construction not resulting in nil (#15831) by @vaxerski
 - config/lua: fix forwarding of details to lua values (#15651) by @vaxerski
 - config/lua: fix minor typo in mouseResize (#16454) by @vaxerski
 - config/lua: fix misspelling of `damping` as `dampening` for spring animations (#15993) by @erstarr
 - config/lua: fix potential crash in error prints (#16246) by @vaxerski
 - config/lua: fix segfault on non-string errors (#16505) by @darkwater
 - config/values: fixup shadow limits (#15682) by @vaxerski
 - config: fix CONFIG_VALUES not returning proper current values (#15948) by @vaxerski
 - config: fix duplicate config value crash (#15708) by @gulafaran
 - config: fix on_current_monitor (#14615) by @tomben13
 - core/fullscreen: allow layout managed fullscreens to not block seeking window in direction, and other fixes (#15569) by @erstarr
 - core/fullscreen: fix floating window rendering order when one of them is FSed (#15703) by @erstarr
 - core/fullscreen: fix not accounting for special workspaces when client requests FS with a monitor request attached (#15806) by @erstarr
 - core/layers: top layers go below fullscreen windows, fix DS solitary (#15937) by @erstarr
 - core/tests: fix sporadically failing test, add helper to get wi

## v0.56.2 · 2026-08-05T14:14:01Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.56.2

A standard patch release backporting some fixes from main on top of 0.56.2.

## Fixes backported
 - algo/scrolling: fix unFSing window sticking to the left corner instead of respecting `focus_fit_method` (#15716) by @erstarr
 - config: fix duplicate config value crash (#15708) by @gulafaran
 - core/fullscreen: allow layout managed fullscreens to not block seeking window in direction, and other fixes (#15569) by @erstarr
 - core/fullscreen: fix floating window rendering order when one of them is FSed (#15703) by @erstarr
 - desktop/rules: fix gaps_out rule overriding float_gaps (#15662) by @Dregu
 - hyprctl: fix wiki strings (#15739) by @vaxerski
 - screenshare: fix toplevel capture missing software cursor (#15638) by @Dregu
 - algo/scrolling: bring back old behavior of fs (#15660) by @vaxerski
 - bindings/dispatchers: Don't inherit key state modmask during key sym lookup (#15401) by @masnax
 - config/monitorRuleManager: recheck mirrors on ensure (#15733) by @vaxerski
 - desktop/hitTest: exclusive layer popup event handling (#15729) by @aurelleb
 - desktop: render IME above all desktop components (#15646) by @vaxerski
 - feat: add missing lua stub (#15579) by @nath1416
 - ipc/socket1: don't round/truncate `hyprctl monitors` scale (#15628) by @frebib
 - layout/scrolling/fullscreen: minor improvements ontop of 15660 (#15685) by @erstarr
 - opengl: invalidate depth too (#15657) by @gulafaran
 
 
## Special thanks

Special thanks as always to these gigachads for supporting Hyprland's continued development:

### Sponsors

#### Diamond

37Signals

#### Gold

Framework, Butterfly

### Donators

#### Top Supporters:

soy_3l.beantser, taigrr, RaymondLC92, Xoores, Bonsai, d, DHH, alukortti, miget.com, Ammar Hossain, Jas Singh, yamauchihiroshi, iain, Seishin, Brandon Wang, ExBhal, Hunter Wesson, RayJameson, Kay, Ki☆, alexmanman5, Tonao Paneguini, John Shelburne, 3RM, gfunnymoney, ari-cake, TyrHeimdal, Illyan, --, Insprill, lzieniew, MadCatX, Theory_Lukas

#### New Monthly Supporters:

Anon, wmeints, Twinkybot, ryan, jakhub, JMH, Le Juju, ercument, xff, Mike Raphone, Mike E, Martijn, mfed, leomoon, OldPastaFace, ferngg_, damirk, Ghostxsalmon, Flo, DavDood, bamboo, Justin, Cpl. Roth, irontom10, Eric, phage-zn, erotourtes, Streifenfrei

#### One-time Donators:

Wawan, Jim, Marco Celis, JDM, LPGames, joscani, trvnkwil, davinsky, Santiago Perez, Mantas, Javier, asdfasdfasdfasdf, Leo, saltchicken, Yakedo, J Fernandes, PasiS, Marcelo, RammFire, jrgd, elandi, Xenia, Paul H, Jonathan Lopez, mir0, sheik, Supporter, Gérald, Ghoul, uniuni, Lei Huang, BTCharlie, marckeelingiv, ArisTheInquiring, anon, 9x25dillon, DCyph360, inittux111, Steve, Rowan, Awachuwere, Hank, Chloessica, escuco, Boriana, CRUDB, EndoliteMatrix, King, tdha, SillyingAround, Ag, MrElo, fraxineus, Dobrovschi Stefan, MrCharless, 4everN00b, bogdan.bagno@gmail.com, Shoh Berdy, araneae, Skrazzo, Carlos martinez, Kimli, Antoni, Ed R, Aphrofluff, ThatOneShortGuy, gtm, ChristophLHR, Sam C, deven, Alezarine, golanv, Praegustator, zaafiel428, skatos24, Louis Nicholas, Ivan Ucha, Andrejs, mirolPirol, dacero, cmquesada, Nando, an, shkz, Rob H, TrentZent#5307, Snil, Rigle, NikodemRafalski, Bishop James, Some random dude from China, jo, Roy, ProfessorNova, Ikey, nihilfm, Serj007, GVM, DucSpa, LinuxHG, WetSeal, sikor666, djledda, Dominik, jolteroli, Jkob, Valerie, Valentino, A374377, evandroev@gmail.com, w00z4, Mateusz, Dirk, mdereje, Joy, Celerodlak, BabawabatheSuperSlender, Paulin, Manuel P., Cobra1one, Abhinav, houdinihacker, JohnAtl, Blackcat, yDog-1, CUhRip, Alex, Kodlak, ReallyFluffy, Miguel Padilla, wronguy, JWHall, TheGreatMcPain, mykey, ThePreviousOne, poor_man, FarLT, Élder Bernardi, Citizen5, Gus, GKL, falparsi, @ericmoyer@hachyderm.io, labo, MeaTLoTioN, Caja, Willem van Ede, @elmorek, anonymous-supporter, William Caicedo, Hello, aussiedini, omnicroissant, cadds, Evan LeSage, Pierre, Marugun, Robbie, Henry, paradaimu, Cody Weaver, jbsbuilde

## v0.56.1 · 2026-07-27T16:37:57Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.56.1

As usual, a patch release with a few fixes backported from main onto 0.56.0

## Fixes backported
 - compositor: add a deprecation notice to .conf configs (#15538) by @vaxerski
 - workspace: add changeworkspaceid to socket2 (#15571) by @vaxerski
 - desktop/windowRule: fix exec rules leaking (#15543) by @vaxerski
 - hyprctl: fix json output for binds (#15507) by @vaxerski
 - input-capture: fix `allow_input_capture` bind flag with `capture_modifiers` enabled (#15477) by @littleblack111
 - monitor: fix rotate and mirror regression (#15587) by @gulafaran
 - scrolling: fix in-band resize for the first window of a band (#15532) by @jwiseuk
 - build: update hyprutils dependency to 0.14.0 (#15518) by @aruhier
 - compositor: init eventManager earlier (#15522) by @vaxerski
 - config/lua: do not nuke package.path (#15622) by @vaxerski
 - config/lua: use openLate for window.open events (#15540) by @vaxerski
 - example: update hyprland.lua default springs (#15499) by @cebem1nt
 - input: nullptr check eis_client_get_name (#15520) by @gulafaran
 - protocols/pointerwarp: send mouse frame event after motion (#15599) by @awused
 - renderer: round m_scale calculations (#15594) by @gulafaran
 - view: do not render monitor for tearing if it's blocked (#15500) by @vaxerski

## Special thanks

Special thanks as always to these gigachads for supporting Hyprland's continued development:

### Sponsors

#### Diamond

37Signals

#### Gold

Framework, Butterfly

### Donators

#### Top Supporters:

soy_3l.beantser, taigrr, RaymondLC92, Xoores, Bonsai, d, DHH, alukortti, miget.com, Ammar Hossain, Jas Singh, yamauchihiroshi, iain, Seishin, Brandon Wang, ExBhal, Hunter Wesson, RayJameson, Kay, Ki☆, alexmanman5, Tonao Paneguini, John Shelburne, 3RM, gfunnymoney, ari-cake, TyrHeimdal, Illyan, --, Insprill, lzieniew, MadCatX, Theory_Lukas

#### New Monthly Supporters:

Anon, wmeints, Twinkybot, ryan, jakhub, JMH, Le Juju, ercument, xff, Mike Raphone, Mike E, Martijn, mfed, leomoon, OldPastaFace, ferngg_, damirk, Ghostxsalmon, Flo, DavDood, bamboo, Justin, Cpl. Roth, irontom10, Eric, phage-zn, erotourtes, Streifenfrei

#### One-time Donators:

Wawan, Jim, Marco Celis, JDM, LPGames, joscani, trvnkwil, davinsky, Santiago Perez, Mantas, Javier, asdfasdfasdfasdf, Leo, saltchicken, Yakedo, J Fernandes, PasiS, Marcelo, RammFire, jrgd, elandi, Xenia, Paul H, Jonathan Lopez, mir0, sheik, Supporter, Gérald, Ghoul, uniuni, Lei Huang, BTCharlie, marckeelingiv, ArisTheInquiring, anon, 9x25dillon, DCyph360, inittux111, Steve, Rowan, Awachuwere, Hank, Chloessica, escuco, Boriana, CRUDB, EndoliteMatrix, King, tdha, SillyingAround, Ag, MrElo, fraxineus, Dobrovschi Stefan, MrCharless, 4everN00b, bogdan.bagno@gmail.com, Shoh Berdy, araneae, Skrazzo, Carlos martinez, Kimli, Antoni, Ed R, Aphrofluff, ThatOneShortGuy, gtm, ChristophLHR, Sam C, deven, Alezarine, golanv, Praegustator, zaafiel428, skatos24, Louis Nicholas, Ivan Ucha, Andrejs, mirolPirol, dacero, cmquesada, Nando, an, shkz, Rob H, TrentZent#5307, Snil, Rigle, NikodemRafalski, Bishop James, Some random dude from China, jo, Roy, ProfessorNova, Ikey, nihilfm, Serj007, GVM, DucSpa, LinuxHG, WetSeal, sikor666, djledda, Dominik, jolteroli, Jkob, Valerie, Valentino, A374377, evandroev@gmail.com, w00z4, Mateusz, Dirk, mdereje, Joy, Celerodlak, BabawabatheSuperSlender, Paulin, Manuel P., Cobra1one, Abhinav, houdinihacker, JohnAtl, Blackcat, yDog-1, CUhRip, Alex, Kodlak, ReallyFluffy, Miguel Padilla, wronguy, JWHall, TheGreatMcPain, mykey, ThePreviousOne, poor_man, FarLT, Élder Bernardi, Citizen5, Gus, GKL, falparsi, @ericmoyer@hachyderm.io, labo, MeaTLoTioN, Caja, Willem van Ede, @elmorek, anonymous-supporter, William Caicedo, Hello, aussiedini, omnicroissant, cadds, Evan LeSage, Pierre, Marugun, Robbie, Henry, paradaimu, Cody Weaver, jbsbuilder, zongben, Pawel, ManosG, revitalist, marcs100, Azrael Alpha, erkre, brainfxk, PaulG, Ivan Shakuta, taqashh/abbo0dio, curu, Chaosz, GedeSaika, 

## v0.56.0 · 2026-07-20T08:36:24Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.56.0

A big new release with tons of features and fixes, brought to you by the Hyprland Corp.

No breaking changes! :)

## New features:
 - algo/master: add an option to focus master when window is closed (#14306) by @ArchSav
 - algo/scrolling: add `inhibit_scroll` dispatch for scrolling algorithm (#13955) by @erstarr
 - algo/scrolling: add a "fit expand" layout message (#14761) by @LichtMarv
 - algo/scrolling: add new `fit_into_view` layout msg (#14991) by @erstarr
 - cm/icc: add Primaries to ICC-generated SImageDescription (#15227) by @GamingLiamStudios
 - config/lua: add a change_id workspace API (#15298) by @vaxerski
 - config/lua: add get_loaded_plugins (#14582) by @vaxerski
 - config/lua: add hl.clear_crashed_lockscreen() and fix tty instructions (#15299) by @vaxerski
 - config/lua: add is_key_down and a key event (#14779) by @zacoons
 - config/lua: add lua-driven custom live gestures (#15393) by @vaxerski
 - config/lua: add physicalWidth and physicalHeight to lua's Monitor (#14657) by @leiserfg
 - config/propRefresher: add capability to execute scheduled prop refresh immediately with lua helper function, add event for prop refresh (#14990) by @erstarr
 - crashreporter: fix SIGSEGV on dladdr1 failure (#15352) by @oclaw
 - decoration/glow: add gradient and angle animation (#15208) by @Undeadamien
 - decoration/shadow: add gradient and angle animation (#14809) by @Undeadamien
 - desktop/windowRule: add `no_auto_hdr` window rule (#14694) by @fxzzi
 - desktop/windowRule: add `stableid:` window selector (#14984) by @LRitzdorf
 - desktop/windowRule: add a suppressevent for X11 configure requests (#13313) by @lichie567
 - desktop/windowrule: add silent option to monitor effect (#14357) by @ArchSav
 - event/bus: add specialActive event to workspace (#14971) by @vaxerski
 - groups: add groupbar disable_when_only option (#15009) by @feelamee
 - groups: sync window monitor/workspace when added to a group (#14478) by @andresilva
 - hyprctl: add config full-reload for performing a ground-up reload (#14748) by @vaxerski
 - hyprctl: add interactive Lua REPL mode (#15043) by @Dregu
 - hyprctl: add onCreatedEmpty field to workspacerules dispatcher data (#14826) by @ikalco
 - hyprtester: add -t option for running specific tests (#14846) by @ArchSav
 - input/tablet: add TabletTool config options for eraser button and tool pressure (#14110) by @marcello505
 - lua/monitor: add set_ functions for raw workspace management (#14875) by @vaxerski
 - lua/objects: add cm and reserved properties to monitor (#14523) by @ndavd
 - meta/lua: add missing notification text field and make timeout required (#14665) by @atomicptr
 - meta/lua: add proper lua stub types to the general config (#14993) by @JustLinuxUser
 - plugins: add api for registering and dispatching events (#14734) by @zacoons
 - protocols/xdg-shell: add support for xdg interactive drags (#15343) by @vaxerski
 - renderer: add a motion blur option to windows (#14911) by @vaxerski
 - renderer: add tonemap settings (#14903) by @UjinT34
 - renderer: add wrapping options to SRenderData (#14666) by @zacoons
 - socket2: add back changefloatingmode and togglegroup events (#14089) by @ErrorNoInternet
 - splashes: add 5th comp winner's splash

## Fixes:
 - Minor fixes today (#14401) by @vaxerski
 - Tests/scroll: fix window hiding test  passing inconsistently (#15384) by @erstarr
 - algo/dwindle: fix moving windows across a split (#15079) by @LRitzdorf
 - algo/master: fix drag-swap with two tiled windows (#14974) by @karaolidis
 - animation: refactor manager, fixup desktopAnimationManager, clean up code (#15302) by @vaxerski
 - binds/submap: fix mouse binds inside submaps (#15060) by @jestemleonard
 - binds/submap: fix submap enter bind == bind inside submap (#14856) by @bendi-github
 - ci: fix codeownersplus (#15383) by @vaxerski
 - AGENTS: add agents.md (#14835) by @vaxerski
 - CI/Arch: add libheif dep
 - code: fix clang-format
 - compositor: fix mon

## v0.55.4 · 2026-06-11T17:10:22Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.55.4

Another small round of patches on top of 0.55.3.

## Fixes backported
 - config/lua: fix layout ctx checking the wrong argument (#15061)
 - desktop/popup: fix subsurface scaling (#14936)
 - gestures: fix live cursorZoom anchoring to a mid-animation value (#14996)
 - gestures: fix toggle cursorZoom sharing a single on/off flag (#14998)
 - groups: fix border color for locked groups (#15015)
 - protocols/foreignToplevel: fix class and title reporting on map and afterwards (#15037)
 - protocols/pointerWarp: fix crash when warp is on a non interactive surf (#15021)
 - renderer: fix SEGV on monitor disconnect (#15048)
 - gestures: clamp toggle cursorZoom like mult and live (#14997)
 - gestures: configure client to final size on fullscreen/float gesture completion (#14981)

## Special Thanks

As always, special thanks to these people / companies for supporting Hyprland's continued development:

### Sponsors

#### Diamond

37Signals

#### Gold

Framework, Butterfly

### Donators

#### Top Supporters:

Tonao Paneguini, Semtex, soy_3l.beantser, Seishin, Nox Æterna, Illyan, Snorezor, Bonsai, Joshua Weaver, ExBhal, DHH, Mikko_Nyman, Kay, iain, TyrHeimdal, miget.com, alexmanman5, Hunter Wesson, --, RaymondLC92, Theory_Lukas, Brandon Wang, Insprill, lzieniew, 3RM, johndoe42, Jas Singh, RayJameson, MadCatX, Xoores, d, Ammar Hossain, Ki☆, inittux111, Arkevius, John Shelburne, DeWattaUnk, ari-cake, gfunnymoney, alukortti, taigrr

#### New Monthly Supporters:

tubid2wenty, Uros Cotman, yafantik, Guy, goblin_engineer, Julius John Puno, Peter Buijs, mb, StellaBuckley, haikuolin, Antibaddy, sludge10123, C Money, Lipski, KampotKaca, Kazuhide Takahashi, Skeptomai, bombadurelli, Rebellen, Álan, StreamCyper, taras, Yury, Sherab, Filinto Delgado, Taddelladius

#### One-time Donators:

Quuton, Selvan, Tyler Adams, tonis, Sam, Dimitrios Liappis, Chivtar, Eric, aponsasan888, bkode, LonestarF1, Chris, Dogmatic Polack, Larry, maxx, MonolithImmortal, edrix, I like GameNative, take my money., nyxloom, Frederic Toemboel, Schmendiey, himes, brandonia, Xphelus, New user, Miguel Flores-Acton, R3dGh0st, Glen, Vitor Moura GUEDES, Anersyum, le_04, Dan, AT, chorr, Awesome, IdeaSpring, Jacobrale, anonymous, Elias Griffin, w00z4, Marcus Edvardsson, Gerhard, Bashmaks, Benjaneb, R4dicalEdward, Matýsek ^^, Michael, Gene Raymond, naivesheep, Neginja, anarchuser, Uta, Francois KERISIT, ay4, Lorenzo santacreu, Gitznik, Jure S, Oliver, Pipes, Mein, ironick, Nlight, Pfoid, DasCleverle, Jaf Endee, DIEBUSTER, senorBeard, alex, Mike, luxxa, JasonPettys, One, Daniel, Sven Eppler, L3rdy, Ilunn, Thorff, XurxoMF, Wonkhester, Brian, Doc O, Mortja, Spook, Miguel Cordero Collar, bennyzen, deah, Sean, Higor, nanea808, Torsten Schieber, I3lack5hield, Kevin Steffer, Zarenno, vfosterm, Nikola, EGB, Dietmar, KilahDentist, Wilf Lin, Rad, Yuza, Supporter, nooob, esseonline, Naresh, darquill, BrnPrs, Pani, BYK, Amaury, nythix, Mika, Patriarch, Gambit, GoatCedric, Adam, MirasM, bl4ckb1rd, Loon, KevOlek, AsciiWolf, Brian Barrow, Anon, Kilian, Cristian M., abhinavmishra094, Dejv78, LinoDB, Trofim, Konstantin, JoaquinCamposPlaza(Ximo), Gabo, Phil, dev2and0m, Neil Brown, zarilion, JavierArias(Javi), Thank you, Mystrasun, Skrazzo, MeguminLoli, revitalist, barcellos-pedro, Juh, Goldie, benabrig, mynus, Daniel Zudel, Grant, Jacob Felknor, Noah, e033x, Nick, Niklas, mkami, Slippy, joenu, Oleksandr, t.i.m., Joss001, M4CETO, Nighty, Donater, David N, Cameron, Ekoban, Kieran, brotiii, Doug, Hypruser#0224975, Shadesofastar, sonicbhoc, GKL, Damien, João Seixas, mothmashine, James Freiwirth, Mek, Krizzkrozz, Panzer, mika.dev, Franky Valley, Sycho sMILEz, Roy, Amundis, willibenmula ❤️, Justin, marvelousIT, pablo, Alex, Ryan, cito, Juergen, Eric Koslow, valerius21, jfk, Andrejs, tyforupdate, skwrl, DaintyFox
 


**Full Changelog**: https://github.com/hyprwm/Hyprland/compare/v0.55.3...v0.55.4

## v0.55.3 · 2026-06-07T10:36:23Z

URL: https://github.com/hyprwm/Hyprland/releases/tag/v0.55.3

A small (or maybe not that small) patch release backporting some fixes from main onto 0.55.2.

## Fixes backported
 - hyprctl: add config full-reload for performing a ground-up reload (#14748)
 - meta/lua: add missing notification text field and make timeout required (#14665)
 - binds/submap: fix submap enter bind == bind inside submap (#14856)
 - compositor: fix monitor re-enabling on hotplug when dpms is off (#14818)
 - compositor: fix render unfocused for subsurfaces (#14718)
 - config/actions: fix null derefs in pin dispatcher (#14914)
 - config: fix VRR not applying on runtime change (#14744)
 - config: fix decoration values to refresh on runtime eval/keyword change (#14590)
 - core: fix a few fd leaks (#14870)
 - decoration/glow: fix visibility when no decorate is set (#14602)
 - desktop/popup: fix reposition artifacts (#14820)
 - desktop/window: fix wrong scale being applied after workspace rules (#14832)
 - internal: fix null deref in setWindowFullscreenInternal when fullscreen state stale (#14725)
 - jeremy: fix auto-generating hyprlang instead of lua config file by default (#14944)
 - renderer: fix `cursor:zoom_rigid` being ignored with detached camera (#14995)
 - renderer: fix screenshader with fp16 (#14918)
 - renderer: minor shader fixes (#14584)
 - screencopy: fix screenshare copyfb pending frames (#14837)
 - xwayland: fix ICCCM synthetic event comparison (#14827)
 - algo/master: guard target in remove (#14756)
 - compositor: give preference to same-workspace windows in getWindowInDirection (#14941)
 - config/lua: improve error handle-ability with Lua `require` (#14937)
 - config/lua: report errors better without check* (#14695)
 - config/monitor: refresh splash texture on monitor reload (#14632)
 - config/propRefresher: schedule frames on screen shader refresh (#14874)
 - desktop/rule: optimize mapping rule properties to strings and engines (#14945)
 - desktop/window: allow focus while held to non-OR X11 windows (#14821)
 - input: aggregate modifier states from all keyboards on focus enter (#14633)
 - internal: replace O_CLOEXEC with FD_CLOEXEC for file descriptor flags (#14909)
 - keybinds: set a fallback releasePending flag for special lua binds (#14600)
 - keybinds: store hit binds first, then execute callbacks (#14743)
 - layersurface: inform layer surfaces of scale changes (#14771)
 - layout/dragController: reset floating offset on ended drag (#14940)
 - layout/scrolling: check if cursor overlaps with target in focusOnInput (#14687)
 - main: gain SCHED_RR and drop CAP_SYS_NICE earlier (#14897)
 - meta/lua: Gestures can accept a lua function (#14649)
 - monitor: move floating windows with layout changes (#14928)
 - monitor: retry transient mode selection failures (#14927)
 - protocols/fractional-scale: track if scale is known and send scales eagerly when known (#14798)
 - protocols: bump xdg-decoration to rev 2 (#14869)
 - renderer/gl: release failed fence syncs (#14956)
 - renderer/gl: skip invalidation clear on empty damage (#14921)
 - renderer: reduce per-frame heap allocations (#14932)
 - renderer: send frame callbacks on presented if no change (#14849)
 - texture: cache G and A swizzle channels aswell (#14605)
 
 
## Special Thanks

As always, special thanks to these people / companies for supporting Hyprland's continued development:

### Sponsors

#### Diamond

37Signals

#### Gold

Framework, Butterfly

### Donators

#### Top Supporters:

Tonao Paneguini, Semtex, soy_3l.beantser, Seishin, Nox Æterna, Illyan, Snorezor, Bonsai, Joshua Weaver, ExBhal, DHH, Mikko_Nyman, Kay, iain, TyrHeimdal, miget.com, alexmanman5, Hunter Wesson, --, RaymondLC92, Theory_Lukas, Brandon Wang, Insprill, lzieniew, 3RM, johndoe42, Jas Singh, RayJameson, MadCatX, Xoores, d, Ammar Hossain, Ki☆, inittux111, Arkevius, John Shelburne, DeWattaUnk, ari-cake, gfunnymoney, alukortti, taigrr

#### New Monthly Supporters:

tubid2wenty, Uros Cotman, yafantik, Guy, go
