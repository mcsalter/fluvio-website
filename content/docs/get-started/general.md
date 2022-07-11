---
title: Install Guide
menu: General Getting Started
weight: 1
---


There are two things needed for using Fluvio. The first is the Fluvio CLI.
Second is the database on which Fluvio stores its cluster.

Currently there are two options for managing it:
- Using the InfinyOn Cloud
- Installing Kubernetes locally on your computer



## Install Fluvio CLI

The Fluvio CLI (_command-line interface_) is an all-in-one tool for setting up, interacting with, and managing Fluvio clusters.

Install the Fluvio CLI by running the following command:

%copy first-line%
```bash
curl -fsS https://packages.fluvio.io/v1/install.sh | bash
```

### Environment Variables and Fluvio

Fluvio installs to `~/.fluvio/bin/`. This is **not** in the PATH [environment variable], and as such will not be found as a program to execute by default.
Please add it with one of these three commands.

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

## Setting up Fluvio:

At this point, there are multiple ways to install:

{{< h-list tabTotal="5" tabID="0" tabName1="Cloud / Raspberry Pi" tabName2="Linux" tabName3="MacOS (Intel)" tabName4="MacOS (M1)" tabName5="⚠ Windows ⚠">}}

{{<h-item tabNum="1">}}

### Cloud and Raspberry Pi:

Using the InfinyOn Cloud is the easiest way to use Fluvio.

Head on over to the [InfinyOn Cloud signup page](https://infinyon.cloud) to create an account.

<img src="../images/cloud-signup.jpg"
     alt="A screenshot of the InfinyOn new account form, with Name, Organization, Email, and Password fields"
     style="justify: center; max-width: 300px" />

After filling out the form, you'll be greeted with a success message telling you to verify your email. You'll need to complete this step in order to continue.

<img src="../images/cloud-verification.jpg"
     alt="A screenshot of the verification email received after completing the signup form, including a verification link"
     style="justify: center; max-width: 500px" />

You should get a confirmation that your account is ready to use.

<img src="../images/cloud-confirmation.jpg"
     alt="A screenshot of the prompt received after clicking the verification link, saying the account is ready to use"
     style="justify: center; max-width: 300px" />


At this point, you can log in via the Fluvio CLI and start sending and receiving messages to your Fluvio cluster. To log in with the CLI, you'll need to run the `fluvio cloud login` command, then type in your email and password when prompted.

%copy first-line%
```bash
$ fluvio cloud login
InfinyOn Cloud email: batman@justiceleague.com
Password:
```

You'll be able to tell that everything worked if your current profile is set to `cloud`. You can check with this command:

%copy first-line%
```bash
$ fluvio profile current
cloud
```

If you installed fluvio locally it will be listed alongside `cloud`:

%copy first-line%
```bash
$ fluvio profile list
    PROFILE       CLUSTER       ADDRESS                          TLS 
    local         local         localhost:9003                   Disabled 
 *  cloud         cloud         router.infinyon.cloud:9003       Verified
```

-> Use `fluvio profile switch` command to switch between clusters.


{{</h-item>}}

{{<h-item tabNum="2">}}

### Linux

#### Installing a Kubenetes Cluster

For installing the cluster on your local machine, here are some suggested Kubernetes installation options:
  * [K3d](https://k3d.io)
  * [Kind](https://kind.sigs.k8s.io)
  * [Minikube](https://minikube.sigs.k8s.io/docs/start/)

Most of these should be available in your package manager. Either install there or use the links above, it is a simple download!

Not quite as simple as using the cloud, though.

{{</h-item>}}


{{<h-item tabNum="3">}}

### Mac OS Intel

_[This is rather sparse for information]_

#### Installing a Kubenetes Cluster

We recommend [Minikube](https://minikube.sigs.k8s.io/docs/start/) as the Kubernetes cluster of choice. 

%copy first-line%
```bash
$ brew install minikube
```

The minikube driver `hyperkit` is recommended, as other drivers have not been tested. Please install with:

%copy first-line%
```bash
$ brew install hyperkit
```

When running `minikube`, please run with the `--driver=hyperkit` flag:

%copy first-line%
```bash
$ minikube start --driver=hyperkit
```

{{</h-item>}}

{{<h-item tabNum="4">}}

### Mac OS M1

_[A bit less sparse compared to Intel]_

#### Installing a Kubenetes Cluster

We recommend using [Kind](https://kind.sigs.k8s.io) as the Kubernetes cluster for the M1 Macs. 

Please either follow the instructions in the link, or use Homebrew:

%copy first-line%
```bash
$ brew install kind
```

#### Start a Kubernetes cluster

To configure kind cluster creation, you will need to create a YAML config file. This file follows Kubernetes conventions for versioning, etc.
Create a file named: `config.yaml` in a directory `k8-util/cluster` with the following content:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    # port forward 80 on the host to 80 on this node
    extraPortMappings:
      - containerPort: 30003 #sc
        hostPort: 30003
        protocol: TCP
      - containerPort: 30004 #spu 1
        hostPort: 30004
        protocol: TCP
      - containerPort: 30005 #spu 2
        hostPort: 30005
        protocol: TCP
      - containerPort: 30006 #spu 3
        hostPort: 30006
        protocol: TCP

```
Start a Kubernetes cluster locally with by running the following in a terminal window:

%copy first-line%
```bash
$ kind create cluster --config k8-util/cluster/config.yaml 
```

{{</h-item>}}

{{<h-item tabNum="5">}}

### Windows

~> At the current moment Windows is not supported.

IF you are determined to run this on Windows, we would suggest installing the Fluvio CLI in [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) 
(as bash scripts will not run in Windows) and use the InfinOn Cloud.



_[Should we test out running k8s and fluvio in wsl?
I guess best suggestion would be to install fluvio CLI and use the cloud]_

{{</h-item>}}
{{</h-list>}}

## Checking Installs

Some of Kubernetes installation will install `kubectl` and `helm`, these are important and useful for running Kubernetes. 
`Docker` is a requirement for some Kubernetes systems, and may not be installed automatically.
You can check if they are installed by running:

%copy first-line%
```bash
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.2", GitCommit:"f66044f4361b9f1f96f0053dd46cb7dce5e990a8", GitTreeState:"clean", BuildDate:"2022-06-15T14:22:29Z", GoVersion:"go1.18.3", Compiler:"gc", Platform:"linux/amd64"}
Kustomize Version: v4.5.4
Server Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.1", GitCommit:"3ddd0f45aa91e2f30c70734b175631bec5b5825a", GitTreeState:"clean", BuildDate:"2022-05-24T12:18:48Z", GoVersion:"go1.18.2", Compiler:"gc", Platform:"linux/amd64"}
```

-> Note, the output of this command is deprecated, and will be replaced by the output of `kubectl version --short` in the future. Don't worry if there is a warning attached to it.

%copy first-line%
```bash
$ helm version
version.BuildInfo{Version:"v3.8.2", 
GitCommit:"d506314abfb5d21419df8c7e7e68012379db2354", 
GitTreeState:"clean", 
GoVersion:"go1.17.11"}
```

%copy first-line%
```bash
$ docker --version
Docker version 20.10.17-ce, build a89b84221c85
```

If any of these were not installed, you can install them the following way:


### Install Kubectl

`kubectl` is the Kubernetes command-line tool. It is used to run commands against Kubernetes clusters.

Follow the instructions at the [kubectl installation page] and you will soon have `kubectl` installed.

[kubectl installation page]: https://kubernetes.io/docs/tasks/tools/#kubectl

### Install Helm

`helm` is the package manager for Kubernetes. 

Follow the instructions at the [helm installation page] and `helm` can easily be installed.

[helm installation page]: https://v3.helm.sh/docs/intro/install/ 

### Install Docker

`Docker` is container system used by several Kubernetes systems. It helps ensure that everything is in its own little custom OS.

Follow the instructions at the [Docker installation guide] – they should tell you how to download and install `Docker` for your chosen OS.

[Docker installation guide]: (https://docs.docker.com/engine/install/)

## start Fluvio cluster

You can start a Fluvio cluster with the command `fluvio cluster start`.

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

If you need help, you can reach us on [Discord](https://discordapp.com/invite/bBG2dTz)
or in [Github](https://github.com/infinyon/fluvio/issues).


### Related topics

_[warning Link rot]_

- ["Hello World" in Java](https://www.infinyon.com/tutorials/java/hello-world/)
- ["Hello World" in Node.js](https://www.infinyon.com/tutorials/node/hello-world/)
- ["Hello World" in Python](https://www.infinyon.com/tutorials/python/hello-world/)
- ["Hello World" in Rust](https://www.infinyon.com/tutorials/rust/hello-world/)

---

If you run into any problems along the way, make sure to check out our [troubleshooting]
page to find a fix.

[troubleshooting]: {{< ref "/docs/operations/troubleshoot.md" >}}
