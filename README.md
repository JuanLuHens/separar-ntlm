# separar-ntlm

## Funcionamiento

```
usage: ntlmtohash.py [-h] [-e | -i] [--file-secretsdump FILE_SECRETSDUMP] [-u EFUH] [-a EFOH] [-p PASSWORD] [-o EPASS] [-f FILTRADO [FILTRADO ...]] [-n] [-v]
```

```
optional arguments:
  -h, --help            show this help message and exit
  -e, --export          Export user&hash and onlyhash
  -i, --import          Import hash&pass from crack
  --file-secretsdump FILE_SECRETSDUMP
                        With -e.File impacket secretsdump
  -u EFUH               File export/import user&Hash
  -a EFOH               With -e. File export only hash for crack
  -p PASSWORD, --password PASSWORD
                        With -i. File import hash:password from crack
  -o EPASS              With -i. File export user and pass
  -f FILTRADO [FILTRADO ...], --filter FILTRADO [FILTRADO ...]
                        With -e.Words/Domain Filter
  -n, --null            With -i. Add user with pass no found in export file
  -v                    verbose                   verbose
```

## Ejemplo básico:

## Opcion e

**Generar ficheros desde el dump con filtrado de dominios**:

- Opción e
- Pasamos el fichero dump generado desde secretsdump con parametro --file-secretsdump
- Se generan dos ficheros:
  - usuariosyhashes.csv. Fichero con los usuarios y sus hashes para cruzar más adelante con el resultado del hashcat con hashes.txt.
  - hashes.txt. Fichero con los hashes unicos (se elimina duplicados) para pasarlos por hashcat o similar.
- Se pasan los dominios separados por espacio con el parametro -f.

```
python .\ntlmtohash.py -e --file-secretsdump dump -f domain1.com domain2.org
Finalizado
--------------------------
Pasa hashes.txt al crack
```
**Generar ficheros desde el dump con filtrado de dominios y personalizando salida de los ficheros.**:

- Opción e
- Pasamos el fichero dump generado desde secretsdump con parametro --file-secretsdump
- Se generan dos ficheros:
  - Opcion u usuariosyhashes.csv. Fichero con los usuarios y sus hashes para cruzar más adelante con el resultado del hashcat con hashes.txt.
  - Opcion a hashes.txt. Fichero con los hashes unicos (se elimina duplicados) para pasarlos por hashcat o similar.
- Se pasan los dominios separados por espacio con el parametro -f.

```
python .\ntlmtohash.py -e --file-secretsdump dump -f domain1.com domain2.org -u usuariosyhashes.csv -a hashes.txt
```
## Opcion i

**Cruzar usuarios:hashes con hashes:pass**:

- Opción i
- Salida del fichero userypass.csv con los datos cruzados. 
- Si no personalizamos, los ficheros deben ser:
  - usuariosyhashes.csv. Fichero con los usuarios y sus hashes
  - password.txt. Fichero con los hashes:pass 

```
python .\ntlmtohash.py -i
Hay 13465 usuarios, de los cuales 9719 se ha obtenido la contraseña
Esto corresponde a un 72.18% de usuarios crackeados
Exportado a userypass.csv
Finalizado
```

**Cruzar usuarios:hashes con hashes:pass personalizando entradas**:

- Opción i
- Salida del fichero userypass.csv con los datos cruzados. 
- Si personalizamos las entradas:
  - Opción u usuariosyhashes.csv. Fichero con los usuarios y sus hashes
  - Opcion p password.txt. Fichero con los hashes:pass 

```
python .\ntlmtohash.py -i -u usuariosyhashes.csv -p password.txt
```
**Cruzar usuarios:hashes con hashes:pass personalizando entradas y salida**:

- Opción i
- Con opcion o salida del fichero userypass.csv con los datos cruzados. 
- Si personalizamos las entradas:
  - Opción u usuariosyhashes.csv. Fichero con los usuarios y sus hashes
  - Opcion p password.txt. Fichero con los hashes:pass 

```
python .\ntlmtohash.py -i -u usuariosyhashes.csv -p password.txt -o userypass.csv
```
