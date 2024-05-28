# templates

Here we store jinja (j2) templates.  
Jinja templates are pre-defined files (not always yaml) that can project variables with {{ }} but also has a full power of loops and if-then-else.  

https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html  

You can use the "template" module to convert a template to a file.  
You can also use the "lookup('template',...)" plugin to load the result of a template.  

- family_summary.j2 : will apply some summary calculations on the families variables we load in the vars/families.yaml
- appache.conf.j2 : holds an xml-template we need to configure an apache website.
- index.html.j2 : holds an html-template that lists the variables found in families.yaml

