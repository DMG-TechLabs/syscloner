# syscloner

A cli tool to backup and restore your linux system

## Prerequisites

- [python3](https://www.python.org/downloads/)

## Install

```console
git clone https://github.com/DMG-TechLabs/syscloner
cd syscloner
./install.sh
```

## Usage

### Backup

To backup everything available try:

```console
syscloner backup example --all --git-repos=~/repos
```

If you want to select exactly what is being backed up try `syscloner -h` to see the options available

```
  --system                  include system settings
  --apt                     include apt packages
  --snap                    include snap packages
  --flatpak                 include flatpak packages
  --themes                  include shell themes
  --exts                    include shell extensions
  --keys                    include repository keys
  --ssh                     include ssh keys
  --git-repos GIT_REPOS     include git repos (Specify path)
  --apt-repos               include apt repos
```

**WARNING:** If the `--ssh` option is being used, explicitely or through `--all`, everything in the `~/.ssh` directory is being copied in the cvf file. So be careful where you upload the generated cvf file

### Restore

To restore everything in your computer try:

```console
syscloner restore example_ub_gn.cvf --all
```

Or again select excactly what you want to restore using the options above

## System Compatibility

Current support

| Distro     |
|------------|
| Debian     |
| Ubuntu     |

| GUI        |
|------------|
| Gnome      |

Checking system compatibility on restore is not perfect (*yet*)

## Help

Try `syscloner -h` or `man syscloner`

## Lisense

[MIT](./LICENSE)

## Authors

- [ThanasisGeorg](https://github.com/ThanasisGeorg)
- [creatorkostas](https://github.com/creatorkostas)
- [KDesp73](https://github.com/KDesp73)

