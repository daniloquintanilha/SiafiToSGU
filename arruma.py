import csv

with open('TABMUN-SIAFI.csv') as f:
    arquivo = csv.reader(f, delimiter=';')
    next(arquivo)
    with open('tabela_siafi_corrigida.csv', mode='w', newline='') as arq:
        colunas = ['cidad_cod', 'uf_cod', 'cidad_des', 'cidad_cod_ibge', 'cidad_des_abrev',
                   'cidad_tip', 'cidad_cod_prftra', 'cidad_cod_siafi']
        writer = csv.DictWriter(arq, fieldnames=colunas)
        writer.writeheader()

        for linha in arquivo:
             # print(linha[4] + ';' + linha[3] + ';' + linha[2] + ';' + linha[4] + ';' + ';' + ';' + ';' + linha[0])
                writer.writerow({'cidad_cod':linha[4], 'uf_cod':linha[3], 'cidad_des':linha[2],
                                 'cidad_cod_ibge':linha[4], 'cidad_des_abrev':'', 'cidad_tip':'',
                                 'cidad_cod_prftra':'', 'cidad_cod_siafi':linha[0]})
