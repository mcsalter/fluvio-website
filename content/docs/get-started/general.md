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

## Setting up Fluvio:

At this point, there are multiple ways to install

{{< h-list tabTotal="5" tabID="2" tabName1="Cloud / Raspberry Pi" tabName2="Linux" tabName3="MacOS" tabName4="⚠ Windows ⚠">}}

{{<h-item tabNum="1">}}
{{<download-card>}}

### Cloud and Raspberry Pi:

This is the easiest way of getting started with Fluvio.

_[Will mostly be a repeat of cloud.]_



{{</download-card>}}
{{</h-item>}}

{{<h-item tabNum="2">}}
{{<download-card>}}

### Linux

#### Installing a Kubenetes Cluster

For installing the cluster on your local machine, here are some suggested Kubernetes installation options:
  * [K3d](https://k3d.io)
  * [Kind](https://kind.sigs.k8s.io)
  * [Minikube](https://minikube.sigs.k8s.io/docs/start/)


{{</download-card>}}
{{</h-item>}}


{{<h-item tabNum="3">}}
{{<download-card>}}

### Mac OS

_[]_



{{</download-card>}}
{{</h-item>}}

{{<h-item tabNum="4">}}
{{<download-card>}}

### Windows

~> At the current moment Windows is not supported.

_[Should we test out running k8s and fluvio in wsl?
I guess best suggestion would be to install fluvio CLI and use the cloud]_

{{</download-card>}}
{{</h-item>}}
{{</h-list>}}

## Checking Installs

Some of Kubernetes installation will install `kubectl` and `helm`.  You can check their install status by:

%copy first-line%
```bash
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.2", GitCommit:"f66044f4361b9f1f96f0053dd46cb7dce5e990a8", GitTreeState:"clean", BuildDate:"2022-06-15T14:22:29Z", GoVersion:"go1.18.3", Compiler:"gc", Platform:"linux/amd64"}
Kustomize Version: v4.5.4
Server Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.1", GitCommit:"3ddd0f45aa91e2f30c70734b175631bec5b5825a", GitTreeState:"clean", BuildDate:"2022-05-24T12:18:48Z", GoVersion:"go1.18.2", Compiler:"gc", Platform:"linux/amd64"}
```

-> Note, the output of this command is soon due to change, do not worry if there is a warning attached to it.

%copy first-line%
```bash
$ helm version
version.BuildInfo{Version:"v3.8.2", 
GitCommit:"d506314abfb5d21419df8c7e7e68012379db2354", 
GitTreeState:"clean", 
GoVersion:"go1.17.11"}
```

If `kubectl` or `helm` were not installed, you can installed them the following way:


### Install Kubectl

`kubectl` is the Kubernetes command-line tool. It is used to run commands against Kubernetes clusters.

Follow the instructions at the [kubectl installation page] and follow the instructions to download and install `kubectl` on Linux.

[kubectl installation page]: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/ 

### Install Helm

`helm` is the package manager for Kubernetes. 

Follow the instructions at the [helm installation page] and follow the instructions to download and install `helm` on Linux.

[helm installation page]: https://v3.helm.sh/docs/intro/install/ 

## start Fluvio cluster

you can start a Fluvio cluster with the command `fluvio cluster start`.

%copy first-line%
```bash
$ fluvio cluster start
Current channel: stable
📝 Running pre-flight checks
    ✅ Kubectl active cluster minikube at: https://192.168.49.2:8443 found
    ✅ Supported helm version 3.8.2+gd506314 is installed
    ✅ Supported Kubernetes server 1.23.3 found
    ✅ Fixed: Fluvio Sys chart 0.9.30 is installed
    ✅ Previous fluvio installation not found
🎉 All checks passed!
✅ Installed Fluvio app chart: 0.9.30
✅ Connected to SC: 192.168.49.2:30003
👤 Profile set
✅ SPU group main launched with 1 replicas
🎯 Successfully installed Fluvio!

```

## Verify Fluvio is installed

You can check the information of Fluvio by running:

%copy first-line%
```bash
$ fluvio version
Release Channel      : stable
Fluvio CLI           : 0.9.30
Fluvio CLI SHA256    : b2c7ed79f8c252539f3e59218569f6b6b3c451ca0f3f66a25ae760f2635bee9a
Fluvio channel frontend SHA256 : 6f71beb65c7ece8a13695e4fb438a5bf5603794ffc9fccfdef6406fe0e721322
Fluvio Platform      : Not available (minikube)
Git Commit           : 140f78317abaec4d83e01685c8ce522aeb8c0138
OS Details           : openSUSE Tumbleweed 20220706 (kernel 5.18.9-1-default)
=== Plugin Versions ===
Infinyon Cloud CLI (fluvio-cloud) : 0.1.8
Fluvio Runner (fluvio-run)     : 0.0.0
```

## Hello, Fluvio!

Congratulations, you've successfully installed Fluvio on your local machine! 

Let's use the Fluvio CLI to play with some basic functionality.

The first thing we need to do is create a [topic].

%copy first-line%
```bash
$ fluvio topic create greetings
topic "greetings" created
```

Now that we have a topic, we can [produce] some messages!

Use the following command to send a message to the `greetings` topic:

%copy first-line%
```bash
$ echo "Hello, Fluvio" | fluvio produce greetings
```

Finally, we can [consume] messages back from the topic

%copy first-line%
```bash
$ fluvio consume greetings -B -d
Consuming records from the beginning of topic 'greetings'
Hello, Fluvio
```

Way to go! You're well on your way to writing real-time distributed apps with Fluvio!

Next, check out our [Tutorials page] to see real-world examples of Fluvio in action.

[topic]: {{< ref "/cli/commands/topic.md" >}}
[produce]: {{< ref "/cli/commands/produce.md" >}}
[consume]: {{< ref "/cli/commands/consume.md" >}}
[Tutorials page]: https://www.infinyon.com/tutorials 

## Getting help

If you need help, you can reach us on [Discord](https://discordapp.com/invite/bBG2dTz).
or in [Github](https://github.com/infinyon/fluvio/issues).


### Related topics

~> warning Link rot

- ["Hello World" in Java](https://www.infinyon.com/tutorials/java/hello-world/)
- ["Hello World" in Node.js](https://www.infinyon.com/tutorials/node/hello-world/)
- ["Hello World" in Python](https://www.infinyon.com/tutorials/python/hello-world/)
- ["Hello World" in Rust](https://www.infinyon.com/tutorials/rust/hello-world/)

---

If you run into any problems along the way, make sure to check out our [troubleshooting]
page to find a fix.

[troubleshooting]: {{< ref "/docs/operations/troubleshoot.md" >}}
