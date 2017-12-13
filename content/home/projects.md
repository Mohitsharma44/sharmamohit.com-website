+++
# Projects widget.
# This widget displays all projects from `content/project/`.
widget = "projects"
active = true
date = "2016-04-20T00:00:00"

title = "Projects"
subtitle = ""

# Order that this section will appear in.
weight = 50

# View.
# Customize how projects are displayed.
# Legend: 0 = list, 1 = cards.
view = 1

# Filter toolbar.

# Default filter index (e.g. 0 corresponds to the first `[[filter]]` instance below).
filter_default = 0

# Add or remove as many filters (`[[filter]]` instances) as you like.
# Use "*" tag to show all projects or an existing tag prefixed with "." to filter by specific tag.
# To remove toolbar, delete/comment all instances of `[[filter]]` below.
[[filter]]
  name = "All"
  tag = "*"

[[filter]]
  name = "IoT"
  tag = ".iot"

[[filter]]
  name = "Imaging"
  tag = ".imaging"

[[filter]]
  name = "Config Mgmnt Tools"
  tag = ".config mgmnt tools"

[[filter]]
  name = "python"
  tag = ".python"

[[filter]]
  name = "kubernetes"
  tag = ".kubernetes"

[[filter]]
  name = "c/c++"
  tag = ".c"

[[filter]]
  name = "Pi"
  tag = ".pi"

[[filter]]
  name = "Container"
  tag = ".container"

+++
