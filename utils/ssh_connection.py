# utils/ssh_utils.py

from time import sleep
import paramiko
from utils.logging_config import logger

def ssh_connect(ip, username, password, commands):
    try:
        logger.info(f'Connecting to device {ip}...')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)

        ssh = client.invoke_shell()
        for command in commands:
            logger.info(f'Sending command: {command}')
            ssh.send(command + '\n')
            sleep(1)
            output = ssh.recv(65535).decode('utf-8')
            logger.info(f'Command output: {output}')

        logger.info('Closing SSH connection...')
        ssh.close()
        client.close()
        logger.info('SSH connection closed successfully.')
    except Exception as e:
        logger.error(f'Error during SSH connection to device {ip}: {e}')
