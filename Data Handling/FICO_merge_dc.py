import pandas as pd
import os


def save_dfs(df_list, sheet_list, file_name):
    '''
        Salvamento das visualizações criadas na função groupby() em planilha .xlsx
    '''
    writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter') # Criar objeto para salvamento em formato .xlsx
    for dataframe, sheet in zip(df_list, sheet_list):
        dataframe.to_excel(writer, sheet_name = sheet, startrow = 0 , startcol = 0, index = False) # Salvar arquivo em múltiplas abas (1 por DF)
    writer.save()
    return True


def merge(gbs, sheets, path):
    for gb in gbs:
        if os.path.exists(gb + '_KE5Z.xlsx') == True and os.path.exists(gb + '_KE24.xlsx') == True: # Verificar se as bases existem
            comparison = {} # Dicionário para armazenar DataFrames
            output = gb + '_COMPARISON.xlsx'
            for sheet in sheets:
                KE5Z = path + "\\" + gb + "_KE5Z.xlsx"
                KE24 = path + "\\" + gb + "_KE24.xlsx"
                KE5Z = pd.read_excel(KE5Z, sheet_name = sheet)
                KE24 = pd.read_excel(KE24, sheet_name = sheet)
                KE5Z.iloc[:,0] = [x.upper().strip() for x in KE5Z.iloc[:,0].astype(str)] # List comprehension para padronizar colunas de busca
                KE24.iloc[:,0] = [x.upper().strip() for x in KE24.iloc[:,0].astype(str)]
                merge = KE5Z.merge(KE24, left_on = KE5Z.columns[0], right_on = KE24.columns[0], how = 'left').fillna(0) # Agrupar bases
                if len(merge.columns) == 4: # Caso as colunas não tenham o mesmo nome, remover a duplicata que é gerada pelo left join
                    merge.drop(columns = merge.columns[2], inplace = True)
                merge.rename(columns = {merge.columns[2]:'KE24'}, inplace = True)
                merge['Delta'] = merge.iloc[:, [1]].sum(axis = 1) - merge.iloc[:, [2]].sum(axis = 1) # Incluir coluna 'Delta' B2-C2
                merge[merge.columns[1]] = pd.to_numeric(merge[merge.columns[1]]) # Converter colunas para numérico
                merge[merge.columns[2]] = pd.to_numeric(merge[merge.columns[2]])
                merge[merge.columns[1]].apply(lambda x: '%.2f' % x) # Remover máscara de notação científica
                merge[merge.columns[2]].apply(lambda x: '%.2f' % x)
                merge[merge.columns[3]].apply(lambda x: '%.2f' % x)
                comparison[sheet] = merge # Passar Dataframes para dicionário
            save_dfs(comparison.values(), comparison.keys(), output) # Gerar .xlsx com abas das comparações
            print(output)
    return True

def main():
    path = r'\\bosch.com\dfsrb\DfsBR\LOC\Ca1\Pur\rbla\pur1\Internal_Datastore\Automation Anywhere Files\GS\Reconciliation FIxCO' # Mudar diretório
    os.chdir(path)
    # gbs = ['MFT', 'BEG', 'CC', 'ED', 'BT', 'PS_CAP', 'PS_CtP', 'PT', 'SG', 'TT', 'AA', 'ONM']
    gbs = ['CC']
    sheets = ['0100_1', '0100_2',' 0100_3', '0200_1', '0200_2', '0250_1', '0250_2',\
              '0250_3', '0300_1', '0300_2', '0300_3', '0300_4', '0400_1', '0400_2',\
              '0400_3', '0400_4', '0500_1', '0500_2', '0500_3', '0600_1', '0600_2']
    merge(gbs, sheets, path)
    return True

main()