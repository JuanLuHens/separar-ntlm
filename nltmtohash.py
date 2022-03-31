import argparse
import csv
import re

def get_args():
    parser = argparse.ArgumentParser(
        description='Script para preparar NTLM DUMP \nBy @z3r082')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--export', dest='exportar',
                        action='store_true', help='Export user&hash and onlyhash ')
    group.add_argument('-i', '--import', dest='importar',
                        action='store_true', help='Import hash&pass from crack')
    parser.add_argument('--file-secretdumps', type=str,
                        required=False, help='With -e.File impacket secretdumps')
    parser.add_argument('-efuh', type=str, required=False,
                        default="usuariosyhashes.csv", help='With -e.File export user & Hash')
    parser.add_argument('-efoh', type=str, required=False,
                        default="hashes.txt", help='With -e.File export only hash for crack')
    parser.add_argument('-f', '--filter', dest='filtrado',
                        nargs='+', help='With -e.Words/Domain Filter')
    parser.add_argument('-v', dest='verbose',
                        action="store_true", required=False, help="verbose")
    return parser.parse_args()


def exporthash(args):
    bad_words = ['aes256-cts', 'aes128-cts', 'des-cb', 'rc4_hmac', '$']
    usuario = []
    hash = []
    with open(args.file_secretdumps,'r') as f:
        for linea in f.readlines():
            linea=linea.rstrip('\n')
            linea = linea.lower()
            regexp = re.compile(r'\w*:\w*:\w*:\w*:',flags=re.IGNORECASE)
            if (any (dominio in linea for dominio in args.filtrado)) or (regexp.search(linea)):
                if not any (bad_word in linea for bad_word in bad_words):
                    linea = linea.replace(':',' ')
                    usuario.append(re.split("\s",linea)[0])
                    hash.append(re.split("\s",linea)[3])
    listado = dict(zip(usuario,hash))
    #eliminar duplicados
    hash = list(dict.fromkeys(hash)) 
    #fin eliminar duplicados
    fichero = csv.writer(open(args.efuh,"w",newline=''))
    hashestxt = open(args.efoh,'w')
    hashess1='\n'.join(hash)
    hashestxt.write(hashess1)
    for key,value in listado.items():
        fichero.writerow([key,value])
    print("Finalizado\n--------------------------\nSube hashes.txt al crack")
                
if __name__ == '__main__':
    args = get_args()
    if args.exportar:
        if args.file_secretdumps:
            exporthash(args)
        else:
            print("No file secrets dumps")
    elif args.importar:
        print("Working... Try new version")
    else:
        print("You must select -e or -i")
