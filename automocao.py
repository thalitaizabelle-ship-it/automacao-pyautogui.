import time
import pyautogui
import pandas as pd

# Pausa de segurança entre cada comando
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# No Fedora/GNOME usamos a tecla Super para abrir o menu de aplicativos
pyautogui.press("super")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

# Pausa para o carregamento da página
time.sleep(5)

# Passo 2: Fazer login
# Substitua as coordenadas x e y conforme a sua resolução no Fedora
pyautogui.click(x=500, y=400) 
pyautogui.write("seu_usuario@exemplo.com") # E-mail removido para segurança
pyautogui.press("tab")
pyautogui.write("sua_senha_aqui") # Senha removida para segurança
pyautogui.press("enter")

# Passo 3: Abrir a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar produtos
for linha in tabela.index:
    # Clica no campo de início do formulário
    pyautogui.click(x=500, y=500)
    
    # Preenchimento das colunas do seu arquivo CSV
    pyautogui.write(str(tabela.loc[linha, "nome"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")
    
    # Repita o processo de .write e .press("tab") para as outras colunas se houver
    
    pyautogui.press("enter") # Clica no botão de salvar/cadastrar
    
    # Scroll para cima para o próximo produto (se necessário)
    pyautogui.scroll(500)
    
    # Atualiza o status no CSV para controle
    tabela.loc[linha, "status"] = "cadastrado"
    tabela.to_csv("produtos.csv", index=False)

pyautogui.alert("Processo finalizado com sucesso!")