import platform
import os
import psutil

def get_system_info():

    info = {}
    info['SISTEMA OPERATIVO'] = platform.system()
    info['NOMBRE DEL SISTEMA'] = platform.node()
    info['VERSIÓN DE SO'] = platform.version()
    info['RELEASE DEL SO'] = platform.release()
    info['ARQUITECTURA'] = platform.machine()
    info['PROCESADOR'] = platform.processor()
    info['CORES FÍSICOS'] = psutil.cpu_count(logical=False)
    info['CORES LÓGICOS'] = psutil.cpu_count(logical=True)
    info['FRECUENCIA CPU'] = psutil.cpu_freq().max
    mem = psutil.virtual_memory()
    info['MEMORIA TOTAL'] = f"{mem.total / (1024 ** 3):.2f} GB"
    info['MEMORIA DISPONIBLE'] = f"{mem.available / (1024 ** 3):.2f} GB"
    
    def print_system_info(info):
        print("+------------------------------------------------------------------+")
        print("| MATE SYSTEMS		    COPRA S.A		    version 0.0.1  |")
        print("+------------------------------------------------------------------+")
        print(f"| SISTEMA OPERATIVO: {info['SISTEMA OPERATIVO']}                                       |")
        print(f"| NOMBRE DEL SISTEMA: {info['NOMBRE DEL SISTEMA']}                              |")
        print(f"| VERSIÓN DE SO: {info['VERSIÓN DE SO']}                                        |")
        print(f"| RELEASE DEL SO: {info['RELEASE DEL SO']}                                               |")
        print(f"| ARQUITECTURA: {info['ARQUITECTURA']}                                              |")
        print(f"| PROCESADOR: {info['PROCESADOR']}  |")
        print(f"| CORES FÍSICOS: {info['CORES FÍSICOS']}                                                 |")
        print(f"| CORES LÓGICOS: {info['CORES LÓGICOS']}                                                 |")
        print(f"| FRECUENCIA CPU: {info['FRECUENCIA CPU']} MHz                                       |")
        print(f"| MEMORIA TOTAL: {info['MEMORIA TOTAL']}                                           |")
        print(f"| MEMORIA DISPONIBLE: {info['MEMORIA DISPONIBLE']}                                      |")
        print("+------------------------------------------------------------------+")
    
    print_system_info(info)
