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