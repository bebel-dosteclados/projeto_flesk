# Template Flask — Aula de Programação Web

Projeto-base para atividades de Python + Flask no VS Code.

## Opção recomendada para computadores sem Python e sem administrador

Use o GitHub Codespaces. O Python e o ambiente de desenvolvimento serão executados na nuvem, sem instalar Python no Windows do laboratório.

1. Entre no GitHub e abra o repositório criado a partir deste template.
2. Clique em **Code** → **Codespaces** → **Create codespace on main**.
3. Aguarde a preparação do ambiente.
4. O Codespaces cria automaticamente o ambiente `.venv` e instala o Flask na primeira preparação. Se precisar recriá-lo, execute `python -m venv .venv` no terminal.

5. Ative o ambiente:
   - Linux/macOS/Codespaces: `source .venv/bin/activate`
   - Windows PowerShell local: `.venv\\Scripts\\Activate.ps1`
6. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

7. Execute o Flask:

   ```bash
   python app.py
   ```

8. No Codespaces, clique em **Open in Browser** quando a notificação de encaminhamento da porta 5000 aparecer. Se não aparecer, abra a aba **Ports** e encaminhe a porta `5000`.

## Criar um repositório GitHub usando este projeto como template

1. Crie um repositório vazio no GitHub, por exemplo `flask-template-aula`.
2. Envie os arquivos desta pasta para ele (botão **Add file** → **Upload files**, ou use Git).
3. Em **Settings** → **General**, marque **Template repository**.
4. Os alunos poderão clicar em **Use this template** → **Create a new repository**.
5. Para trabalhar sem instalar Python no laboratório, cada aluno abre o próprio repositório e cria um Codespace.

## Alternativa: rodar no próprio Windows

Esta alternativa exige que o computador tenha Python instalado ou que a política de TI permita usar uma distribuição portátil/instalador por usuário. O script `setup-windows.ps1` tenta instalar o ambiente virtual, mas **não instala Python** e não contorna bloqueios de rede ou políticas administrativas.

## Estrutura

- `app.py`: aplicação Flask inicial.
- `requirements.txt`: dependências Python.
- `templates/index.html`: página HTML.
- `.devcontainer/devcontainer.json`: ambiente de desenvolvimento para Codespaces.
- `.gitignore`: evita enviar o ambiente virtual e arquivos temporários ao Git.

## Observação para o professor

Codespaces depende de internet, conta GitHub e disponibilidade/cota do serviço. Verifique as cotas das contas antes da aula. Para uma turma sem acesso ao Codespaces, a solução mais confiável é solicitar à TI a instalação do Python para todos os usuários ou preparar uma imagem padronizada dos computadores.
