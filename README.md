# 2048
Este projeto se trata de um software na linguagem python , versão python 3.5, que acessa um jogo conhecido com 2048, em sua página na internet, e obtém altas pontuações no jogo, executando comandos pré-determinados no código, tudo isso de forma automatizada. O jogo 2048 consiste em unir blocos de mesmo valor para assim realizar a soma deles e obter o bloco com o maior número possível no jogo, que é justamente 2048, sempre que se move os blocos para algum lado(ESQUERDA, DIREITA, CIMA, BAIXO) novos blocos surgem com números diferentes. O link do site oficial do jogo é:  https://gabrielecirulli.github.io/2048/ .
Como pré-requisitos para se entender com mais facilidade esse projeto é sugerida a leitura do capítulo 11 Web Scraping do livro Automate the Boring Stuff wiht Python, e alguma compreensão básica de HTML, porém o código aqui apresentado será explicado linha-por-linha.

 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

jogo = "http://gabrielecirulli.github.io/2048/"
browser = webdriver.Firefox()
browser.get(jogo)
caixa = browser.find_element_by_class_name("game-container")
game = browser.find_element_by_class_name("retry-button")

while game.is_displayed() == False:

    caixa.send_keys(Keys.UP)
    caixa.send_keys(Keys.RIGTH)
    caixa.send_keys(Keys.DOWN)
    caixa.send_keys(Keys.LEFT)

print("Voce perdeu!")


Este código está disponível no meu github alpinista06 ou através do link: https://github.com/alpinista06/2048









Neste projeto o foco é voltado para o uso do módulo ‘selenium’ que simula o controle de um browser(navegador) de forma idêntica a um usuário real com cliques, preenchimento de formulários, acesso a URL’s e outros mais. Sua documentação para um entendimento mais profundo é encontrada no link: http://selenium-python.readthedocs.io/. 
Nas primeiras duas linhas importamos dois métodos do módulo selenium. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

O primeiro é o ‘webdriver’ que nos permite o o controle, como mencionado acima, do browser, e o segundo importa o método ‘Keys’ que trás uma praticidade enorme para o desenvolvedor, ambos serão explicados com mais detalhes no decorrer do código para assim ocorrer uma absorção maior dos conceitos.
No trecho:
  
jogo = "http://gabrielecirulli.github.io/2048/"
browser = webdriver.Firefox()
browser.get(jogo)

Definimos a variável ‘jogo’ e a configuramos com a string do url do site oficial do jogo 2048, na próxima linha usamos o método ‘webdriver’ para abrir o navegador que desejamos controlar, neste caso é o Firefox, e essa chama é guardada na variável ‘browser’ portanto sempre q ela aparecer indica que um novo  navegador firefox será aberto. Ela necessita de 1 único argumento na chamada, que é o url que queremos abrir, através de ‘browser.get(jogo)’ o método ‘.get’ faz a abertura do navegador(browser) na url e logo em seguida o download da página o que permite o trabalho offline após essa linha do código.
Nas linhas seguintes:

caixa = browser.find_element_by_class_name("game-container")
game = browser.find_element_by_class_name("retry-button")

O método ‘ .find_element_by_’ de webdriver, permite encontrar qualquer elemento da página da web seja ele um elemento ‘class, head, tag’s’, qualquer elemento da pagina para que o programa possa trabalhar sobre o elemento conhecido. Nos casos acima ambos os elementos são ‘class_name’ ou seja o nome de uma determinada classe do código HTML ‘game-container’ é o nome da classe onde se encontra a grade de controle do jogo e ‘retry-button’ é o botão que aparece quando se perde o jogo, atenção a esse botão ele irá controlar o fluxo principal do código. Ambos são salvos respectivamente nas variáveis caixa e game.
No trecho :

    

while game.is_displayed() == False:

    caixa.send_keys(Keys.UP)
    caixa.send_keys(Keys.RIGTH)
    caixa.send_keys(Keys.DOWN)
    caixa.send_keys(Keys.LEFT)


através do loop ‘while’ o código irá continuar mandando os comandos para a página enquanto a condição de controle for ‘False’. ‘.is_displayed()’ é um método que permite verificar se determinada condição está ou não visível na pagina no presente momento em que é chamada, neste caso enquanto o conteúdo da variável ‘game’ NÃO estiver visível na página o loop continua rodando e verificando. A classe ‘retry-button’ só aparece quando o jogador perde, portanto nesse momento a o teste ‘ game.is_displayed()’ retornará ‘True’(verdadeiro) e então o código segue o fluxo para o seu fim.
Na última linha caso o teste do loop falhe é mostrada na tela a mensagem ‘ Voce perdeu!’


print("Voce perdeu!")

Projeto aparentemente muito simples, e realmente é quando já se tem conhecimento das possibilidades dos métodos do módulo selenium, porém existe uma conceituação muito grande por trás desse pequeno código, entendo ele bem e conhecendo o módulo selenium várias oportunidades são abertas!





Bibliografia

https://docs.python.org/2/library/selenium.html

sweigart, Al. Automate boring stuff with python.

https://github.com
