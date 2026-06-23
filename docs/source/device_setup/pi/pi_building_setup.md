# How to setup a Raspberry Pi for a building

1. **Setup the Raspberry Pi with the following steps:**
    - Download Raspberry Pi Imager <a href="https://www.raspberrypi.com/software/">here</a>
    - Select your Raspberry Pi device
    - Under "Other general-purpose OS" select the OS: `UBUNTU SERVER 24.04.2 LTS (64-BIT)`
    - Select your micro-SD card storage
    - Enter appropriate hostname (use `<building-name>-floor<floor-id>` for floor-level pis; use `<building-name>-master` for building-level pis)
        - E.g. `hospital-floor1` for a Pi on floor 1 of the hospital building
        - E.g. `hospital-master` for the building-level Pi in the hospital building
    - **All Pi's must have the user as `pi` and the password as `raspberry`**
    - Enter the Wi-Fi settings, if you do not, you will be unable to SSH into the Pi after setup.
    - Make sure to enable SSH and use password authentication for SSH.
    - Click "Write" and wait for the process to complete.

2. **After the Raspberry Pi has been flashed, insert the micro-SD card into the Raspberry Pi and power it on.** 
    - Wait for the Raspberry Pi to boot up. This may take a few minutes.

3. **SSH into the Raspberry Pi** 
    - Use the hostname you set in step 1. You can use the following command:
    ```
    ssh pi@<hostname>.local
    ```
    - Make sure you are on the same network as the Raspberry Pi. If you are unable to connect using the hostname, you can also try connecting using the IP address of the Raspberry Pi. You can find the IP address by checking your router's connected devices list or by using a network scanning tool like `nmap`.
4. **Login with the username `pi` and the password `raspberry`.**

5. **Set a static IP address for the Raspberry Pi.**
    > **Note:** Almost all devices in the OpenCyberCity Testbed project are configured to use static IP addresses. Some address ranges are reserved for specific types of devices, or devices within specific systems. <br> All this information is documented in the IP Address Registry spreadsheet in the Google Drive. Make sure to refer to this document to find the appropriate static IP address for the Raspberry Pi you are setting up.<br> For example, all floor-level Raspberry Pis in the hospital building are assigned static IP addresses in the range `10.213.1.91 -> 10.213.1.94` (90 is the master, and 91-94 are the floor-level Pis for floors 1-4, respectively).
    - Run `ip route` to check the current IP address of the gateway and the network interface name (e.g. `eth0` or `wlan0`).
        - Look for the line that starts with `default via` to find the gateway IP address and the network interface name. Take note of these values as you will need them later.
    - Run `resolvectl status` to check the current DNS server IP address.
        - Look for the line that starts with `DNS Servers` to find the DNS server IP address. Take note of this value as you will need it later. If they are identical to the gateway IP address, you can use the gateway IP address as the DNS server IP address in the next step.
    - Edit the netplan configuration file to set a static IP address for the Raspberry Pi. You can use the following command to open the file in a text editor:
    ```
    cd /etc/netplan
    sudo nano 50-cloud-init.yaml
    ```
    You will see a configuration file that looks something like this:
    ```yaml
    network:
    version: 2
    ethernets:
      eth0:
        optional: true
        dhcp4: true
        dhcp6: true
    wifis:
      wlan0:
        optional: true
        dhcp4: true
        regulatory-domain: "US"
        access-points:
          "OpenCyberCity_5GHz":
            auth:
                key-management: "psk"
                password: "[LOTS OF CHARACTERS]"
    ```
    - Edit the file to look like the following, replacing `[STATIC_IP_ADDRESS]`, `[GATEWAY_IP_ADDRESS]`, and `[DNS_SERVER_IP_ADDRESS]` with the appropriate values you noted in the previous steps:
    ```yaml
    network:
    version: 2
    ethernets:
      eth0:
        optional: true
        dhcp4: false # MAKE SURE TO SET THIS TO FALSE
        dhcp6: true
    wifis:
      wlan0:
        optional: true
        dhcp4: false # MAKE SURE TO SET THIS TO FALSE
        dhcp6: true
        regulatory-domain: "US"
        access-points:
          "OpenCyberCity_5GHz":
            auth:
                key-management: "psk"
                password: "[LOTS OF CHARACTERS]"
        # ADD STATIC IP CONFIGURATION BELOW
        addresses:
          - [STATIC_IP_ADDRESS]/24
        routes:
          - to: default
            via: [GATEWAY_IP_ADDRESS]
        nameservers:
          addresses: 
            - [DNS_SERVER_IP_ADDRESS]
    ```
    - Save and exit the file (Ctrl+X, then Y, then Enter).
        - Note: yaml files are very sensitive to indentation. Make sure to use spaces instead of tabs and maintain the correct indentation levels as shown in the example above.
    - Apply the new netplan configuration with the following command:
    ```
    sudo netplan apply
    ```
    Note: If you are ssh'd into the Raspberry Pi, you may lose your connection after applying the new configuration. If this happens, simply reconnect using the new static IP address you set.
    - Optionally, you can reboot the Raspberry Pi to ensure that the new static IP address is applied correctly:
    ```
    sudo reboot now
    ``` 
    - Finally confirm that the static IP address has been set correctly by running `ip addr` and checking that the correct IP address is assigned to the appropriate network interface.

5. Update the Raspberry Pi's package list and upgrade all installed packages to their latest versions:
    ```
    sudo apt update
    sudo apt upgrade -y
    ```
6. **Install ROS 2 Jazzy on the Raspberry Pi.** 
    - Follow the official ROS 2 installation guide for Ubuntu <a href="https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debians.html">here</a>.
    - Make sure to select the appropriate ROS 2 distribution (Jazzy) and follow the instructions for installing the desktop version of ROS 2, which includes the necessary tools and libraries for development.
    - After installing ROS 2, you can verify the installation by running the following command:
    ```
    source /opt/ros/jazzy/setup.bash
    ```
    - You can also check that ROS 2 is working correctly by running a simple ROS 2 command, such as:
    ```
    ros2 topic list
    ```
    - If you see a list of ROS 2 topics (which may be empty if there are no nodes running on the network), then ROS 2 is installed and working correctly on your Raspberry Pi.

8. **Make your life easier by adding some shortcuts.**
    - In your home directory lives a hidden file called `.bashrc`. This file is executed every time you open a new terminal session. You can add some shortcuts to this file to make your life easier when working with ROS 2 on the Raspberry Pi.
    - Open the `.bashrc` file in a text editor:
    ```
    nano ~/.bashrc
    ```
    - Add the following lines to the end of the file:
    ```bash
    # Source ROS 2 setup script
    source /opt/ros/jazzy/setup.bash
    
    # An alias is a shortcut for a command or a series of commands. 

    # Alias for building the ROS 2 workspace and sourcing the setup script
    alias build='colcon build && source install/setup.bash'

    # Aliases for common ROS 2 commands
    alias tl='ros2 topic list'
    alias te='ros2 topic echo'

    # Add any other shortcuts or aliases you find useful
    ```
    - Save and exit the file (Ctrl+X, then Y, then Enter).
    - Now, every time you open a new terminal session, ROS 2 will be sourced automatically, and you can use the `build` alias to build your ROS 2 workspace and source the setup script in one command. 
    - You can also use the `tl` and `te` aliases to list ROS 2 topics and echo topic messages more easily. Feel free to add any other shortcuts or aliases that you find useful for your development workflow.

**Continue to the building specific setup guides for the hospital, office, and residential buildings to learn how to set up the specific devices and systems in each building.**

