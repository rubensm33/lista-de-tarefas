# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista_tarefas = []
backup = []
while True:
    print('Digite um comando ou uma tarefa')
    acao_recebida = input('[d]esfazer\n[r]efazer\n[l]istar\n')
    
    if acao_recebida == 'd':
        if not lista_tarefas:
            print('Não há nada para desfazer')
            continue
        backup = lista_tarefas.pop()
        
    elif acao_recebida == 'r':
        if not backup:
            print('Não há nada para resfazer')
            continue
        lista_tarefas.append(backup)
       
    elif acao_recebida == 'l':
        for lista in lista_tarefas:
            print(lista)
    else: 
        lista_tarefas.append(acao_recebida)