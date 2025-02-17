

# Documentación de Datos Procesados para Análisis y Visualización en Tableau

Este directorio contiene los archivos CSV procesados del proyecto de Análisis de Recursos Humanos de IBM para fines de visualización en Tableau. Todos los archivos están codificados en UTF-8 y han sido preparados específicamente para su visualización en Tableau.

## Los archivos disponibles son:

### 1. datos_hr_tableau.csv
Conjunto de datos principal con las variables más relevantes para el análisis.
- **Variables incluidas**: 
  - Department: Departamento del empleado
  - JobLevel: Nivel de trabajo (1-5)
  - JobRole: Rol específico
  - Gender: Género
  - Age: Edad
  - MonthlyIncome: Salario mensual
  - YearsAtCompany: Años en la empresa
  - DistanceFromHome: Distancia al trabajo
  - WorkLifeBalance: Balance vida-trabajo (1-4)
  - JobSatisfaction: Satisfacción laboral (1-4)
  - Attrition: Rotación (Yes/No)
  - Attrition_Numeric: Rotación en formato numérico (1/0)
  - SalarioAnual: Salario anual calculado

### 2. dept_analysis.csv
Análisis agregado por departamento.
- **Columnas**:
  - Número_Empleados: Total de empleados por departamento
  - Salario_Promedio: Salario mensual promedio
  - Tasa_Rotación: Porcentaje de rotación
  - Satisfacción_Promedio: Nivel promedio de satisfacción

### 3. rotacion_dept.csv
Métricas detalladas de rotación por departamento.
- **Columnas**:
  - Total_Empleados: Número de empleados
  - Tasa_Rotacion: Porcentaje de rotación
  - Promedio_Anos_Empresa: Promedio de años en la empresa

### 4. salarios_dept.csv
Análisis salarial detallado por departamento.
- **Columnas**:
  - Salario_Promedio: Media salarial
  - Salario_Mediana: Mediana salarial
  - Salario_Desviacion: Desviación estándar
  - Salario_Minimo: Salario mínimo
  - Salario_Maximo: Salario máximo

### 5. satisfaccion.csv
Métricas de satisfacción por departamento.
- **Columnas**:
  - Satisfaccion_Laboral: Promedio de satisfacción laboral
  - Balance_Vida_Trabajo: Promedio de balance vida-trabajo
  - Satisfaccion_Ambiente: Promedio de satisfacción con el ambiente
  - Satisfaccion_Relaciones: Promedio de satisfacción en relaciones

### 6. demograficos.csv
Información demográfica detallada.
- **Columnas**:
  - Department: Departamento
  - JobLevel: Nivel de trabajo
  - Gender: Género
  - EmployeeCount: Conteo de empleados
  - Age: Estadísticas de edad (media, mínimo, máximo)
  - Education: Nivel educativo promedio
  - MaritalStatus: Distribución de estado civil

### 7. rendimiento.csv
Métricas de rendimiento y desarrollo.
- **Columnas**:
  - PerformanceRating: Calificación de desempeño (media, mín, máx)
  - PercentSalaryHike: Porcentaje de aumento salarial (media, mediana)
  - TrainingTimesLastYear: Promedio de capacitaciones en el último año

## Uso en Tableau

Para comenzar el análisis en Tableau:
1. Usar 'dataset_principal.csv' como fuente principal de datos
2. Los archivos agregados pueden utilizarse para dashboards específicos
3. Se recomienda crear relaciones entre archivos usando 'Department' como campo clave

## Notas Importantes

- Todos los archivos han sido limpiados y no contienen valores nulos
- Los nombres de las columnas no contienen espacios ni caracteres especiales
- Los valores numéricos han sido redondeados a 2 decimales
- Las fechas están en formato YYYY-MM-DD

## Actualización de Datos

Los archivos se actualizan automáticamente al ejecutar el script `analysis.py`. La última actualización fue realizada el [FECHA].