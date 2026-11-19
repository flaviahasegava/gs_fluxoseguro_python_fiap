# Uso de IA no Fluxo Seguro
Durante a revisão do Fluxo Seguro, usamos o ChatGPT para tirar algumas dúvidas sobre o cadastro dos bueiros, o registro das leituras e o pedido de limpeza.


## Perguntas à ferramenta
**Prompt 1**
Se eu cadastrar “Rua da Praça” e depois digitar “rua da praça” com um espaço no final, o programa entende que é o mesmo bueiro? E se eu deixar um espaço depois do número no menu?

**Prompt 2**
Na hora de informar o nível da água, posso digitar 72,5 ou precisa ser um número inteiro? O que acontece se eu digitar 101 sem querer?

**Prompt 3**
Se o nível chegar a 85% durante a chuva e depois da chuva baixar pra 22%, o pedido de limpeza continua aberto? E se outro bueiro também estiver com 22%, a situação dos dois vai ser a mesma?


## Como funciona a entrada de dados
No cadastro, o .strip() tira os espaços do começo e do fim do nome da rua. O .lower() ajuda a comparar os nomes mesmo quando alguém muda as maiúsculas e minúsculas. Por isso, o programa reconhece que “Rua da Praça” e “rua da praça ” são o mesmo local. Se a pessoa digitar só espaços, aparece um aviso e ela volta ao menu. Já no menu, a opção precisa ser digitada sem espaços.

Para registrar o nível da água, o programa aceita números inteiros de 0 a 100. Se a pessoa digitar 72,5, a vírgula faz o programa pedir outra leitura. Se digitar 101, o valor também é recusado porque passou de 100.


## O que aprendemos com a revisão
Entendemos que dois bueiros com 22% de água depois da chuva podem ter situações diferentes. Se um deles chegou a 85% durante a chuva, o pedido foi aberto e continua pendente. Se o outro estava sem pedido, os 22% mantêm essa situação. Depois da chuva, o pedido abre com 25% ou mais. Se já estiver aberto, continua assim com 20% e só fecha quando a leitura fica abaixo disso.
