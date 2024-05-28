# filter plugins

"filter_plugins" is the typical folder to store custom filter plugins.

A filter plugin is typically used like :

```
"myinput" | my_filter_plugin(additional_attributes)
```

In our case we create simple plugins to manipulate strings or calculate numbers.  

The advantage vs "jinja" is that you have the full python power.  It's sometimes easier to code your own plugin with the specific logic you need.  