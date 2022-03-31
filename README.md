# separar-ntlm

## Objetivo

Al import el dump generado por impacket-secretsdump, se generan dos ficheros por defecto (se puede cambiar por parametro):

- Hashes.txt. Fichero con los hashes ya filtrado para pasarlos por hashcat o similar.
- Usuariosyhashes.csv. Fichero con dominio/usuarios,hashes para luego unificar con las pass desencriptadas.

## Funcionamiento

```bash
usage: nltmtohash.py [-h] [-e | -i] [--file-secretdumps FILE_SECRETDUMPS] [-efuh EFUH] [-efoh EFOH] [-f FILTRADO [FILTRADO ...]] [-v]
```

```bash
optional arguments:
  -h, --help            show this help message and exit
  -e, --export          Export user&hash and onlyhash
  -i, --import          Import hash&pass from crack
  --file-secretdumps FILE_SECRETDUMPS
                        With -e.File impacket secretdumps
  -efuh EFUH            With -e.File export user & Hash
  -efoh EFOH            With -e.File export only hash for crack
  -f FILTRADO [FILTRADO ...], --filter FILTRADO [FILTRADO ...]
                        With -e.Words/Domain Filter
  -v                    verbose
```

Ejemplo básico:

```bash
python .\nltmtohash.py -e --file-secretdumps usershashes.txt -f domain1.com domain2.org
```

```bash
  -e, --export          Para generar los ficheros Usuarios y hash // Solo Hash
  -i, --import          Para importar los ficheros Usuarios y hash // Solo Hash ya crackeado para unificar datos. Proxima versión
  --file-secretdumps Fichero generado por el secretsdump
                        
  -efuh                Por defecto usuariosyhashes.csv. Opcional
  -efoh                Por defecto hashes.txt. Opcional
  -f --filter          Pasamos los dominos a filtar separados por un espacio

```
