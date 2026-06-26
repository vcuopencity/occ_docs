(nmap-instructions)=
# How to use `nmap`

`nmap` ("Network Mapper") is a free tool that scans a network for devices. We use it for one job: after you image a Pi and power it on, you know its **hostname** (you set it during imaging) but not its **IP address**. Pointing `nmap` at the hostname resolves it and tells you the IP.

## Install it

On your own machine (not the Pi):

```bash
# Ubuntu
sudo apt install nmap
```

Windows users can grab the installer from [nmap.org/download](https://nmap.org/download).

## Get the Pi's IP

Run a scan against the hostname you set during imaging (here, `hospital-floor1`):

```bash
nmap hospital-floor1
```

`nmap` resolves the hostname and prints a scan report. The IP address is on the first line, in parentheses next to the hostname:

```
Nmap scan report for hospital-floor1 (10.213.1.91)
Host is up (0.012s latency).
```

In this example the Pi's IP is `10.213.1.91`. If the bare hostname doesn't resolve, try `nmap hospital-floor1.local` instead.

Now SSH straight into that IP:

```bash
ssh pi@10.213.1.91
```
