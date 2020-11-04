# Caso 5
from caso_generico import caso_generico, gif, puntos

# (a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso)
 
a = 1                    # alto
b = 1                    # ancho
Nx = 30                  # numero de intervalos en x
Ny = 30                  # numero de intervalos en y

# Condiciones de borde
c_in = 5                 # T° inicial                 
c_sup = 'solo'				 # Borde superior
c_inf = 'solo'                # Borde inferior
c_izq = 25               # Borde izquierdo
c_der = 25			     # Borde derecho

# Gradientes
g_sup = 0                # Gradiente superior
g_inf = 0                # Gradiente inferior
g_izq = 0                # Gradiente izquierdo
g_der = 0                # Gradiente derecho

caso = "caso_5"          # Nombre del caso

p1, p2, p3,sup = caso_generico(a, b, Nx, Ny, c_in, c_sup, c_inf, c_izq, c_der, g_sup, g_inf, g_izq, g_der, caso)

# GIF
fp_in = "caso_5/frame_*.png"
fp_out = "caso_5.gif"
gif(fp_in, fp_out)

# Grafico Evolucion
puntos(p1,p2,p3,sup,caso)