#!/usr/bin/python
from os import system as run_command
import argparse
import subprocess


def Change_DNS():

    with open("/etc/resolv.conf","r") as f:
        if "Auto" in f.readline():
            name = "Shekan"
            dns = "178.22.122.100"
            dns2 = "185.51.200.2"
        else:
            name = "Auto"
            dns = "5.200.200.200"
            dns2 = "8.8.8.8"
    # Change DNS
    print(f"Change to {name} DNS")
    run_command(f'echo "# {name}" | sudo tee /etc/resolv.conf > /dev/null')
    run_command(f'echo "nameserver {dns}" | sudo tee -a /etc/resolv.conf > /dev/null')
    run_command(f'echo "nameserver {dns2}" | sudo tee -a /etc/resolv.conf > /dev/null')
    

def get_proxy_mode():
    output = subprocess.check_output(["gsettings", "get", "org.gnome.system.proxy", "mode"])
    proxy_mode = output.decode().strip()
    return proxy_mode


def Change_Mode():
    proxy_mode = get_proxy_mode()
    print(f"Current Mode: {proxy_mode}")

    flag = input("[0] reverse mode or [1] manual or [2] none or [any] not change mode: ")
    if flag == "1":
        proxy_mode = "'manual'"
    elif flag == "2":
        proxy_mode = "'none'"
    elif flag == "0":
        if proxy_mode =="'none'":
            proxy_mode = "manual"
        elif proxy_mode =="'manual'":
            proxy_mode = "none"

    else:
        print("not change")
        return 
    print(f"Change to {proxy_mode}")
    run_command(f"gsettings set org.gnome.system.proxy mode '{proxy_mode}'")

def command_change_port(port,type):
    return f"gsettings set org.gnome.system.proxy.{type} port {port}"

def Change_Port():
    http = subprocess.check_output(["gsettings", "get", "org.gnome.system.proxy.http", "port"]).decode().strip()
    https = subprocess.check_output(["gsettings", "get", "org.gnome.system.proxy.https", "port"]).decode().strip()
    socks = subprocess.check_output(["gsettings", "get", "org.gnome.system.proxy.socks", "port"]).decode().strip()
    print(f"http:{http}, https:{https}, socks:{socks}")
    print(f"-"*20)
    print(f"[N]ekoray: http:2081, https:2081, socks:2080")
    print(f"[V]2ray-ng: http:10809, https:10809, socks:10808")
    flag = input("Change Port [M]anual or [N]ekoray or [V]2ray-ng or empty(not change):")
    http_port = ""
    https_port= ""
    socks_port= ""
    if flag == "N":
        http_port= "2081"
        https_port= "2081"
        socks_port= "2080"
    elif flag == "V":
        http_port= "10809"
        https_port= "10809"
        socks_port= "10808"
    elif flag == "M":
        print("if empty then not change")
        http_port = input("http port:")
        https_port = input("https port:")
        socks_port = input("socks port:")
    elif flag == "":
        print("not change")
        return 

    print(f"change Port http,https to {http_port}")
    run_command(command_change_port(http_port,"http"))
    run_command(command_change_port(https_port,"https"))

    print(f"change Port socks to {socks_port}")
    run_command(command_change_port(socks_port,"socks"))



def Start_VPN(config, flag=True):
	if flag:
		run_command(f"/home/msa/.local/etc/v2ray/v2ray --confdir {config}")
	else:
		run_command(f"/home/msa/.local/etc/v2ray/v2ray --config {config}")
		

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change DNS and Proxy")
    parser.add_argument("--dns", action=argparse.BooleanOptionalAction)
    parser.add_argument("--mode", action=argparse.BooleanOptionalAction)
    parser.add_argument("--vpn", action=argparse.BooleanOptionalAction)
    parser.add_argument("--dir", action=argparse.BooleanOptionalAction)
    parser.add_argument("--config_dir", type=str, default="$HOME/Config_v2ray")
    parser.add_argument("--config", type=str, default="$HOME/Config_v2ray/config.json")
    parser.add_argument("--port", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    try:
        if args.dns:
            Change_DNS()
        if args.mode:
            Change_Mode()
        if args.vpn:
            if args.dir:
                Start_VPN(args.config_dir)
                    
            else:
                Start_VPN(args.config)
        if args.port:
            Change_Port()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)
    input("Enter Key")

