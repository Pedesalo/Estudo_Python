1. Janelas e Containers (Estrutura da Interface)

Essas classes servem de base para você colocar os botões, textos e outros elementos dentro.

    ctk.CTk: É a classe principal. Ela cria a janela raiz (a janela principal do seu programa). Todo aplicativo CustomTkinter precisa de uma dessa para funcionar.

    ctk.CTkToplevel: Cria uma janela extra (secundária). Útil para criar telas de "Configurações", "Ajuda" ou avisos que abrem por cima da janela principal.

    ctk.CTkFrame: Cria um bloco/container retangular dentro da janela. Serve para agrupar e organizar elementos visualmente (ex: um frame para o menu lateral, outro para o conteúdo).

    ctk.CTkScrollableFrame: Igual ao Frame, mas adiciona barras de rolagem automaticamente se o conteúdo dentro dele for maior que o espaço disponível. Excelente para feeds ou listas longas.

2. Elementos de Exibição e Texto

Classes usadas para mostrar informações ao usuário.

    ctk.CTkLabel: Exibe textos ou imagens estáticas na tela (títulos, legendas, instruções).

    ctk.CTkProgressBar: Uma barra de progresso. Ideal para mostrar o andamento de um download, carregamento ou tarefa demorada.

3. Elementos de Entrada de Dados (Formulários)

Classes que permitem ao usuário digitar ou interagir para enviar informações.

    ctk.CTkEntry: Cria uma caixa de entrada de texto simples de apenas uma linha. Usada para campos como "Nome", "E-mail" ou "Senha".

    ctk.CTkTextbox: Cria uma caixa de texto de múltiplas linhas. Permite que o usuário digite textos longos (parágrafos) ou exiba logs do sistema.

4. Elementos de Seleção e Controle (Cliques e Opções)

Classes que oferecem opções e botões para o usuário interagir.

    ctk.CTkButton: O clássico botão. Executa uma função/ação quando é clicado.

    ctk.CTkCheckBox: Caixa de seleção estilo "check" (quadradinho). Permite marcar/desmarcar opções independentes (ex: "Aceito os termos").

    ctk.CTkRadioButton: Botão de opção redondo. Usado quando o usuário deve escolher apenas uma opção dentro de um grupo (ex: Gênero: "Masculino" ou "Feminino").

    ctk.CTkSwitch: Um botão estilo "interruptor" (liga/desliga). Muito moderno, ideal para configurações como "Modo Escuro: Ativado/Desativado".

    ctk.CTkComboBox: Um menu dropdown (caixa de combinação) onde o usuário pode selecionar uma opção de uma lista ou digitar a sua própria.

    ctk.CTkOptionMenu: Muito parecido com o ComboBox, mas o usuário apenas escolhe uma das opções predefinidas, sem a permissão de digitar algo novo.

    ctk.CTkSlider: Uma barra deslizante. Usada para selecionar valores numéricos em uma faixa (ex: controlar o volume de 0 a 100 ou o brilho da tela).

5. Caixas de Diálogo Integradas (Pop-ups)

Classes prontas para interagir rapidamente com o usuário sem precisar criar uma nova janela do zero.

    ctk.CTkInputDialog: Abre uma caixinha de mensagem padrão (pop-up) que pede para o usuário digitar um valor e retorna esse valor para o código.

Dica de Roteiro de Estudos:

Para não se sentir sobrecarregado, sugiro que monte pequenos projetos estudando as classes nesta ordem:

    Crie uma janela com CTk.

    Adicione um título com CTkLabel, uma entrada com CTkEntry e um botão com CTkButton.

    Tente organizar esses elementos usando um CTkFrame.

    Depois, experimente componentes mais avançados como o CTkSwitch e o CTkScrollableFrame.