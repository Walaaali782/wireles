import pywifi
import time
import random

def disconnect_current_wifi(iface):
    current_status = iface.status()
    if current_status == pywifi.const.IFACE_CONNECTED:
        iface.disconnect()
        print("Disconnected from the current network.")
    elif current_status == pywifi.const.IFACE_DISCONNECTED:
        print("No active Wi-Fi connection.")
    else:
        print("Unknown Wi-Fi connection status.")

def connect_to_wifi(iface, ssid):
    profile = pywifi.Profile()
    profile.ssid = ssid

    iface.remove_all_network_profiles()
    temp_profile = iface.add_network_profile(profile)
    iface.connect(temp_profile)

 
    timeout = 15 
    start_time = time.time()

    while iface.status() != pywifi.const.IFACE_CONNECTED:
        if time.time() - start_time > timeout:
            print("Connection timeout. Unable to connect. Please check your settings and try again.")
            return False
        time.sleep(1)

    print(f"Connected to {ssid} successfully!")
    return True



def scan_and_connect():
    wifi = pywifi.PyWiFi()

    if len(wifi.interfaces()) == 0:
        print("No Wi-Fi interfaces found. Exiting.")
        exit()

    iface = wifi.interfaces()[0]

    disconnect_current_wifi(iface)

    networks = sorted(iface.scan_results(), key=lambda x: x.signal, reverse=True)

    print("Available Networks (sorted by signal strength):")
    
    visible_networks = [network for network in networks if network.bssid != '00:00:00:00:00:00']

    for i, network in enumerate(visible_networks):
        print(f"{i + 1}. {network.ssid} (Signal: {network.signal}%)")

    selected_index = int(input("Enter the number of the network you want to connect to: ")) - 1

    if 0 <= selected_index < len(visible_networks):
        selected_network = visible_networks[selected_index]
        print(f"You selected: {selected_network.ssid} (Network {selected_index + 1})")
    else:
        print("Invalid selection. Exiting.")
        exit()

    password_correct = connect_to_wifi(iface, selected_network.ssid)

    if password_correct:
        print("Connected successfully.")
        calculate_and_display_data_transfer_rate(iface)
    else:
        print("Unable to connect. Please check your settings and try again.")

if __name__ == "__main__":
    scan_and_connect()
