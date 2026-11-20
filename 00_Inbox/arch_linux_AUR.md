**AUR (Arch User Repository)** is a community-maintained repository containing package build instructions for Arch Linux software that isn't available in the official Arch repositories.

### **How does AUR installation work?**

Unlike official Arch packages, AUR typically provides a file called `PKGBUILD`, which contains instructions to:

1. Download the software's source code.
2. Install required dependencies.
3. Compile the software (if necessary).
4. Package it into an Arch-compatible package.
5. Install that package using `pacman`.

### **Official repository vs AUR**

| Feature         | Official repository           | AUR                        |
| --------------- | ----------------------------- | -------------------------- |
| Maintained by   | Arch developers               | Community contributors     |
| Package format  | Pre-built packages            | Usually build instructions |
| Installation    | `pacman`                      | `makepkg` or AUR helper    |
| Security review | Official repository processes | User must review PKGBUILD  |

**Important:** AUR is not an official Arch repository. Review the `PKGBUILD` and installation scripts before installing packages.

Official documentation: [Arch Wiki – AUR](https://wiki.archlinux.org/title/Arch_User_Repository).
