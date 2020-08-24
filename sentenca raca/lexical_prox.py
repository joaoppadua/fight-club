#Script to analyze lexical proximity between words in judicial decision

import spacy, re 

ex_text = """I – RELATÓRIO
A representante do Ministério Público do Estado do Paraná,
em exercício nesta Vara, ofereceu denúncia contra:
ADEMILSON ANTÔNIO MARCELINO, conhecido por “Toni”,
brasileiro, solteiro, desempregado, portador do RG no 7.350.348-5/PR, natural de Joaquim
Távora/PR, nascido em 02 de outubro de 1977, filho de Conceição Aparecida Marcelino e
João Antônio Marcelino, residente na Rua Honoratta Baldo, no 715, Jardim Eucaliptos,
Colombo/PR, como incurso nas penas previstas no art. 2o, da Lei no 12.850/13 e art. 155,
§4o, inciso II e IV do Código Penal, em concurso material (fato I e II);
RODRIGO TREVISAN, conhecido por “Aranha”, brasileiro,
casado, pintor, portador do RG no 2.401.663-3/PR, natural de Curitiba/PR, nascido em 03
de dezembro de 1976, filho de Lucini Gomes Alves e Jose Trevisan, residente na Rua
Marechal Hugo Panasco de Alvin, 74, Alto Boqueirão, Curitiba/PR, como incurso nas penas
previstas no art. 2o, da Lei no 12.850/13 e art. 155, §4o, inciso II e IV do Código Penal, em
concurso material (fato I e V);
LUIZ ALMEIDA ESPINOLA, brasileiro, solteiro, desempregado,
portador do RG no 9.120.450-9/PR, natural de Curitiba/PR, nascido em 06 de fevereiro de
1987, filho de Sandra Mara Claro de Almeida e Luiz Alberto Espínola, residente e
domiciliado na Rua Ireno Marchesini. No 581, casa 02, Bairro Boqueirão, Curitiba/PR, como
incurso nas penas previstas no art. 2o, da Lei no 12.850/13 e art. 155, §4o, inciso II e IV do
Código Penal, em concurso material (fato I e V);
ELOIR DE ASSIS CORREA JUNIOR, conhecido por
“Polaquinho”, brasileiro, portador do RG no 9.272.868-4/PR, natural de Curitiba/PR,
nascido em 14 de setembro de 1985, filho de Eloir de Assis Correa e Maria Elizabeth de
Assis Correa, residente e domiciliado na Rua Nossa Senhora Aparecida, 126, bairro Parque
São Jorge, Almirante Tamandaré/PR, como incurso nas penas previstas no art. 2o, da Lei no
Página 1/115
PROJUDI - Processo: 0017441-07.2018.8.16.0013 - Ref. mov. 855.1 - Assinado digitalmente por Ines Marchalek Zarpelon:6208
19/06/2020: PROFERIDA SENTENÇA CONDENATÓRIA. Arq: sentença condenatóriaPODER JUDICIÁRIO
FORO CENTRAL DA COMARCA DA REGIÃO
METROPOLITANA DE CURITIBA-PR
1a Vara Criminal
Autos no: 0017441-07.2018.8.16.0196
Autora: Justiça Pública
Réus: ADEMILSON ANTÔNIO MARCELINO e OUTROS
12.850/13; art. 157, §2o, inciso II, do Código Penal; art. 155, §4o, incisos II e IV do Código
Penal e art. 155, §4o, inciso IV do Código Penal, em concurso material (fatos I, III, V e VII);
NOELI APARECIDA ALVES, conhecida por “Lindinha”,
brasileira, solteira, portadora do RG no 5.958.209-7/PR, natural de Laranjeiras do Sul/PR,
nascida em 22 de abril de 1974, filha de João Moacir Alves e Natalia Ribeiro Alves,
residente e domiciliada na Rua Henrique Coelho Neto, 1104, bairro Vargem Grande,
Pinhais/PR, como incurso nas penas previstas no art. 2o, da Lei no 12.850/13; art. 155, §4o,
inciso II e IV do Código Penal e art. 155, §4o, inciso IV, do Código Penal , em concurso
material (fato I, VI e VII);
EROS MARCOS ALVES, brasileiro, convivente, portador do RG
no 8.207.937-8/PR, natural de Laranjeiras do Sul/PR, nascido em 31 de dezembro de 1981,
filho de João Moacir Alves e Natalia Ribeiro Alves, residente e domiciliado na Rua Henrique
Coelho Neto, 1104, bairro Vargem Grande, Pinhais/PR, como incurso nas penas previstas
no art. 2o, da Lei no 12.850/13; art. 155, §4o, inciso II e IV do Código Penal e art. 155, §4o,
inciso IV, do Código Penal em concurso material (fato I, IV e VII);
NATAN VIEIRA DA PAZ, brasileiro, convivente, autônomo,
portador do RG no 14.081.604-3/PR, natural de São Paulo/SP, nascido em 19 de janeiro de
1972, filho de Nair Vieira da Paz e Luiz Targino da Paz, residente na Rua Joaquim Da Costa
Ribeiro 1820, Bairro Alto, Casa 4, Curitiba/PR, como incurso nas penas previstas no art. 2o,
da Lei no 12.850/13; art. 157, §2o, inciso II do Código Penal, art. 155, §4o, incisos II e IV, do
Código Penal e art. 155, §4o, inciso IV, do Código Penal , em concurso material (fato I, """

#Create a function to clean the data from meta-text stamps
def clean_txt(text):
    pattern = r'Página(\s.*){9}\sOUTROS'
    mod_text = re.sub(pattern, ' ', text)
    final_text = re.sub('[^\w\s]', ' ', mod_text)
    return final_text

#load spacy object
nlp = spacy.load('pt_core_news_lg')

#Open file, read, vectorize data
with open('Sentenca raca.txt', 'r') as f:
    data = f.read()
    text = clean_txt(data)
    tokens = nlp(text)
    
#Create a loop with conditional statement to find similar lexical items to "raça"
    count = 0
    rate = float(input('Qual o grau de similaridade? '))
    for token1 in tokens:
        if token1.text == 'raça':
            print(token1.text)
            count += 1
        for token2 in tokens:
            if token1.text == 'raça' and token1.similarity(token2) >= rate:
                print(token1, token2, token1.similarity(token2))
    print(f'Número de ocorrências da palavra "raça": {count}')

#DEBUG
#for token in tokens[:50]:
#    print(token.text, token.has_vector)