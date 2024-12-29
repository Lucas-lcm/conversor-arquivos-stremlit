# Conversor de arquivos usando Python / Stremlit / Electron (NodeJS)
Realizei o desenvolvimento de um conversor universal de arquivos, para uma demanda da equipe que atuei na Marsh.

## Objeitvo e contexto
Conversor recebe um arquivo que define quais colunas finais você deseja e o arquivo de dados que deseja converter, o usuário informa o de/para das colunas e o aplicativo realiza a transformação e disponibiliza a tabela transformada para download.
Também é possível salvar um arquivo Json com o mapeamento realizado, para utilizado posteriormente.

## Tecnologias usadas
Utilizei basicamente Python com o framework Stremlit, para gerar a interface gráfica para o usuário, e utilizei o Stlie que é um feature do Electron do NodeJs que cria progrmas executáveis e standalones com Pyodie, veja a documentação no link: 
https://github.com/whitphx/stlite/blob/main/packages/desktop/README.md
