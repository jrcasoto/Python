import os
import pandas as pd
import string


def concatenate(gb, path):
    '''
        Concatenar arquivos baixados do SAP em formato $GB$_KE5Z.txt
    '''
    concatenated = ''
    counter = 0
    n = 9 # Usado para remover cabeçalho duplicado
    for f in os.listdir(path): # Iterar para cada arquivo na pasta de desenvolvimento
        if '.txt' in f and gb in f[:7] and 'KE5Z' in f: # Checar se extensão do arquivo = '.txt' e se a GB é a respectiva (até primeiros 7 caracteres)
            with open(f) as fp:
                for _ in range(n): # Pular cabeçalho
                    next(fp)
                data = fp.read()
            concatenated += data # Concatenar arquivos
            counter += 1
            if counter > 0: # Não colar cabeçalho das próximas n+1 bases
                n = 10
    if counter > 0:
        with open(gb + '_KE5Z.txt', 'a+') as appended: # Gerar novo arquivo $GB$.txt
            appended.write(concatenated) # Gerar base concatenada
        return appended
    else:
        return 1


def convert_file(gb, path):
    '''
        Converter encoding do arquivo de texto consolidado na função concatenate() em formato 'utf-8
    '''
    f= open(path, 'r', encoding="ANSI") # Abrir file original
    content= f.read()
    f.close()
    f= open(path, 'w', encoding="utf-8") # Passar conteúdo em novo file com encoding
    f.write(content)
    f.close()
    print(gb + ' file converted.')
    return f


def read_file(gb, path):
    '''
        Ler DataFrame consolidado para consolidação das tabelas na função groupby()
    '''
    df = pd.read_csv(path, delimiter = '\t') # Ler DataFrame concatenado
    mcont = str(df.filter(like='MCont').columns[0])
    df[mcont] = df[mcont].str.replace(' ', '').str.replace(',','.') # Formatar coluna 'Moeda em contabilização'
    df[mcont] = pd.to_numeric(df[mcont]).fillna(0)
    df.iloc[:,[x for x in range(18,24)]] = df.iloc[:,[x for x in range(18,24)]].fillna('blank')
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
    # Nomes das colunas podemo variar. logo é feita um filtro com termo de busca aproximado
    mcont = str(df.filter(like='MCont').columns[0])
    pep = str(df.filter(like='PEP').columns[0])

    # AF 0100
    # 0100-1 > AF 0100 + Material e Soma(Em moeda de contabilização)
    AF0100_1 = df.loc[(df['Área func.'] == 100)].groupby('Material')[mcont].sum()

    # 0100-2 > AF 0100 + Centro de Lucro e Soma(Em moeda de contabilização)
    AF0100_2 = df.loc[(df['Área func.'] == 100)].groupby('Cen.lucro')[mcont].sum()

    # 0100-3 > AF 0100 + Num. Doc. Ref. e Soma(Em moeda de contabilização)
    AF0100_3 = df.loc[(df['Área func.'] == 100)].groupby('Nº doc.')[mcont].sum() # número documento referência

    # AF 0200
    # 0200-1 > AF 0200 + Material e Soma(Em moeda de contabilização)
    AF0200_1 = df.loc[(df['Área func.'] == 200)].groupby('Material')[mcont].sum()

    # 0200-2 > AF 0200 + Centro de Lucro e Soma(Em moeda de contabilização)
    AF0200_2 = df.loc[(df['Área func.'] == 200)].groupby('Cen.lucro')[mcont].sum()

    # AF 0250
    # 0250-1 > AF 0250 + Centro custo e Soma(Em moeda de contabilização)
    AF0250_1 = df.loc[(df['Área func.'] == 250)].groupby('Centro cst')[mcont].sum()

    # 0250-2 > AF 0250 + Ordem e Soma(Em moeda de contabilização)
    AF0250_2 = df.loc[(df['Área func.'] == 250)].groupby('Ordem')[mcont].sum()

    # 0250-3 > AF 0250 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0250_3 = df.loc[(df['Área func.'] == 250)].groupby(pep)[mcont].sum()

    # 0250-4 > AF 0250 + Num. Conta e Soma(Em moeda de contabilização)
    AF0250_4 = df.loc[(df['Área func.'] == 250)].groupby('Nº conta')[mcont].sum()

    # AF 0300
    # 0300-1 > AF 0300 + Ordem e Soma(Em moeda de contabilização)
    AF0300_1 = df.loc[(df['Área func.'] == 300)].groupby('Ordem')[mcont].sum()

    # 0300-2 > AF 0300 + Centro Custo e Soma(Em moeda de contabilização)
    AF0300_2 = df.loc[(df['Área func.'] == 300)].groupby('Centro cst')[mcont].sum()

    # 0300-3 > AF 0300 + Material e Soma(Em moeda de contabilização)
    AF0300_3 = df.loc[(df['Área func.'] == 300)].groupby('Material')[mcont].sum()

    # 0300-4 > AF 0300 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0300_4 = df.loc[(df['Área func.'] == 300)].groupby('Cen.lucro')[mcont].sum()

    # AF 0400
    # 0400-1 > AF 0400 + Centro Custo e Soma(Em moeda de contabilização)
    AF0400_1 = df.loc[(df['Área func.'] == 400)].groupby('Centro cst')[mcont].sum()

    # 0400-2 > AF 0400 + Ordem e Soma(Em moeda de contabilização)
    AF0400_2 = df.loc[(df['Área func.'] == 400)].groupby('Ordem')[mcont].sum()

    # 0400-3 > AF 0400 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0400_3 = df.loc[(df['Área func.'] == 400)].groupby(pep)[mcont].sum()

    # 0400-4 > AF 0400 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0400_4 = df.loc[(df['Área func.'] == 400)].groupby('Cen.lucro')[mcont].sum()

    # AF 0500
    # 0500-1 > AF 0500 + Centro Custo e Soma(Em moeda de contabilização)
    AF0500_1 = df.loc[(df['Área func.'] == 500)].groupby('Centro cst')[mcont].sum()

    # 0500-2 > AF 0500 + Ordem e Soma(Em moeda de contabilização)
    AF0500_2 = df.loc[(df['Área func.'] == 500)].groupby('Ordem')[mcont].sum()

    # 0500-3 > AF 0500 + Elem.PEP e Soma(Em moeda de contabilização)
    AF0500_3 = df.loc[(df['Área func.'] == 500)].groupby(pep)[mcont].sum()

    # AF 0600
    # 0600-1 > AF 0600 + Centro Lucro e Soma(Em moeda de contabilização)
    AF0600_1 = df.loc[(df['Área func.'] == 600)].groupby('Cen.lucro')[mcont].sum()

    # 0600-2 > AF 0600 + Ordem e Soma(Em moeda de contabilização)
    AF0600_2 = df.loc[(df['Área func.'] == 600)].groupby('Nº conta')[mcont].sum()

    dfs = [AF0100_1, AF0100_2, AF0100_3, AF0200_1, AF0200_2, AF0250_1, AF0250_2,\
             AF0250_3, AF0250_4, AF0300_1, AF0300_2, AF0300_3, AF0300_4, AF0400_1, \
             AF0400_2, AF0400_3, AF0400_4, AF0500_1, AF0500_2, AF0500_3, AF0600_1, \
             AF0600_2]
    return dfs

def main():
    '''
        Chamada de funções
    '''
    path = r'\\bosch.com\dfsrb\DfsBR\LOC\Ca1\Pur\rbla\pur1\Internal_Datastore\Automation Anywhere Files\GS\Reconciliation FIxCO' # Mudar diretório
    os.chdir(path) # Lista com nome das abas e GBs
    sheets = ['0100_1', '0100_2',' 0100_3', '0200_1', '0200_2', '0250_1', '0250_2',\
              '0250_3', '0250_4', '0300_1', '0300_2', '0300_3', '0300_4', '0400_1', \
              '0400_2', '0400_3', '0400_4', '0500_1', '0500_2', '0500_3', '0600_1', \
              '0600_2']
    # gbs = ['MFT', 'BEG', 'CC', 'ED', 'BT', 'PS_CAP', 'PS_CtP', 'PT', 'SG', 'TT', 'AA', 'ONM']
    gbs = ['CC']
    for gb in gbs:
        try:
            path = r'\\bosch.com\dfsrb\DfsBR\LOC\Ca1\Pur\rbla\pur1\Internal_Datastore\Automation Anywhere Files\GS\Reconciliation FIxCO'
            concatenate(gb, path)
            path = path + '\\' + gb + '_KE5Z.txt'
            convert_file(gb, path)
            df = read_file(gb, path)
            dfs = groupby(df)
            output = gb + '_KE5Z.xlsx'
            save_dfs(dfs, sheets, output)
        except:
            print('error in GB ' + gb)
    return df

d = main()