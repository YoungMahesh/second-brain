### Enable dictation

#### 1. install `voxtype`
At first, when you click on 'Dictate' icon on 'Status Bar'/'Waybar', you will get error: `voxtype: command not found`

For following [official voxtype documentation](https://voxtype.io/docs/#arch-linux), you can install voxtype with:
```sh
paru -S voxtype-bin
```

If paru is not already installed, checkout [paru documentation](./paru.md)


### 2. install base model

```sh
# download base model (Whisper - base english)
voxtype setup --download

# start voxtype
systemctl --user restart voxtype
```

### 3. define key for dictation

Update `~/.config/hypr/bindings.lua` with this command:
```lua
-- start and stop voxtype recording with contrl+0 key
o.bind("CTRL+0", "Toggle dictation", "voxtype record toggle")
```
