This feature allows a user to define their own keywords to replace in their `.base` files, updating the `$HOME/.config/wpg/keywords.conf` file these custom keywords take precedence over `wpgtk`'s default keywords so if there is any one keyword you want to override, here's how:


```python
[default]
custom = #fdfdfd
font01 = Times new Roman
font02 = Comic Sans
inactive = {color9} # let's pretend I don't like the inactive color

[custom-name]
custom = #000000
font01 = Font Awesome
font02 = Sf Pro
inactive = {color7}
```


Now, to add new keywords you can do it via the config file as pictured above, or via the GUI, in the `Keywords` tab

Notice the existence of various categories inside the `keywords.conf` file, this means you can easily switch between various definitions of keywords by just setting which one of those to use using the dropdown in the GUI

You can now place these keywords in any `.base` files surrounded by `{}` and they will be replaced by the value on the right when the color-scheme is applied, this allows for things like unified fonts across various configuration files and other amazing things.

<p align="center">
  <img src="https://i.imgur.com/9C0J1qZ.png" alt="keyword-tab"/>
</p>

A typical base file with custom keywords (in this example we use the ones defined above)
will look like this:

```
background-color: {custom}
bar-font: {font01}
task-font: {font02}
```

