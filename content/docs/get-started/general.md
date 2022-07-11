---
title: Install Guide
menu: General Getting Started
weight: 1
---

There are two things needed for using Fluvio. The first is the Fluvio CLI.
Second is the database on which Fluvio stores it's cluster.

Currently there are two options for managing it:
- Using the InfinyOn Cloud
- Installing Kubernetes locally on your computer

## Install Fluvio CLI

The Fluvio CLI (_command-line interface_) is an all-in-one tool for setting up, interacting, and managing with Fluvio clusters.

Install the Fluvio CLI by running the following command:

%copy first-line%
```bash
curl -fsS https://packages.fluvio.io/v1/install.sh | bash
```

### Environment Variables and Fluvio

Fluvio installs to `~/.fluvio/bin/`. This is not in the PATH [environment variable], and as such will not be found as a program to execute by default. Please add it with one of these three commands.

%copy first-line%
```bash
$ export PATH=${HOME}/.fluvio/bin:${PATH} >> ~/.bashrc
```

%copy first-line%
```zsh
$ export PATH=${HOME}/.fluvio/bin:${PATH} >> ~/.zshrc
```

%copy first-line%
```fish
$ fish_add_path $HOME/.fluvio/bin
```
[environment variable]:(https://www.ibm.com/docs/en/aix/7.2?topic=accounts-path-environment-variable) 
## Connect to InfinyOn Cloud

This is the easiest way of getting started with Fluvio.
For the small price of creating an account, you too can avoid setting up a Kubernetes cluster!

Follow the instructions below to be on your way.

[Cloud with InfiniOn]

## Install Dependencies Locally

If you decide to run a Fluvio cluster locally, you must set up a Kubernetes cluster.
Please follow these guides for setting it up on your OS of choice:

### Linux

[Kubernetes on Linux]

~> You can install the Fluvio CLI on a Raspberry Pi, but at the current moment local clusters are not supported.

### Mac OS

[Kubernetes on MacOS (Intel)]

[Kubernetes on MacOS (M1)]

### Windows

~> At the current moment Windows is not supported.

_[Should we test out running k8s and fluvio in wsl?
I guess best suggestion would be to install fluvio CLI and use the cloud]_

[Cloud with InfiniOn]: {{< ref "/docs/get-started/cloud.md" >}}
[Kubernetes on Linux]: {{<ref "/docs/get-started/linux.md">}}
[Kubernetes on MacOS (Intel)]: {{<ref "/docs/get-started/mac.md">}}
[Kubernetes on MacOS (M1)]: {{<ref "/docs/get-started/mac_m1.md">}}


## Getting help

If you need help, you can reach us on [Discord](https://discordapp.com/invite/bBG2dTz),
or in [Github](https://github.com/infinyon/fluvio/issues)
