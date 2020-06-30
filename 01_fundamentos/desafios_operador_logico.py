trabalho_terca = True
trabalho_quinta = False

"""
- confirmando os 2: TV de 50'+ sorvete
- Confirmando apenas 1: TV 32'+ sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #xor
mais_saudavel = not sorvete

print(f"TV 50 {tv_50}, TV 32 {tv_32}, Sorvete {sorvete}, Mais saudavel {mais_saudavel}")