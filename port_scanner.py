import socket
import threading
import logging

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,  # Menampilkan pesan INFO dan lebih penting
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def scan_port(host, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            logging.info(f"Port {port} terbuka")
            open_ports.append(port)
        else:
            logging.debug(f"Port {port} tidak terbuka")
    except Exception as e:
        logging.error(f"Kesalahan saat memeriksa port {port}: {e}")
    finally:
        sock.close()

def scan_ports(host, ports):
    open_ports = []
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

def main():
    domain = 'domain.com'  # Ganti dengan domain yang ingin Anda periksa
    ports_to_check = range(1, 1025)  # Port yang akan diperiksa (1-1024)

    logging.info(f"Memeriksa port terbuka di {domain}...")
    open_ports = scan_ports(domain, ports_to_check)

    if open_ports:
        logging.info("Port yang terbuka:")
        for port in open_ports:
            logging.info(f"Port {port}")
    else:
        logging.info("Tidak ada port terbuka yang ditemukan.")

if __name__ == "__main__":
    main()
