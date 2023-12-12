import get_methods
import install_methods

# exts = get_methods.get_gnome_extensions()
# install_methods.install_gnome_extensions(exts)
apt_repos = get_methods.get_apt_repos()
print(apt_repos)
