[Paru](https://github.com/Morganamilo/paru) is your standard pacman wrapping [AUR](./arch_linux_AUR.md) helper with lots of features and minimal interaction.
It automates the process of downloading, building and installing AUR packages.

There are no pre-built Linux binaries provided for Paru installation, this is the [official way to install](https://github.com/Morganamilo/paru#installation)

```sh
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

If installation:
```sh
# check if installation is working
paru --version

# remove downloaded paru repository
rm -rf paru
```
