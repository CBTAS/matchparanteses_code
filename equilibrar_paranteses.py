
def equilibrar_parenteses(s):
    pilha = []
    for char in s:
        if pilha and ((pilha[-1] == '(' and char == ')')):
            pilha.pop()  # Parênteses correspondentes, remove o último da pilha
        else:
            pilha.append(char)  # Adiciona o parêntese atual à pilha

    # Adiciona parênteses de abertura adicionais para equilibrar
    s_balanceada = '(' * (len(pilha)-pilha.count('(')) + s

    # Adiciona parênteses de fechamento para equilibrar
    s_balanceada += ')' * (len(pilha)-pilha.count(')'))

    return s_balanceada

# Teste 1
str1_input = ")("
str1_output = equilibrar_parenteses(str1_input)
print(f"Input: {str1_input}, Output: {str1_output}")

# Teste 2
str2_input = ")()))()())"
str2_output = equilibrar_parenteses(str2_input)
print(f"Input: {str2_input}, Output: {str2_output}")

# Teste 3
str4_input = "((()))(((((())))(((("
str4_output = equilibrar_parenteses(str4_input)
print(f"Input: {str4_input}, Output: {str4_output}")
