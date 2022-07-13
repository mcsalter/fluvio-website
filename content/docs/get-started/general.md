---
title: Install Guide
menu: General Getting Started
weight: 1
---

All you need to get started with Fluvio is to install the Fluvio CLI, and link it to a database.

Currently there are two options for the database:
- Using the [InfinyOn Cloud](https://www.infinyon.com/cloud/), the easiest (and recommended) option.
- Installing Kubernetes locally on your computer.

## Install The Fluvio CLI

The Fluvio <abbr title="command-line interface">CLI</abbr> is an all-in-one tool for setting up, interacting with, and managing Fluvio clusters.

Install the Fluvio CLI by running the following command:

%copy first-line%
```bash
$ curl -fsS https://packages.fluvio.io/v1/install.sh | bash
```

### Environment Variables and Fluvio

Fluvio installs to `~/.fluvio/bin/`. This is not in the [PATH environment variable](https://www.ibm.com/docs/en/aix/7.2?topic=accounts-path-environment-variable), and as such will not be found as a program to execute by default. Please add it with one of these three commands.

**Zsh**

%copy first-line%
```zsh
$ export $PATH="$HOME/.fluvio/bin:${PATH}" >> ~/.zshrc
```

**Bash**

%copy first-line%
```bash
$ export $PATH="$HOME/.fluvio/bin:${PATH}" >> ~/.bashrc
```

**Fish**

%copy first-line%
```fish
$ fish_add_path $HOME/.fluvio/bin
```
## Connect to InfinyOn Cloud

This is the easiest way to get started with Fluvio.
(You too can avoid setting up a Kubernetes cluster!)

Follow the instructions in the link to set up an InfiniOn cloud account and connect it to Fluvio.

**[Cloud with InfiniOn]**

## Install Dependencies Locally

If you decide to run a Fluvio cluster locally, you must set up a Kubernetes cluster.
Please follow these guides for setting it up on your OS of choice:

### docker
Docker can be a quiet dependency of several Kubernetes systems. You can test if it is installed with:

%copy first-line%
```bash
$ docker --version
Docker version 20.10.17-ce, build a89b84221c85
```
If you need to install docker, follow the instructions found on the [docker install guide](https://docs.docker.com/engine/install/).

### Linux

[Kubernetes on Linux]

### Mac OS

[Kubernetes on MacOS (Intel)]

[Kubernetes on MacOS (M1)]

### Raspberry Pi

~> Local Fluvio clusters are not currently supported on the Raspberry Pi. Please follow the instructions for using [InfiniOn Cloud]({{< ref "/docs/get-started/cloud.md" >}}) instead.

### Windows

~> Windows is not currently supported.

_[Should we test out running k8s and fluvio in wsl?
I guess best suggestion would be to install fluvio CLI and use the cloud]_

[Cloud with InfiniOn]: {{< ref "/docs/get-started/cloud.md" >}}
[Kubernetes on Linux]: {{<ref "/docs/get-started/linux.md">}}
[Kubernetes on MacOS (Intel)]: {{<ref "/docs/get-started/mac.md">}}
[Kubernetes on MacOS (M1)]: {{<ref "/docs/get-started/mac_m1.md">}}


## Getting help

If you need help, please reach out to us on [Discord](https://discordapp.com/invite/bBG2dTz),
or post an issue on [Github](https://github.com/infinyon/fluvio/issues)
