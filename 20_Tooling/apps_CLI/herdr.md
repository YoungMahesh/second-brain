
Default prefix mode keymap: `ctrl+b`

```bash
# start herdr on local computer
herdr
# start herdr on remote server
# instead of `ssh <server-name>` use `herdr --remote <server-name>`
herdr --remote <server-name>

# set prefix mode to `ctrl+space`, as we use default `ctrl+b` to move backward in terminal
prefix-mode q # detach; processes will continue run in background
prefix-mode v # split tab veritically
prefix-mode - # split tab horizontally

# after config change, you must stop herdr server and then launch herdr again
herdr server stop

# list keymaps
prefix-mode ?
# switch workspaces(tabs)
prefix-mode <tab> # <tab> = 1 or 2 or 3 ...
```

My config:
To reload config, execute: `herdr server reload-config`
```toml
# ~/.config/herdr/config.toml 
onboarding = false

[keys]
prefix = "ctrl+space"
new_tab = "prefix+t"

[keys.indexed]
tabs = "ctrl"       # e.g. "ctrl" makes ctrl+1..9 switch tabs directly
```

### connect herdr mobile app to herdr on remote server
1. Connect both devices to [tailscale network](10_Foundations/linux/vpn/tailscale.md)
2. From tailscale dashboard (Network -> Machines), click 'Setup SSH' on remote-server device
3. Open herdr app -> Click 'Connect new machine'
    - Address: \<tailscale-name-of-remote-server>
    - User: \<username on remote-server> (e.g. root)
    - Port: 22
4. After clicking connect, you will be asked to authenticate ssh connection from mobile-phone to remove-server through tailscale login from browser
5. Authenticate, and you are connected.
