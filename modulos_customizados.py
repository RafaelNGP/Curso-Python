"""
Modulos Customizados - Udemy

Como modulos Python nada mais sao do que arquivos python, entao TODOS os arquivos que criamos neste
curso sao modulos Python prontos para serem utilizados.

Um modulo Python nao deve conter execucao de codigo (como foi desenvolvido ate agora no curso, boa)
entao o resultado no console desta aula mostra a execucao do codigo importado primeiro e apenas na ultima
linha, que traz o resultado 10, que faz a resolucao da funcao importada soma(5,5).

Se tivesse alguma variavel na importacao, tambem poderia usa-la aqui.
PS: Para que toda a execucao do modulo nao seja transportada para o programa que a importou, devo utilizar
uma condicao __name__ == "__main__" na execucao do modulo, para que apenas seja executado caso ele seja
o programa principal.
"""
import funcoes_parametro_default as fpd
import listas_aula as lst

print(fpd.soma(5, 5))
print(lst.lista1, lst.lista2, lst.lista3, lst.lista4, lst.lista5, lst.num)
