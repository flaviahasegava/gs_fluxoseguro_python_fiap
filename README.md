# Fluxo Seguro em Python
O Fluxo Seguro é o projeto da equipe Core sobre monitoramento preditivo de alagamentos em São Paulo. Na parte de Python, simulamos o nível de água nos bueiros durante e depois da chuva. Você escolhe um ponto cadastrado e informa a porcentagem dele que está ocupada pela água. Durante a chuva, o programa mostra o nível de risco. Depois da chuva, é possível acompanhar se aquele ponto tem um pedido de limpeza pendente.


## Como rodar?
Extraia o ZIP e abra no VS Code a pasta onde está o `main.py`. No terminal dessa pasta, digite `py main.py` no Windows ou `python3 main.py` no macOS ou Linux. Use o Python 3.10 ou mais recente, porque o menu usa `match/case`.

No macOS ou Linux, pode aparecer um aviso de que o comando `cls` não foi encontrado. Ele serve para limpar a tela no Windows. O menu abre normalmente depois do aviso.


## Um exemplo para testar o programa
1. No menu, escolha **1** e cadastre o ponto (Ex: **Bueiro da praça**, **Avenida Paulista**).
2. Escolha **2** para registrar uma leitura. Selecione o bueiro **1**, escolha **1** para indicar que está chovendo e digite **72**. Na tela aparece `Situação: PERIGO`. O nível deve ser um número inteiro de 0 a 100. Se digitar `72,5` ou `72.5`, o programa pede o valor de novo.
3. Escolha **2** no menu e selecione o mesmo bueiro. Dessa vez, escolha o período **2** (após a chuva) e digite **30**. A situação passa para `LIMPEZA SOLICITADA`.
4. Registre mais duas leituras para esse bueiro, ambas após a chuva. Digite **22** na primeira e **19** na segunda. Com 22%, o pedido continua aberto. Com 19%, aparece `SEM PEDIDO DE LIMPEZA`.
5. Escolha **3** para ver as quatro leituras na ordem em que foram registradas. A opção **0** encerra o programa. O histórico fica guardado só enquanto o programa está aberto.

O histórico desse exemplo fica assim:
```text
Bueiro da praça | Durante a chuva | 72% | PERIGO
Bueiro da praça | Após a chuva | 30% | LIMPEZA SOLICITADA
Bueiro da praça | Após a chuva | 22% | LIMPEZA SOLICITADA
Bueiro da praça | Após a chuva | 19% | SEM PEDIDO DE LIMPEZA
```


## Como o programa decide?
Durante a chuva, o programa usa estas faixas para indicar o risco.
| Ocupação do bueiro | Resultado |
| --- | --- |
| 0% a 39% | NORMAL |
| 40% a 59% | ATENÇÃO |
| 60% a 89% | PERIGO |
| 90% a 100% | EMERGÊNCIA |

Se o nível passar de **80% durante a chuva**, o programa também registra um pedido de limpeza. Por exemplo, com 81% o risco ainda é `PERIGO`, mas o pedido já fica aberto. Uma leitura mais baixa durante a mesma chuva mantém o pedido pendente.

Após a chuva, uma leitura de **25% ou mais** abre ou mantém o pedido. Entre **20% e 24%**, vale a situação anterior daquele bueiro. Com **19% ou menos**, o pedido é encerrado. Cada bueiro tem seu próprio pedido.


## Onde encontrar isso no código?
O `while` mantém o menu aberto, e o `match/case` encaminha a opção digitada. No `case "2"`, o programa valida a leitura, compara o nível com as faixas de risco e atualiza o pedido do bueiro escolhido em `limpeza_pendente`. No fim desse bloco, ele monta a linha `registro_leitura` e a guarda na lista `historico_leituras`. Na opção **3**, um `for` percorre essa lista e mostra as leituras na tela.


## Informações do projeto (FIAP - 1ESPA)
- **Projeto:** Fluxo Seguro (Sistema de Monitoramento Preditivo de Alagamentos)
- **Desafio:** Global Solution - CitizenTech
- **Disciplina:** Computational Thinking with Python
- **Professores:** Edson de Oliveira


## Integrantes (Grupo Core)
• Eduardo Miranda Mororo
• Flávia Sirahata Hasegava
• Henrique Nascimento
• Leandro Rodrigues Barbosa 
• Victor Krause Esteves