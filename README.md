# Tessa
Simplest console based game engine

Visit [Wiki](https://github.com/JackGlow/Tessa/wiki) for more information.
If you getting weird messages turn off debug mode in `settings.txt`.

## Stable release
You can get Stable release at [Releases page](https://github.com/lmnyx/Tessa/releases).

## Tessa.NET
Tessa.NET - is a code name of planned port of Tessa to C#.

## Changelog

### 4 Aug 2019 (1.4.0)
* Added experimental visual editor (prototype), activates on `tessa.py -e`
* Added experimental saving system. (CTRL+C)
* Added experimental inventory system.
* Added `health` and `inventory` to settings. This systems now may be disabled.
* Debug was removed from settings and now debugmode activates on `-d` or `--debug` argument.
* Added `py` action type. So you can do some Doki Doki stuff. *( maybe call tessa.CleanupSaves() )*
### 3 Aug 2019 (1.3.0)
* Added low-freq beep sound on damage.
* Added `go` action type.
* Added `goend` action type.
* Added `sound` action type. *(only WAV)*
* Added `tsound` action type.
* Added `beep` action type.
* Rewritten gameplay.
### 1 Aug 2019 (1.2.0)
* Removed goodbye parameter from settings.
* Removed engine parameter from settings.
* Removed clearing the screen after game ends.
* Added new settings parameter `pastebinplay`.
* Debug parameter now can be removed from settings without error.
* Cleared and optimized tessa_funcs.
* Tessa will now try to recreate needed files if they are missing.
### 30 Jul 2019 (1.1.0)
* Added new action type: `comparestr`.
* [FIX] Fixed variable with `_` was `NoneType`.
