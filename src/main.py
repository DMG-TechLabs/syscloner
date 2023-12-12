import get_methods
import install_methods

# exts = get_methods.get_gnome_extensions()
# install_methods.install_gnome_extensions(exts)

print(get_methods.get_apt_packages(), "\n\n\n")
print(get_methods.get_snap_packages(), "\n\n\n")
print(get_methods.get_flatpak_packages(), "\n\n\n")
