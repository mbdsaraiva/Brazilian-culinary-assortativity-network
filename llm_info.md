# LLM Information

This file contains information about the language model used and the prompts used to identify ingredients and their types.

## Language Model

**Model Name**: ChatGPT 4.0, Microsoft Copilot, Manus AI

For the creation of the main code, the script used to download the recipe images and the classification of ingredients by their type, GPT-4 was used.

To obtain the ingredients from the recipes based on their images, Microsoft Copilot was used.

And finally, for the creation of the .csv file containing information about 'recipe, ingredients, ingredient types' separated by ';', Manus AI and GPT-4 were used."

## Prompts Used

## 1. Prompt for generating 50 recipes

Sugira 50 receitas que são tipicamente brasileiras, para a criação de um grafo de assortatividade contendo as informações sobre ingredientes e seus tipos observando o seguinte:

Construir um grafo de co-ocorrência de ingredientes a partir
de pelo menos 50 receitas populares da culinária brasileira,
classificar os ingredientes por tipo (proteína, carboidrato,
vegetal etc.) e analisar a assortatividade do grafo com base
nesses tipos, discutindo se a gastronomia brasileira tende a
valorizar combinações homogêneas (entre ingredientes do
mesmo tipo) ou contrastantes (entre tipos diferentes).

A primeira etapa é a geração da base de dados, e alguns detalhes devem ser observados, são eles: 

1- Gerar a descrição dos ingredientes a partir de uma imagem da receita.

2- Extrair automaticamente os ingredientes descritos na receita.

3- Classificar cada ingrediente em uma das seguintes categorias:

Proteína, caboidrato, vegetal, fruta, etc...

 A princípio vou fazer apenas essa primeira etapa de levantamento dos dados, sugira portanto 50 receitas, é importante que não classifique agora, a classificação virá na próxima etapa após a reunião de todas as imagens.

## 2. **Script creation**

Crie um script em python que recebe uma URL contendo imagens e faz o download delas para uma pasta qualquer

## 3. **Ingredients identification**

Preciso que extraia os ingredientes dos 50 pratos a partir da imagem, tome como base apenas as imagens e o que vc consegue perceber: 
[Imagens anexadas]

## 4. **Ingredients classification**

Para a etapa de classificação montei um arquivo.txt contendo todas as receitas e seus respectivos ingredientes, agora preciso ir para a próxima etapa que é a classificação deles, vou mandar as informações contidas no txt e preciso que me retorne a classificação de cada um dos ingredientes quanto sua categoria, por exemplo: 

 Proteína 
 
 Carboidrato 
 
 Vegetal
 
 Fruta
 
 Laticínio
 
 Gordura
 
 Condimento 
 
 Outro mais

## 5. **CSV file**

Preciso que monte um arquivo CSV contendo todas as informações das receitas, ingredientes e classificação, separados por ";", seguindo o seguinte padrão: 

nome_receita  ingredientes  tipos_ingredientes

[arquivo.txt anexado]

## 6. **Main code and assortativity analysis process**

Crie um código em python que faça a leitura do arquivo.csv e exiba a rede, o programa deve destacar pelo tamanho os nós com mais conexões e o tamanho dos nomes deve ser proporcional ao tamanho do nó, além disso o atributo do nó deve ser demarcado através de cores, considere ainda que o código deve anteder os seguintes critérios: 

Nós = ingredientes

Arestas = ligação entre ingredientes que aparecem na mesma receita

Atributo dos nós = tipo de ingrediente

Calcular:

Coeficiente de assortatividade por tipo usando networkx.attribute_assortativity_coefficient(G, "tipo")

Visualizar o grafo com layout adequado e coloração por tipo (nxviz)

por fim gere algumas informações sobre assortatividade, quantos nós e quantas arestas tem no total e quais nós se conectam com quais.
