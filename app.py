
import os

# Criar o diretorio pai
diretorio = 'C:/Meus documentos/Projetos Python/Criar shapefiles/criar-arquivos-padrao-QGIS/arquivos/'

# Declarar variáveis - sistema de coordenadas, nomes e tipos de geometrias dos shapefiles
epsg = 'EPSG:31982'

shapefiles = {
    'Talhao':'Polygon',
    'App':'Polygon',
    'Obstaculos':'Polygon',
    'Local':'Point',
    'Postes':'Point',
    'Estradas':'LineString',
    'Basculamento':'LineString',
    'Arvores':'Polygon',
    'Entrada':'Point',
    'Saida':'Point',
    'Sede':'Point',
    'Canal':'Polygon',
    'Canal escoadouro':'Polygon',
    'Mato':'Polygon',
    'ln_poste':'LineString',
    'Ventosa':'Point',
    'Caixa de agua':'Polygon',
    'Sem cana':'Polygon',
    'Pedreira':'Polygon',
    'pt_Arvores':'Point'
}


for key, value in shapefiles.items():

    # Cria camadas na memória
    camada = QgsVectorLayer(value + f'?crs={epsg}', key, 'memory')

    # Adiciona campos às camadas
    camada.dataProvider().addAttributes([QgsField('ID', QVariant.Int)])
    camada.dataProvider().addAttributes([QgsField('Nome', QVariant.String)])
    camada.dataProvider().addAttributes([QgsField('Valor', QVariant.Double)])
    camada.updateFields()

    # Montar os nomes dos diretórios + shps criados
    url_final = os.path.join(diretorio, key)

    # Checa se os arquivos já existem, senão, são criados.
    # Isso evita que arquivos sejam sobreescritos
    
    if os.path.isfile(url_final + '.shp'):
        print(f'O Arquivo {url_final} já existe, altere o diretório no início do código')
        print('')

    else:
        QgsVectorFileWriter.writeAsVectorFormat(camada, url_final, 'utf-8', camada.crs(), 'ESRI Shapefile')
        print(f'Arquivo {key} criado com sucesso no diretório {url_final}')
        print('')
        iface.addVectorLayer(str(url_final) + '.shp', '', 'ogr')