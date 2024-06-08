import lupa
import time
from lupa import LuaRuntime
from engine.functions import RecepcionArroz, CargaDescarga, Almacenamiento, Secado, Mantenimiento, NuevaOrden

lua = LuaRuntime(unpack_returned_tuples=True)
with open('performance_test.lua', 'r') as file:
    lua_code = file.read()
lua.execute(lua_code)

# Obtener la función de prueba de rendimiento desde Lua
measure_performance = lua.globals().measure_performance

# Convertir la función de Python para que sea llamada desde Lua
lua_my_python_function = lua.eval('function(n) return python.eval("prueba")(n) end')

# Definir el número de iteraciones
n = 1000000

# Ejecutar la prueba de rendimiento
result, elapsed_time = measure_performance(lua_my_python_function, n)

print(f"Resultado: {result}")
print(f"Tiempo transcurrido: {elapsed_time:.5f} segundos")
