import xml.etree.ElementTree as ET

tree = ET.parse('Diagrama-de-classes-vertical.drawio')
root = tree.getroot()

# Encontrar a raiz dos elementos
model = root.find('.//root')

# 1. Remover waypoints (Array as="points") de todas as linhas para que o Drawio desenhe ortogonalmente automatico
for cell in model.findall('mxCell'):
    if cell.get('edge') == '1':
        geo = cell.find('mxGeometry')
        if geo is not None:
            arr = geo.find('Array')
            if arr is not None:
                geo.remove(arr)

# 2. Reorganizar as classes (vertices) em um grid vertical
classes = []
for cell in model.findall('mxCell'):
    if cell.get('vertex') == '1' and cell.get('style') and 'swimlane' in cell.get('style'):
        classes.append(cell)

col_width = 450
row_height = 380
cols = 2 # 2 colunas para focar bem na vertical

for idx, cell in enumerate(classes):
    geo = cell.find('mxGeometry')
    if geo is not None:
        col = idx % cols
        row = idx // cols
        geo.set('x', str(col * col_width + 50))
        geo.set('y', str(row * row_height + 50))

tree.write('Diagrama-de-classes-vertical.drawio', encoding='utf-8', xml_declaration=True)
print('Script executado com sucesso!')
