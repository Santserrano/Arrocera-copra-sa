def run_test():
    from colors import colors
    import timeit
    from almacenamiento_arroz import almacenamiento_arroz
    from carga_y_descarga import carga_y_descarga
    from dashboard import dashboard
    from ID_log import ID_log
    from ID_log_2 import ID_log_2
    from login import login
    from mapa_transporte import mapa_transporte
    from ops_transporte_b import ops_transporte_b
    from pagos_transporte import pagos_transporte
    from listado_ordenes import listado_ordenes
    from secadores_disponibles import secadores_disponibles
    ###########################################
    start_time1 = timeit.default_timer()
    test_1 = almacenamiento_arroz
    end_time1 = timeit.default_timer()
    ###########################################
    start_time2 = timeit.default_timer()
    test_2 = carga_y_descarga
    end_time2 = timeit.default_timer()
    ###########################################
    start_time3 = timeit.default_timer()
    test_3 = dashboard
    end_time3 = timeit.default_timer()
    ###########################################
    start_time4 = timeit.default_timer()
    test_4 = ID_log
    end_time4 = timeit.default_timer()
    ###########################################
    start_time5 = timeit.default_timer()
    test_5 = ID_log_2
    end_time5 = timeit.default_timer()
    ###########################################
    start_time6 = timeit.default_timer()
    test_6 = login
    end_time6 = timeit.default_timer()
    ###########################################
    start_time7 = timeit.default_timer()
    test_7 = mapa_transporte
    end_time7 = timeit.default_timer()
    ###########################################
    start_time8 = timeit.default_timer()
    test_8 = ops_transporte_b
    end_time8 = timeit.default_timer()
    ###########################################
    start_time9 = timeit.default_timer()
    test_9 = pagos_transporte
    end_time9 = timeit.default_timer()
    ###########################################
    start_time10 = timeit.default_timer()
    test_10 = listado_ordenes
    end_time10 = timeit.default_timer()
    ###########################################
    start_time11 = timeit.default_timer()
    test_11 = secadores_disponibles
    end_time11 = timeit.default_timer()
    ###########################################

    # Calcular la diferencia de tiempo
    execution_time_1 = end_time1 - start_time1 # almacenamiento_arroz 
    execution_time_2 = end_time2 - start_time2 # carga_y_descarga 
    execution_time_3 = end_time3 - start_time3 # dashboard 
    execution_time_4 = end_time4 - start_time4 # ID_log 
    execution_time_5 = end_time5 - start_time5 # ID_log_2 
    execution_time_6 = end_time6 - start_time6 # login 
    execution_time_7 = end_time7 - start_time7 # mapa_transporte 
    execution_time_8 = end_time8 - start_time8 # ops_transporte_b 
    execution_time_9 = end_time9 - start_time9 # pagos_transporte 
    execution_time_10 = end_time10 - start_time10 # listado_ordenes 
    execution_time_11 = end_time11 - start_time11 # secadores_disponibles

    print(colors.MAGENTA + '*** Bechmarks ***')
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 0]  : [Ventana 1] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_1),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 1]  : [Ventana 2] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_2),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 2]  : [Ventana 3] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_3),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 3]  : [Ventana 4] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_4),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 5]  : [Ventana 5] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_5),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 6]  : [Ventana 6] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_6),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 7]  : [Ventana 7] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_7),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 8]  : [Ventana 8] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_8),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 9]  : [Ventana 9] ",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_9),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 10] : [Ventana 10]",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_10),  colors.RED + " segundos"  + colors.RESET)
    print(colors.GREEN  + "***", colors.WHITE  + "[kernel 11] : [Ventana 11]",  colors.GREEN  + "***  :  " + colors.RESET, colors.RED  + "Tiempo de ejecución:", colors.YELLOW  + str(execution_time_11),  colors.RED + " segundos"  + colors.RESET)


if __name__ == "__main__":
    run_test()