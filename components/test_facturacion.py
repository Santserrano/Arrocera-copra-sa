import tkinter as tk
import sqlite3
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch

def generar_factura():
    # Crear un nuevo archivo PDF
    pdf_path = "reporte.pdf"
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
    elements = []

    # Agregar el logo
    from reportlab.platypus import Image, Spacer
    logo_path = "assets/logo.png"
    logo = Image(logo_path, 0.70 * inch, 0.75 * inch)

    # Crear una tabla con el logo en la esquina superior izquierda
    header_table = Table([[logo]], colWidths=[1 * inch], rowHeights=[1 * inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))
    elements.append(header_table)

    # Espacio después del logo
    elements.append(Spacer(1, 12))

    data = [
        ["N° Orden", "Item", "Cliente", "Dirección", "Estado", "Cantidad"],
        ['3833', 'Arroz blanco', 'Juan Perez', 'Av. Rivadavia 123', 'Enviado', '8'],
        ['6432', 'Arroz integral', 'María Gomez', 'Calle Corrientes 456', 'Entregado', '10'],
        ['2180', 'Arroz blanco', 'Pedro Rodriguez', 'Av. Belgrano', 'Pendiente', '3'],
        ['5412', 'Arroz basmati', 'Ana Fernandez', 'Calle San Martin 789', 'Enviado', '5'],
        ['6587', 'Arroz jazmín', 'Luis Martinez', 'Av. Santa Fe 321', 'Pendiente', '2'],
        ['7432', 'Arroz integral', 'Sofia Lopez', 'Calle Mitre 654', 'Entregado', '7'],
        ['8743', 'Arroz blanco', 'Carlos Gomez', 'Av. Callao 987', 'Enviado', '6'],
        ['9123', 'Arroz basmati', 'Elena Garcia', 'Calle Lavalle 123', 'Pendiente', '4']
    ]

    conn = sqlite3.connect('ordenes.db')
    cursor = conn.cursor()

    # Query a la db
    cursor.execute("SELECT * FROM ordenes")
    ordenes = cursor.fetchall()
    conn.close()

    for orden in ordenes:
        data.append(orden)

    # Crear la tabla con anchos de columna ajustados
    table = Table(data, colWidths=[0.75 * inch, 1.25 * inch, 1.25 * inch, 2 * inch, 1.25 * inch, 0.75 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    pdf.build(elements)
    print(f"Factura generada en {pdf_path}")

