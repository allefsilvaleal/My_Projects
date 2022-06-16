programa
{
	
	funcao inicio()
	{
	
		real n1, n2, n3, n4, media
		cadeia nome
	
		escreva("Nome do aluno: ")
		leia(nome)
		escreva("Digite a nota 1: ")
		leia(n1)
		escreva("Digite a nota 2: ")
		leia(n2)
		escreva("Digite a nota 3: ")
		leia(n3)
		escreva("Digite a nota 4: ")
		leia(n4)

		media = (n1 + n2 + n3 + n4) / 4
		escreva("Sua média é: " + media + ".")

		// Verifica se a média é maior ou igual a 7
		se (media >= 7) {
			escreva("\n", "Parabéns " + nome +  ", você foi aprovado :)")
		}
		// Verifica se a média é menor que 7
		senao {
			escreva("\n", "Ahhh, que pena :( ... Estude mais, pois infelizmente foi reprovado")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 0; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */