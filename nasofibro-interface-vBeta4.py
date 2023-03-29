from PySimpleGUI import PySimpleGUI as sg

from datetime import date

data_atual = date.today()
data_em_texto = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)

def janela_inicial():
    layout = [
        [sg.Text("Bem vindo ao Nasofibrolaudator: A melhor solução para laudo de nasofibrolaringoscopia.")],
        [sg.Text("Criado e desenvolvido por: Carlos Nardi")],
        [sg.Button("Iniciar")]
    ]
    return sg.Window("Nasofibrolaudator",layout = layout,finalize=True)



def janela_laudo():
    layout = [
       # Identificação:
       [sg.Text('Dados de identificação:'), sg.Checkbox('Não acrescentar',key='sem_id_pac'), sg.Text('Nome: '), sg.Input(size=(20,0),key='nome'), sg.Text('Nome do médico solicitante:'), sg.Input(size=(20,0),key='medico'), sg.Text('Data de nascimento:'), sg.Input(size=(9,0),key='nascimento')],
       [sg.Text('Foi utilizado anestésico:'), sg.Radio('Sim','anest',key='com_anestesico'), sg.Radio('Não','anest',key='sem_anestesico'), sg.Text('Paciente colaborou para o procedimento:'), sg.Radio('Sim','colab',key='colaborou'), sg.Radio('Não','colab',key='nao_colaborou')],
       # Cavidade Nasal:
       [sg.Text('Cavidade nasal:', text_color='yellow'), sg.Text('Mucosa pálida: '), sg.Radio('Sim','cnp',key='palidez'), sg.Radio('Não','cnp',key='sem_palidez'), sg.Text('Hipertrofia de conchas nasais:'), sg.Radio('Não','cnh',key='sem_hipert_concha'), sg.Radio('Bilateral','cnh',key='hipert_bilateral'), sg.Radio('Direita','cnh',key='hipert_dir'), sg.Radio('Esquerda','cnh',key='hipert_esq'), sg.Text('Meato médio livre:'), sg.Checkbox('Sim',key='meato_livre'), sg.Text('Não:'), sg.Input(size=(20,0),key='meato_comp')], 
       [sg.Text('Desvio septal:'), sg.Checkbox('Não',key='sem_desvio'), sg.Text('Qual a zona afetada*?'), sg.Checkbox('1',key='desvio1'), sg.Checkbox('2',key='desvio2'), sg.Checkbox('3',key='desvio3'), sg.Checkbox('4',key='desvio4'), sg.Checkbox('5',key='desvio5'), sg.Text('Qual o tipo de desvio septal?'), sg.Radio('Simples','tipo_desvio',key='desvio_simples'), sg.Radio('Crista','tipo_desvio',key='desvio_crista'), sg.Radio('Esporão','tipo_desvio',key='desvio_esporao'), sg.Radio('Misto','tipo_desvio',key='desvio_misto'), sg.Text('Lateralidade:'), sg.Checkbox('Direita', key='desvio_dir'), sg.Checkbox('Esquerda', key='desvio_esq'), sg.Checkbox('Bilateral', key='desvio_bilat')],
       [sg.Text('Realizado teste com vasoconstritor*?'), sg.Radio('Não','teste_vaso',key='sem_teste_vaso'), sg.Radio('Grau 1','teste_vaso',key='teste_vaso_1'), sg.Radio('Grau 2','teste_vaso',key='teste_vaso_2'), sg.Radio('Grau 3','teste_vaso',key='teste_vaso_3')],
       [sg.Text('Há sinais de sangramento recente?'), sg.Radio('Não','epistaxe',key='sem_epistaxe'), sg.Text('Qual área está o foco de sangramento*?'), sg.Radio('Área de Little','epistaxe',key='epistaxe_ant'), sg.Radio('Área de Woodruff','epistaxe',key='epistaxe_post'), sg.Text('Lateralidade:'), sg.Checkbox('Direita',key='epistaxe_dir'), sg.Checkbox('Esquerda',key='epistaxe_esq')],
       # Rinofaringe:
       [sg.Text('Rinofaringe:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='rino_nl')],
       [sg.Text('Apresenta adenóide?'), sg.Radio('Não','adenoide',key='sem_adenoide'), sg.Radio('Granulações','adenoide',key='adenoide_gran'), sg.Radio('Hipertrofia','adenoide',key='adenoide_hiper'), sg.Text('Qual o grau?*'), sg.Radio('1','adenoide_grau',key='adenoide_1'), sg.Radio('2','adenoide_grau',key='adenoide_2'), sg.Radio('3','adenoide_grau',key='adenoide_3'), sg.Text('Fossetas de Rosenmüller livres?'), sg.Checkbox('Sim',key='fosseta_livre'), sg.Text('Não:'), sg.Input(size=(20,0),key='fosseta_acometida'), sg.Text('Fechamento velopalatino:'), sg.Radio('Completo','velo',key='velo_completo'), sg.Radio('Incompleto','velo',key='velo_incompleto'), sg.Text('Padrão de fechamento:*'), sg.Radio('Coronal','velo_padrao',key='velo_coronal'), sg.Radio('Sagital','velo_padrao',key='velo_sagital'), sg.Radio('Circular','velo_padrao',key='velo_circular')], 
       [sg.Text('Óstios das tubas auditivas pérvios?'), sg.Checkbox('Sim',key='tuba_livre'), sg.Text('Não:'), sg.Input(size=(20,0), key='tuba_acometida'), sg.Text('Presença de tumor?'), sg.Radio('Não','rino_tu',key='sem_rino_tu'), sg.Text('Localização:'), sg.Radio('Parede posterior','rino_tu',key='rino_tu_post'), sg.Radio('Fosseta de Rosenmüller','rino_tu',key='rino_tu_fosseta'), sg.Text('Lateralidade:'), sg.Radio('Direita','rino_lat',key='rino_dir'), sg.Radio('Esquerda','rino_lat',key='rino_esq')],
       # Orofaringe:
       [sg.Text('Orofaringe:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='oro_nl'), sg.Text('Presença de hipertrofia de amígdalas?'), sg.Checkbox('Sim',key='amig_sim'), sg.Checkbox('Simétricas?',key='amig_simetrica'), sg.Text('Assimétricas?'), sg.Input(size=(10,0), key='amig_assim'), sg.Text('Grau:*'), sg.Radio('I', 'amig_grau', key='amig_1'), sg.Radio('II', 'amig_grau',key='amig_2'), sg.Radio('III', 'amig_grau',key='amig_3'), sg.Radio('IV', 'amig_grau',key='amig_4'), sg.Text('Há alguma alteração adicional?'), sg.Checkbox('Não',key='oro_sem_ad'), sg.Text('Se sim, descreva o achado e o que está normal:'), sg.Input(size=(30,0),key='oro_anl')],
       # Laringe: 
       [sg.Text('Supraglote:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='supra_nl'), sg.Text('Mobilidade preservada?'), sg.Radio('Sim','mobil_supra',key='mobil_supra_ok'), sg.Radio('Paresia','mobil_supra',key='paresia_supra'), sg.Radio('Paralisia','mobil_supra',key='paralisia_supra'), sg.Text("Lateralidade:"), sg.Radio('Direita', 'lat_mobil_supra', key='lat_mobil_supra_dir'), sg.Radio('Esquerda', 'lat_mobil_supra', key='lat_mobil_supra_esq')],
       [sg.Text('Há sinais secundários a Doença do Refluxo Gastroesofágico?'), sg.Checkbox('Não', key='drge_ausente'), sg.Checkbox('Hiperemia', key='drge_hiper'), sg.Checkbox('Edema', key='drge_edema'), sg.Checkbox('Paquidermia', key='drge_paqui'), sg.Text('Há alguma alteração adicional?'), sg.Checkbox('Não',key='sem_ach_ad_supra'), sg.Text('Descreva os achados incluindo a normalidade:'), sg.Input(size=(10,0), key='alter_supra')],
       [sg.Text('Glote:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='glote_nl'), sg.Text('Mobilidade glótica preservada?'), sg.Radio('Sim','motil_glote',key='motil_glote_ok'), sg.Radio('Paresia','motil_glote',key='paresia_glote'), sg.Radio('Paralisia','motil_glote',key='paralisia_glote'), sg.Text('Lateralidade:'), sg.Radio('Direita','motil_glote_lat',key='motil_glote_lat_dir'), sg.Radio('Esquerda','motil_glote_lat',key='motil_glote_lat_esq')], 
       [sg.Text('Lesão glótica?'), sg.Radio('Não','lesao_glote',key='glote_sem_lesao'), sg.Text('|'), sg.Radio('Nódulo','lesao_glote',key='nodulo_vocal'), sg.Checkbox('Reação Contralateral',key='nodulo_reac_contra'), sg.Text('|'), sg.Radio('Edema de Reinke','lesao_glote',key='edema_reinke'), sg.Text('Grau*:'), sg.Radio('1','grau_edema',key='reinke_1'), sg.Radio('2','grau_edema',key='reinke_2'), sg.Radio('3','grau_edema',key='reinke_3'), sg.Text('|'), sg.Radio('Cisto','lesao_glote',key='cisto_vocal'), sg.Text('|'), sg.Radio('Pólipo','lesao_glote',key='polipo_vocal')], 
       [sg.Text('Lateralidade e localização(s/n):'), sg.Checkbox('Direita',key='glote_lesao_lat_dir'), sg.Text('Terço:'), sg.Checkbox('Anterior',key='glote_terco_ant_dir'), sg.Checkbox('Médio',key='glote_terco_med_dir'), sg.Checkbox('Posterior',key='glote_terco_post_dir'), sg.Text('|'), sg.Checkbox('Esquerda',key='glote_lesao_lat_esq'), sg.Text('Terço:'), sg.Checkbox('Anterior',key='glote_terco_ant_esq'), sg.Checkbox('Médio',key='glote_terco_med_esq'), sg.Checkbox('Posterior',key='glote_terco_post_esq'), sg.Text('|'), sg.Checkbox('Bilateral',key='glote_lesao_lat_bilat')],
       [sg.Radio('Leucoplasia','lesao_glote',key='glote_leuco'), sg.Text('|'), sg.Radio('Tumor','lesao_glote',key='glote_tumor'), sg.Text('Aspecto:'), sg.Radio('Vegetante','tu_glote_asp',key='tu_glote_veg'), sg.Radio('Ulcerado','tu_glote_asp',key='tu_glote_ulc'), sg.Radio('Úlcero-infiltrativo','tu_glote_asp',key='tu_glote_ui'), sg.Radio('Pediculado','tu_glote_asp',key='tu_glote_ped'), sg.Radio('Séssil','tu_glote_asp',key='tu_glote_sess'), sg.Radio('Submucoso','tu_glote_asp',key='tu_glote_sub'), sg.Text('Descreva localização e lateralidade para leucoplasia ou tumor:'), sg.Input(size=(10,0), key='desc_leuco_tu')],  
       [sg.Text('Fenda vocal:'), sg.Radio('Ausente','fenda_vocal',key='fenda_ausente'), sg.Radio('Triangular posterior','fenda_vocal',key='fenda_tri_post'), sg.Radio('Triangular médio posterior','fenda_vocal',key='fenda_tri_med_post'), sg.Radio('Triangular ântero-posterior','fenda_vocal',key='fenda_tri_ant_post'), sg.Radio('Fusiforme','fenda_vocal',key='fenda_fusiforme'), sg.Radio('Fusiforme anterior','fenda_vocal',key='fenda_fusi_ant'), sg.Radio('Fusiforme ântero-posterior','fenda_vocal',key='fenda_fusi_ant_post'), sg.Radio('Fusiforme posterior','fenda_vocal',key='fenda_fusi_post')], 
       [sg.Radio('Paralela','fenda_vocal',key='fenda_paralela'), sg.Radio('Dupla','fenda_vocal',key='fenda_dupla'), sg.Radio('Ampulheta','fenda_vocal',key='fenda_ampu'), sg.Radio('Irregular','fenda_vocal',key='fenda_irreg')], 
       [sg.Text('Infraglote:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='infra_nl'), sg.Text('Se sim, descreva o achado:'), sg.Input(size=(30,0),key='infra_alterado')],
       # Hipofaringe:
       [sg.Text('Hipofaringe:', text_color='yellow'), sg.Text('Há alguma alteração?'), sg.Checkbox('Não',key='hipofaringe_nl'), sg.Text('Tumor? Qual subsítio acometido?'), sg.Checkbox('Recesso Piriforme',key='lesao_recesso'), sg.Checkbox('Parede posterior',key='lesao_par_post'), sg.Checkbox('Área retrocricóide',key='lesao_retrocri'), sg.Text('Aspecto:'), sg.Radio('Vegetante','lesao_hipo',key='lesao_hipo_veg'), sg.Radio('Úlcero-infiltrativo','lesao_hipo',key='lesao_hipo_ui')], 
       [sg.Text('Lateralidade:'), sg.Radio('Direita','lesao_hipo_lat',key='lesao_hipo_lat_dir'), sg.Radio('Esquerda','lesao_hipo_lat',key='lesao_hipo_lat_esq')],


       [sg.Button('Finalizar'), sg.Button('Comentários'), sg.Button('Reiniciar'), sg.Text('OBS: Itens identificados com (*) apresentam comentários no botão dedicado.')]
    ]

    return sg.Window('Nasofibrolaudator', layout = layout,finalize=True)

def janela_coment():
    layout = [
        [sg.Text('Cavidade nasal:', text_color='yellow')],
        [sg.Text('''--> Zonas de desvio septal: (3 e 4 são as mais comuns).
        Zona 1: vestíbulo nasal. Zona 2: entre vestibulo fossal e vãlvula nasal. Zona 3: limitada entre 2 e 4. Zona 4: metade anterior dos cornetos. Zona 5: metade posterior dos cornetos.         
        --> Graduação do desvio septal através de teste com vasoconstritor:
        1. Desvio discreto; 2. Septo toca à parede lateral, mas perde contato após uso de vasoconstritor; 3. Septo encosta na parede lateral, mantendo mesmo após vasoconstritor.
        --> Áreas de epistaxe: 
        Área de Little (porção anterior do septo nasal na topografia do plexo de Kisselbach); área de Woodruff (posterior a concha média)
        ''')],
        [sg.Text('Rinofaringe:', text_color='yellow')],
        [sg.Text('''--> Graduação da hipertrofia de adenóide segundo Wormald & Prescott: 
        Grau 1: compromete até 1/3 da coana; Grau 2: 2/3 da coana, podendo causar compressão do óstio da tuba auditiva; Grau 3: mais de 2/3 da coana podendo causar obstrução extrínseca da tuba auditiva. 
        ''')],
        [sg.Text('''--> Fechamento velopalatino: 
        Os padrões de fechamento velofaríngeo podem ser classificados em: 
        - coronal, em que há movimentação predominante do palato mole em direção à parede posterior da faringe
        - sagital, em que há movimentação predominante das paredes laterais da faringe em sentido medial 
        - circular, em que ocorre movimentação de forma equilibrada entre paredes laterais e palato mole''')],
        [sg.Text('Orofaringe:', text_color='yellow')],
        [sg.Text(r'''--> Graduação da hipertrofia de amígdalas: 
        Grau 1: amígdalas ocupam 25% do espaço orofaríngeo; Grau 2: entre 25 - 50%; Grau 3: entre 50 - 75%; Grau 4: mais de 75%
        ''')], 
        [sg.Text('''--> Graduação do edema de Reinke: 
        Grau 1: contato apenas da porção anterior das PPVV; Grau 2: anterior e médio; Grau 3: toda a porção membranosa.
        ''')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Comentários', layout=layout, finalize=True)

def janela_final():
    layout = [
        [sg.Output(size=(150,20))],
        [sg.Button('Voltar'), sg.Button('Fechar')]
    ]
    return sg.Window('Nasofibrolaudator', layout=layout, finalize=True)

janela1 = janela_inicial()

janela1, janela2, janela3, janela4 = janela_inicial(), None, None, None

while True: 
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED and sg.popup_yes_no('Deseja realmente sair?') == 'Yes':
        break
    if window == janela2 and event == sg.WIN_CLOSED and sg.popup_yes_no('Deseja realmente sair?') == 'Yes':
        break


    if window == janela1 and event == "Iniciar":
        janela2 = janela_laudo()
        janela1.hide()
    if window == janela2 and event == 'Reiniciar':
        janela2.close()
        janela1.un_hide()
    if window == janela2 and event == 'Comentários':
        janela3 = janela_coment()
    if window == janela3 and event == 'Fechar':
        janela3.close()
        #rever erro ao fechar a janela comentários
    if window == janela2 and event == 'Finalizar':
        janela4 = janela_final()
        janela2.hide()
    if window == janela4 and event == 'Voltar' or event == sg.WIN_CLOSED:
        janela4 = janela_final()
        janela4.hide()
        janela2.un_hide()



    
    if window == janela2:
       nome = values['nome']
       nascimento = values['nascimento']
       medico = values['medico']

       
    
    if window == janela2 and values['sem_anestesico'] == True:
        anestesia = "sem uso de anestesia tópica"
    elif window == janela2 and values['com_anestesico'] == True:
        anestesia = "sob anestesia tópica com lidocaína a 10%"    
   
    if window == janela2 and values['nao_colaborou'] == True:
        colaboracao = 'Paciente com baixa tolerância a realização do exame sendo esse realizado com dificuldade técnica.'
    elif window == janela2 and values['colaborou'] == True:
        colaboracao = 'Paciente colaborou bem para o exame.'
    
    #Inicio - Cavidade nasal
    if window == janela2 and values['palidez'] == True:
        mucosa_nasal = 'Mucosa nasal pálida'
    elif window == janela2 and values['sem_palidez'] == True:
        mucosa_nasal = 'mucosa nasal de coloração habitual'

    if window == janela2 and values['sem_hipert_concha']:
        concha_nasal = 'conchas nasais normotróficas'
    elif window == janela2 and values['hipert_bilateral']:
        concha_nasal = 'hipertrofia de conchas nasais bilaterais'
    elif window == janela2 and values['hipert_dir']:
        concha_nasal = 'hipertrofia de conchas nasais à direita'
    elif window == janela2 and values['hipert_esq']:
        concha_nasal = 'hipertrofia de conchas nasais à esquerda'

    if window == janela2 and values['meato_livre']:
        meato_medio = 'meato médio livre'
    elif window == janela2 and values['meato_comp']:
        meato_medio = values['meato_comp']

    if window == janela2 and values['sem_desvio']:
        desvio_septal = 'ausência de desvio septal'
    elif window == janela2 and values['desvio1']:
        desvio_septal = 'presença de desvio septal localizado na zona 1, '
    elif window == janela2 and values['desvio2']:
        desvio_septal = 'presença de desvio septal localizado na zona 2, '
    elif window == janela2 and values['desvio3']:
        desvio_septal = 'presença de desvio septal localizado na zona 3, '
    elif window == janela2 and values['desvio4']:
        desvio_septal = 'presença de desvio septal localizado na zona 4, '
    elif window == janela2 and values['desvio5']:
        desvio_septal = 'presença de desvio septal localizado na zona 5, '
    if window == janela2 and values['desvio_simples']:        
        desvio_septal = desvio_septal + 'do tipo simples, '
    elif window == janela2 and values['desvio_crista']:        
        desvio_septal = desvio_septal + 'do tipo crista, '
    elif window == janela2 and values['desvio_esporao']:        
        desvio_septal = desvio_septal + 'do tipo esporão, '
    elif window == janela2 and values['desvio_misto']:         
        desvio_septal = desvio_septal + 'do tipo misto, '    
    if window == janela2 and values['desvio_dir']:
        desvio_septal = desvio_septal + 'à direita'
    elif window == janela2 and values['desvio_esq']: 
        desvio_septal = desvio_septal + 'à esquerda'
    elif window == janela2 and values['desvio_bilat']: 
        desvio_septal = desvio_septal + 'bilateral'  
    if window == janela2 and values['sem_teste_vaso']:
        desvio_septal = desvio_septal
    elif window == janela2 and values['teste_vaso_1']:
        desvio_septal = desvio_septal + ' grau I'
    elif window == janela2 and values['teste_vaso_2']:
        desvio_septal = desvio_septal + ' grau II'
    elif window == janela2 and values['teste_vaso_3']:
        desvio_septal = desvio_septal + ' grau III'
    
    if window == janela2 and values['sem_epistaxe']:
        epistaxe = 'ausência de sinais de sangramento'
    elif window == janela2 and values['epistaxe_ant']:
        epistaxe = 'presença de foco de sangramento localizado na área de Little, '
    elif window == janela2 and values['epistaxe_post']:
        epistaxe = 'presença de foco de sangramento localizado na área de Woodruff, '
    if window == janela2 and values['epistaxe_dir']:
        epistaxe = epistaxe + 'à direita'
    elif window == janela2 and values['epistaxe_esq']:
        epistaxe = epistaxe + 'à esquerda'

    # início - Rinofaringe:
    if window == janela2 and values['rino_nl'] == True:
        rinofaringe = r'Mucosa íntegra e sem alterações, óstios de tubas auditivas pérvios, fossetas de Rosenmüller livres de lesões.'
    elif window == janela2 and values['sem_adenoide']:
        rinofaringe = ''
    elif window == janela2 and values['adenoide_gran']:
        rinofaringe = 'Presença de granulações adenóideas, '
    elif window == janela2 and values['adenoide_hiper']:
        rinofaringe = 'Presença de hipertrofia de adenóide, '
    if window == janela2 and values['adenoide_1']:
        rinofaringe = rinofaringe + 'grau I segundo Wormald & Prescott, '
    elif window == janela2 and values['adenoide_2']:
        rinofaringe = rinofaringe + 'grau II segundo Wormald & Prescott, '
    elif window == janela2 and values['adenoide_3']:
        rinofaringe = rinofaringe + 'grau III segundo Wormald & Prescott, '
    if window == janela2 and values['fosseta_livre']:
        rinofaringe = rinofaringe + 'fossetas de Rosenmüller livres, '
    elif window == janela2 and values['fosseta_acometida']:
        fosseta_acom = values['fosseta_acometida']
        rinofaringe = rinofaringe + fosseta_acom + ', '
    if window == janela2 and values['velo_completo']:
        rinofaringe = rinofaringe + 'fechamento velopalatino preservado, '
    elif window == janela2 and values['velo_incompleto']:
        rinofaringe = rinofaringe + 'fechamento velopalatino incompleto, '
    if window == janela2 and values['velo_coronal']:
        rinofaringe = rinofaringe + 'de padrão coronal, '
    if window == janela2 and values['velo_sagital']:
        rinofaringe = rinofaringe + 'de padrão sagital, '
    if window == janela2 and values['velo_circular']:
        rinofaringe = rinofaringe + 'de padrão circular, '
    if window == janela2 and values['tuba_livre']:
        rinofaringe = rinofaringe + 'óstio das tubas auditivas pérvios, '
    elif window == janela2 and values['tuba_acometida']:
        tuba_acom = values['tuba_acometida']
        rinofaringe = rinofaringe + tuba_acom + ', '
    if window == janela2 and values['sem_rino_tu']:
        rinofaringe = rinofaringe + 'ausência de lesões.'
    elif window == janela2 and values['rino_tu_post']:
        rinofaringe = rinofaringe + 'presenca de lesão tumoral, localizado na parede posterior, '
    elif window == janela2 and values['rino_tu_fosseta'] and values['rino_dir']:
        rinofaringe = rinofaringe + 'presenca de lesão tumoral, localizado na na fosseta de Rosenmüller direita.'
    elif window == janela2 and values['rino_tu_fosseta'] and values['rino_esq']:
        rinofaringe = rinofaringe + 'presenca de lesão tumoral, localizado na na fosseta de Rosenmüller esquerda.'

    # Início - Orofaringe:
    if window == janela2 and values['oro_nl']:
        orofaringe = 'Base da língua, lojas amigdalinas, palato mole e parede posterior preservados'
    if window == janela2 and values['amig_sim']:
        orofaringe = 'Base da língua, palato mole e parede posterior preservados, hipertrofia de amígdalas '
        if window == janela2 and values['amig_1']:
            orofaringe = orofaringe + r' grau I'
        elif window == janela2 and values['amig_2']:
            orofaringe = orofaringe + r' grau II'
        elif window == janela2 and values['amig_3']:
            orofaringe = orofaringe + r' grau III'
        elif window == janela2 and values['amig_4']:
            orofaringe = orofaringe + r' grau IV'
        if window == janela2 and values['amig_simetrica']:
            orofaringe = orofaringe + ', simétricas e de aspecto habitual'  
        elif window == janela2 and values['amig_assim']:
            amig_assimetrica = values['amig_assim']
            orofaringe = orofaringe + ', ' + amig_assimetrica      
    elif window == janela2 and values['oro_anl']:
        orofaringe = values['oro_anl']

    # Início - Laringe:
    # Início - Supraglote:
    if window == janela2 and values['supra_nl']:
        supraglote = 'epiglote, aritenóides e bandas ventriculares com mobilidade e relevo sem alterações'
    elif window == janela2 and values['mobil_supra_ok']:
        supraglote = 'mobilidade preservada, '
    elif window == janela2 and values['paresia_supra'] and values['lat_mobil_supra_dir']:
        supraglote = 'paresia de hemilaringe direita, '
    elif window == janela2 and values['paresia_supra'] and values['lat_mobil_supra_esq']:
        supraglote = 'paresia de hemilaringe esquerda, '
    elif window == janela2 and values['paralisia_supra'] and values['lat_mobil_supra_dir']:
        supraglote = 'paralisia de hemilaringe direita, '
    elif window == janela2 and values['paralisia_supra'] and values['lat_mobil_supra_esq']:
        supraglote = 'paralisia de hemilaringe esquerda, '
    if window == janela2 and values['drge_ausente']:
        supraglote = supraglote + 'região interaritenóidea com mucosa de aspecto preservado'
    if window == janela2 and values['drge_hiper'] and values['drge_edema'] and values['drge_paqui']:
        supraglote = supraglote + 'presença de hiperemia e edema da mucosa interaritenóidea associado a paquidermia interaritenóidea'
    elif window == janela2 and values['drge_hiper'] and values['drge_paqui']:
        supraglote = supraglote + 'presença de hiperemia associado a paquidermia interaritenóidea'
    elif window == janela2 and values['drge_edema'] and values['drge_paqui']:
        supraglote = supraglote + 'presença de edema associado a paquidermia interaritenóidea'
    elif window == janela2 and values['drge_hiper'] and values['drge_edema']:
        supraglote = supraglote + 'presença de edema e hiperemia da região interaritenóidea'
    elif window == janela2 and values['drge_hiper']: 
        supraglote = supraglote + 'presença de hiperemia interaritenóidea'
    elif window == janela2 and values['drge_edema']:
        supraglote = supraglote + 'presença de edema da mucosa interaritenóidea'
    elif window == janela2 and values['drge_paqui']: 
        supraglote = supraglote + 'presença de paquidermia da mucosa interaritenóidea'
    if window == janela2 and values['sem_ach_ad_supra']:
        supraglote = supraglote + ', epiglote, aritenóides e bandas ventriculares sem lesões com relevo preservado'
    elif window == janela2 and values['alter_supra']:
        supraglote = supraglote + ', ' + values['alter_supra']
    # Início - Glote: 
    if window == janela2 and values['glote_nl']: 
        glote = 'mobilidade glótica preservada, pregas vocais livres e sem lesões'
    elif window == janela2 and values['motil_glote_ok']:
        glote = 'mobilidade glótica preservada, '
    elif window == janela2 and values['paresia_glote'] and values['motil_glote_lat_dir']:
        glote = 'paresia de prega vocal direita, '
    elif window == janela2 and values['paralisia_glote'] and values['motil_glote_lat_dir']:
        glote = 'paralisia de prega vocal direita, '
    elif window == janela2 and values['paresia_glote'] and values['motil_glote_lat_esq']:
        glote = 'paresia de prega vocal esquerda, '
    elif window == janela2 and values['paralisia_glote'] and values['motil_glote_lat_esq']:
        glote = 'paralisia de prega vocal esquerda, '
    
    #pensar no caso de paralisia bilateral - laringe congelada
    
    #agora será a parte de lesao
    if window == janela2 and values['glote_sem_lesao']:
        glote = glote + 'ausência de lesões nas pregas vocais'
    # Nódulo vocal:
    elif window == janela2 and values['nodulo_vocal'] and values['glote_lesao_lat_dir']:
        glote = glote + 'presença de nódulo vocal à direita, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_lesao_lat_esq']:
        glote = glote + 'presença de nódulo vocal à esquerda, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_lesao_lat_dir'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal à direita com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_lesao_lat_esq'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal à esquerda com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_ant_dir']:
        glote = glote + 'presença de nódulo vocal localizado no terço anterior da prega vocal direita, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_med_dir']:
        glote = glote + 'presença de nódulo vocal localizado no terço médio da prega vocal direita, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_post_dir']:
        glote = glote + 'presença de nódulo vocal localizado no terço posterior da prega vocal direita, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_ant_esq']:
        glote = glote + 'presença de nódulo vocal localizado no terço anterior da prega vocal esquerda, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_med_esq']:
        glote = glote + 'presença de nódulo vocal localizado no terço médio da prega vocal esquerda, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_post_esq']:
        glote = glote + 'presença de nódulo vocal localizado no terço posterior da prega vocal esquerda, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_ant_dir'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço anterior da prega vocal direita com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_med_dir'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço médio da prega vocal direita com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_post_dir'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço posterior da prega vocal direita com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_ant_esq'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço anterior da prega vocal esquerda com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_med_esq'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço médio da prega vocal esquerda com reação contralateral, '
    elif window == janela2 and values['nodulo_vocal'] and values['glote_terco_post_esq'] and values['nodulo_reac_contra']:
        glote = glote + 'presença de nódulo vocal localizado no terço posterior da prega vocal esquerda com reação contralateral, '
    # Edema de Reinke:
    if window == janela2 and values['edema_reinke']:
        glote = glote + 'presença de edema de Reinke, '
    if window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_dir']:
        glote = glote + 'presença de edema de Reinke à direita, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_esq']:
        glote = glote + 'presença de edema de Reinke à esquerda, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_bilat']:
        glote = glote + 'presença de edema de Reinke em pregas vocais, '
    elif window == janela2 and values['edema_reinke'] and values['reinke_1']:
        glote = glote + 'presença de edema de Reinke grau 1, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_dir'] and values['reinke_1']:
        glote = glote + 'presença de edema de Reinke à direita grau 1, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_esq'] and values['reinke_1']:
        glote = glote + 'presença de edema de Reinke à esquerda grau 1, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_bilat'] and values['reinke_1']:
        glote = glote + 'presença de edema de Reinke em pregas vocais grau 1, '
    elif window == janela2 and values['edema_reinke'] and values['reinke_2']:
        glote = glote + 'presença de edema de Reinke grau 2, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_dir'] and values['reinke_2']:
        glote = glote + 'presença de edema de Reinke à direita grau 2, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_esq'] and values['reinke_2']:
        glote = glote + 'presença de edema de Reinke à esquerda grau 2, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_bilat'] and values['reinke_2']:
        glote = glote + 'presença de edema de Reinke em pregas vocais grau 2, '     
    elif window == janela2 and values['edema_reinke'] and values['reinke_3']:
        glote = glote + 'presença de edema de Reinke grau 3, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_dir'] and values['reinke_3']:
        glote = glote + 'presença de edema de Reinke à direita grau 3, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_esq'] and values['reinke_3']:
        glote = glote + 'presença de edema de Reinke à esquerda grau 3, '
    elif window == janela2 and values['edema_reinke'] and values['glote_lesao_lat_bilat'] and values['reinke_3']:
        glote = glote + 'presença de edema de Reinke em pregas vocais grau 3, '
    # Cisto:
    if window == janela2 and values['cisto_vocal']: 
        glote = glote + 'presença de cisto vocal, '
    if window == janela2 and values['cisto_vocal'] and values['glote_lesao_lat_dir']:
        glote = glote + 'presença de cisto em prega vocal à direita, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_lesao_lat_esq']:
        glote = glote + 'presença de cisto em prega vocal à esquerda, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_ant_dir']:
        glote = glote + 'presença de cisto localizado no terço anterior da prega vocal direita, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_med_dir']:
        glote = glote + 'presença de cisto localizado no terço médio da prega vocal direita, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_post_dir']:
        glote = glote + 'presença de cisto localizado no terço posterior da prega vocal direita, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_ant_esq']:
        glote = glote + 'presença de cisto localizado no terço anterior da prega vocal esquerda, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_med_esq']:
        glote = glote + 'presença de cisto localizado no terço médio da prega vocal esquerda, '
    elif window == janela2 and values['cisto_vocal'] and values['glote_terco_post_esq']:
        glote = glote + 'presença de cisto localizado no terço posterior da prega vocal esquerda, '
    # Pólipo: 
    if window == janela2 and values['polipo_vocal']: 
        glote = glote + 'presença de pólipo vocal, '
    if window == janela2 and values['polipo_vocal'] and values['glote_lesao_lat_dir']:
        glote = glote + 'presença de pólipo em prega vocal à direita, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_lesao_lat_esq']:
        glote = glote + 'presença de pólipo em prega vocal à esquerda, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_ant_dir']:
        glote = glote + 'presença de pólipo localizado no terço anterior da prega vocal direita, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_med_dir']:
        glote = glote + 'presença de pólipo localizado no terço médio da prega vocal direita, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_post_dir']:
        glote = glote + 'presença de pólipo localizado no terço posterior da prega vocal direita, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_ant_esq']:
        glote = glote + 'presença de pólipo localizado no terço anterior da prega vocal esquerda, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_med_esq']:
        glote = glote + 'presença de pólipo localizado no terço médio da prega vocal esquerda, '
    elif window == janela2 and values['polipo_vocal'] and values['glote_terco_post_esq']:
        glote = glote + 'presença de pólipo localizado no terço posterior da prega vocal esquerda, '
    #Leucoplasia:
    if window == janela2 and values['glote_leuco']: 
        desc_leuco = values['desc_leuco_tu']
        glote = glote + 'presença de leucoplasia, ' + desc_leuco
    # if window == janela2 and values['glote_leuco'] and values['glote_lesao_lat_dir']:
    #     glote = glote + 'presença de leucoplasia na prega vocal à direita, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_lesao_lat_esq']:
    #     glote = glote + 'presença de leucoplasia na prega vocal à esquerda, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_ant_dir']:
    #     glote = glote + 'presença de leucoplasia localizada no terço anterior da prega vocal direita, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_med_dir']:
    #     glote = glote + 'presença de leucoplasia localizada no terço médio da prega vocal direita, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_post_dir']:
    #     glote = glote + 'presença de leucoplasia localizada no terço posterior da prega vocal direita, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_ant_esq']:
    #     glote = glote + 'presença de leucoplasia localizada no terço anterior da prega vocal esquerda, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_med_esq']:
    #     glote = glote + 'presença de leucoplasia localizada no terço médio da prega vocal esquerda, '
    # elif window == janela2 and values['glote_leuco'] and values['glote_terco_post_esq']:
    #     glote = glote + 'presença de leucoplasia localizada no terço posterior da prega vocal esquerda, '
    # Tumor:
    if window == janela2 and values['glote_tumor']:
        if window == janela2 and values['tu_glote_veg']:
            asp_tu = 'vegetante'
        elif window == janela2 and values['tu_glote_ulc']:
            asp_tu = 'ulcerado'
        elif window == janela2 and values['tu_glote_ui']:
            asp_tu = 'úlcero-infiltrativo'
        elif window == janela2 and values['tu_glote_ped']:
            asp_tu = 'pediculado'
        elif window == janela2 and values['tu_glote_sess']:
            asp_tu = 'séssil'
        elif window == janela2 and values['tu_glote_sub']:
            asp_tu = 'submucoso'
        # if window == janela2 and values['glote_terco_ant_dir']:
        #     loc_tu = 'no terço anterior da prega vocal direita, '
        # elif window == janela2 and values['glote_terco_ant_dir'] and values['glote_terco_med_dir']:
        #     loc_tu = 'no terço anterior e médio da prega vocal direita, '
        # elif window == janela2 and values['glote_terco_ant_dir'] and values['glote_terco_med_dir']:
        #     loc_tu = 'no terço anterior e médio da prega vocal direita, '
        desc_tu = values['desc_leuco_tu']
        glote = glote + f'lesão de aspecto {asp_tu}, localizado {desc_tu}, '

    # Fendas:
    if window == janela2 and values['fenda_ausente']:
        glote = glote + 'ausência de fenda vocal'
    elif window == janela2 and values['fenda_tri_post']:
        glote = glote + 'fenda vocal triangular posterior'
    elif window == janela2 and values['fenda_tri_med_post']:
        glote = glote + 'fenda vocal triangular médio-posterior'
    elif window == janela2 and values['fenda_tri_ant_post']:
        glote = glote + 'fenda vocal triangular ântero-posterior'
    elif window == janela2 and values['fenda_fusiforme']:
        glote = glote + 'fenda vocal fusiforme'
    elif window == janela2 and values['fenda_fusi_ant']:
        glote = glote + 'fenda vocal fusiforme anterior'
    elif window == janela2 and values['fenda_fusi_ant_post']:
        glote = glote + 'fenda vocal fusiforme ântero-posterior'
    elif window == janela2 and values['fenda_fusi_post']:
        glote = glote + 'fenda vocal fusiforme posterior'
    elif window == janela2 and values['fenda_paralela']:
        glote = glote + 'fenda vocal paralela'
    elif window == janela2 and values['fenda_dupla']:
        glote = glote + 'fenda vocal dupla'
    elif window == janela2 and values['fenda_ampu']:
        glote = glote + 'fenda vocal em ampulheta'
    elif window == janela2 and values['fenda_irreg']:
        glote = glote + 'fenda vocal irregular'

    # Início - Infraglote: 
    if window == janela2 and values['infra_nl']:
        infraglote = 'ausência de lesão, calibre preservado'
    elif window == janela2 and values['infra_alterado']:
        infraglote == values['infra_alterado']
    
    # Início - Hipofaringe:
    if window == janela2 and values['hipofaringe_nl']:
        hipofaringe = 'recessos piriformes, paredes da faringe e área retrocricóidea livres'
    elif window == janela2 and values['lesao_recesso'] and values['lesao_hipo_lat_dir']:
        hipofaringe = 'Presença de lesão tumoral acometendo o recesso piriforme direito'
    elif window == janela2 and values['lesao_recesso'] and values['lesao_hipo_lat_esq']:
        hipofaringe = 'Presença de lesão tumoral acometendo o recesso piriforme esquerdo'
    elif window == janela2 and values['lesao_par_post'] and values['lesao_hipo_lat_dir']:
        hipofaringe = 'Presença de lesão tumoral acometendo a parede posterior à direita'
    elif window == janela2 and values['lesao_par_post'] and values['lesao_hipo_lat_esq']:
        hipofaringe = 'Presença de lesão tumoral acometendo a parede posterior à esquerda'
    elif window == janela2 and values['lesao_retrocri']:
        hipofaringe = 'Presença de lesão tumoral acometendo a área retrocricóide'    
    elif window == janela2 and values['lesao_retrocri'] and values['lesao_hipo_lat_dir']:
        hipofaringe = 'Presença de lesão tumoral acometendo a área retrocricóide à direita'
    elif window == janela2 and values['lesao_retrocri'] and values['lesao_hipo_lat_esq']:
        hipofaringe = 'Presença de lesão tumoral acometendo o área retrocricóide à esquerda'
    if window == janela2 and values['lesao_hipo_veg']:
        hipofaringe = hipofaringe + 'de aspecto vegetante'
    elif window == janela2 and values['lesao_hipo_ui']:
        hipofaringe = hipofaringe + 'de aspecto úlcero-infiltrativo'

    
   
    
    


    
    
        

    





    # Confecção do laudo:
    if window == janela2 and event == 'Finalizar':   
        print(f'''
Nome: {nome.title()}
Data de nascimento: {nascimento}
Médico solicitante: Dr(a) {medico.title()}
Data do exame: {data_em_texto}
    
Exame realizado {anestesia} e através de nasofibroscopia. {colaboracao}
    
Cavidade nasal: {mucosa_nasal.capitalize()}, {concha_nasal}, {meato_medio}, {desvio_septal}, {epistaxe}.
Rinofaringe: {rinofaringe}
Orofaringe: {orofaringe}. 
Supraglote: {supraglote.capitalize()}
Glote: {glote} 
Infraglote: {infraglote.capitalize()}
Hipofaringe: {hipofaringe.capitalize()}
    ''')

