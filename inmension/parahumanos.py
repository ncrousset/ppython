# parahumanos.py

SUFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def tamanyo_aproximado(tamanyo, un_kilobyte_es_1024_bytes=True):
    '''Convierte un tamanyo de fichero en formato legible por personas

        Argumentos/parametros
        tamanyo -- tamanyo de dichero en bytes
        un_kilobyte_es_1024_bytes --- si True (por defecto),
                                      usa multiplos de 1024
                                      si False, usa multiplos de 1000

        retorna: string

    '''

    if tamanyo < 0:
        raise ValueError('El numero debe ser no negativo')

    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUFIJOS[multiplo]:
        tamanyo /= multiplo
        if tamanyo < multiplo:
            return '{0:.1f} {1}'.format(tamanyo, sufijo)

    raise ValueError('numero demasiado grande')

if __name__ == '__main__':
    print(tamanyo_aproximado(1000000000000, False))
    print(tamanyo_aproximado(1000000000000))
