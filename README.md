# Diretrizes Vigilância

<br>

[Diretriz Nacional do Plano de Amostragem da Vigilância da Qualidade da Água para Consumo Humano](bvsms.saude.gov.br/bvs/publicacoes/diretriz_nacional_plano_amostragem_agua.pdf) que *"visa orientar a elaboração e a implementação dos planos de amostragem da vigilância da qualidade da água para consumo humano, abordando o quantitativo mínimo de amostras, a frequência de amostragem, os parâmetros a serem analisados, bem como as orientações para a seleção dos pontos de coleta"*.

As diretrizes trazem informações sobre o número de amostras que devem ser realizadas.

<br>

----

### Objetivo

O projeto objetiva disponibilizar os parâmetros de qualidade em formato tabular, adequado para utilização em análises computacionais.

<br>

----

### Como Instalar?

<br>

```bash
pip3 install diretriz-vigilancia --upgrade
```

<br>

----

### Como Usar?

<br>

```python
from normas import diretriz

# Get Table
pop=156726
diretriz.numero_amostras_cloro(pop)
diretriz.numero_amostras_fluoreto(pop)

df['n_habitantes'].apply(lambda x: diretriz.numero_amostras_cloro(x))
df['n_habitantes'].apply(lambda x: diretriz.numero_amostras_fluoreto(x))
```

<br>

-----

### Testes

Caso queira testar, segue um [*Google Colab*](https://colab.research.google.com/drive/1JsnMfzkj97DMPNBdB09bPLQ5HuDPjIuv?usp=sharing).

<br>

-----

### *TODO*

1. ...
2. ...
3. ...
