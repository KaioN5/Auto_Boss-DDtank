# DDTank Automation Scripts

Este repositório contém scripts de automação para o jogo DDTank, desenvolvidos em Python usando a biblioteca PyAutoGUI. Os scripts automatizam ataques contra diferentes inimigos no jogo.

## Descrição

Os scripts foram criados para facilitar a execução de ataques repetitivos contra monstros específicos no DDTank. Cada script é projetado para um tipo de inimigo diferente:

- **Conde_auto.py**: Automação para batalha contra o Conde
- **Dragao_auto.py**: Automação para batalha contra o Dragão
- **Frango_auto.py**: Automação para batalha contra o Frango
- **Click.py**: Utilitário para capturar posições do mouse

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/ddtank-automation.git
   cd ddtank-automation
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install pyautogui
   ```

## Uso

### Pré-requisitos

- Python 3.x instalado
- DDTank em execução em modo janela (não tela cheia)
- Resolução de tela compatível com as coordenadas programadas

### Executando os Scripts

1. Abra o DDTank e posicione-se na área de batalha apropriada
2. Execute o script correspondente ao inimigo desejado:
   ```bash
   python Conde_auto.py
   python Dragao_auto.py
   python Frango_auto.py
   ```

### Utilitário Click.py

Para capturar posições do mouse (útil para ajustar coordenadas):

```bash
python Click.py
```

Posicione o mouse onde desejar e aguarde 5 segundos. A posição será exibida no console.

## Funcionalidades dos Scripts

### Conde_auto.py

- Executa 200 rodadas de ataque
- Ajusta ângulo automaticamente no início
- Alterna direção de ataque a cada 4 rodadas
- Usa comando 'by239' para ataque

### Dragao_auto.py

- Executa 200 rodadas de ataque
- Ajusta ângulo para cima (8 pressões)
- Vira para a direita inicialmente
- Usa comando 'by239' para ataque

### Frango_auto.py

- Executa 200 rodadas de ataque
- Ajusta ângulo para cima (8 pressões)
- Vira para a direita inicialmente
- Usa comando '239' para ataque

## Configuração

Os scripts usam tempos de espera fixos. Você pode ajustar:

- `TOTAL_RODADAS`: Número de rodadas a executar
- Tempos de `time.sleep()`: Ajuste conforme a velocidade do seu sistema
- Comandos de ataque: Modifique `pt.typewrite()` conforme necessário

## Avisos Importantes

⚠️ **ATENÇÃO**: O uso de automação em jogos pode violar os termos de serviço do jogo. Use por sua própria conta e risco.

- Certifique-se de que o jogo esteja visível e em foco durante a execução
- Não mova o mouse ou pressione teclas durante a automação
- Monitore o progresso através do console
- Pare a execução com Ctrl+C se necessário

## Dependências

- Python 3.x
- PyAutoGUI

## Autor

**Kaio Julio**  
📧 Email: kaiojuliobvb@outlook.com

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou relatar problemas. Para dúvidas ou sugestões, entre em contato através do email acima.

## Licença

Este projeto é distribuído sob a licença MIT.
