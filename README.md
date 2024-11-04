<h1> TextBasedGame </h1>

<h1> FLORESTA OBSCURA </h1>

<p> Este jogo é baseado numa aventura, estarás perdido numa floresta, que ao longo do jogo irá ter alguns desafios e escolherem o caminho certo, com o objetivo principal de encontrar os amigos e ir embora. Este jogo é feito para adolescentes ou adultos. </p>

 

**FUNCIONALIDADES DO JOGO**

Como este jogo é textbasedgame, o jogador apenas consegue interagir com o jogo usando comandos. Também vai ter progressão ao longo do jogo, ou seja, a cada escolha que o jogador faça, irá haver conquistas e perder algumas coisas. Acrescentando que é um jogo single-player (só dá para um jogador). 

**MECÂNICAS DO JOGO**

Como todos os jogos, este jogo tem um movimento diferente (Só irá conseguir andar pela esquerda ou direita). O combate neste jogo também pode-se ver em algumas fases, este inclui pegar armas e tem sistema de ataque e defesa. 

**ESTRUTURA NARRATIVA E LÓGICA DAS ESCOLHAS**

Neste jogo, a narrativa é muito utilizada, pois a história segue um caminho fixo, onde o jogador avança para uma cena sem desvios (E neste jogo, irá ter diálogos entre algumas personagens, logo a narrativa vai ter que ser usada). 

A lógica deste jogo tem decisões, ou seja, elas têm consequências significativas, como a vida e a morte do jogador, encontrar objetos e mais.  

Dependendo das escolhas feitas, o jogador pode seguir diferentes caminhos na narrativa. Por exemplo, um jogador pode optar por interagir com um personagem, resultando em um desfecho diferente em comparação com um jogador que escolhe ignorá-lo.  

Também tem momentos críticos, onde o jogador deve tomar uma decisão que afetará apenas a narrativa imediata pois o futuro do jogo irá ser o mesmo. Este jogo contém também a possibilidade de jogar outra vez. Assim o jogador pode experimentar diferentes decisões e diferentes desafios. Esta opção só aparece quando o jogador morre ou acaba o jogo. 

**TÉCNICAS DE  IMPLEMENTAÇÃO**

*Estrutura do Código*  

O código está dividido em 6 partes: 

	- Comandos necessários; 

	- Introdução; 

	- Fase 1; 

	- Fase 2; 

	- Fase 3; 

	- Fase Final. 

*Controlo de fluxo*

O jogo é constituído por ifs e whiles. (O if é o mais utilizado durante o jogo) 

O if é utilizado para escolhas, por exemplo, tem 2 caminhos à frente do jogador, se escolher o caminho x, acontece algo, senão escolhe o y, e irá acontecer outra coisa diferente. 

O while é utilizado para quando o jogador morre ou acaba o jogo, o while é utilizado para voltar ao início do jogo.

*Gestão de dados* 

Para guardar o progresso do jogador, o jogo tem listas e variáveis (por exemplo, o jogo tem uma mochila onde guarda os itens que o jogador apanha e o jogador tem vida e dependendo das escolhas, a vida irá ser guardada.) 

*Interatividade com utilizador* 

O input do jogo é utilizado em várias coisas. É utilizado nas escolhas, na narrativa e nos diálogos. Quando input é utilizado nas escolhas, é apenas usado uma vogal ou uma palavra que dê seguimento ao jogo. Na narrativa e nos diálogos é utilizado o input para dar tempo ao jogador ler (Quando aparece o diálogo ou narrativa, a cada ENTER que o jogador dê, aparece outra nova frase. Se usasse o print, ficava tudo junto e aparecia tudo seguido, com o input é mais limpo e bonito.) 

**COMANDOS NECESSÁRIOS**

	E - Escolher esquerda
	D - Escolher direita
	M - Ver mochila
 	Seguinte - Ir para a próxima fase
	Fugir - Fugir de alguma coisa
	Atacar - Atacar alguma coisa
	ENTER - (Clicar na tecla ENTER)Só se usa quando acontece diálogo ou narrativa
	Usar comida - Usa-se apenas numa fase



**DESAFIOS E SOLUÇÕES**

O if na fase 3 estava a dar erro mas consegui resolver (o elif estava na linha errada e então dava erro) e o while para acabar o jogo (não me estava a dar para voltar ao jogo mas consegui resolver). 

**CONCLUSÃO**

Para o 1º jogo feito na vida, acho que o trabalho tá bom, não 100% perfeito, mas acho que dá para perceber que tentei e que esforcei-me. No futuro quero melhorar a minha programação e não usar muito o if e usar mais while ou outro tipo de loops e tar mais concentrado no código. Usar o que aprendi com o professor e com o w3school mais tarde quando tiver um emprego. 
