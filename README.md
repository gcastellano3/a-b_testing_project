**Vanguard A/B Test: Digital Interface Analysis**

1. Project Overview
Este proyecto analiza los resultados de un experimento digital llevado a cabo por Vanguard entre el 15 de marzo y el 20 de junio de 2017. El objetivo principal es determinar si una nueva Interfaz de Usuario (UI) y el uso de "prompts" en contexto aumentan la tasa de finalización de los procesos de inversión en comparación con la interfaz tradicional.
- Control Group: Interacción con el proceso online tradicional.
- Test Group: Interacción con la nueva interfaz moderna.

2. Project Structure

main.ipynb              # Análisis completo: EDA, Limpieza, KPIs y Test de hipótesis.
a_b_testing.pbix        # Dashboard interactivo en Power BI.
.gitignore              # Archivos excluidos (entornos virtuales, datasets pesados).
src/                    # Módulos de Python con funciones de limpieza (data_wrangling.py).
README.md               # Documentación del proyecto.

3. Methodology & KPIs
El análisis se dividió en tres fases:

A. EDA & Data Cleaning
Unión de los datasets de huellas digitales (pt_1 y pt_2).
Identificación del perfil del cliente: Edad promedio, género y antigüedad (tenure)
Limpieza de nulos y estandarización de pasos del proceso.

B. Performance Metrics (KPIs)
Calculamos la efectividad del diseño basándonos en:

Completion Rate: Proporción de usuarios que alcanzaron el paso final (confirm).
Time Spent on Each Step: Duración media por fase del proceso.
Error Rates: Identificación de retrocesos (ir de un paso posterior a uno anterior) como indicador de confusión.

C. Hypothesis Testing
Realizamos pruebas estadísticas para validar los resultados:

Z-test de dos proporciones: Para confirmar si la diferencia en la tasa de finalización es estadísticamente significativa.
Umbral de Rentabilidad (5%): Validación de si la mejora supera el 5% de incremento mínimo requerido por Vanguard para justificar los costes de desarrollo.
Sesgo de Edad: Test para asegurar que la aleatorización de grupos no fue afectada por la edad de los clientes.

4. Key Findings
Efectividad: El grupo de prueba mostró una tasa de finalización superior, superando las pruebas de significancia estadística ($p < 0.05$).
Fricción detectada: A pesar de la mayor finalización, la tasa de error (retrocesos) aumentó del 6.82% al 9.22% en la nueva interfaz.
Conclusión: Se recomienda el despliegue de la nueva UI, pero con una optimización urgente en los pasos 2 y 3 para reducir la confusión del usuario.

