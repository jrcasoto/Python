import os
import pandas as pd
import string


def concatenate(gb, path):
    '''
        Concatenar arquivos baixados do SAP em formato $GB$_KE24.txt
    '''
    counter = 0
    concatenated = pd.DataFrame()
    for f in os.listdir(path): # Iterar para cada arquivo na pasta de desenvolvimento
        if '.xlsx' in f and gb in f[:7] and 'KE24' in f: # Checar se extensão do arquivo = '.txt' e se a GB é a respectiva (até primeiros 7 caracteres)
            if counter == 0:
                df = pd.read_excel(f)
                header = df.columns.to_list() # Passar cabeçalho como parâmetro para próximas n bases
            else:
                df = pd.read_excel(f, usecols = header) # Pular cabeçalho das próximas n bases
            df.drop(len(df)-1, inplace = True) # Eliminar linha subtotal
            concatenated = pd.concat([df, concatenated])
            counter += 1
    # Adicionar colunas calculadas para groupbys
    concatenated['TNS'] = concatenated.iloc[:, [x for x in range(27,37)]+[38]].sum(axis=1) - concatenated.iloc[:, [x for x in range(46,54)]+[37]].sum(axis=1)
    concatenated['PPC'] = concatenated.iloc[:, [x for x in range(56,61)]].sum(axis=1)
    concatenated['PPCVariances'] = concatenated.iloc[:, [x for x in range(61,76)]].sum(axis=1)
    concatenated['Selling Costs'] = concatenated.iloc[:, [x for x in range(76,100)]].sum(axis=1)
    concatenated['Admin Costs Fixed'] = concatenated.iloc[:, [x for x in range(100,105)]].sum(axis=1)
    concatenated['R&D Costs'] = concatenated.iloc[:, [x for x in range(105,118)]].sum(axis=1)
    concatenated['OOIE'] = concatenated.iloc[:, [118,120]].sum(axis=1) - concatenated.iloc[:, [119]].sum(axis=1)
    concatenated.to_excel(gb + "_KE24.xlsx", index = False)
    return concatenated


def read_file(gb, path):
    '''
        Ler DataFrame consolidado para consolidação das tabelas na função groupby()
    '''
    df = pd.read_excel(path) # Ler DataFrame concatenado
    return df


def save_dfs(df_list, sheet_list, file_name):
    '''
        Salvamento das visualizações criadas na função groupby() em planilha .xlsx
    '''
    writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter') # Criar objeto para salvamento em formato .xlsx
    for dataframe, sheet in zip(df_list, sheet_list):
        dataframe.to_excel(writer, sheet_name = sheet, startrow = 0 , startcol = 0) # Salvar arquivo em múltiplas abas (1 por DF)
    writer.save()
    return True


def groupby(df):
    '''
        Agrupa visões em formato de tabela dinâmica para consolidação do relatório final
    '''
    # AF 0100
    # 0100-1 > AF 0100 + Artigo e Soma(Em moeda de contabilização)
    AF0100_1 = df.groupby('Artigo')['TNS'].sum()

    # 0100-2 > AF 0100 + Centro de Lucro e Soma(Em moeda de contabilização)
    AF0100_2 = df.groupby('Centro de lucro')['TNS'].sum()

    # 0100-3 > AF 0100 + Num. Doc. Ref. e Soma(Em moeda de contabilização)
    AF0100_3 = df.groupby('Nº documento refer.')['TNS'].sum()

    # AF 0200
    # 0200-1 > AF 0200 + Artigo e Soma(Em moeda de contabilização)
    AF0200_1 = df.groupby('Artigo')['PPC'].sum()

    # 0200-2 > AF 0200 + Centro de Lucro e Soma(Em moeda de contabilização)
    AF0200_2 = df.groupby('Centro de lucro')['PPC'].sum()

    # AF 0250
    # 0250-1 > AF 0250 + Centro custo e Soma(Em moeda de contabilização)
    AF0250_1 = df.groupby('Centro custo emissor')['PPCVariances'].sum()

    # 0250-2 > AF 0250 + Ordem e Soma(Em moeda de contabilização)
    AF0250_2 = df.groupby('Ordem')['PPCVariances'].sum()

    # 0250-3 > AF 0250 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0250_3 = df.groupby('Elemento PEP')['PPCVariances'].sum()

    # 0250-4 > AF 0250 + Num. Conta e Soma(Em moeda de contabilização)
    # AF0250_4 = df.groupby('Nº conta')['PPCVariances'].sum() # Não há comparação com a KE24

    # AF 0300
    # 0300-1 > AF 0300 + Ordem e Soma(Em moeda de contabilização)
    AF0300_1 = df.groupby('Ordem')['Selling Costs'].sum()

    # 0300-2 > AF 0300 + Centro Custo e Soma(Em moeda de contabilização)
    AF0300_2 = df.groupby('Centro custo emissor')['Selling Costs'].sum()

    # 0300-3 > AF 0300 + Artigo e Soma(Em moeda de contabilização)
    AF0300_3 = df.groupby('Artigo')['Selling Costs'].sum()

    # 0300-4 > AF 0300 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0300_4 = df.groupby('Centro de lucro')['Selling Costs'].sum()

    # AF 0400
    # 0400-1 > AF 0400 + Centro Custo e Soma(Em moeda de contabilização)
    AF0400_1 = df.groupby('Centro custo emissor')['Admin Costs Fixed'].sum()

    # 0400-2 > AF 0400 + Ordem e Soma(Em moeda de contabilização)
    AF0400_2 = df.groupby('Ordem')['Admin Costs Fixed'].sum()

    # 0400-3 > AF 0400 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0400_3 = df.groupby('Elemento PEP')['Admin Costs Fixed'].sum()

    # 0400-4 > AF 0400 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0400_4 = df.groupby('Centro de lucro')['Admin Costs Fixed'].sum()

    # AF 0500
    # 0500-1 > AF 0500 + Centro Custo e Soma(Em moeda de contabilização)
    AF0500_1 = df.groupby('Centro custo emissor')['R&D Costs'].sum()

    # 0500-2 > AF 0500 + Ordem e Soma(Em moeda de contabilização)
    AF0500_2 = df.groupby('Ordem')['R&D Costs'].sum()

    # 0500-3 > AF 0500 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0500_3 = df.groupby('Elemento PEP')['R&D Costs'].sum()

    # AF 0600
    # 0600-1 > AF 0600 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0600_1 = df.groupby('Centro de lucro')['OOIE'].sum()

    # 0600-2 > AF 0600 + Ordem e Soma(Em moeda de contabilização)
    AF0600_2 = df.groupby('Ordem')['OOIE'].sum()

    dfs = [AF0100_1, AF0100_2, AF0100_3, AF0200_1, AF0200_2, AF0250_1, AF0250_2,\
           AF0250_3, AF0300_1, AF0300_2, AF0300_3, AF0300_4, AF0400_1, AF0400_2,\
           AF0400_3, AF0400_4, AF0500_1, AF0500_2, AF0500_3, AF0600_1, AF0600_2]
    return dfs

def main():
    '''
        Chamada de funções
    '''
    path = r'\\bosch.com\dfsrb\DfsBR\LOC\Ca1\Pur\rbla\pur1\Internal_Datastore\Automation Anywhere Files\GS\Reconciliation FIxCO' # Mudar diretório
    os.chdir(path) # Lista com nome das abas e GBs
    sheets = ['0100_1', '0100_2',' 0100_3', '0200_1', '0200_2', '0250_1', '0250_2',\
              '0250_3', '0300_1', '0300_2', '0300_3', '0300_4', '0400_1', '0400_2',\
              '0400_3', '0400_4', '0500_1', '0500_2', '0500_3', '0600_1', '0600_2']
    # gbs = ['MFT', 'BEG', 'CC', 'ED', 'BT', 'PS_CAP', 'PS_CtP', 'PT', 'SG', 'TT', 'AA', 'ONM']
    gbs = ['CC']
    for gb in gbs:
        try:
            path = r'\\bosch.com\dfsrb\DfsBR\LOC\Ca1\Pur\rbla\pur1\Internal_Datastore\Automation Anywhere Files\GS\Reconciliation FIxCO'
            concatenate(gb, path)
            path = path + '\\' + gb + '_KE24.xlsx'
            df = read_file(gb, path)
            dfs = groupby(df)
            output = gb + '_KE24.xlsx'
            save_dfs(dfs, sheets, output)
        except:
            print('error in GB ' + gb)
    return df

df = main()