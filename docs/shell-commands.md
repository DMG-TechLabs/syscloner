# Shell Commands

## Gnome Extensions

```bash
gnome-extensions list
```

## Snap Packages

```bash
snap list | tr -s " " | cut -d " " -f1 | tail -n +2
```

## Flatpak Packages

```bash
flatpak list | tr -s '\t' | cut -d$'\t' -f1
```
