# Site Plan

based on the [diataxis](https://diataxis.fr/start-here/) philosophy for documentation.

this file just contains my brain map for what the documentation structure should look like.

## Get Started
- about the testbed
- testbed goals
- standards and conventions
- systems and their maintainer/contributors
- wsl/ubuntu/ros2 setup (point to ros2 tutorials)
- practice (maybe?)

## Systems
Each system should try and use the template at the bottom.

- traffic lights
- street lights
- buildings
  - hospital building
  - residential building
  - office building
- ITS vehicles
- ITS drones
- vicon
- factory
    - arm
    - conveyor
- occ_docs

## Platform & Architecture
- ROS 2
- Zenoh
- network topology / IPs
- namespacing & coordinate-frame conventions

## Lab & Device Setup
- hardware
  - wiring
  - power/mounting
- setup
  - imaging Raspberry Pis
  - imaging Jetsons
- networking
  - finding a device on the network (`nmap`)
  - static IPs
- maintenance
  - updating software on all devices
  - replacing a device

## Contributing
- documentation about documentation and how to contribute
- small markdown tutorial
- adding sections
- linking sections/pages
- adding images
- local build and test
- adding a new system
- etc...


---

## Diátaxis template

```
systems.md                       # :glob: systems/*
systems/
  traffic_lights.md              # explicit toctree
                                 #   traffic_lights/tutorials
                                 #   traffic_lights/how_to
                                 #   traffic_lights/reference
                                 #   traffic_lights/explanation
  traffic_lights/
    tutorials.md    + tutorials/    # setup instructions
    how_to.md       + how_to/       # usage: gui, controllers, arduino
    reference.md    + reference/    # package docs, param/config docs, resources
    explanation.md  + explanation/  # decisions, progress, goals, current approaches
```

What goes in each Diátaxis category:
- **Tutorials:** learning-oriented, step-by-step setup (get it running the first time).
- **How-to guides:** task-oriented usage (operate the GUI, running Arduino, etc.).
- **Reference:** information-oriented: package docs, param/config docs
  ([example](https://docs.nav2.org/configuration/packages/configuring-navfn.html)), resources.
- **Explanation:** understanding-oriented: reasons behind decisions, current progress, future goals, current approaches.