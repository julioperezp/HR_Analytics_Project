# analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar y realizar la limpieza inicial del dataset de IBM HR Analytics
def load_and_clean_data():
    """
    Carga y realiza la limpieza inicial del dataset de IBM HR Analytics
    """
    # Cargar datos
    df = pd.read_csv('c:/Users/L-Garage/Desktop/HR_Analytics_Project/data/raw/IBM_HR_Analytics.csv')
    
    # Crear variables derivadas útiles
    df['SalarioAnual'] = df['MonthlyIncome'] * 12
    
    # Convertir Attrition a numérico para facilitar análisis
    df['Attrition_Numeric'] = (df['Attrition'] == 'Yes').astype(int)
    
    return df

# Análisis exploratorio detallado del dataset
def analisis_exploratorio(df):
    """
    Realiza análisis exploratorio detallado del dataset
    """
    # Estadísticas generales
    stats = {
        'total_empleados': len(df),
        'tasa_rotacion': (df['Attrition'] == 'Yes').mean() * 100,
        'promedio_salario': df['MonthlyIncome'].mean(),
        'promedio_edad': df['Age'].mean(),
        'promedio_años_empresa': df['YearsAtCompany'].mean()
    }
    
    # Análisis por departamento
    dept_analysis = df.groupby('Department').agg({
        'EmployeeCount': 'count',
        'MonthlyIncome': 'mean',
        'Attrition_Numeric': 'mean',
        'JobSatisfaction': 'mean'
    }).round(2)
    
    # Renombrar columnas para mejor comprensión
    dept_analysis.columns = ['Número_Empleados', 'Salario_Promedio', 
                           'Tasa_Rotación', 'Satisfacción_Promedio']
    
    return stats, dept_analysis

# Crear visualizaciones clave para el análisis de RRHH
def crear_visualizaciones(df):
    """
    Genera visualizaciones clave para el análisis de RRHH
    """
    # Cambiar la configuración del estilo
    sns.set_theme()  # En lugar de plt.style.use('seaborn')
    
    # 1. Distribución salarial por departamento
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Department', y='MonthlyIncome', data=df)
    plt.xticks(rotation=45)
    plt.title('Distribución de Salarios por Departamento')
    plt.tight_layout()
    plt.savefig('../visualizations/figures/salarios_dept.png')
    plt.close()  # Cerrar la figura después de guardarla
    
    # 2. Relación entre años en la empresa y salario
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='YearsAtCompany', y='MonthlyIncome', 
                    hue='Attrition', data=df, alpha=0.6)
    plt.title('Relación entre Antigüedad y Salario')
    plt.tight_layout()
    plt.savefig('../visualizations/figures/antiguedad_salario.png')
    plt.close()
    
    # 3. Tasa de rotación por nivel de trabajo
    plt.figure(figsize=(8, 6))
    attrition_by_level = df.groupby('JobLevel')['Attrition_Numeric'].mean() * 100
    sns.barplot(x=attrition_by_level.index, y=attrition_by_level.values)
    plt.title('Tasa de Rotación por Nivel de Trabajo')
    plt.ylabel('Tasa de Rotación (%)')
    plt.tight_layout()
    plt.savefig('../visualizations/figures/rotacion_nivel.png')
    plt.close()
    
    # 4. Satisfacción laboral vs Balance vida-trabajo
    plt.figure(figsize=(8, 6))
    sns.heatmap(pd.crosstab(df['JobSatisfaction'], df['WorkLifeBalance'],
                           normalize='index') * 100,
                annot=True, fmt='.1f', cmap='YlOrRd')
    plt.title('Satisfacción Laboral vs Balance Vida-Trabajo')
    plt.tight_layout()
    plt.savefig('../visualizations/figures/satisfaccion_balance.png')
    plt.close()

def analisis_avanzado(df):
    """
    Realiza análisis estadísticos más profundos
    """
    # Factores que influyen en la rotación
    factores_rotacion = pd.DataFrame({
        'Factor': [
            'Distancia_al_trabajo',
            'Años_empresa',
            'Edad',
            'Salario_mensual',
            'Satisfaccion_laboral'
        ],
        'Correlacion': [
            df['DistanceFromHome'].corr(df['Attrition_Numeric']),
            df['YearsAtCompany'].corr(df['Attrition_Numeric']),
            df['Age'].corr(df['Attrition_Numeric']),
            df['MonthlyIncome'].corr(df['Attrition_Numeric']),
            df['JobSatisfaction'].corr(df['Attrition_Numeric'])
        ]
    })
    
    return factores_rotacion.sort_values('Correlacion', ascending=False)

def generar_reporte(stats, dept_analysis, factores_rotacion):
    """
    Genera un reporte ejecutivo con los hallazgos principales
    """
    reporte = f"""
    # Análisis de Recursos Humanos IBM - Reporte Ejecutivo

    ## Métricas Generales
    - Total de Empleados: {stats['total_empleados']:,}
    - Tasa de Rotación: {stats['tasa_rotacion']:.1f}%
    - Salario Promedio Mensual: ${stats['promedio_salario']:,.2f}
    - Edad Promedio: {stats['promedio_edad']:.1f} años
    - Antigüedad Promedio: {stats['promedio_años_empresa']:.1f} años

    ## Análisis por Departamento
    {dept_analysis.to_string()}

    ## Factores Principales de Rotación
    {factores_rotacion.to_string(index=False)}
    """
    
    with open('../docs/reporte_ejecutivo.md', 'w', encoding='utf-8') as f:
        f.write(reporte)
    
    return reporte

def crear_estructura_directorios():
    """
    Crea la estructura de directorios necesaria para el proyecto
    """
    directorios = [
        'data/raw',
        'data/processed',  # Añadimos la carpeta processed
        'visualizations/figures',
        'docs'
    ]
    
    for directorio in directorios:
        os.makedirs(directorio, exist_ok=True)

def exportar_datos_para_tableau(df, dept_analysis):
    """
    Prepara y exporta los datos para Tableau en múltiples archivos CSV
    """
    # Asegurarse que el directorio existe
    os.makedirs('../data/processed', exist_ok=True)
    
    # 1. Exportar análisis por departamento
    dept_analysis.to_csv('../data/processed/dept_analysis.csv', encoding='utf-8')
    
    # 2. Exportar datos de rotación por departamento
    rotacion_dept = df.groupby('Department').agg({
        'Attrition_Numeric': ['count', 'mean'],
        'YearsAtCompany': 'mean'
    }).round(3)
    rotacion_dept.columns = ['Total_Empleados', 'Tasa_Rotacion', 'Promedio_Anos_Empresa']
    rotacion_dept.to_csv('../data/processed/rotacion_dept.csv', encoding='utf-8')
    
    # 3. Exportar análisis salarial por departamento
    salarios_dept = df.groupby('Department').agg({
        'MonthlyIncome': ['mean', 'median', 'std', 'min', 'max']
    }).round(2)
    salarios_dept.columns = ['Salario_Promedio', 'Salario_Mediana', 
                            'Salario_Desviacion', 'Salario_Minimo', 'Salario_Maximo']
    salarios_dept.to_csv('../data/processed/salarios_dept.csv', encoding='utf-8')
    
    # 4. Exportar datos de satisfacción
    satisfaccion = df.groupby('Department').agg({
        'JobSatisfaction': 'mean',
        'WorkLifeBalance': 'mean',
        'EnvironmentSatisfaction': 'mean',
        'RelationshipSatisfaction': 'mean'
    }).round(2)
    satisfaccion.columns = ['Satisfaccion_Laboral', 'Balance_Vida_Trabajo',
                           'Satisfaccion_Ambiente', 'Satisfaccion_Relaciones']
    satisfaccion.to_csv('../data/processed/satisfaccion.csv', encoding='utf-8')
    
    print("Archivos CSV exportados exitosamente en la carpeta 'data/processed':")
    print("- dept_analysis.csv")
    print("- rotacion_dept.csv")
    print("- salarios_dept.csv")
    print("- satisfaccion.csv")

def main():
    # Crear estructura de directorios
    crear_estructura_directorios()
    
    # Cargar y limpiar datos
    df = load_and_clean_data()
    
    # Realizar análisis
    stats, dept_analysis = analisis_exploratorio(df)
    factores_rotacion = analisis_avanzado(df)
    
    # Crear visualizaciones
    crear_visualizaciones(df)
    
    # Generar reporte
    reporte = generar_reporte(stats, dept_analysis, factores_rotacion)
    
    # Exportar datos para Tableau
    exportar_datos_para_tableau(df, dept_analysis)
    
    return df, stats, dept_analysis, factores_rotacion, reporte

if __name__ == "__main__":
    main()
