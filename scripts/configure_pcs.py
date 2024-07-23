from utils.netmiko_connection import create_connection, send_commands, save_configuration, close_connection

def automate_pcs(zone):
    pcs = {
        "green": [
            # Add green zone PCs configurations here
        ],
        "yellow": [
            # Add yellow zone PCs configurations here
        ]
    }

    for pc in pcs[zone]:
        connection = create_connection(pc)
        if connection:
            output = send_commands(connection, pc['commands'])
            print(output)
            save_configuration(connection)
            close_connection(connection)

if __name__ == "__main__":
    zone = input("Enter zone (green/yellow): ").strip().lower()
    automate_pcs(zone)
