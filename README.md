# Teste Useful Suggestion

## Descrição 

Teste:
Uma empresa de entrega de encomendas precisa de um sistema onde possa registar a movimentação das encomendas entre as suas unidades, será necessário 2 tipos de acesso, um para motorista e admin. 

Motorista:
- Login
- Registar a saída e chegada ao destino. (Os locais de saída e destino são as unidades da empresa que devem ser previamente cadastradas no sistema para serem selecionadas na saída e chegada ao destino.)

Admin:
- Login
- Cadastrar unidades da empresa (nome, cidade, rua, numero, código postal)
- Cadastrar motoristas (nome, unidade que pertence)
- Listar motoristas ao selecionar a unidade em um combobox (usar ajax)
- Listar as movimentações registadas pelos motoristas com possibilidade de editar e ‘apagar’ o registo
- Relatório com o total dos movimentos (registos dos motoristas), contar quantas movimentações em cada trecho por periodo pesquisado (mesma saída e mesma chegada) 

Obs.: Usar bootstrap e jQuery 
	    Postar no GitHub

## Instalação

- Primeiramente deve ser criado um arquivo settings.ini na raiz do projeto com a seguinte estrutura

        [settings]
        DEBUG=
        SECRET_KEY=

- Deve-se instalar as bibliotecas necessárias

        pip install -r requirements.txt

- Aplicando as migrações
        
        python manage.py makemigrations
        python manage.py migrate

- Executando a aplicação

        python mange.py runserver localhost:8000

