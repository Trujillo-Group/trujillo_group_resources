# VI Editor Tutorial

VI is a powerful and versatile text editor commonly found on Unix-based systems. 
It has a unique mode-based interface that might seem daunting at first, but once you get the hang of it, you'll find it efficient and powerful. 

Original VI is not commonly used anymore, more recent version are used instead (e.g. [NVIM](https://neovim.io/)).
The information bellow works for any of the newer versions.

This tutorial will introduce you to the basics of VI, including the different modes, essential keybindings, and general usage.

## Modes in VI

VI operates in three main modes: Normal Mode, Insert Mode, and Command-Line Mode.

- **Normal Mode**: This is the default mode when you open VI. In this mode, you can navigate through the text, delete, copy, and paste text, and perform various editing tasks.

- **Insert Mode**: This mode is used for inserting or editing text. To enter Insert Mode:
    - Press `i` to insert before the cursor.
    - Press `a` to insert after the cursor.
    - Press `I` to insert at the beginning of the current line.
    - Press `A` to insert at the end of the current line.
    - Press `o` to open a new line below the current line and enter Insert Mode.
    - Press `O` to open a new line above the current line and enter Insert Mode.

- **Command-Line Mode**: This mode is used for saving, quitting, searching, and other more complex commands (e.g. substiting text). To enter Command-Line Mode:
    - Press : in Normal Mode.

### Navigation:

| Keybinding | Description                                    |
|------------|------------------------------------------------|
| `h`        | Move left (equivalent to the left arrow key).  |
| `j`        | Move down (equivalent to the down arrow key).  |
| `k`        | Move up (equivalent to the up arrow key).      |
| `l`        | Move right (equivalent to the right arrow key).|
| `w`        | Move forward by word.                          |
| `b`        | Move backward by word.                         |
| `0`        | Move to the beginning of the current line.     |
| `$`        | Move to the end of the current line.           |
| `G`        | Move to the end of the file.                   |
| `gg`       | Move to the beginning of the file.             |
| `{`        | Move up one paragraph.                         |
| `}`        | Move down one paragraph.                       |

### Editing:

| Keybinding | Description                                        |
|------------|----------------------------------------------------|
| `x`        | Delete the character under the cursor.             |
| `dd`       | Delete the current line.                           |
| `yy`       | Copy (yank) the current line.                      |
| `p`        | Paste the copied or deleted text after the cursor. |
| `P`        | Paste the copied or deleted text before the cursor.|
| `u`        | Undo the last change.                              |
| `Ctrl + r` | Redo the last undone change.                       |

### Saving and Quitting:

| Command        | Description                                   |
|----------------|-----------------------------------------------|
| `:w`           | Save the file.                                |
| `:q`           | Quit (close) the file.                        |
| `:q!`          | Quit without saving (force quit).             |
| `:wq` or `ZZ`  | Save and quit.                                |
| `:x`           | Save and quit (similar to `:wq`).             |

### Searching:

| Keybinding | Description                                   |
|------------|-----------------------------------------------|
| `/`        | Enter search mode.                            |
| `n`        | Find the next occurrence.                     |
| `N`        | Find the previous occurrence.                 |

## General Usage

1. **Opening a File**:
   - Open a terminal.
   - Type `vi` followed by the filename to open an existing file or `vi` to create a new one (`vi [filename]`).

2. **Switching Modes**:
   - Use `i`, `a`, `I`, or `A` to enter **Insert Mode**.
   - Press `Esc` to exit Insert Mode and return to **Normal Mode**.

3. **Making Edits**:
   - Use the navigation and editing keybindings mentioned above to modify the text.

4. **Saving and Quitting**:
   - To save changes, press `:` to enter Command-Line Mode, then type `w` and press `Enter`.
   - To quit VI, press `:` to enter Command-Line Mode, then type `q` and press `Enter`.
   - To save and quit, combine the above two steps with `:wq` or simply `ZZ`.

Remember that VI can be challenging to learn initially, but with practice, it becomes a powerful tool for text editing and manipulation. 
Start with these basics, and as you become more comfortable, explore additional features and commands and, as always, do not hesitate to ask any member of the group!

Good luck!



