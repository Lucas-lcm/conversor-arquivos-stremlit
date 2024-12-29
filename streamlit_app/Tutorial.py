import streamlit as st

st.set_page_config(
    page_title="Tutorial",
    page_icon=":house:",
)

st.write("# Como usar o conversor MMB")


st.markdown(
    """
    Este tutorial irá guiá-lo passo a passo no uso da nossa aplicação Streamlit 
    para conversão de arquivos. A ferramenta permite que você converta seus dados 
    de um formato para outro de forma eficiente e personalizada.

    **Instalação:**
    Para utilizar a aplicação, basta baixar e executar o arquivo .exe disponível em 
    [link para download]. 
    Um ícone será criado em sua área de trabalho, facilitando o acesso.

    **Escolhendo o Caminho:**
    Ao iniciar a aplicação, você se deparará com duas opções:
    - Um novo mapeamento: Ideal para quem deseja configurar a conversão do zero.
    - Utilizar um mapeamento já existente: Perfeito para quem já criou um mapeamento anteriormente e deseja reutilizá-lo.
   
     ### Caminho 1: Um Novo Mapeamento

    - **Etapa 1:** Carregando o Arquivo Modelo
        - Objetivo: Definir as colunas e tipos de dados desejados no arquivo de saída.
        - Como fazer:
            Clique no botão para fazer o download do arquivo modelo.
            Abra o arquivo em um editor de texto (como Excel).
            Preencha as informações das colunas e seus respectivos tipos.
            Salve o arquivo e carregue-o.

    - **Etapa 2:** Carregando o Arquivo de Dados e Realizando o Mapeamento
        - Objetivo: Carregar o arquivo que será convertido e definir o mapeamento entre 
        as colunas do arquivo original e do arquivo de saída.
        - Como fazer:
            Carregue o arquivo de dados que você deseja converter.
            Informe em qual linha se inicia o cabeçalho do arquivo.
            - Realize o mapeamento:
                - Selecione a coluna do arquivo original.
                - Escolha a coluna correspondente no arquivo de saída (conforme definido no arquivo modelo).
                - Repita o processo para todas as colunas.
            - Salvar o mapeamento: Clique no botão para baixar o arquivo JSON com o mapeamento configurado. 
            Isso permitirá que você reutilize este mapeamento em futuras conversões.

    - **Etapa 3:** Download do Arquivo Transformado
        - Objetivo: Visualizar e baixar o arquivo com os dados convertidos.
        - Como fazer:
            A aplicação exibirá uma tabela com os dados convertidos.
            Verifique se os dados estão corretos.
            Clique no botão para baixar o arquivo em formato Excel.

    ### Caminho 2: Utilizar um Mapeamento Já Existente

    - **Etapa 1:** Carregando o Mapeamento e o Arquivo de Dados
        - Objetivo: Utilizar um mapeamento já configurado para converter um novo arquivo.
        - Como fazer:
            - Carregue o arquivo JSON com o mapeamento que você salvou anteriormente.
            - Carregue o arquivo de dados que você deseja converter.
            - Informe em qual linha se inicia o cabeçalho do arquivo.

    - **Etapa 2:** Download do Arquivo Transformado
        - Objetivo: Visualizar e baixar o arquivo com os dados convertidos.
        - Como fazer:
            - A aplicação exibirá uma tabela com os dados convertidos.
            - Verifique se os dados estão corretos.
            - Clique no botão para baixar o arquivo em formato Excel.
   
    ### Dicas Adicionais

    - **Formatos de Arquivo:**
        - A aplicação suporta diversos formatos de arquivo (CSV, Excel, etc.);
        - Verifique os formatos disponíveis.
    - **Tipos de Dados:**
        - Certifique-se de que os tipos de dados definidos no arquivo modelo
        sejam compatíveis com os dados do seu arquivo original.
    - **Mapeamento:**
        - O mapeamento é crucial para a conversão correta dos dados;
        - Dedique tempo para verificar se todas as colunas estão mapeadas corretamente.
    - **Salvar Mapeamentos:**
        - Salve seus mapeamentos para reutilizá-los em futuras conversões.
    - **Suporte:**
        - Em caso de dúvidas, entre em contato com o suporte.
    
    Com este tutorial, você estará pronto para utilizar a aplicação de forma eficiente e 
    realizar suas conversões de arquivos de maneira rápida e precisa.
    
    ### Sobre os Desenvolvedores
    - **Lucas Cardoso:** Engenheiro de Computação e pós-graduando em Machine Learning engineering.
    - **Heitor Tanzi:** Administrador pela Ahembi Morumbi e Analista de Dados.
    
    ### Reportando Bugs

    **Encontrou algum problema? Entre em contato conosco através dos e-mails:**
    - **Lucas Cardoso:** lucas.cardoso@mercermarshbeneficios.com
    - **Heitor Tanzi:** heitor.tanzi@mercermarshbeneficios.com

    **Sua contribuição é fundamental para melhorarmos a nossa ferramenta!**
    """
)
