"""
Dunder Name e Dunder Main

Dunder -> Doble Under __<...>__
Dunder Name -> __name__
Dunder Main -> __main__

Em Python, sao utilizados dunder para criar funcoes, atributos, propriedades e etc utilizando Dunder para
nao gerar conflituo com os nomes desses elementos na programacao.

Na linguagem C, temos um programa da seguinte forma:

    int main(){
        return 0;
    }

Na linguagem Java, temos um programa da seguinte forma:

    public static void main(String[] args){

    }

Em Python, se executarmos um modulo Python diretamente na linha de comando, internamente o Python
atribuira a variavel __name__ o valor __main__ indicando que este modulo eh o modulo de execucao
principal.
"""
from funcoes_parametro_default import soma

