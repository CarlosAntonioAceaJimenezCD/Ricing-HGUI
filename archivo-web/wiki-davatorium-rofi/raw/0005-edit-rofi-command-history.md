**rofi** stores a history of previously used commands. 

This history is used to determine the order in which commands are displayed.

## File Location
**rofi** command history is stored in plaintext under the user's cache directory as  `rofi-3.runcache`  

On most systems the full path will be `~/.cache/rofi-3.runcache`

Note that these files are generated and should not be edited. The format can change at any time.

## Reset History
`rm ~/.cache/rofi-3.runcache`

## Set Cache Directory
See [man page](https://github.com/davatorium/rofi/blob/next/doc/rofi.1.markdown)
